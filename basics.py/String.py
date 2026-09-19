w = "hello welcome back";
# Slicing
print(w[0:8])
print(w[-1::-1])
print(w[6:13])

# iteration in string
print(" ")
t=len(w)
print(t)
for a in range(t):
    print(w[a])

# reverse iteration
w=w[-1::-1]
for a in range(len(w)):
    print(w[a])

for a in range(t-1,-1,-1):
    print(w[a])

for a in w:
    print(a)