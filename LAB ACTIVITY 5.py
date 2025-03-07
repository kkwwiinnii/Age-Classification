#custom function
def classify_age(x):
    if x > -1:
        if x <= 12:
            print("You are a Child.")
        elif x <= 19:
            print("You are a Teen.")
        elif x <= 64:
            print("You are an Adult.")
        elif x >= 65:
            print("You are a Senior.")
        else:
            print("You have entered an invalid age number.")
    else:
        print("You have entered an invalid age number.")


#main code
age = int(input("Enter your age: "))
classify_age(age)

while True:
    a = input("Run again? (yes/no): ")
    if a == "yes":
        age = int(input("Enter your age: "))
        classify_age(age)
    else:
        print("Exiting Program.")
        break