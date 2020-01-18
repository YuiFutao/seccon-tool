print('investigate 2 local files DIFF. plz type filename in me.')

K = open("kitters.jpg", "rb").read()
C = open("cattos.jpg", "rb").read()

ans = ""
for k, c in zip(K, C):
  if k!=c:
    ans += chr(c)
print (ans)
