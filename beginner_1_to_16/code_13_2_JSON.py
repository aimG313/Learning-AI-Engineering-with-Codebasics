book = {}
book['tom']={
  'name':'tom',
  'address':'1 red street,NY',
  'phone': 123456
}
book['bob']={
  'name':'bob',
  'address':'1 green street,NY',
  'phone': 654321
}

import json
s=json.dumps(book)
print(s)


import json
s = json.dumps(book)
print(s)

with open("D:\\Desktop\\AI course\\Python with code basics\\files\\book.txt","w") as f:

  f.write(s)



