def hello():
    print("Hello")
    print("User")

hello()

def pack(x,y,z):
    return[x,y,z]

print(pack("x","y","x"))

def eat_lunch(lunch_list):
    if len(lunch_list) == 0:
        print("My lunchbox is empty")
    else:
        for x in range(len(lunch_list)):
            if x == 0:
                print(f"First I eat {lunch_list[0]}")
            else:
                print(f"Nect I eat {lunch_list[1]}")

eat_lunch([])
eat_lunch(["salad","sandwich"])