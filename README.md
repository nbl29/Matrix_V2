# Matrix Operations with AI

Program operasi matriks dengan implementasi AI untuk analisis pola dan clustering. Program ini dibuat menggunakan Python dan memanfaatkan beberapa library seperti NumPy, scikit-learn untuk operasi matematika dan analisis data.

## Fitur

- Input dan manipulasi matriks
- Operasi dasar matriks (penjumlahan, pengurangan, perkalian)
- Transpose matriks
- Perhitungan determinan
- Penyelesaian sistem persamaan linear
- Analisis AI:
  - Prediksi pola matriks
  - Clustering data matriks

## Persyaratan Sistem

- Python 3.x
- NumPy
- scikit-learn

## Instalasi

### Untuk PC/Laptop

1. Clone repository ini
```bash
git clone https://github.com/[username]/matrix-operations.git
cd matrix-operations
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Jalankan program
```bash
python main.py
```

### Untuk Termux (Android)

1. Update dan upgrade package
```bash
pkg update && pkg upgrade
```

2. Install Python dan pip
```bash
pkg install python pip
```

3. Clone repository
```bash
git clone https://github.com/[username]/matrix-operations.git
cd matrix-operations
```

4. Install dependencies
```bash
pip install -r requirements.txt
```

5. Jalankan program
```bash
python main.py
```

## Penggunaan

1. Pilih menu yang tersedia (1-11)
2. Untuk input matriks:
   - Masukkan jumlah baris dan kolom
   - Input nilai untuk setiap elemen (bilangan bulat)
3. Program akan menampilkan hasil sesuai operasi yang dipilih
4. Untuk keluar dari program, pilih menu 11

## Menu Program

1. Input Matriks
2. Tampilkan Matriks
3. Penjumlahan Matriks
4. Pengurangan Matriks
5. Perkalian Matriks
6. Transpose Matriks
7. Determinan Matriks
8. Sistem Persamaan Linear
9. Analisis AI - Prediksi Pola
10. Analisis AI - Clustering
11. Keluar

## Struktur Project

```
matrix-operations/
│
├── main.py                 # File utama untuk menjalankan program
├── matrix_operations.py    # Implementasi kelas dan fungsi
├── requirements.txt        # Daftar dependencies
└── README.md              # Dokumentasi project
```

## Requirements

Buat file `requirements.txt` dengan isi:
```
numpy
scikit-learn
```

## Kontribusi

Jika Anda ingin berkontribusi pada project ini:
1. Fork repository
2. Buat branch baru (`git checkout -b fitur-baru`)
3. Commit perubahan (`git commit -m 'Menambahkan fitur baru'`)
4. Push ke branch (`git push origin fitur-baru`)
5. Buat Pull Request

## Lisensi

Project ini dilisensikan di bawah [MIT License](LICENSE)

## Author

Nabil Ganteng

## Catatan

- Program ini menggunakan bilangan bulat untuk input dan output
- Pastikan semua dependencies terinstall sebelum menjalankan program
- Untuk pengguna Termux, pastikan memiliki cukup ruang penyimpanan untuk instalasi

## Troubleshooting

Jika menemui error:
1. Pastikan Python dan pip terinstall dengan benar
2. Cek versi dependencies di requirements.txt
3. Untuk Termux, pastikan package sudah diupdate
4. Jika ada error specific, buat issue di repository

## Update Log

- v1.0.0 (2024-12-04)
  - Rilis pertama
  - Implementasi dasar operasi matriks
  - Penambahan fitur AI
