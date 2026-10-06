#                                  transaksi_penjualan.py
def transaksi_penjualan():
    #LIST AWAL
    list_id = []
    list_nama = []
    list_harga = []
    list_jumlah = []
    list_subtotal = []
    while True:
        #INPUT YANG DIBELI
        lihat_produk()
        id_beli = int(input("Masukkan ID Barang: "))
        jumlah_beli = int(input("Masukkan Jumlah Pembelian: "))
        #EKSEKUSI HASIL INPUT DARI TABEL PRODUK
        cursor.execute("SELECT * FROM produk WHERE id = ?", (id_beli,))
        p = cursor.fetchone()
        if p != None:
            stok_tersedia = p[4]
            #TOTAL BELANJAAN
            jumlah_lama_di_keranjang = 0
            for i in range(len(list_id)):
                if list_id[i] == id_beli:
                    jumlah_lama_di_keranjang = jumlah_lama_di_keranjang + list_jumlah[i]
            total_minta = jumlah_beli + jumlah_lama_di_keranjang
            if total_minta > stok_tersedia:
                print("\n ERROR: Stok tidak mencukupi.")
                print("\n Stok tersedia:", stok_tersedia)
                print("\n Silakan masukkan jumlah yang lebih kecil.")
            elif jumlah_beli <= 0:
                print("Jumlah harus lebih dari 0!")
            else:
                sub = p[3] * jumlah_beli
                list_id.append(p[0])
                list_nama.append(p[1])
                list_harga.append(p[3])
                list_jumlah.append(jumlah_beli)
                list_subtotal.append(sub)
                print("Berhasil menambahkan", p[1], "ke keranjang!")
        else:
            print("ID Barang tidak ditemukan!")
        lagi = input("\nTambah barang lain? (Y/T): ")
        if lagi != "Y" and lagi != "y":
            break
    #KERANJANG KOSONG
    if len(list_id) == 0:
        print("Transaksi dibatalkan karena keranjang kosong.\n")
        return
    #HITUNG TOTAL BELANJA
    total_belanja = 0
    for sub in list_subtotal:
        total_belanja = total_belanja + sub
    print("SMART RETAIL")
    print("Toko Maju Jaya")
    for i in range(len(list_id)):
        print(list_nama[i] + "  " + str(list_jumlah[i]) + " x " + str(list_harga[i]) + " = Rp" + str(list_subtotal[i]))
    print("TOTAL BELANJA : Rp" + str(total_belanja))
    #PEMBAYARAN
    uang_bayar = 0
    while True:
        uang_bayar = int(input("\nMasukkan Uang Bayar: Rp"))
        if uang_bayar < total_belanja:
            print("Uang bayar kurang! Kurang Rp" + str(total_belanja - uang_bayar))
        else:
            break
    kembalian = uang_bayar - total_belanja
    print("Kembalian     : Rp" + str(kembalian))

    #SIMPAN PENJUALAN KE DATABASE
    tgl = datetime.now().strftime("%d/%m/%Y %H:%M")
    cursor.execute("INSERT INTO transaksi (tanggal, total_bayar) VALUES (?, ?)", (tgl, total_belanja))
    conn.commit()
    id_transaksi_baru = cursor.lastrowid
    #UPDATE PADA TABEL PRODUK
    for i in range(len(list_id)):
        cursor.execute("INSERT INTO detail_transaksi (id_transaksi, id_produk, jumlah, subtotal) VALUES (?, ?, ?, ?)",
                       (id_transaksi_baru, list_id[i], list_jumlah[i], list_subtotal[i]))
        cursor.execute("UPDATE produk SET stok = stok - ? WHERE id = ?", (list_jumlah[i], list_id[i]))
    conn.commit()
    print("\n[SUCCESS] Transaksi berhasil disimpan!")

    #CETAK STRUK DALAM TXT
    nama_file = "struk_TX" + str(id_transaksi_baru) + ".txt"
    with open(nama_file, "w") as f:
        f.write("\n===SMART RETAIL===\n")
        f.write("\n===Toko Maju Jaya===\n")
        f.write("No Transaksi : TX" + str(id_transaksi_baru) + "\n")
        f.write("Tanggal      : " + tgl + "\n")
        for i in range(len(list_id)):
            f.write(list_nama[i] + "  " + str(list_jumlah[i]) + " x " + str(list_harga[i]) + " = Rp" + str(list_subtotal[i]) + "\n")
        f.write("TOTAL BELANJA : Rp" + str(total_belanja) + "\n")
        f.write("UANG BAYAR    : Rp" + str(uang_bayar) + "\n")
        f.write("KEMBALIAN     : Rp" + str(kembalian) + "\n")
    print("Struk dicetak ke file:", nama_file, "\n")
