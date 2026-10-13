import re

text = "My Contact Number is 8276568656"

output = re.findall(r"[\d+]", text)

print(output)

print()

import re

text = "My Contact Number is 8276568656"

output = re.findall(r"[\D+]", text)

print(output)

print()

import re

def validate_pnr(pnr):
    pattern = r"^\d{8}$"
    if re.fullmatch(pattern, pnr):
        print("Valid PNR:", pnr)
    else:
        print("Invalid PNR:", pnr)

validate_pnr("12345678")
validate_pnr("876756459")

