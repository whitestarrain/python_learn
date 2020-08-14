
class TempClass:
    def __init__(self, name):
        self.new_name = name
        self.temp = None
        self.__serect='serect'
        print(self.new_name)

    def testmethod(self):
        print(dir(self))

    def __str__(self):
        return self.new_name

    def __del__(self):
        print("被删除")


temp = TempClass('name')
print(temp.new_name)
print(temp)
print("%x" % id(temp))
del temp
print("-"*50)

print([TempClass('11'), TempClass('2')])

temp=TempClass('temp')
print(dir(temp))
print(temp._TempClass__serect)

