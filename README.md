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

## Tracing

Tracing untuk n = 3 pada program 04_hitung_pasangan.py:

| i | j | i + j <= 3 | count |
|---|---|------------|-------|
| 1 | 1 | Ya         | 1     |
| 1 | 2 | Ya         | 2     |
| 1 | 3 | Tidak      | 2     |
| 2 | 1 | Ya         | 3     |
| 2 | 2 | Tidak      | 3     |
| 2 | 3 | Tidak      | 3     |
| 3 | 1 | Tidak      | 3     |
| 3 | 2 | Tidak      | 3     |
| 3 | 3 | Tidak      | 3     |

Hasil akhir:
Banyak pasangan = 3

## Efisiensi

Program menggunakan nested loop sehingga untuk nilai n, proses perkalian dilakukan sebanyak n × n kali. Kompleksitas waktunya adalah O(n²).

## Refleksi

Pada tugas ini saya belajar menggunakan nested loop untuk melakukan perulangan di dalam perulangan. Saya juga belajar menggunakan akumulasi untuk menghitung total dan pencacahan untuk menghitung banyak hasil yang memenuhi kondisi tertentu.

## Kuis Formatif

1. 24 iterasi.

2. Loop dalam kembali ke nilai awal setiap kali loop luar melakukan iterasi baru.

3. `print()` digunakan untuk pindah ke baris berikutnya pada pola simbol.

4. `total_baris` diinisialisasi di dalam loop luar, sebelum loop dalam dimulai.

5. `total_semua` diinisialisasi sebelum loop luar dimulai agar dapat mencakup seluruh pasangan.

6. Counter digunakan untuk menghitung banyaknya kejadian, sedangkan accumulator digunakan untuk menjumlahkan nilai.

7. 9 pasangan.

8. `if` digunakan untuk memeriksa kondisi pada setiap pasangan, kemudian counter ditambah jika kondisi terpenuhi.

9. `working tree clean` berarti tidak ada perubahan pada working tree yang belum di-commit.

10. Perintah yang digunakan adalah `git push`.