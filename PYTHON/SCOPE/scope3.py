text="Hello from Python"

def Function():
    global text
    print(f'Text before reassignment:{text}')
    text="Text Change:DIT UOI"

Function()
print(text)