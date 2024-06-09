
# f.write("I love python")
# print(f.read())
# f.close() 

# for line in f: #line by line code iteration
  
#   print(line)

# f.close()

'''for line in f: #array of words
  tokens = line.split(' ')
  print(str(tokens))

f.close()'''


'''for line in f: #length of array of words
  tokens = line.split(' ')
  print(len(tokens))

f.close()'''
# f =  open("D:\\Desktop\\AI course\\Python with code basics\\files\\funny.txt", "r")
# f_out = open("D:\\Desktop\\AI course\\Python with code basics\\files\\funny_wc.txt", "w")
# for line in f: #length of array of words
#   tokens = line.split(' ')
#   f_out.write("wordcount: "+str(len(tokens))+line)


# f.close()
# f_out.close()


with open("D:\\Desktop\\AI course\\Python with code basics\\files\\funny.txt","r") as f:
  print(f.read())

print(f.closed)