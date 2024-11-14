import time


def total(*args):
    total = 0
    for arg in args:
        total += arg
    return total
#print(total(1,2,3,4,5))

def address(**kwargs):
    address = ""
    for key, value in kwargs.items():
        print(f"{key} : {value}")

#address(street_no = "123", street_name = "rue de blabla", commune = "Paris", pays = "France")
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
   # for value in kwargs.values(): # we can use for key, value in kwargs.items() as well !
    print(f"{kwargs.get('street_no')} {kwargs.get('street_name')}")
    if "code_postal" in kwargs:
        print(f"{kwargs.get('code_postal')} {kwargs.get('commune')} {kwargs.get('pays')}")
    else:
        print(f"{kwargs.get('commune')} {kwargs.get('pays')}")

    print()

print()

shipping_label("Dr.","Spongebob","Squarepants","III",street_no = "123", street_name = "rue de blabla",code_postal="75000", commune = "Paris", pays = "France")