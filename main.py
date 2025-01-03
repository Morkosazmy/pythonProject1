# Exception handling ( try, except, finally )
# try ( try some code )
# except (
# ZeroDivisionError ( divide by zero )
# ValueError ( enter a string in an int input )
# TypeError (
inter = "3"
try:
    number = int(input("Enter a number "))
    print(1 / number)
#    print(1 / inter)
except ZeroDivisionError:
    print("Cant divide by zero !")
except ValueError:
    print("Cant divide by a string !")
except TypeError:
    print("inter must be an integer/double and not a string !")

except Exception:
    print("Something went wrong")

finally:
    print("we are done here ! ")