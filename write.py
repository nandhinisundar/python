f=open("d:\modules\fun.py",w)
str=f.read()
print(str)
print(f.name)
print(f.mode)
print(f.closed)
f.write("hi python\n")
print(f.read(4))
print(f.seek(5,0))
print(f.read(10))
print(f.tell())
