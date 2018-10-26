k= int(input("İlk kaç asal sayıyı görmek istersin?"))

sayac=0
x=2

while sayac!=k :
	i=2
	while i*i<=x :
		if x%i==0 :
			break
		i+=1
	else :
		print(x)
		sayac +=1
	x += 1
