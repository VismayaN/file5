l=input("enter the names")
word=l.split()
print(word)
count=0
for i in l:
    if i=="a":
        count+=1
        print("the ocurance of a is",count)