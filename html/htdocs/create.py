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
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">메인화면</a></h1>
  <ol>
      {listStr}
  </ol>
  <a href="create.py"><문의하기></a>
  <form action="processCreate.py" method="post">
    <p><input type="text" name="title" placeholder="title"></p>
    <p><textarea rows="4" name="description" placeholder="description"></textarea></p>
    <p><input type="submit"></p>
  </form>
</body>
</html>
'''.format(title=pageId, desc =description, listStr=listStr))
#form은 url query string의 생성자
#method를 사용하지 않으면 get 방식으로 사용한다. post로 해야 노출되지 않는다