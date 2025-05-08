print("program menghitung segitiga dan persegi panjang")
print("=**=* menu =*=*=* \n 1. Menghitung Segitiga \n 2. Menghitung Persegi Panjang \n =*=*=*=*=*=*=*")

userinput = int(input("pilih menu: "))
if userinput == 2:
    print ("menghitung persegi")
    inputpanjang = int(input("masukan panjag = "))
    inputlebar = int(input("masukan lebar = "))
    luas = inputpanjang * inputlebar
    print(f"hasildari {inputpanjang} x {inputlebar} = {luas}")
elif userinput == 1:
    print("menghitung segitiga")
    inputalas = int(input("masukan alas = "))
    inputtinggi = int(input("masukam tinggi = "  ))
    hasil = 0.5 * inputalas * inputtinggi 
    print( f"hasil dari {inputalas} x {inputtinggi} = {hasil}")
else:
    print("input tidak valid")
