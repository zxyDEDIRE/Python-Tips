
class MyClass:

    def Bfo(self):
        print('b')


    @classmethod
    def Afo(cls):
        print("a")

    @classmethod
    def doit(cls):
        print("sdf")
        cls.Afo()



if __name__ == '__main__':
    MyClass.doit()