K = open("kitters.jpg", "rb").read()
C = open("cattos.jpg", "rb").read()

ans = ""
for k, c in zip(K, C):
  if k!=c:
    ans += c
print (ans)
