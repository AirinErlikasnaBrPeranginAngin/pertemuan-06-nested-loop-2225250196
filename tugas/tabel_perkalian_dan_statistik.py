n = int(input("n: "))

while n <= 0:
    n = int(input("n harus positif, masukkan lagi: "))

total = 0
count_even = 0

for i in range(1, n + 1):
    total_baris = 0

    for j in range(1, n + 1):
        hasil = i * j
        print(hasil, end=" ")
        
        total += hasil
        total_baris += hasil

        if hasil % 2 == 0:
            count_even += 1

    print(f" | Jumlah baris {i} = {total_baris}")

print(f"Total = {total}")
print(f"Banyak hasil genap = {count_even}")