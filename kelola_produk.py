
#                                   kelola_produk.py
#OPSI TAMBAH PRODUK
def tambah_produk():
    print("\n ===TAMBAH PRODUK BARU===")
    nama = input("Nama Barang : ")
    modal = int(input("Harga Modal : "))
    jual = int(input("Harga Jual  : "))
    stok = int(input("Stok        : "))

    #MEMASUKKAN DATA INPUT KE TABEL PRODUK
    cursor.execute("INSERT INTO produk (nama_produk, harga_modal, harga_jual, stok) VALUES (?, ?, ?, ?)", (nama, modal, jual, stok))
    conn.commit()
    print("Produk berhasil ditambahkan!\n")

#OPSI LIHAT PRODUK
def lihat_produk():
    cursor.execute("SELECT * FROM produk")
    semua_produk = cursor.fetchall()
    print("ID|Nama Barang|Harga Modal|Harga Jual|Stok ")
    for p in semua_produk:
       print(p[0], "|", p[1], "| Rp", p[2], "| Rp", p[3], "|", p[4])

#OPSI UPDATE PRODUK
def update_produk():
    lihat_produk()
    id_edit = int(input("Masukkan ID Produk yang mau diubah: "))
    cursor.execute("SELECT * FROM produk WHERE id = ?", (id_edit,))
    p = cursor.fetchone()

    #PERCABANGAN PADA UPDATE PRODUK
    if p!= None :
        print("Data lama:", p[1], "| Harga Jual:", p[3], "| Stok:", p[4])
        nama_baru = input("Nama Baru (kosongkan jika tidak diubah): ")
        if nama_baru == "":
            nama_baru = p[1]
        modal_baru = input("Harga Modal Baru (kosongkan jika tidak diubah): ")
        if modal_baru == "":
            modal_baru = p[2]
        else:
            modal_baru = int(modal_baru)
        jual_baru = input("Harga Jual Baru (kosongkan jika tidak diubah): ")
        if jual_baru == "":
            jual_baru = p[3]
        else:
            jual_baru = int(jual_baru)

        stok_baru = input("Stok Baru (kosongkan jika tidak diubah): ")
        if stok_baru == "":
            stok_baru = p[4]
        else:
            stok_baru = int(stok_baru)
        #EKSEKUSI UPDATE PRODUK KE TABEL PRODUK
        cursor.execute("UPDATE produk SET nama_produk = ?, harga_modal = ?, harga_jual = ?, stok = ? WHERE id = ?", (nama_baru, modal_baru, jual_baru, stok_baru, id_edit))
        conn.commit()
        print("Data produk berhasil diubah!\n")
    else:
        print("ID Produk tidak ada!\n")

#HAPUS PRODUK
def hapus_produk():
    lihat_produk()
    id_hapus = int(input("Masukkan ID Produk yang mau dihapus: "))
    cursor.execute("SELECT * FROM produk WHERE id = ?", (id_hapus,))
    p = cursor.fetchone()
    #PERCABANGAN PADA HAPUS PRODUK
    if p != None:
        yakin = input("Yakin menghapus " + p[1] + "? (Y/T): ")
        if yakin == "Y" or yakin == "y":
            cursor.execute("DELETE FROM produk WHERE id = ?", (id_hapus,))
            conn.commit()
            print("Produk berhasil dihapus!\n")
        else:
            print("Batal menghapus.\n")
    else:
        print("ID Produk tidak ditemukan!\n")

#MENU KELOLA PRODUK
def menu_kelola_produk():
    while True:
        print("====KELOLA PRODUK====")
        print("1. Lihat Produk")
        print("2. Tambah Produk")
        print("3. Update Produk")
        print("4. Hapus Produk")
        print("5. Kembali ke Menu Utama")
        pilih = input("Pilih menu (1-5): ")
        #PERCABANGAN PADA MENU KELOLA PRODUK
        if pilih == "1":
            lihat_produk()
        elif pilih == "2":
            tambah_produk()
        elif pilih == "3":
            update_produk()
        elif pilih == "4":
            hapus_produk()
        elif pilih == "5":
            break
        else:
            print("Pilihan tidak ada!")
