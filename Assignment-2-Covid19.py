age = str(input("Are you addicted to cigarette and older than 75 years old?: (Yes/No) ")).title().strip()
chronic = str(input("Do you have severe chronic disease?: (Yes/No) ")).title().strip()
immune = str(input("Do you have weak immune system?: (Yes/No) ")).title().strip()

risk = age or chronic or immune

if risk == "Yes":
    print("You are in risky group")
else:
    print("You are not in risky group")

