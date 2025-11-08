#!/usr/bin/env python3
"""
Lädt alle Confluence-Seiten aus dem WEG-Space herunter und konvertiert sie zu Markdown.
"""

import requests
from requests.auth import HTTPBasicAuth
import os
import re
from pathlib import Path

# Konfiguration
JIRA_BASE_URL = os.getenv("JIRA_BASE_URL", "https://maierharry.atlassian.net")
CONFLUENCE_BASE_URL = f"{JIRA_BASE_URL}/wiki"
USERNAME = os.getenv("ATLASSIAN_USERNAME", "Maier.harry@gmail.com")
API_TOKEN = os.getenv("ATLASSIAN_API_TOKEN")

if not API_TOKEN:
    print("ERROR: ATLASSIAN_API_TOKEN environment variable not set!")
    print("Please set it with: export ATLASSIAN_API_TOKEN='your-token-here'")
    exit(1)

auth = HTTPBasicAuth(USERNAME, API_TOKEN)
headers = {"Accept": "application/json"}


def sanitize_filename(title):
    """Konvertiert einen Seitentitel in einen gültigen Dateinamen."""
    # Ersetze ungültige Zeichen
    filename = re.sub(r'[<>:"/\\|?*]', '-', title)
    # Ersetze mehrfache Leerzeichen/Bindestriche
    filename = re.sub(r'[-\s]+', '-', filename)
    # Entferne führende/trailing Bindestriche
    filename = filename.strip('-')
    return filename


def html_to_markdown_simple(html):
    """
    Einfache HTML-zu-Markdown-Konvertierung.
    Für bessere Ergebnisse könnte man 'markdownify' oder 'html2text' verwenden.
    """
    # Entferne HTML-Tags für eine einfache Textversion
    # In Produktion sollte man eine richtige Bibliothek wie markdownify verwenden
    text = html

    # Grundlegende Konvertierungen
    text = re.sub(r'<h1[^>]*>(.*?)</h1>', r'# \1\n', text, flags=re.DOTALL)
    text = re.sub(r'<h2[^>]*>(.*?)</h2>', r'## \1\n', text, flags=re.DOTALL)
    text = re.sub(r'<h3[^>]*>(.*?)</h3>', r'### \1\n', text, flags=re.DOTALL)
    text = re.sub(r'<h4[^>]*>(.*?)</h4>', r'#### \1\n', text, flags=re.DOTALL)
    text = re.sub(r'<h5[^>]*>(.*?)</h5>', r'##### \1\n', text, flags=re.DOTALL)
    text = re.sub(r'<h6[^>]*>(.*?)</h6>', r'###### \1\n', text, flags=re.DOTALL)

    text = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', text, flags=re.DOTALL)
    text = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', text, flags=re.DOTALL)
    text = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', text, flags=re.DOTALL)
    text = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', text, flags=re.DOTALL)

    text = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)', text, flags=re.DOTALL)

    text = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n\n', text, flags=re.DOTALL)
    text = re.sub(r'<br\s*/?>', '\n', text)
    text = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', text, flags=re.DOTALL)

    # Entferne verbleibende HTML-Tags
    text = re.sub(r'<[^>]+>', '', text)

    # HTML-Entities dekodieren
    text = text.replace('&nbsp;', ' ')
    text = text.replace('&amp;', '&')
    text = text.replace('&lt;', '<')
    text = text.replace('&gt;', '>')
    text = text.replace('&quot;', '"')
    text = text.replace('&ndash;', '–')
    text = text.replace('&mdash;', '—')
    text = text.replace('&auml;', 'ä')
    text = text.replace('&ouml;', 'ö')
    text = text.replace('&uuml;', 'ü')
    text = text.replace('&Auml;', 'Ä')
    text = text.replace('&Ouml;', 'Ö')
    text = text.replace('&Uuml;', 'Ü')
    text = text.replace('&szlig;', 'ß')

    # Bereinige mehrfache Zeilenumbrüche
    text = re.sub(r'\n{3,}', '\n\n', text)

    return text.strip()


def get_all_pages(space_key, limit=100):
    """Ruft alle Seiten aus einem Confluence-Space ab."""
    all_pages = []
    start = 0

    while True:
        url = f"{CONFLUENCE_BASE_URL}/rest/api/content"
        params = {
            "spaceKey": space_key,
            "type": "page",
            "limit": limit,
            "start": start,
            "expand": "body.storage,version"
        }

        response = requests.get(url, headers=headers, auth=auth, params=params)

        if response.status_code != 200:
            print(f"Fehler beim Abrufen der Seiten: {response.status_code}")
            break

        data = response.json()
        results = data.get("results", [])

        if not results:
            break

        all_pages.extend(results)

        # Prüfe, ob es weitere Seiten gibt
        if len(results) < limit:
            break

        start += limit

    return all_pages


def save_page_as_markdown(page, output_dir):
    """Speichert eine Confluence-Seite als Markdown-Datei."""
    title = page['title']
    page_id = page['id']
    html_content = page['body']['storage']['value']
    version = page['version']['number']

    # Konvertiere HTML zu Markdown
    markdown_content = html_to_markdown_simple(html_content)

    # Erstelle Frontmatter
    frontmatter = f"""---
title: {title}
confluence_id: {page_id}
version: {version}
url: {CONFLUENCE_BASE_URL}{page['_links']['webui']}
---

"""

    full_content = frontmatter + markdown_content

    # Erstelle Dateinamen
    filename = sanitize_filename(title) + '.md'
    filepath = output_dir / filename

    # Speichere Datei
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(full_content)

    return filepath


def main():
    print("=" * 70)
    print("Confluence → Markdown Export")
    print("=" * 70)

    # Erstelle Output-Verzeichnis
    output_dir = Path("confluence_export")
    output_dir.mkdir(exist_ok=True)
    print(f"\nOutput-Verzeichnis: {output_dir.absolute()}")

    # Hole alle Seiten
    print(f"\nRufe Seiten aus dem WEG-Space ab...")
    pages = get_all_pages("WEG")
    print(f"✅ {len(pages)} Seiten gefunden")

    # Konvertiere und speichere jede Seite
    print(f"\nKonvertiere Seiten zu Markdown...")
    for i, page in enumerate(pages, 1):
        title = page['title']
        filepath = save_page_as_markdown(page, output_dir)
        print(f"  [{i}/{len(pages)}] {title}")
        print(f"           → {filepath.name}")

    print(f"\n{'=' * 70}")
    print(f"✅ Export abgeschlossen!")
    print(f"   {len(pages)} Seiten wurden nach {output_dir.absolute()} exportiert")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    main()
