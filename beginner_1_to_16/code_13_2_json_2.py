Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> f = open(""D:\\Desktop\\AI course\\Python with code basics\\files\\book.txt","r")
...          
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> f = open("D:\\Desktop\\AI course\\Python with code basics\\files\\book.txt","r")
...          
>>> s=f.read()
...          
>>> s
...          
'{"tom": {"name": "tom", "address": "1 red street,NY", "phone": 123456}, "bob": {"name": "bob", "address": "1 green street,NY", "phone": 654321}}'
>>> print(s)
...          
{"tom": {"name": "tom", "address": "1 red street,NY", "phone": 123456}, "bob": {"name": "bob", "address": "1 green street,NY", "phone": 654321}}
>>> 
>>> import json
>>> json.loads(s)
{'tom': {'name': 'tom', 'address': '1 red street,NY', 'phone': 123456}, 'bob': {'name': 'bob', 'address': '1 green street,NY', 'phone': 654321}}
>>> book = json.loads(s)
>>> print(book)
{'tom': {'name': 'tom', 'address': '1 red street,NY', 'phone': 123456}, 'bob': {'name': 'bob', 'address': '1 green street,NY', 'phone': 654321}}
>>> book['bob']
{'name': 'bob', 'address': '1 green street,NY', 'phone': 654321}
>>> book['bob']['phine']
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    book['bob']['phine']
KeyError: 'phine'
>>> book['bob']['phone']
654321
>>> for person in book:
...     print(book[person])
... 
    
{'name': 'tom', 'address': '1 red street,NY', 'phone': 123456}
{'name': 'bob', 'address': '1 green street,NY', 'phone': 654321}

