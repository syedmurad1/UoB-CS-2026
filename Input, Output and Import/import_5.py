from datetime import date

d = date(2022, 12, 25)
print(f"My DOB: {d}")

# date object of today's date
today = date.today() 

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)
