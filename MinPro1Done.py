Menu = ("1. Daftar Pasien Baru", "2. Ubah Data Pasien", "3. Hapus Data Pasien", "4. Lihat Data Pasien")
Data_Pasien = []

print("Tampilan Menu: ")
for i in Menu:
    print (i)

while True:
    A_menu = input("Silahkan memilih Menu (ketik keluar untuk berhenti): ")
    if A_menu == "keluar":
        break

    if A_menu == "1" :
        Nama = str(input("Masukkan nama pasien: "))
        umur = int(input("Masukkan umur pasien: "))
        keluhan = str(input("Masukkan keluhan pasien: "))

        if keluhan == "gigi":
            poli = "Poli Gigi"

        elif umur < 17:
            poli = "Poli Anak"

        else:
            poli = "Poli Umum"

        pasien = {
            "Nama" : Nama,
            "Umur" : umur,
            "Keluhan" : keluhan,
            "Poli" : poli
        }
        Data_Pasien.append(pasien)
        print("Pendaftaran pasien berhasil! Silahkan menuju poli yang sudah ditentukan.")
        print("Data pasien baru: ")

        for pasien in Data_Pasien:
            print (pasien)

    elif A_menu == "2":
      Cari_nama = str(input("Masukkan nama pasien yang ingin diubah: "))

      for pasien in Data_Pasien:
          if pasien ["Nama"] == Cari_nama:

              nama_baru = str(input("masukkan nama baru pasien: "))
              umur_baru = int(input("masukkan umur baru pasien: "))
              keluhan_baru = str(input("masukkan keluhan baru pasien: "))

              if keluhan_baru == "gigi":
                  poli_baru = "Poli Gigi"
              elif umur_baru <17:
                  poli_baru = "Poli Anak"
              else:
                  poli_baru = "Poli Umum"

              pasien["Nama"] = nama_baru
              pasien["Umur"] = umur_baru
              pasien["Keluhan"] = keluhan_baru
              pasien["Poli"] = poli_baru   

              print("Data pasien berhasil diubah!")
              print("Data pasien terbaru: ")
              for pasien in Data_Pasien:
                  print(pasien)

              break
              
      else:    
            print("nama atau data pasien tidak valid, silahkan memilih ulang") 
            

    elif A_menu == "3":
        Cari_nama = str(input("Masukkan nama pasien yang ingin dihapus: "))   

        for pasien in Data_Pasien:
             if pasien ["Nama"] == Cari_nama:
                 Data_Pasien.remove(pasien)

                 print("Pasien berhasil dihapus dari daftar")
                 print("Data pasien terbaru: ")
                 for pasien in Data_Pasien:
                     print(pasien)

                 break
                
        else:
            print("Nama pasien tidak valid")
        

    elif A_menu == "4":
         print("Daftar data pasien: ")

         if not Data_Pasien:
             print("Belum ada data pasien")

         else:
             for pasien in Data_Pasien:
                print(pasien) 
            

    else:
        print("Pilihan tidak valid. Harap pilih ulang sesuai dengan pilihan yang disediakan.")
       