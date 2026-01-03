x = 10  # global

def modify():
    global x
    x = 20
    print("Inside:", x)

modify()
print("Outside:", x)
