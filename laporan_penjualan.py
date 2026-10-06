#              laporan_penjualan.py
def laporan_penjualan():
    #TOTAL PENJUALAN
    cursor.execute("SELECT COUNT(*) FROM transaksi")
    total_tx = cursor.fetchone()[0]

    #TOTAL PENDAPATAN
    cursor.execute("SELECT SUM(total_bayar) FROM transaksi")
    total_uang = cursor.fetchone()[0] or 0

    #PRODUK TERLARIS
    cursor.execute("""
        SELECT produk.nama_produk, SUM(detail_transaksi.jumlah)
        FROM detail_transaksi
        JOIN produk ON detail_transaksi.id_produk = produk.id
        GROUP BY detail_transaksi.id_produk
        ORDER BY SUM(detail_transaksi.jumlah) DESC
        LIMIT 1
    """)
    terlaris = cursor.fetchone()

    #STOK DALAM KEADAAN SEKARAT (STOK < 10)
    cursor.execute("SELECT nama_produk, stok FROM produk WHERE stok < 10")
    stok_tipis = cursor.fetchall()

    print("\n==========================================")
    print("            LAPORAN PENJUALAN             ")
    print("==========================================")
    print("Jumlah Transaksi :", str({total_tx}))
    print("Total Penjualan  :", "Rp.", str({total_uang}))

    print("\nProduk Terlaris  :")
    if terlaris is not None:
        print(f"- {terlaris[0]} (Terjual {terlaris[1]} pcs)")
    else:
        print("- Belum ada data transaksi")

    print("\nStok Hampir Habis (< 10):")
    if len(stok_tipis) > 0:
        for s in stok_tipis:
            print(f"- {s[0]} ({s[1]} pcs)")
    else:
        print("Semua stok aman.")
    print("====================\n")


def main():
    buat_tabel()

    while True:
        status_login, username_login, role_login = login()
        if status_login:
            while True:
                print("=== SMART RETAIL ===")
                print(f" User: {username_login} | Role: {role_login}")
                print("==============================================")

                if role_login == "Admin":
                    print("1. Kelola Produk")
                    print("2. Transaksi Penjualan")
                    print("3. Cari Produk")
                    print("4. Riwayat Transaksi")
                    print("5. Laporan Penjualan")
                    print("6. Logout")

                    pilih = input("Pilih menu (1-6): ")

                    if pilih == "1":
                        menu_kelola_produk()
                    elif pilih == "2":
                        transaksi_penjualan()
                    elif pilih == "3":
                        cari_produk()
                    elif pilih == "4":
                        riwayat_transaksi()
                    elif pilih == "5":
                        laporan_penjualan()
                    elif pilih == "6":
                        print("Logout berhasil.\n")
                        break
                    else:
                        print("Pilihan menu salah!")

                elif role_login == "Kasir":
                    print("1. Transaksi Penjualan")
                    print("2. Lihat Daftar Produk")
                    print("3. Cari Produk")
                    print("4. Logout")

                    pilih = input("Pilih menu (1-4): ")

                    if pilih == "1":
                        transaksi_penjualan()
                    elif pilih == "2":
                        lihat_produk()
                    elif pilih == "3":
                        cari_produk()
                    elif pilih == "4":
                        print("Logout berhasil.\n")
                        break
                    else:
                        print("Pilihan menu salah!")

        keluar = input("Keluar dari aplikasi? (Y/T): ")
        if keluar == "Y":
            print("Terima kasih sudah menggunakan aplikasi ini!")
            break

if __name__ == "__main__":
    main()
