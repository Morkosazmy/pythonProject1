def day_of_week(day):
    match day:
        case 1:
            return "Sunday"
        case 2:
            return"Monday"
        case 3:
            return"Tuesday"
        case 4:
            return"Wednesday"
        case 5:
            return"Thursday"
        case 6:
            return"Friday"
        case 7:
            return"Saturday"
        case _:
            return"NOT A VALID DAY "

print(day_of_week(1))
print(day_of_week(9))

def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case _:
            return False
print(is_weekend("Saturday"))
print(is_weekend("Sunday"))
print(is_weekend("Monday"))