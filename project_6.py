print('Hello and welcome to personal journal manager')
print(end="\n")
print(end="\n")
print(end="\n")

class JournalManager:
    def __init__(self):
        self.f=open('C:\\Users\\Admin\\Desktop\\journal.txt','r+')
        while True:
            print('select a option')
            print('1.add a entry')
            print('2.view a entry')
            print('3.search entry')
            print('4.delete')
            print('5.exit')
            a=int(input('Enter your choice: '))
            
            try:
                if a==1:
                    try:
                        write=input('Enter the entry')
                        self.f.write(write)
                        print('Entry added succesfully!')
                    except:
                        print('entry is not added')
                
                elif a==2:
                    try:
                        print('your journal entries:')
                        print(self.f.read())
                    except:
                        print('file not found')
                
                elif a==3:
                    try:
                        e=input('enter a keyword to search: ')
                        if e in self.f:
                            print(self.f.readline(e))
                        else:
                            print('no keyword found')
                    except:
                        print('file not found')
                elif a==4:
                    try:
                        d=input('are you sure you wanna delete all entries?(yes/no): ')
                        if d=='yes':
                            del(self.f)
                        elif d=='no':
                            continue
                    except:
                        print('invalid syntax')
                elif a==5:
                    print('Thank you for using Employee management system , hope you liked it')
                    print('    __________                                                     ___             ')
                    print('         |     |     |     /\      |\   |   | /          \   /    /   \    |      |')
                    print('         |     |_____|    /__\     | \  |   |/            \ /    |     |   |      |')
                    print('         |     |     |   /    \    |  \ |   |\             |     |     |   |      |')
                    print('         |     |     |  /      \   |   \|   | \            |      \___/     \____/ ') 
                    break
            except:
                print('invalid number')
g=JournalManager()
print(g)