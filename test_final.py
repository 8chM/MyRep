#!/usr/bin/env python3
"""Finaler Test mit korrektem Seitentitel"""

import requests
from requests.auth import HTTPBasicAuth
import json
import os

JIRA_BASE_URL = os.getenv("JIRA_BASE_URL", "https://maierharry.atlassian.net")
CONFLUENCE_BASE_URL = f"{JIRA_BASE_URL}/wiki"
USERNAME = os.getenv("ATLASSIAN_USERNAME", "Maier.harry@gmail.com")
API_TOKEN = os.getenv("ATLASSIAN_API_TOKEN")

if not API_TOKEN:
    print("ERROR: ATLASSIAN_API_TOKEN environment variable not set!")
    exit(1)

auth = HTTPBasicAuth(USERNAME, API_TOKEN)
headers = {"Accept": "application/json", "Content-Type": "application/json"}


def get_confluence_page(space_key, title):
    """Ruft eine Confluence-Seite ab."""
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
    return None


# Test mit korrektem Titel
print("=" * 70)
print("Finaler Test: Confluence-Seite WEG-7 mit korrektem Titel abrufen")
print("=" * 70)

page = get_confluence_page("WEG", "WEG-7 – Metering (Manual Readings & Lifecycle)")
if page:
    print("\n✅ ERFOLGREICH! Seite gefunden:")
    print(f"\n   Titel: {page['title']}")
    print(f"   ID: {page['id']}")
    print(f"   Version: {page['version']['number']}")
    print(f"   URL: {CONFLUENCE_BASE_URL}{page['_links']['webui']}")
    print(f"\n   Erste 500 Zeichen des Inhalts:")
    print(f"   {'-' * 66}")
    content = page['body']['storage']['value']
    print(f"   {content[:500]}...")
    print(f"\n   Gesamtlänge: {len(content)} Zeichen")
else:
    print("\n❌ Seite nicht gefunden")

print("\n" + "=" * 70)
