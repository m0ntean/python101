def print_two(*args):
    argl, arg2 = args
    print(f"argl: {argl}, arg2: {arg2}")


def print_two_again(argl, arg2):
    print(f"argl: {argl}, arg2: {arg2}")


def print_one(argl):
    print(f"argl: {argl}")


def print_none():
    print("I got nothin' . ")


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()