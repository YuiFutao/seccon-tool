print('type encorded string here, then I will return candidates.')
encorded_string = str(input())
for i in range(26):
    print ( i, ": " + "".join(chr((ord(x)-ord("a")+i)%26+ord("a")) for x in encorded_string) )
