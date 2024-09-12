# ========================================================== CAPSTONE PROJECT MODULE 1 ==============================================================================
# ========================================================== ATHAYA ZAHRANI IRMANSYAH ===============================================================================
# ================================================================= JCDS - 0408 =====================================================================================
# ============================================================== DATA NILAI SISWA ===================================================================================
# ============= Portal Data Nilai Mahasiswa Mata Kuliah Kalkulus (Semester Ganjil) di Fakultas Teknik Sipil dan Perencanaan Tahun 2024 ==============================

# INISIASI DATA =====================================================================================================================================================
from tabulate import tabulate 

list_dict_data = [
    {
        'nim':20242119, 
        'nama':'Mahasiro Shimada', 
        'jurusan':'Teknik Geodesi', 
        'semester':1, 
        'angkatan':2024, 
        'nilaikuis': 80, 
        'nilaiuts': 60, 
        'nilaiuas': 78
    },
    {
        'nim':20232235, 
        'nama':'Sho Kurama', 
        'jurusan':'Teknik Sipil', 
        'semester':3, 
        'angkatan':2023, 
        'nilaikuis': 45, 
        'nilaiuts': 24, 
        'nilaiuas': 55
    },
    {
        'nim':20212201, 
        'nama':'Shimada Kanno', 
        'jurusan':'Teknik Sipil', 
        'semester':7, 
        'angkatan':2021, 
        'nilaikuis': 60, 
        'nilaiuts': 76, 
        'nilaiuas': 85
    },
    {
        'nim':20232245, 
        'nama':'Makiko Ariga', 
        'jurusan':'Teknik Sipil', 
        'semester':3, 
        'angkatan':2023, 
        'nilaikuis': 80, 
        'nilaiuts': 67, 
        'nilaiuas': 89
    },
    {
        'nim':20222156, 
        'nama':'Kotoko Oyama', 
        'jurusan':'Teknik Geodesi', 
        'semester':5, 
        'angkatan':2022, 
        'nilaikuis': 95, 
        'nilaiuts': 85, 
        'nilaiuas': 90
    }
]

list_dict_data_update = list_dict_data.copy()
nomor = 0 

# FUNGSI SUB MENU 1 (MENAMPILKAN SELURUH ATAU SEBAGIAN DATA) ========================================================================================================

def view_menu():
    while True:
        try:
            print('\nData Nilai Mahasiswa Mata Kuliah Kalkulus (Semester Ganjil) di Fakultas Teknik Sipil dan Perencanaan Tahun 2024')
            print(tabulate(list_dict_data_update, headers = 'keys', tablefmt = 'pretty'))
        except:
            print('Mohon Maaf. Data Mahasiswa Kosong.')
        break

def read_menu():
    print('''
    Sub Menu Menampilkan Semua Data Mahasiswa

    1. Menampilkan Semua Data Mahasiswa
    2. Data Mahasiswa Menurut NIM
    3. Kembali ke Menu Utama
    
    ''')
    read_submenu = input('Silakan Pilih Menu (1/2/3): ')

    if read_submenu == '1': 
        if len(list_dict_data_update) == 0:
            no_data()
            read_menu()
        else:
            view_menu()
            read_menu()
    elif read_submenu == '2': 
        if len(list_dict_data_update) == 0:
            no_data()
            read_menu()
        else:
            nomor_input()
            for data_update in list_dict_data_update:
                if data_update['nim'] == nomor:
                    print(f'\nBerikut adalah Data Mahasiswa dengan NIM {nomor}')
                    print(f'''
    NIM : {data_update['nim']}
    Nama : {data_update['nama']}
    Jurusan : {data_update['jurusan']}
    Semester : {data_update['semester']}
    Angkatan : {data_update['angkatan']} 
    Nilai Kuis : {data_update['nilaikuis']}
    Nilai UTS : {data_update['nilaiuts']}    
                    ''')
                    break
            if data_update['nim'] != nomor:
                no_data()
            read_menu()
    elif read_submenu == '3':
        portal_data_mahasiswa()
    else:
        pilihan_salah()
        read_menu()

# FUNGSI SUB MENU 2 (MENAMBAHKAN DATA) ==============================================================================================================================

def add_menu():
    print('''
    Sub Menu Menambahkan Data Mahasiswa

    1. Menambahkan Data Mahasiswa
    2. Kembali ke Menu Utama

    ''')
    add_submenu = input('Silakan Pilih Menu (1/2): ')

    if add_submenu == '1':
        nomor_input()
        for data_update in list_dict_data_update:
            if data_update['nim'] == nomor:
                print(f'Mohon Maaf. Data dengan NIM {nomor} Sudah Ada.')
                break
        if data_update['nim'] != nomor:
            nama_lengkap = validasi_nama().capitalize()
            jurusan_baru = validasi_jurusan().capitalize()
            semester_baru = validasi_semester()
            angkatan_baru = validasi_angkatan()
            nilai_kuis = validasi_kuis()
            nilai_uts = validasi_uts()
            nilai_uas = validasi_uas()

            konfirmasi = input('\nSimpan Data Baru Anda (Y/N)? ').upper()
            if konfirmasi == 'Y':
                list_dict_data_update.append({'nim': nomor, 'nama': nama_lengkap, 'jurusan': jurusan_baru, 'semester': semester_baru, 'angkatan': angkatan_baru, 'nilaikuis': nilai_kuis, 'nilaiuts': nilai_uts, 'nilaiuas': nilai_uas})
                print('\nTerima Kasih. Data Anda Berhasil Disimpan.')
        add_menu()
    elif add_submenu == '2':
        portal_data_mahasiswa()
    else:
        pilihan_salah()
        add_menu()

# FUNGSI SUB MENU 3 (MENGUBAH DATA) =================================================================================================================================
def change_menu():
    while True:
        try:
            print('''
            Sub Menu Mengubah Data Mahasiswa
                
            1. Mengubah Data Mahasiswa
            2. Kembali ke Menu Utama
                
            ''')

            change_submenu = input('Silakan Pilih Menu (1/2): ')

            if change_submenu == '1':
                nomor_input()
                nomor_awal = nomor
                change_subject = ''
                for data_update in list_dict_data_update:
                    if data_update['nim'] == nomor_awal:

                        # Menampilkan Data Lengkap Mahasiswa Terlebih Dahulu
                        print(f"\nNomor Induk Mahasiswa (NIM) : {data_update['nim']}, Nama : {data_update['nama']}, Jurusan : {data_update['jurusan']}, Semester : {data_update['semester']}, Angkatan : {data_update['angkatan']}, Nilai Kuis : {data_update['nilaikuis']}, Nilai UTS : {data_update['nilaiuts']}, Nilai UAS : {data_update['nilaiuas']}")
                        
                        # Melanjutkan Proses Update Data
                        update = input('\nLanjutkan Mengubah Data Mahasiswa (Y/N)? ').upper()
                        if update == 'Y':
                            change_subject = input('\nMasukkan subjek data yang akan diubah (NIM/Nama/Jurusan/Semester/Angkatan/Nilai Kuis/Nilai UTS/Nilai UAS): ').lower()
                            if change_subject.replace(' ','').lower() in list_dict_data_update[0].keys():
                                if change_subject == 'nim':
                                    nomor_input()
                                    nilai_baru = nomor

                                    # Memastikan NIM Tidak Duplikat
                                    list_nomor = [data_update['nim'] for data_update in list_dict_data_update]
                                    while nilai_baru in list_nomor:
                                        print('\nMohon maaf. NIM Sudah Terpakai.')
                                        nomor_input()
                                        nilai_baru = nomor
                                else:
                                    nilai_baru = input(f'\nMasukkan {change_subject} baru: ')

                                # Proses Update Data
                                confirm = input('\nApakah Data Akan Diubah (Y/N)? ').upper()
                                if confirm == 'Y':
                                    data_update[change_subject.replace(' ','').lower()] = nilai_baru
                                    print('\nTerima Kasih. Data Berhasil Diubah.')
                            else:
                                pilihan_salah()
                        break
                if change_subject != nomor:
                    if data_update['nim'] != nomor_awal:
                        no_data()
                change_menu()
            elif change_submenu == '2':
                portal_data_mahasiswa()  
            else:
                pilihan_salah()
                change_menu()
        except:
            print('\nMohon Maaf. Data Mahasiswa Kosong.')
            change_menu()
        break

# FUNGSI SUB MENU 4 (MENGHAPUS DATA) ================================================================================================================================
def delete_menu():
    while True:
        try:
            print('''
            Sub Menu Menghapus Data Mahasiswa
                
            1. Menghapus Data Mahasiswa
            2. Kembali ke Menu Utama
                
            ''')

            delete_submenu = input('Silakan Pilih Menu (1/2): ')

            if delete_submenu == '1':
                nomor_input()
                for i, data_update in enumerate(list_dict_data_update):
                    if data_update['nim'] == nomor:
                        delete = input(f'\nApakah Data Mahasiswa dengan NIM {nomor} Akan Dihapus (Y/N)? ').upper()
                        if delete == 'Y':
                            del list_dict_data_update[i]
                            print('\nData dengan Keterangan:')
                            print(f"\nNIM : {data_update['nim']}, Nama : {data_update['nama']}, Jurusan : {data_update['jurusan']}, Semester : {data_update['semester']}, Angkatan : {data_update['angkatan']}, Nilai Kuis : {data_update['nilaikuis']}, Nilai UTS : {data_update['nilaiuts']}, Nilai UAS : {data_update['nilaiuas']}")
                            print('\nBerhasil Dihapus.')
                        break
                if data_update['nim'] != nomor:
                    no_data()
                delete_menu()
            elif delete_submenu == '2':
                portal_data_mahasiswa()
            else:
                pilihan_salah()
                delete_menu()
        except:
            print('\nMohon Maaf. Data Mahasiswa Kosong.')
            delete_menu()
        break

# FUNGSI SUB MENU 5 (INFORMASI NILAI MAHASISWA) ==============================================================================================================================
def count_menu():
    while True:
        try:
            print('''
            Sub Menu Informasi Nilai Mahasiswa
            
            1. Informasi Rata-rata Nilai Mahasiswa
            2. Informasi Indeks Akhir Mahasiswa
            3. Kembali ke Menu Utama

            ''') 

            count_submenu = input('Silakan Pilih Menu (1/2/3): ')

            # Menghitung Rata-rata Nilai Mahasiswa
            if count_submenu == '1':
                nomor_input()
                for data_update in list_dict_data_update:
                    if data_update['nim'] == nomor:
                        rerata = (int(data_update['nilaikuis']) + int(data_update['nilaiuts']) + int(data_update['nilaiuas']))/3
                        print(f'\n Informasi Rata-rata Nilai Mahasiswa dengan NIM {nomor}: ')
                        print(f'\n Rata-rata Nilai Keseluruhan Anda: {rerata:.2f}')
                        break
                if data_update['nim'] != nomor:
                    no_data()
                count_menu()
            
            # Menghitung Indeks Akhir Mahasiswa
            elif count_submenu == '2':
                nomor_input()
                for data_update in list_dict_data_update:
                    if data_update['nim'] == nomor:
                        count = (20/100) * int(data_update['nilaikuis']) + (40/100) * int(data_update['nilaiuts']) + (40/100) * int(data_update['nilaiuas'])
                        print(f'\nInformasi Indeks Akhir Mahasiswa dengan NIM {nomor}: ')
                        if count > 80:
                            grade = 'A'
                            print(f'\nSELAMAT! Nilai Akhir Anda {count:.2f}. \n Indeks Akhir Anda {grade}. \n Anda Lulus Mata Kuliah Ini.')
                        elif count > 65:
                            grade = 'B' 
                            print(f'\nSELAMAT! Nilai Akhir Anda {count:.2f}. \n Indeks Akhir Anda {grade}. \n Anda Lulus Mata Kuliah Ini.')
                        elif count > 50:
                            grade = 'C'
                            print(f'\nNilai Akhir Anda {count:.2f}. \n Indeks Akhir Anda {grade}. \n Anda Lulus Mata Kuliah Ini.')
                        elif count > 35:
                            grade = 'D'
                            print(f'\nNilai Akhir Anda {count:.2f}. \n Indeks Akhir Anda {grade}. \n Anda Lulus Mata Kuliah Ini.')
                        else:
                            grade = 'E'
                            print(f'\nNilai Akhir Anda {count:.2f}. \n Indeks Akhir Anda {grade}. \n Anda Tidak Lulus Mata Kuliah Ini. Anda Harus Mengulang.')
                        break
                if data_update['nim'] != nomor:
                    no_data()
                count_menu()
            elif count_submenu == '3':
                portal_data_mahasiswa()
            else: 
                pilihan_salah()
                count_menu()
        except:
            print('\nMohon Maaf. Data Mahasiswa Kosong.')
            delete_menu()
        break

# FUNGSI-FUNGSI PENDUKUNG UNTUK MEMVALIDASI DATA ====================================================================================================================
def validasi_nama():
    while True:
        global nama_lengkap
        nama_lengkap = input('\nMasukkan Nama Anda: ')
        if nama_lengkap.replace(' ','').isalpha() == True:
            return(nama_lengkap)
            break
        print('\nMohon Maaf. Input Tidak Valid. Silakan Masukkan Nama yang Hanya Mengandung Alfabet.')

def validasi_jurusan():
    while True:
        global jurusan_baru
        jurusan_baru = input('\nMasukkan Jurusan Anda: ')
        if jurusan_baru.replace(' ','').isalpha() == True:
            return(jurusan_baru)
            break
        print('\nMohon Maaf. Input Tidak Valid. Silakan Masukkan Jurusan yang Hanya Mengandung Alfabet.')

def validasi_semester():
    while True:
        global semester_baru
        semester_baru = input('\nMasukkan Semester Anda (Semester Ganjil): ')
        if semester_baru.isnumeric() == True:
            if int(semester_baru) >= 1 and int(semester_baru) <= 13:
                if int(semester_baru) % 2 == 1:
                    return(semester_baru)
                    break
                else:
                    print('\nMohon Maaf. Input Tidak Valid. Silakan Masukan Ulang Semester.')
            else:
                print('\nMohon Maaf. Input Tidak Valid. Silakan Masukan Ulang Semester.')
        else:
            print('\nMohon Maaf. Input Tidak Valid. Silakan Masukkan Ulang Semester.')

def validasi_angkatan():
    while True:
        global angkatan_baru
        angkatan_baru = input('\nMasukkan Angkatan Anda dalam Tahun (2018-2024): ')
        if angkatan_baru.isnumeric() == True:
            if int(angkatan_baru) >= 2018 and int(angkatan_baru) <= 2024:
                return(angkatan_baru)
                break
            else:
                print('\nMohon Maaf. Input Tidak Valid. Silakan Masukkan Ulang Angkatan.')
        else: 
            print('\nMohon Maaf. Input Tidak Valid. Silakan Masukkan Ulang Angkatan.')

# Fungsi Validasi Nilai Kuis
def validasi_kuis():
    while True:
        global nilai_kuis
        nilai_kuis = input('\nMasukkan Nilai Kuis (0-100): ')
        if nilai_kuis.isnumeric() == True:
            if int(nilai_kuis) >= 0 and int(nilai_kuis) <= 100:
                return(nilai_kuis)
                break
            else:
                print('\nMohon Maaf. Nilai Kuis Anda di Luar Jangkauan Nilai. Silakan Masukan Ulang Nilai Kuis Anda.')
        else: 
            print('\nMohon Maaf. Input Tidak Valid. Silakan Masukkan Ulang Nilai Kuis.')

# Fungsi Validasi Nilai UTS
def validasi_uts():
    while True:
        global nilai_uts
        nilai_uts = input('\nMasukkan Nilai UTS (0-100): ')
        if nilai_uts.isnumeric() == True:
            if int(nilai_uts) >= 0 and int(nilai_uts) <= 100:
                return(nilai_uts)
                break
            else:
                print('\nMohon Maaf. Nilai UTS Anda di Luar Jangkauan Nilai. Silakan Masukan Ulang Nilai UTS Anda.')
        else: 
            print('\nMohon Maaf. Input Tidak Valid. Silakan Masukkan Ulang Nilai UTS.')

# Fungsi Validasi Nilai UAS
def validasi_uas():
    while True:
        global nilai_uas
        nilai_uas = input('\nMasukkan Nilai UAS (0-100): ')
        if nilai_uas.isnumeric() == True:
            if int(nilai_uas) >= 0 and int(nilai_uas) <= 100:
                return(nilai_uas)
                break
            else:
                print('\nMohon Maaf. Nilai UAS Anda di Luar Jangkauan Nilai. Silakan Masukan Ulang Nilai UAS Anda.')
        else: 
            print('\nMohon Maaf. Input Tidak Valid. Silakan Masukkan Ulang Nilai UAS.')

# FUNGSI-FUNGSI PENDUKUNG UNTUK PERINTAH YANG BERULANG ==============================================================================================================

# Fungsi Input NIM
def nomor_input():
    while True:
        global nomor
        nomor = input('\nMasukkan NIM: ')
        if nomor.isdigit() == True:
            if int(len(nomor)) != 8:
                print('\nMohon Maaf. NIM Harus Terdiri dari 8 Angka. ')
            else:
                nomor = int(nomor)
                break
        else:
            print('\nMohon Maaf. NIM Harus Terdiri dari 8 angka.') 

# Fungsi Jika Inputan Tidak Sesuai
def pilihan_salah():
    print('\nMohon Maaf. Pilihan yang Anda Masukkan Salah.')

# Fungsi Jika Data Kosong
def no_data():
    print('\nMohon Maaf. Data Tidak Tersedia.')    

# FUNGSI MENU UTAMA =================================================================================================================================================

def portal_data_mahasiswa():
    print('''
    Selamat Datang di Portal Data Nilai Mahasiswa Mata Kuliah Kalkulus (Semester Ganjil) di Fakultas Teknik Sipil dan Perencanaan (FTSP) Tahun 2024
    \n    Daftar Menu Utama:
    1. Menampilkan Seluruh Data Mahasiswa
    2. Menambahkan Data Mahasiswa
    3. Mengubah Data Mahasiswa
    4. Menghapus Data Mahasiswa
    5. Informasi Nilai Akhir Mahasiswa
    6. Keluar 
    ''')

    mainmenu_input = input('Silakan Pilih Menu yang Anda Inginkan (1-6): ')
    if mainmenu_input == '1':
        read_menu() 
    elif mainmenu_input == '2':
        add_menu()  
    elif mainmenu_input == '3':
        change_menu()
    elif mainmenu_input == '4':
        delete_menu()
    elif mainmenu_input == '5':
        count_menu()
    elif mainmenu_input == '6':
        print('\nTerima Kasih. Sukses Selalu.\n')
    else:
        pilihan_salah()
        portal_data_mahasiswa()

portal_data_mahasiswa() 
