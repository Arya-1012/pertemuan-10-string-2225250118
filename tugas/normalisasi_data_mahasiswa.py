# Tugas 4: Normalisasi Data Mahasiswa

def normalisasi_nama(nama):
    """Menghapus spasi berlebih dan mengubah nama menjadi title case."""
    return " ".join(nama.strip().split()).title()


def buat_inisial(nama):
    """Mengambil huruf pertama setiap kata pada nama."""
    kata = normalisasi_nama(nama).split()
    return "".join(item[0] for item in kata)


def normalisasi_kode(kode):
    """Mengubah kode menjadi huruf besar dan mengganti spasi dengan tanda hubung."""
    return "-".join(kode.strip().upper().split())


def main():
    nama = input("Nama: ")
    kode = input("Kode kelas: ")

    nama_bersih = normalisasi_nama(nama)
    kode_bersih = normalisasi_kode(kode)
    jumlah_kata = len(nama_bersih.split())
    inisial = buat_inisial(nama)

    print("\n=== HASIL NORMALISASI ===")
    print(f"Nama bersih : {nama_bersih}")
    print(f"Kode kelas  : {kode_bersih}")
    print(f"Jumlah kata : {jumlah_kata}")
    print(f"Inisial     : {inisial}")


if __name__ == "__main__":
    main()
