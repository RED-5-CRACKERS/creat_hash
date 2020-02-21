#
#
print("                        🇭 🇦 🇸 🇭 -🇨 🇷 🇪 🇦 🇹 🇪 🇷                                               ")
#crear a hases 
az='y'
while az is 'y':
    import hashlib
    b=input('Hash/:> ')
    if b == 'md5':
        while b == 'md5':
            a=input('Hash/md5/:> ')
            if a == 'get' :
                c=input('Hash/md5/getting:> ')
                print('Hash/md5/:> ',hashlib.md5(c.encode('UTF-8')).hexdigest())
            elif a == '..':
                break
            elif a == 'exit':
                b=a
                break
            elif a == '?':
                print("sha1,sha224,sha256,sha384  ")
                print('sha512 : algorithm   ')
                print('..     : go back')
                print('get    : ready to get the input')
                print('?      : this banner will appear ')
                print("exit   : exit")
            elif a == '':
                print('Hash/md5/:> ')
            else:
                print("Error: 'get' unspecefied, use: ?")
    elif b == 'sha1':
        while b == 'sha1':
            a=input('Hash/sha1/:> ')
            if a == 'get':
                c=input('Hash/sha1/getting:> ')
                print('Hash/sha1/:> ',hashlib.sha1(c.encode('UTF-8')).hexdigest())
            elif a == '..':
                break
            elif a == 'exit':
                break
            elif a == '?':
                print("sha1,sha224,sha256,sha384  ")
                print('sha512 : algorithm   ')
                print('..     : go back')
                print('get    : ready to get the input')
                print('?      : this banner will appear ')
                print("exit   : exit")
            elif a == '':
                print('Hash/sha1/:> ')
            else:
                print("Error: 'get' unspecefied, use ? ")
    elif b == 'exit':
        break
    elif a == '?':
                print("sha1,sha224,sha256,sha384  ")
                print('sha512 : algorithm   ')
                print('..     : go back')
                print('get    : ready to get the input')
                print('?      : this banner will appear ')
                print("exit   : exit")
    elif b == '':
        print('Hash/:> ')
    elif b == 'sha224':
        while b == 'sha224':
            a=input('Hash/sha224/:> ')
            if a == 'get':
                c=input('Hash/sha224/getting:> ')
                print('Hash/sha224:> ',hashlib.sha224(c.encode('UTF-8')).hexdigest())
            elif a == '..':
                break
            elif a == '':
                print('Hash/sha224:> ')
            elif a == '?':
                print("sha1,sha224,sha256,sha384  ")
                print('sha512 : algorithm   ')
                print('..     : go back')
                print('get    : ready to get the input')
                print('?      : this banner will appear ')
                print("exit   : exit")
            else:
                print('Error : 'get' unspecified ,use ? ') 
         
    elif b == 'sha256':
        while b == 'sha256':
            a=input('Hash/sha256/:> ')
            if a == 'get':
                c=input('Hash/sha256/getting:> ')
                print('Hash/sha256/:> ',hashlib.sha265(c.encode('UTF-8')).hexdigest())
            elif a == '..':
                break
            elif a == 'exit':
                break
            elif a == '?':
                print("sha1,sha224,sha256,sha384  ")
                print('sha512 : algorithm   ')
                print('..     : go back')
                print('get    : ready to get the input')
                print('?      : this banner will appear ')
                print("exit   : exit")
            elif a == '':
                print('Hash/sha256/:> ')
            else:
                print("Error: 'get' unspecefied, use : ? ")
    elif b == 'sha384':
        while b == 'sha384':
            a=input('Hash/sha384/:> ')
            if a == 'get':
                c=input('Hash/sha384/getting:> ')
                print('Hash/sha384/:> ',hashlib.sha384(c.encode('UTF-8')).hexdigest())
            elif a == '..':
                break
            elif a == 'exit':
                break
            elif a == '?':
                print("sha1,sha224,sha256,sha384  ")
                print('sha512 : algorithm   ')
                print('..     : go back')
                print('get    : ready to get the input')
                print('?      : this banner will appear ')
                print("exit   : exit")
            elif a == '':
                print('Hash/sha384/:> ')
            else:
                print("Error: 'get' unspicified , use: ? ")
    elif b == 'sha512':
        while b == 'sha512':
            a=input('Hash/sha512/:> ')
            if a == 'get':
                c=input('Hash/sha512/getting:> ')
                print('Hash/sha512/:> ',hashlib.sha512(c.encode('UTF-8')).hexdigest())
            elif a == '..':
                break
            elif a == 'exit':
                break
            elif a == '?':
                print("sha1,sha224,sha256,sha384  ")
                print('sha512 : algorithm   ')
                print('..     : go back')
                print('get    : ready to get the input')
                print('?      : this banner will appear ')
                print("exit   : exit")
            elif a == '':
                print('Hash/sha512/:> ')
            else:
                print("Error: 'get' unspecified, use : ? ")
    else:
        print("Error: 5035 ")
        print("use '?' to help ")
