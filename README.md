# Pertemuan 10 — String dan Pengolahan Teks
  
**Nama:** Arya Kusmana Anas
**NIM:** 2225250118
**Kelas:** 3B  

## Tujuan
Mengolah dan menormalisasi data teks dengan string Python, termasuk indeks, slicing, method string, pembersihan teks, split, join, dan pencarian kata.

## Struktur Folder
```text
pertemuan-10-string/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_dasar_string.py
│   ├── 02_indeks_slicing.py
│   ├── 03_method_string.py
│   ├── 04_bersihkan_teks.py
│   ├── 05_split_join.py
│   └── 06_pencarian_kata.py
└── tugas/
    └── normalisasi_data_mahasiswa.py
```

## Persiapan VS Code
1. Pastikan Python 3 sudah terpasang.
2. Buka folder proyek melalui **File → Open Folder**.
3. Pilih interpreter melalui **Python: Select Interpreter**.
4. Buka **Terminal → New Terminal**.

## Cara Menjalankan
Jalankan perintah dari terminal di folder utama proyek.

Windows:
```powershell
python latihan/01_dasar_string.py
python latihan/02_indeks_slicing.py
python latihan/03_method_string.py
python latihan/04_bersihkan_teks.py
python latihan/05_split_join.py
python latihan/06_pencarian_kata.py
python tugas/normalisasi_data_mahasiswa.py
```

macOS/Linux (gunakan `python3` jika diperlukan):
```bash
python3 latihan/01_dasar_string.py
python3 latihan/02_indeks_slicing.py
python3 latihan/03_method_string.py
python3 latihan/04_bersihkan_teks.py
python3 latihan/05_split_join.py
python3 latihan/06_pencarian_kata.py
python3 tugas/normalisasi_data_mahasiswa.py
```

Program tugas meminta nama dan kode kelas. Contoh:
```text
Nama:   aan hendrayana
Kode kelas: pmat a 2026
```
Hasil utama yang diharapkan:
```text
Nama bersih : Aan Hendrayana
Kode kelas  : PMAT-A-2026
Jumlah kata : 2
Inisial     : AH
```

## Algoritma Tugas 4
1. Membaca nama dan kode kelas.
2. Menghapus spasi berlebih pada nama dan mengubahnya menjadi title case.
3. Memisahkan nama menjadi kata dan mengambil huruf pertama setiap kata sebagai inisial.
4. Mengubah kode kelas menjadi huruf besar dan mengganti spasi dengan tanda hubung.
5. Menampilkan nama bersih, kode kelas, jumlah kata, dan inisial.

## Test Case
| Input nama | Input kode kelas | Hasil utama yang diharapkan |
|---|---|---|
| `aan hendrayana` | `pmat a 2026` | `Aan Hendrayana`, `PMAT-A-2026`, `AH` |
| `fATHIYYAH mUTHMAINNAH` | `kelas b` | `Fathiyyah Muthmainnah`, `KELAS-B`, `FM` |
| `BUDI` | `pmtk 01` | `Budi`, `PMTK-01`, `B` |
| `siti nur aisyah` | `kelas c` | `Siti Nur Aisyah`, `KELAS-C`, `SNA` |

## Hasil Pengujian
Jalankan setiap file dan catat hasil aktualnya setelah diuji.

| File | Hasil aktual | Status |
|---|---|---|
| `01_dasar_string.py` | Isi setelah diuji | Lulus/Perlu perbaikan |
| `02_indeks_slicing.py` | Isi setelah diuji | Lulus/Perlu perbaikan |
| `03_method_string.py` | Isi setelah diuji | Lulus/Perlu perbaikan |
| `04_bersihkan_teks.py` | Isi setelah diuji | Lulus/Perlu perbaikan |
| `05_split_join.py` | Isi setelah diuji | Lulus/Perlu perbaikan |
| `06_pencarian_kata.py` | Isi setelah diuji | Lulus/Perlu perbaikan |
| `normalisasi_data_mahasiswa.py` | Isi setelah diuji | Lulus/Perlu perbaikan |

## Pengumpulan ke GitHub
Buat repositori bernama `pertemuan-10-string-NIM`, lalu ganti URL contoh berikut dengan URL repositori Anda.

```bash
git init
git add .
git commit -m "feat: menambahkan latihan string pertemuan 10"
git branch -M main
git remote add origin https://github.com/USERNAME/pertemuan-10-string-NIM.git
git push -u origin main
```

Commit bertahap:
```bash
git add latihan
git commit -m "feat: menyelesaikan latihan string"

git add tugas/normalisasi_data_mahasiswa.py
git commit -m "feat: menyelesaikan tugas normalisasi data"

git add README.md
git commit -m "docs: menambahkan test case dan refleksi"

git push
```

Verifikasi:
```bash
git status
git log --oneline --decorate -5
git remote -v
```

## Refleksi
1. Hal yang saya pahami tentang string immutable: ...
2. Masalah teks yang saya temukan dan cara memperbaikinya: ...
3. Method string yang paling berguna bagi saya: ...

## Referensi
- Bahan Ajar Algoritma dan Pemrograman, Pertemuan 10: *String dan Pengolahan Teks dalam Python*.
- Python Software Foundation, dokumentasi Python 3 tentang tipe teks `str`.
- Dokumentasi Visual Studio Code untuk Python.
- Dokumentasi GitHub tentang menambahkan kode lokal ke GitHub.

> Sesuaikan identitas, hasil pengujian, dan refleksi berdasarkan pekerjaan Anda sendiri. Pastikan Anda memahami kode dan cantumkan bantuan atau sumber yang digunakan sesuai kebijakan kelas.
