#classes private,public,protected

class PrivateAccessError(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class A:
    __a = None  # Private
    _b = None   # Protected
    c = None    # Public
    
    def __init__(self, a, b, c):
        self.__a = a
        self._b = b
        self.c = c
    
    def display(self):
        print("a =", self.__a)
        print("b =", self._b)
        print("c =", self.c)

class B(A):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)
    
    def display(self):
        print("Display of class")

        try:
            if self._A__a == self._A__a:  # accessing private member using name mangling
                raise PrivateAccessError("Private member cannot be accessed.")
            else:
                print("a =", self._A__a)
        except PrivateAccessError as pae:
            print(f"{type(pae).__name__} : {pae.args[0]}")

        print("b =", self._b)
        print("c =", self.c)
        print()
        print("Display of class")
        super().display()

# Test the classes
b = B(50, 36, 65)
b.display()
