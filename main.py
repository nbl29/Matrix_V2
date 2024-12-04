from matrix_operations import operasi_matriks

def main():
    print("Selamat datang di Program Operasi Matriks dengan AI")
    print("=" * 50)
    print("Program ini memungkinkan Anda untuk melakukan berbagai")
    print("operasi matriks dan analisis menggunakan AI.")
    print("=" * 50)
    
    try:
        operasi_matriks()
    except KeyboardInterrupt:
        print("\n\nProgram dihentikan oleh pengguna.")
    except Exception as e:
        print(f"\nTerjadi kesalahan: {str(e)}")
    finally:
        print("\nProgram selesai. Sampai jumpa!")

if __name__ == "__main__":
    main()