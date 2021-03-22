def merge (dic1,dic2):
    return (dic1.update(dict2))
dict1={'a':10,'b':8}
dict2={'d':6,'c':4}
print(merge(dict1,dict2))
print(dict1)