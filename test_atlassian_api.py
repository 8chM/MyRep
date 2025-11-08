#!/usr/bin/env python3
"""Test-Skript für JIRA und Confluence API-Zugriff"""

import requests
from requests.auth import HTTPBasicAuth
import json
import os

# --- Konfiguration ---
JIRA_BASE_URL = os.getenv("JIRA_BASE_URL", "https://maierharry.atlassian.net")
CONFLUENCE_BASE_URL = f"{JIRA_BASE_URL}/wiki"
USERNAME = os.getenv("ATLASSIAN_USERNAME", "Maier.harry@gmail.com")
API_TOKEN = os.getenv("ATLASSIAN_API_TOKEN")

if not API_TOKEN:
    print("ERROR: ATLASSIAN_API_TOKEN environment variable not set!")
    print("Please set it with: export ATLASSIAN_API_TOKEN='your-token-here'")
    exit(1)

# Authentifizierungsobjekt
auth = HTTPBasicAuth(USERNAME, API_TOKEN)

# Standard-Header
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}


def get_jira_issue(issue_key):
    """Ruft ein JIRA-Ticket anhand seines Keys ab."""
    url = f"{JIRA_BASE_URL}/rest/api/3/issue/{issue_key}"
    response = requests.get(url, headers=headers, auth=auth)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"❌ Fehler beim Abrufen von {issue_key}: {response.status_code} - {response.text}")
        return None


def get_confluence_page(space_key, title):
    """Ruft eine Confluence-Seite anhand von Space-Key und Titel ab."""
    url = f"{CONFLUENCE_BASE_URL}/rest/api/content"
    params = {
        "spaceKey": space_key,
        "title": title,
        "expand": "body.storage,version"
    }

    response = requests.get(url, headers=headers, auth=auth, params=params)

    if response.status_code == 200:
        results = response.json().get("results", [])
        if results:
            return results[0]
        else:
            print(f"❌ Seite '{title}' nicht gefunden (0 Ergebnisse).")
    else:
        print(f"❌ Fehler beim Abrufen der Seite: {response.status_code} - {response.text}")
    return None


def list_jira_projects():
    """Listet alle verfügbaren JIRA-Projekte auf."""
    url = f"{JIRA_BASE_URL}/rest/api/3/project"
    response = requests.get(url, headers=headers, auth=auth)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"❌ Fehler beim Abrufen der Projekte: {response.status_code}")
        return None


def main():
    print("=" * 60)
    print("Test: Atlassian API-Zugriff (JIRA & Confluence)")
    print("=" * 60)

    # Test 1: JIRA-Projekte auflisten
    print("\n1. JIRA-Projekte auflisten...")
    projects = list_jira_projects()
    if projects:
        print(f"✅ Erfolgreich! Gefundene Projekte:")
        for project in projects:
            print(f"   - {project['key']}: {project['name']}")

    # Test 2: JIRA-Ticket abrufen
    print("\n2. JIRA-Ticket WEG-7 abrufen...")
    issue = get_jira_issue("WEG-7")
    if issue:
        print(f"✅ Ticket gefunden!")
        print(f"   Zusammenfassung: {issue['fields']['summary']}")
        print(f"   Status: {issue['fields']['status']['name']}")
        print(f"   Typ: {issue['fields']['issuetype']['name']}")
        if issue['fields'].get('assignee'):
            print(f"   Zugewiesen an: {issue['fields']['assignee']['displayName']}")
        else:
            print(f"   Zugewiesen an: Nicht zugewiesen")

    # Test 3: Confluence-Seite abrufen
    print("\n3. Confluence-Seite 'WEG-7 – Metering' abrufen...")
    page = get_confluence_page("WEG", "WEG-7 – Metering")
    if page:
        print(f"✅ Seite gefunden!")
        print(f"   Titel: {page['title']}")
        print(f"   ID: {page['id']}")
        print(f"   Version: {page['version']['number']}")
        print(f"   Inhaltslänge: {len(page['body']['storage']['value'])} Zeichen")

    print("\n" + "=" * 60)
    print("Test abgeschlossen!")
    print("=" * 60)


if __name__ == "__main__":
    main()
