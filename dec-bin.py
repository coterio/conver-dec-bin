from time import sleep
import os
def error():
    os.system("clear")
    print("Digite um número válido!")
    sleep(1)
    os.system("clear")
def test_n(n1):
    n1 = int(n1)
def clean():
    os.system("clear")
while(True):
    try:
        decbin = input("Meio de conversão:\n\nDecimal > Binário(1)\nBinário > Decimal(2)\n\nA: ")
        n1 = decbin
        test_n(n1)
    except ValueError:
        error()
    if(decbin == "1"):
        while(True):
            try:
                clean()
                num = int(input("Digite seu numero!\n\nA: "))
                val = num
                break
            except:
                error()
                continue
        bin = " "
        while(num != 0):
            div = int(num/2)
            resu = int(num % 2)
            num = div
            bin = f"{bin}{resu}"
            bino = str(bin)
            bino = bino[::-1]
        sleep(1)
        clean()
        print(f"Decimal: {val}\nBinário: {bino}\n")
    elif(decbin == "2"):
        while(True):
            try:
                clean()
                num = input("Digite seu número!\n\nA: ")
                bino = num[::-1]
                test = int(num)
                value  = len(num)
                break
            except:
                error()
                continue
        resu = 0
        n = 0
                    # n . 2ⁿ
        for i in range(0, value):
            n = int(bino[i]) * 2 ** (i-1)
            n += n
            resu += n
        clean()   
        print(f"R: {resu}")
    procede = input("\nIrá calcular novamente?(s/n)\n\nA: ")
    if(procede != "n"):
        clean()
        continue
    else:
        break
