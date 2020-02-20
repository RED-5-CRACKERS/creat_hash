#
#
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
            elif a == 'help':
                print("sha1    : moves sha1 hash folder")
                print('md5    : moves md5 hash folder')
                print('..     : go back')
                print('get    : ready to get the input')
                print('help/? : this banner will appear ')
                print("exit   : exit")
            elif a == '':
                print('Hash/md5/:> ')
            else:
                print("Error: no 'get' specefied")
                print('use get comment')
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
            elif a == 'help':
                print("sha1    : moves sha1 hash folder")
                print('md5    : moves md5 hash folder')
                print('..     : go back')
                print('get    : ready to get the input')
                print('help/? : this banner will appear ')
                print("exit   : exit")
            elif a == '':
                print('Hash/sha1/:> ')
            else:
                print("Error: 'get' unspecefied ")
    elif b == 'exit':
        break
    elif b == 'help':
        print("sha1    : moves sha1 hash folder")
        print('md5    : moves md5 hash folder')
        print('..     : go back')
        print('get    : ready to get the input')
        print('help/? : this banner will appear ')
        print("exit   : exit")
    elif b == '':
        print('Hash/:> ')

    else:
        print()
        print()
        print('Invalid  !^        operator.')
        print('See at help or ? .' )
