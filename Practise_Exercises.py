def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as ex:
        print(f"an error occured: {ex}")
    except:
        print("unknown error occured!")


#print(divide(4, 0))

#divider = input()
#print(divide(4, divider))

file = None
try:
    file = open(r"C:\tmp\abracadabra.txt")
    data = file.read()
except FileNotFoundError as ex:
    print(f"Error has occured. Description: {ex.strerror}")
else:
    print("maybe else")
finally:
    print("Finally")
    if file:
        file.close()

print("doing some work here")


def get_int():
    while True:
        try:
            reply = int(input("Enter a number..."))
            print("Thanks!")
            return reply
        except:
            print("Not a number!! Try again.")
            continue


number = get_int()
