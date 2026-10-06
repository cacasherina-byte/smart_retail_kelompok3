#                          validasi_stok.py
def validasi_stok_keranjang(produk, id_beli, jumlah_beli, list_id, list_jumlah):
    stok_tersedia = produk[4]
    jumlah_lama_di_keranjang = 0

    #MENGHITUNG TOTAL BELANJA SEBELUMNYA YANG ADA DI KERANJANG
    for i in range(len(list_id)):
        if list_id[i] == id_beli:
            jumlah_lama_di_keranjang += list_jumlah[i]

    total_minta = jumlah_beli + jumlah_lama_di_keranjang

    if total_minta > stok_tersedia:
        print("\nERROR: Stok tidak mencukupi.")
        print(f"Stok tersedia: {stok_tersedia}")
        print("Silakan masukkan jumlah yang lebih kecil.\n")
        return False
    elif jumlah_beli <= 0:
        print("\nJumlah harus lebih dari 0!\n")
        return False

    return True

#FUNGSI CARI PRODUK (AGAR TIDAK ERROR SAAT DIPANGGIL DI MAIN)
def cari_produk():
    keyword = input("Masukkan nama produk yang dicari: ")
    cursor.execute("SELECT * FROM produk WHERE nama_produk LIKE ?", ('%' + keyword + '%',))
    hasil = cursor.fetchall()
    if len(hasil) > 0:
        print("\nID|Nama Barang|Harga Modal|Harga Jual|Stok ")
        for p in hasil:
            print(p[0], "|", p[1], "| Rp", p[2], "| Rp", p[3], "|", p[4])
        print()
    else:
        print("\nProduk tidak ditemukan!\n")
