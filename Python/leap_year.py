year = int(input())

if year % 4 == 0 and year % 100 != 0 :
    print("This is a leap year")
else:
    print("This is not a leap year")