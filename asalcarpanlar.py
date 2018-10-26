sayi = int(input("Asal çarpanlarını görmek istediğiniz sayıyı yazınız."))
x=2

while sayi > 1:
	asal = True
	i=2
	while i*i <=x :
		if x%i==0 :
			asal = False
			break
		i+=1
	if asal and sayi%x == 0 :
		print(x,end=" ")
		while sayi%x == 0 :
			sayi= sayi/x
	x+=1
