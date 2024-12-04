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
git clone https://github.com/nbl29/Matrix_V2.git
cd Matrix_V2
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

Jika mengalami error saat instalasi dependencies, coba install satu per satu:
```bash
pip install numpy
pip install scikit-learn
```

Jika masih error, coba dengan versi spesifik:
```bash
pip install numpy==1.24.3
pip install scikit-learn==1.3.0
```

Jika mengalami error "Microsoft Visual C++ 14.0 or greater is required":
1. Download Visual Studio Build Tools dari [sini](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
2. Install dengan pilihan "Desktop development with C++"
3. Restart komputer
4. Coba install dependencies lagi

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
git clone https://github.com/nbl29/Matrix_V2.git
cd Matrix_V2
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
Matrix_V2/
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

[nbl29](https://github.com/nbl29)

## Catatan

- Program ini menggunakan bilangan bulat untuk input dan output
- Pastikan semua dependencies terinstall sebelum menjalankan program
- Untuk pengguna Termux, pastikan memiliki cukup ruang penyimpanan untuk instalasi

## Troubleshooting

### Untuk PC/Windows
1. Error "Microsoft Visual C++ 14.0 or greater is required":
   - Install Visual Studio Build Tools
   - Pilih workload "Desktop development with C++"
   - Restart komputer
   - Coba install ulang dependencies

2. Error saat install scikit-learn:
   ```bash
   pip install --only-binary :all: scikit-learn
   ```
   atau
   ```bash
   pip install scikit-learn --no-cache-dir
   ```

3. Error dengan NumPy:
   ```bash
   pip install numpy --upgrade
   ```
   atau versi spesifik:
   ```bash
   pip install numpy==1.24.3
   ```

4. Error "Python is not recognized":
   - Pastikan Python sudah diinstall
   - Tambahkan Python ke PATH sistem
   - Restart command prompt/terminal

### Untuk Termux
1. Pastikan Python dan pip terinstall dengan benar
2. Cek versi dependencies di requirements.txt
3. Pastikan package sudah diupdate
4. Jika ada error specific, buat issue di repository

## Update Log

- v1.0.0 (2024-12-04)
  - Rilis pertama
  - Implementasi dasar operasi matriks
  - Penambahan fitur AI
