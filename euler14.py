enb = 1

for n in range(1000001) :
    listem = []
    karsilastir=n
    while n>1 : 
        if n%2 == 0 :
            n = n/2
            listem.append(n) 
        else :
             n = n*3 +1
             listem.append(n)
    if len(listem) > enb :
             enb = karsilastir

print(int(enb))
