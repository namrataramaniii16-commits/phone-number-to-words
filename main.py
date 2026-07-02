phone = input("Enter your phone number: ")

number_names = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
}

output = ""

for digit in phone:
    output += number_names.get(digit, "!") + " "

print(output)
