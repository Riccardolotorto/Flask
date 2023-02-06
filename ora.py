import datetime 
adesso = datetime.datetime.now().time()
print(adesso.hour)

if adesso.hour > 11:
    print("Buonasera")
else:
    print("Buongiorno")