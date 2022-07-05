def string2bits(s=''):
    return [bin(ord(x))[2:].zfill(8) for x in s]

def bits2string(b=None):
    return ''.join([chr(int(x, 2)) for x in b])

s = 'brayan'
b = string2bits(s)
s2 = bits2string(b)

print('String:')
print(s)

print ('\nList of Bits:')
c="0b"
for x in b:
    c=c+x
print(c)
print ('\nString:')
print (s2)