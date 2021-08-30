#Python Program to Convert Decimal to Hexadecimal
"Computer Programming Tutor, Aug 30,2021"

def decimalToHexa(n):
    hexaDec = ["0"]*100
    i = 0
    while(n !=0):
        tmp = 0
        tmp = n% 16
        if(tmp < 10):
            hexaDec[i] = chr(tmp + 48)
            i = i + 1
        else:
            hexaDec[i] = chr(tmp +55)
            i = i + 1
        n = int(n / 16)
    j = i -1
    while(j >= 0):
        print((hexaDec[j]),end="")
        j = j - 1

n = int(input("Enter an Integer Number: "))
print("The Equivalent Hexadecimal Number is: ",end="")
decimalToHexa(n)
