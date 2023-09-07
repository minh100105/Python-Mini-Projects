# USD -> VND
def usdvnd(usdvalue):
    usd = float(usdvalue)
    vnd = usd * 23500
    return print("đ", vnd)
    
# VND -> USD
def vndusd(value):
    vnd = float(value)
    usd = vnd / 23500
    return print("$", usd)

money = input("Which country do you want to convert from into USD?\n VND \n JD\n")
if money == "VND" or money == "vnd":
    value = input("Please enter the amount of money you want to convert into USD\nđ")
    value = float(value)
    vndusd(value)
    
    usconversion = input("Do you want to convert VND into USD? Please respond with Yes(Y) or No(N)\n")
    if usconversion == 'Y' or 'y':
        usdvalue = float(input("Please enter the amount of USD money you wish to convert into VND\n$"))
        usdvnd(usdvalue)
        print("Thank you for converting with us!")
    elif usconversion == 'N' or 'n':
        print("Thank you for converting with us!")
    else:
        usconversion = input("Please enter Yes(Y) or No(N)")
        if usconversion == 'Y' or 'y':
            usdvalue = float(input("Please enter the amount of USD money you wish to convert into VND\n"))
            usdvnd(usdvalue)
            print("Thank you for converting with us!")
        else:
            print("Thank you for converting with us!")
    
        
