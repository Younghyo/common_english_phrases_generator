from docx import Document
import urllib.parse

document = Document('1000 Phrases.docx')
url_base = 'https://youglish.com/pronounce/'

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
    q = urllib.parse.quote(s)

    url = url_base + q
    #print(s, q, url)
    f.write(f"<p><a href='{url}' target='_blank'>{i}. {s}</a></p>\n")

f.write('''
</body>
</html>''')

f.close()
