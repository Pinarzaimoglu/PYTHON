while True : 
    
    x = input("Bir sayı giriniz : ")
    karakter = 'a'
    if x == karakter :
        break;
    if not x:
        break
    try :
        y = float(x)
    except ValueError :
        print("Geçersiz.")
        continue
    print(y**2)
