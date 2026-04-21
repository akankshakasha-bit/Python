class check:
    def __init__(self):
        print("address of self = ",id(self))

obj = check()
print("address of class object = ",id(obj))