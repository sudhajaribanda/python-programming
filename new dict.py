dict_a={"A":"Helloo","B":"World","C":"Buddy"}
keys=[]
values=[]
for key,value in dict_a.items():
    keys.append(key)
    values.append(value)
print(keys)
print(values)
a=keys[0] in dict_a
b=keys[1] in dict_a
c=keys[2] in dict_a
if a and b and c:
    index=values[0]+values[1]+values[2]
    print(index)
if a and b:
    index=values[0]+values[1]
    print(index)

if b and c:
    index=values[1]+values[2]
    print(index)
    
if a and c:
    index=values[0]+values[2]
    print(index)

if a or b:
    if a:
        index=values[0]
    else:
        index=values[1]
    print(index)
if b or c:
    if b:
        index=values[1]
    else:
        index=values[2]
    print(index)
if c or a:
    if c:
        index=values[2]
    else:
        index=values[0]
    print(index)
if a and (b or c):
    if b:
        index=values[0]+values[1]
    else:
        index=values[0]+values[2]
print(index)
if a and (c or d):
    if c:
        index=values[0]+values[2]
    else:
        index=values[0]
print(index)
if a and (b or d) and c:
    if b:
        index=values[0]+values[1]+values[2]
    else:
        index=values[0]+values[1]+values[2]
print(index)