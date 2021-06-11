def Inner():
    value="DIT"
    def Outer():
        import os
        print(os.getcwd())
        print('Value:'+value)
    Outer()

Inner()