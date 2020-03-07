import hashlib,sys
color='\u001b[35;1m'
color1='\u001b[32;1m'
cend='\u001b[34;1m'
print(cend,'''
                                           MAKE A FUN WITH HASHES
        ''')
print(color)
######## ############## ##################
def md5(a):
    
    print(color1,hashlib.md5(a.encode('utf-8')).hexdigest(),color)
def sha1(a):
    print(color1,hashlib.sha1(a.encode('utf-8')).hexdigest(),color)
def sha224(a):
    print(color1,hashlib.sha224(a.encode('utf-8')).hexdigest(),color)
def sha256(a):
    print(color1,hashlib.sha256(a.encode('utf-8')).hexdigest(),color)
def sha384(a):
    print(color1,hashlib.sha384(a.encode('utf-8')).hexdigest(),color)
def sha512(a):
    print(color1,hashlib.sha512(a.encode('utf-8')).hexdigest(),color)
def help():
    print('help')
#################################################
try:
    while True:
        c=input('[HASH] ~> ')
        try:
            while c == 'md5':
                inp=input('[HASH/md5] ~> ')
                if inp == 'get':
                    inp=input('[HASH/md5/getting..] ~> ')
                    print(md5(inp))
                if inp == '..':
                    break
                elif inp == '':
                    z='z'
                else:   
                    help()
            while c == 'sha1':
                inp=input('[HASH/sha1] ~> ')
                if inp == 'get':
                    inp=input('[HASH/sha1/getting..] ~> ')
                    print(sha1(inp))
                if inp == '..':
                    break
            while c == 'sha224':
                inp=input('[HASH/sha224] ~> ')
                if inp == 'get':
                    inp=input('[HASH/sha224/getting..] ~> ')
                    print(sha224(inp))
                if inp == '..':
                    break
            while c == 'sha256':
                inp=input('[HASH/sha256] ~> ')
                if inp == 'get':
                    inp=input('[HASH/sha256/getting..] ~> ')
                    print(sha256(inp))
                if inp == '..':
                    break
            while c == 'sha384':
                inp=input('[HASH/sha384] ~> ')
                if inp == 'get':
                    inp=input('[HASH/sha384/getting..] ~> ')
                    print(sha384(inp))
                if inp == '..':
                    break
            while c == 'sha512':
                inp=input('[HASH/sha512] ~> ')
                if inp == 'get':
                    inp=input('[HASH/sha512/getting..] ~> ')
                    print(sha512(inp))
                if inp == '..':
                    break
            if c == '?':
                help()
        except:
            print('bye')
        if c == '..':
            break
except:
    print('bye')
