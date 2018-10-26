istenen = int(input("Pozitif bir tamsayı giriniz:"))

x = 2

while x <= istenen :
	i = 2
	while i*i <= x :
		if x%i == 0:
			break
		i += 1
	else :
		print(x)
	x += 1
