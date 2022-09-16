from docx import Document
import urllib.parse

import requests
from bs4 import BeautifulSoup

def get_yarn_links(text_find_enc):
    url = f'https://getyarn.io/yarn-find?text={text_find_enc}'
    r = requests.get(url)
    t = r.text

    l = []
    soup = BeautifulSoup(r.text, 'html.parser')
    clips = soup.find_all('a', {'class': 'p'})
    for c in clips:
        if 'href' in c.attrs:
            href = c['href']
            if href.startswith('/yarn-clip/'):
                l.append('https://getyarn.io' + href)
    return l


document = Document('1000 Phrases.docx')
url_base_youglish = 'https://youglish.com/pronounce/'

f = open('output.html', 'w', encoding="utf-8")

f.write('''<!DOCTYPE html>
<html>
<body>
''')
for i, par in enumerate(document.paragraphs):
    s = par.text.strip()
    s = s.replace('…', '')
    s = s.replace('.', '')
    s = s.replace('?', '')
    s = s.replace('!', '')
    if not s:
        continue

    f.write(f"<p>{i}. {s}<br>")

    text_find_enc = urllib.parse.quote(s)
    url_youglish = url_base_youglish + text_find_enc


    f.write(f"<a href='{url_youglish}' target='_blank'>[youglish]</a>&emsp;")

    l = get_yarn_links(text_find_enc)
    for j, link in enumerate(l):
        f.write(f"<a href='{link}' target='_blank'>[yarn. {j}]</a>&emsp;")

    f.write("</p>\n")
    print(i)



f.write('''
</body>
</html>''')

f.close()
