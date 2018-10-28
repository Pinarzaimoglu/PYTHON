sayi = int(input("Asallık testi yapmak istediğiniz sayıyı giriniz:"))

def asalmi(x) :
    i = 2
    while i*i <=x :
        if x % i == 0 :
             return False
        i += 1
    else :
        return True

print(asalmi(sayi))
