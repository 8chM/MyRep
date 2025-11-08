#!/usr/bin/env python3
"""Liste alle Confluence-Seiten im WEG-Space auf"""

import requests
from requests.auth import HTTPBasicAuth
import os

JIRA_BASE_URL = os.getenv("JIRA_BASE_URL", "https://maierharry.atlassian.net")
CONFLUENCE_BASE_URL = f"{JIRA_BASE_URL}/wiki"
USERNAME = os.getenv("ATLASSIAN_USERNAME", "Maier.harry@gmail.com")
API_TOKEN = os.getenv("ATLASSIAN_API_TOKEN")

if not API_TOKEN:
    print("ERROR: ATLASSIAN_API_TOKEN environment variable not set!")
    exit(1)

auth = HTTPBasicAuth(USERNAME, API_TOKEN)
headers = {"Accept": "application/json"}

def list_confluence_pages(space_key):
    """Liste alle Seiten in einem Confluence-Space auf."""
    url = f"{CONFLUENCE_BASE_URL}/rest/api/content"
    params = {
        "spaceKey": space_key,
        "type": "page",
        "limit": 50
    }

    response = requests.get(url, headers=headers, auth=auth, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Fehler: {response.status_code} - {response.text}")
        return None

print("Confluence-Seiten im WEG-Space:")
print("=" * 60)

result = list_confluence_pages("WEG")
if result:
    pages = result.get("results", [])
    print(f"Anzahl der Seiten: {len(pages)}\n")

    for page in pages:
        print(f"- Titel: {page['title']}")
        print(f"  ID: {page['id']}")
        print(f"  URL: {CONFLUENCE_BASE_URL}{page['_links']['webui']}")
        print()
else:
    print("Keine Seiten gefunden oder Fehler beim Abrufen.")
