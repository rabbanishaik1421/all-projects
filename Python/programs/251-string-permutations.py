'''
c'''
string = "123"
string = "1234"
string= str(string)
i=0
perm = set()
while i<len(string):
    dupstring = string
    dupstring = dupstring.replace(string[i], "")
    mstr = string[i]+""+dupstring
    rstr = string[i]+""+dupstring[::-1]
    perm.add(mstr)
    perm.add(rstr)
    i+=1
    
perm = sorted(perm)
for p in perm:
    print(p)