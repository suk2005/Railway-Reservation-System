import re

def check_digit(data):
    pattern = r"\d+"
    if re.fullmatch(pattern, data):
        print("Data having only numeric value")
    else:
        print("Data having both value")

check_digit("123456")
check_digit("AB2345")

print()

import re

def check_digit(data):
    pattern = r"^[A-Z]"
    if re.match(pattern, data):
        print("Data having first Capital Letter")
    else:
        print("Data having not capital Letter")

check_digit("Abc")
check_digit("abc")

print()

import re

def check_vowel(data):
    vowel = re.findall(r"[aeiouAEIOU]", data)
    print("Character number:", len(vowel))

check_vowel("Hello data")

print()

def remove_space(data):
    output = re.sub(r"\s", "", data)
    print(output)

remove_space("Hello Data")

print()

phone_number = re.fullmatch(r"[6,9]\d{9}", number)

print()

emial = re.fullmatch(r"\w+@\w+\.\w+", data)

print()


