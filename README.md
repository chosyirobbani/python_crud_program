# 📚 CRUD Data Siswa (CLI Python)

Proyek ini adalah aplikasi berbasis terminal untuk mengelola **Data Siswa** menggunakan bahasa Python. Aplikasi ini mendukung operasi **CRUD** (Create, Read, Update, Delete) lengkap dengan fitur **validasi data** dan **Recycle Bin**.

---

## 🎯 Fitur Utama

- 🔍 Menampilkan semua data siswa
- 🔃 Sorting (A-Z / Z-A berdasarkan nama)
- 🔎 Pencarian data siswa berdasarkan:
  - NIS
  - Nama
  - Jenis Kelamin
  - Asal
  - Nilai
- ➕ Menambahkan data siswa dengan validasi
- ✏️ Mengubah data siswa
- 🗑️ Menghapus data siswa (dengan backup di Recycle Bin)
- ❌ Exit dari aplikasi

---

## 🛠️ Teknologi yang Digunakan

- Python 3.x
- CLI (Command Line Interface)
- Tanpa library eksternal

---

## 🚀 Cara Menjalankan Program

1. Clone repositori ini:
    ```bash
    git clone https://github.com/username/nama-repo.git
    cd nama-repo
    ```

2. Jalankan program:
    ```bash
    python main.py
    ```

---

## 🗂️ Struktur Program

- `data_siswa` → List berisi dictionary siswa
- `data_recycle_bin` → Penyimpanan sementara data yang dihapus
- Fungsi utama:
  - `validation()`, `cek_nis()`, `input_gender()`
  - `pencarian_data()`, `konfirmasi()`, `table()`

---

## ✍️ Contoh Input

```bash
==================== MENU UTAMA ====================
1. Menampilkan Data Siswa
2. Menambahkan Data Siswa
3. Mengubah Data Siswa
4. Mengurangi Data Siswa
5. Exit Program
Masukan angka Menu yang ingin dijalankan : 2
