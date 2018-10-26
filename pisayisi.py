toplam = 0.0 # ara toplam
isaret = 1 # +1 veya -1 olarak dönüşümlü olarak değişecek
payda = 1.0  # 1,3,5,7,...
terim = isaret / payda
sayac = 1
while abs(terim) > 0.00001:
    toplam += terim
    payda += 2
    isaret *= -1
    terim = isaret / payda
    sayac += 1

print("pi ~", 4*toplam)
print(sayac,"terim toplandı.")
