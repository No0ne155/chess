class Pet():
    def __init__(self, name):
        self.name = name
    
    def changename(self):
        self.name = self.name.upper()

z = 3

hans = Pet('rudi')


def namenänder():
    global z
    hans.name = 'peterli'
    print(hans.name)
    z = 4
    print(z)

def namenscheck():
    print('namenscheck')
    if len(hans.name) == 4:
        return True


print('NOW TEST')
print('----------')

try:
    namenänder()
    if namenscheck() == False:
        print('forcingRuntime')
        raise RuntimeError("WrongName")
except:
    print(hans.name)
    print(z)


print('TEST Results')
print('----------')

print(hans.name)
print(z)