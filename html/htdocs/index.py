#!/usr/bin/env python3 
print("Content-Type: text/html")
print()
import cgi, os
files = os.listdir('data')
listStr = ''
for item in files:
  listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId,'r').read()

else:
    pageId = '메인화면'
    description = '메인을 설명하는 본문입니다'
print('''<!doctype html>
<html>
<head>
  <title>LG display 성과급200%</title>
  <meta charset="utf-8">
  <link type="text/css" rel="stylesheet" href="/styles.css" />
</head>
<body>
  <h1><a href="index.py">메인화면</a></h1>
  <ol>
      {listStr}
  </ol>
  <a href="create.py"><문의하기></a>
  <h2>{title}</h2>
  <p>{desc}</p>
</body>
</html>
'''.format(title=pageId, desc =description, listStr=listStr))
