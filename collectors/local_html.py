"""COLLECTOR: parses tender rows from an HTML table using BeautifulSoup (local demo only)."""

from bs4 import BeautifulSoup


def parse_local_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    out = []
    for tr in soup.select('tr[data-tender-id]'):
        cells = [x.get_text(' ', strip=True) for x in tr.select('td')]
        if len(cells) >= 2:
            out.append(
                {
                    'tender_id': tr.get('data-tender-id'),
                    'tender_title': cells[0],
                    'organization': cells[1],
                }
            )
    return out


# Demonstrates permitted HTML parsing only; no automated government portal access is claimed.
