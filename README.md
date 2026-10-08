# Pertemuan 6 - Nested Loop

Nama: Airin Erlikasna Br Perangin Angin
NIM: 2225250196
Kelas: Pendidikan Matematika

## Tujuan
Mempelajari penggunaan nested loop, pola, akumulasi, dan pencacahan dalam Python.

## Cara Menjalankan

Buka terminal pada folder repository, lalu jalankan:

python tugas/tabel_perkalian_dan_statistik.py

## Algoritma

1. Meminta input bilangan n.
2. Memastikan n merupakan bilangan positif.
3. Menggunakan nested loop untuk membuat tabel perkalian n × n.
4. Menghitung total seluruh hasil perkalian.
5. Menghitung banyak hasil perkalian yang genap.
6. Menghitung jumlah hasil perkalian pada setiap baris.

## Pengujian

| Input n | Banyak pasangan | Total | Hasil genap | Status |
|--------:|----------------:|------:|------------:|--------|
| 1       | 1               | 1     | 0           | Berhasil |
| 2       | 4               | 9     | 3           | Berhasil |
| 3       | 9               | 36    | 5           | Berhasil |

## Efisiensi

Program menggunakan nested loop sehingga untuk nilai n, proses perkalian dilakukan sebanyak n × n kali. Kompleksitas waktunya adalah O(n²).

## Refleksi

Pada tugas ini saya belajar menggunakan nested loop untuk melakukan perulangan di dalam perulangan. Saya juga belajar menggunakan akumulasi untuk menghitung total dan pencacahan untuk menghitung banyak hasil yang memenuhi kondisi tertentu.