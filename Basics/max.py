words=['Hello','world','Test','Logging','Simplefied','Auto','Satisfied_']
x=max(words,key=len)
y=min(words,key=len)
print(x,'-',y)
l=[m for m in words if len(x)==len(m)]
print(l)