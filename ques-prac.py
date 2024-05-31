#classify a person age group 
#child(<13)   teenager (14-19) adult(20-59)  senior(59+)
age=15
if age<13:
    print("child")
elif age<19:
    print("Teenager")
elif age<59:
    print("Adult")
else:
    print("Senior")

#movie tickets prices are based on age group Rs.600 for adult(18 and over)
#and Rs.200 for childrens.Everyoe gets 20rs discount on wednesday.

age=25
day="Thursday"
price=600 if age>=18 else 200
if day=="Wednesday":
    price=price-20
print("The ticket price for you is Rs.",price)