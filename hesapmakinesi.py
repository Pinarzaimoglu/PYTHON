while(True):
    işlem = input("Bir işlem yazın: ")
    if işlem.strip().lower()=="dur": break
    print(eval(işlem))
