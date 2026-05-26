names_str = "john, doe, alice, bob"
names = names_str.split(",")

for name in names:
    str = name.strip()
    print(str.capitalize())