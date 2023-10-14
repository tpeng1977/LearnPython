import sys

print(sys.version_info)
print(sys.version)
a=(b'h\x6fllo')
print(list(a))
print(a)

def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value

print(repr(to_str(b'foo')))
print(repr(to_str('bar')))

def to_bytes(bytes_or_str):
    if isinstance (bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value

print(repr(to_bytes(b'foo')))
print(repr(to_bytes('bar')))

print(b'one'+ b"two")
print('one'+'two')

#b'one'+ 'two'

assert b'red'>b'blue'
assert 'red'>'blue'
#assert 'red'>b'blue'
print(b'foo'=='foo')
print(b'red %s' % b'blue')
print('red %s' % 'blue')

#print(b'red %s' % 'blue')

print('red %s' % b'blue')


#with open('data.bin', 'w') as f:
with open('data.bin', 'wb') as f:
    f.write(b'\xf1\xf2\xf3\xf4\xf5')

#with open('data.bin', 'r') as f:
with open('data.bin', 'rb') as f:
    data = f.read()
assert data == b'\xf1\xf2\xf3\xf4\xf5'



