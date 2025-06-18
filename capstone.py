# ===== DATA =====
# Data Siswa
data_siswa = [
    {
        "NIS": 12096,
        "nama": "Judi",
        "jenis kelamin": "Laki-laki",
        "asal": "Bandung",
        "nilai": 75,
    },
    {
        "NIS": 12098,
        "nama": "Citra",
        "jenis kelamin": "Perempuan",
        "asal": "Surabaya",
        "nilai": 88,
    },
    {
        "NIS": 12090,
        "nama": "Yuni",
        "jenis kelamin": "Perempuan",
        "asal": "Bandung",
        "nilai": 95,
    },
]

# Data Recycle Bin
data_recycle_bin = []

# = MENU =====
# -----------------------------
# Main Menu
menu = """
1. Menampilkan Data Siswa
2. Menambahkan Data Siswa
3. Mengubah Data Siswa
4. Mengurangi Data Siswa
5. Exit Program
"""

# ------------------------------
# MENU READ
menu_read = """
1. Sorting Data
2. Pencarian Data
3. Kembali ke Menu Utama
"""
menu_sorting = """
1. A-Z (ascending)
2. Z-A (descending)
3. Kembali ke Sub Menu
"""
menu_pencarian = """
1. Pencarian Data Siswa Berdasarkan NIS
2. Pencarian Data Siswa Berdasarkan Nama
3. Pencarian Data Siswa Berdasarkan Jenis Kelamin
4. Pencarian Data Siswa Berdasarkan Asal
5. Pencarian Data Siswa Berdasarkan Nilai
6. Kembali ke Sub Menu
"""

# ------------------------------
# MENU PENAMBAHAN
menu_penambahan = """
1. Tambahkan data siswa
2. Kembali ke Menu Utama
"""

# ------------------------------
# MENU PENGUBAHAN
menu_pengubahan = """
1. Ubah data siswa
2. Kembali ke Menu Utama
"""

# ------------------------------
# MENU PENGHAPUSAN
menu_penghapusan = """
1. Hapus data siswa
2. Kembali ke Menu Utama
"""


# ===== FUNCTIONS =====
# -----------------------------
# FUNCTION TABLE
# Print header table
def header():
    print("\nNIS\t|\tNAMA\t\t|\tJENIS KELAMIN\t|\tASAL DAERAH\t|\tNILAI UJIAN")
    print("-" * 100)


# Print isi table
def row_data(i):
    print(
        f"{i['NIS']}\t|\t{i['nama']:<10}\t|\t{i["jenis kelamin"]}\t|\t{i['asal']:<10}\t|\t{i['nilai']}"
    )


# Print full table
def table(jenis_data, i=None, all_data=False, data_sementara=None):
    header()
    if all_data:
        if jenis_data == "siswa":
            for i in data_siswa:
                row_data(i)
        elif jenis_data == "bin":
            for i in data_recycle_bin:
                row_data(i)
        elif jenis_data == "pencarian":
            for i in data_sementara:
                row_data(i)
    else:
        if jenis_data == "siswa":
            row_data(data_siswa[i])
        elif jenis_data == "hasil input":
            row_data(data_sementara)


# Pencarian data berdasarkan nis/nama/umur/asal/nilai
def pencarian_data(jenis_pencarian):
    while True:
        if jenis_pencarian == "nilai":
            pencarian = int(
                validation(
                    f"Ketik {jenis_pencarian} siswa yang ingin dicari: ",
                    angka=True,
                    cek_nilai=True,
                )
            )
        elif jenis_pencarian == "NIS":
            pencarian = int(
                validation(
                    f"Ketik {jenis_pencarian} siswa yang ingin dicari: ", angka=True
                )
            )
        elif jenis_pencarian == "jenis kelamin":
            pencarian = input_gender()

        else:
            pencarian = validation(f"Ketik {jenis_pencarian} siswa yang ingin dicari: ")

        if pencarian == True:
            break

        else:
            header()
            data_ditemukan = False

            for i in data_siswa:
                if jenis_pencarian == "nilai":
                    if pencarian == int(i[jenis_pencarian]):
                        row_data(i)
                        data_ditemukan = True
                elif jenis_pencarian == "NIS":
                    if str(pencarian) in str(i[jenis_pencarian]):
                        row_data(i)
                        data_ditemukan = True

                else:
                    if pencarian.lower() in str(i[jenis_pencarian]).lower():
                        row_data(i)
                        data_ditemukan = True

            if not data_ditemukan:
                print("Data tidak ditemukan.")

            break


# ------------------------------
# Cek data berdasarkan NIS
def cek_nis(nis):
    index = 0
    for siswa in data_siswa:
        if siswa["NIS"] == nis:
            return index
        index += 1
    return -1


# -----------------------------
# FUNCTION INPUT
# Validasi input value data
def validation(notif, angka=False, cek_nis=False, cek_nilai=False):
    kembali = False
    while True:
        nilai = input(notif).strip()

        if not nilai:
            print("Input tidak boleh kosong")
            while True:
                input_lanjut = input("Apakah ingin kembali? (Y / N) : ")
                if input_lanjut.upper() == "Y":
                    kembali = True
                    return kembali
                    # break
                elif input_lanjut.upper() == "N":
                    break
                else:
                    continue
            continue

        if angka:
            if not nilai.isdigit():
                print("Input harus berupa angka")
                while True:
                    input_lanjut = input("Apakah ingin kembali? (Y / N) : ")
                    if input_lanjut.upper() == "Y":
                        kembali = True
                        return kembali
                    elif input_lanjut.upper() == "N":
                        break
                    else:
                        continue
                continue

            if cek_nis and len(nilai) != 5:
                print("Panjang NIS harus 5 digit")
                while True:
                    input_lanjut = input("Apakah ingin kembali? (Y / N) : ")
                    if input_lanjut.upper() == "Y":
                        kembali = True
                        return kembali
                    elif input_lanjut.upper() == "N":
                        break
                    else:
                        continue
                continue

            if cek_nilai and not (0 <= int(nilai) <= 100):
                print("Nilai harus antara 0 - 100")
                while True:
                    input_lanjut = input("Apakah ingin kembali? (Y / N) : ")
                    if input_lanjut.upper() == "Y":
                        kembali = True
                        return kembali
                    elif input_lanjut.upper() == "N":
                        break
                    else:
                        continue
                continue

        return nilai


def input_gender():
    kembali = False
    while True:
        print(
            """
            Jenis Kelamin:
            1. Laki-laki
            2. Perempuan
            """
        )
        pilihan = input("Masukkan angka pilihan : ")

        if pilihan == "1":
            return "Laki-laki"
        elif pilihan == "2":
            return "Perempuan"
        else:
            print("Pilihan tidak valid")
            while True:
                input_lanjut = input("Apakah ingin kembali? (Y / N) : ")
                if input_lanjut.upper() == "Y":
                    kembali = True
                    return kembali
                elif input_lanjut.upper() == "N":
                    break
                else:
                    continue
            continue


# Konfirmasi aksi
def konfirmasi(action, i=None, key=None, input_data=None):
    while True:
        konfirmasi = input(f"Apakah anda yakin untuk {action} data di atas? (Y / N) : ")

        if konfirmasi.upper() == "Y":
            if action == "menambahkan":
                data_siswa.append(input_data)
            if action == "mengubah":
                data_siswa[i][key] = input_data
            if action == "menghapus":
                # Create data siswa saat ini ke recycle bin
                data_recycle_bin.append(data_siswa[i])
                # Menghapus data siswa yang dipilih
                data_siswa.pop(i)

            print(f"Berhasil {action} data siswa")
            if action != 'mengubah':
                print("Data siswa terbaru : ")
                table("siswa", all_data=True)

            # Memunculkan table recycle bin
            if action == "menghapus":
                print("Data recycle bin : ")
                table("bin", all_data=True)
            break

        elif konfirmasi.upper() == "N":
            print(f"Batal {action} data siswa")
            break

        else:
            print("pilihan tidak ada")
            continue


# ===== ACTION ======
while True:
    # ==============================================
    # MAIN
    # ==============================================
    print("\n==================== MENU UTAMA ====================")
    print(menu)
    menu_pilihan = input("Masukan angka Menu yang ingin dijalankan : ")

    # ==============================================
    # READ
    # ==============================================

    # Menampilkan Seluruh Data & Menu Read
    if menu_pilihan == '1':
        while True:
            print("\n==================== MENU LIHAT DATA ====================")
            table("siswa", all_data=True)
            print(menu_read)

            pilihan_read = input("Masukan angka Menu yang ingin dijalankan : ")

            # Sorting Data
            if pilihan_read == '1':
                while True:
                    print(menu_sorting)
                    pilihan_sorting = input(
                        "Masukan angka metode sorting yang ingin dijalankan : "
                    )

                    if pilihan_sorting == "1":
                        data_urut = sorted(data_siswa, key=lambda x: x["nama"].lower())
                        print("Data siswa diurutkan berdasarkan (A - Z):")
                        table("pencarian", all_data=True, data_sementara=data_urut)
                    elif pilihan_sorting == "2":
                        data_urut = sorted(
                            data_siswa, key=lambda x: x["nama"].lower(), reverse=True
                        )
                        print("Data siswa diurutkan berdasarkan (Z - A):")
                        table("pencarian", all_data=True, data_sementara=data_urut)
                    elif pilihan_sorting == "3":
                        break
                    else:
                        print("Mohon masukkan angka yang tersedia")
                        continue

            # Pencarian Data
            elif pilihan_read == '2':
                while True:
                    print(menu_pencarian)
                    pilihan_pencarian = input(
                        "Masukan angka metode pencarian yang ingin dijalankan : "
                    )

                    # Menampilkan data dari pencarian NIS
                    if pilihan_pencarian == "1":
                        pencarian_data("NIS")

                    # Menampilkan data dari pencarian nama
                    elif pilihan_pencarian == "2":
                        pencarian_data("nama")

                    # Menampilkan data dari pencarian nilai
                    elif pilihan_pencarian == "3":
                        pencarian_data("jenis kelamin")

                    # Menampilkan data dari pencarian asal
                    elif pilihan_pencarian == "4":
                        pencarian_data("asal")

                    # Menampilkan data dari pencarian nilai
                    elif pilihan_pencarian == "5":
                        pencarian_data("nilai")

                    # Kembali ke Sub Menu
                    elif pilihan_pencarian == "6":
                        break

                    else:
                        print("Mohon masukkan angka yang tersedia")
                        continue

            # Kembali ke Main Menu
            elif pilihan_read == '3':
                break

            else:
                print("Input tidak valid")
                continue
    # ==============================================
    # CREATE
    # ==============================================

    if menu_pilihan == '2':
        while True:
            print("\n==================== MENU TAMBAH DATA ====================")
            print(menu_penambahan)
            pilihan_create = input("Silakan pilih sub menu yang ingin anda jalankan : ")

            if pilihan_create == '1':
                print("Mohon mengisi data siswa yang ingin ditambahkan")

                # looping input nis
                while True:
                    nis = int(
                        validation(
                            "Masukkan NIS     : ", angka=True, cek_nis=True
                        )
                    )

                    if nis == True:
                        break

                    # Cek ketersediaan NIS
                    nilai_index = cek_nis(nis)
                    if nilai_index != -1:
                        print("NIS sudah ada")
                        input_lanjut = input(
                            "Apakah ingin kembali ke sub menu? (Y / N) : "
                        )
                        if input_lanjut.upper() == "Y":
                            break
                        elif input_lanjut.upper() == "N":
                            continue
                        else:
                            continue

                    nama = validation("Masukkan nama    : ")
                    if nama == True:
                        break

                    jenis_kelamin = input_gender()
                    if jenis_kelamin == True:
                        break

                    asal = validation("Masukkan asal kota     : ")
                    if asal == True:
                        break

                    nilai = int(
                        validation(
                            "Masukkan nilai ujian   : ", angka=True, cek_nilai=True
                        )
                    )
                    if nilai == True:
                        break

                    tambah_siswa = {
                        "NIS": nis,
                        "nama": nama.capitalize(),
                        "jenis kelamin": jenis_kelamin,
                        "asal": asal.capitalize(),
                        "nilai": nilai,
                    }

                    table(jenis_data="hasil input", data_sementara=tambah_siswa)

                    konfirmasi("menambahkan", input_data=tambah_siswa)
                    break

            elif pilihan_create == '2':
                break
            else:
                print("Input tidak valid")
                continue

    # ==============================================
    # UPDATE
    # ==============================================

    if menu_pilihan == '3':
        while True:
            print("\n==================== MENU UBAH DATA ====================")
            print(menu_pengubahan)
            pilihan_update = input("Silakan pilih sub menu yang ingin anda jalankan : ")

            if pilihan_update == '1':
                while True:
                    input_nis_upd = int(
                        validation(
                            "Masukan NIS yang ingin di update: ",
                            angka=True,
                            cek_nis=True,
                        )
                    )
                    if input_nis_upd == True:
                        break

                    # Cek NIS siswa
                    nilai_index = cek_nis(input_nis_upd)
                    if nilai_index == -1:
                        print("data tidak tersedia")
                        input_lanjut = input(
                            "Apakah ingin kembali ke sub menu? (Y / N) : "
                        )
                        if input_lanjut.upper() == "Y":
                            break
                        elif input_lanjut.upper() == "N":
                            continue

                    # Mengubah data siswa
                    elif nilai_index != -1:
                        while True:
                            pilihan_data = """
                                1. Nama
                                2. Jenis Kelamin
                                3. Asal
                                4. Nilai
                                5. Kembali
                                """
                            table("siswa", i=nilai_index)
                            print(pilihan_data)
                            key_pilihan =input(
                                "Masukkan angka sesuai data yang ingin diubah (1 - 5) : "
                            )
                            if key_pilihan == '1':
                                key_baru = "nama"
                            elif key_pilihan == '2':
                                key_baru = "jenis kelamin"
                            elif key_pilihan == '3':
                                key_baru = "asal"
                            elif key_pilihan == '4':
                                key_baru = "nilai"
                            elif key_pilihan == '5':
                                kembali = True
                                break
                            else:
                                print("Input tidak valid. Masukkan angka antara 1 - 5")
                                input_lanjut = input("Apakah ingin kembali? (Y / N) : ")
                                if input_lanjut.upper() == "Y":
                                    kembali = True
                                    break
                                elif input_lanjut.upper() == "N":
                                    continue
                                else:
                                    continue
                            
                            while True:
                                if key_baru == "jenis kelamin":
                                    value_baru = input_gender()
                                elif key_baru == "nilai":
                                    value_baru = int(
                                        validation(
                                            "Masukkan nilai baru (0 - 100): ",
                                            angka=True,
                                            cek_nilai=True,
                                        )
                                    )
                                else:
                                    value_baru = validation(
                                        f"Masukkan {key_baru} baru: "
                                    ).capitalize()
                                
                                if value_baru == True:
                                    break

                                header()
                                print(
                                    f"{data_siswa[nilai_index]['NIS']}\t|\t"
                                    f"{(value_baru if key_baru == 'nama' else data_siswa[nilai_index]['nama']):<10}\t|\t"
                                    f"{(value_baru if key_baru == 'jenis kelamin' else data_siswa[nilai_index]['jenis kelamin']):<15}\t|\t"
                                    f"{(value_baru if key_baru == 'asal' else data_siswa[nilai_index]['asal']):<15}\t|\t"
                                    f"{(value_baru if key_baru == 'nilai' else data_siswa[nilai_index]['nilai'])}"
                                )
                                konfirmasi("mengubah", nilai_index, key_baru, value_baru
                                )
                                break
                        if kembali:
                            break
            elif pilihan_update == '2':
                break

    # ==============================================
    # DELETE
    # ==============================================

    if menu_pilihan == '4':
        while True:
            print("\n==================== MENU DELETE DATA ====================")
            print(menu_penghapusan)
            menu_input = input("Silakan pilih sub menu yang ingin anda jalankan: ")

            # Menghapus Data Siswa dengan NIS
            if menu_input == '1':
                kembali = False
                lanjut = False
                while True:
                    # Cek NIS siswa yang dicari
                    input_nis_del = int(
                        validation(
                            "Masukan NIS yang ingin dihapus: ", angka=True, cek_nis=True
                        )
                    )

                    if input_nis_del == True:
                        break

                    nilai_index = cek_nis(input_nis_del)
                    if nilai_index == -1:
                        while True:
                            print("data tidak tersedia")
                            input_lanjut = input(
                                "Apakah ingin kembali ke sub menu? (Y / N) : "
                            )
                            if input_lanjut.upper() == "Y":
                                kembali = True
                                break
                            elif input_lanjut.upper() == "N":
                                lanjut = True
                                break
                            else:
                                print("Input tidak valid")
                                continue
                        
                        if kembali:
                            break

                        if lanjut:
                            continue

                    # Menghapus data siswa
                    elif nilai_index != -1:
                        table("siswa", i=nilai_index)

                        # konfirmasi aksi
                        konfirmasi("menghapus", i=nilai_index)

                    break
            elif menu_input == '2':
                break
            else:
                print("Input tidak valid")
                continue

    if menu_pilihan == '5':
        print("Terima Kasih. Sampai Jumpa!")
        break

    else:
        print("Input tidak valid")
        continue
