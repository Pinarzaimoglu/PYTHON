r = float(input("0 ile 4 arasında bir r paremetresi giriniz."))

print(0.1)

x = [0.1]

for i in range(1,100) :
    x.append( r * x[i-1] * (1 - x[i-1]) )

for i in range(100) :
   print(x)
