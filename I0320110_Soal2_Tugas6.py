x = int(input("Banyak data: "))

data = []
jumlah = 0
for y in range(0,x):
    nilai = int(input("Masukkan nilai ke-%d: " % (y+1)))
    data.append(nilai)
    jumlah += data[y]

    rata_rata = jumlah/x
print(float(rata_rata))