members = ['admin', 'DX', 'WGZ', 'XZY', 'WXK']
for member in members:
    if member == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello Eric, thank you for logging in again")

# 5-9
members = []
if members:
    for member in members:
        print("Adding" + member + ".")
        print("\nWe need to find some users!")
else:
    print("We need to find some users!")

