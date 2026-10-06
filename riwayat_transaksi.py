#                 riwayat_transaksi.py
def riwayat_transaksi():
    cursor.execute("SELECT * FROM transaksi ORDER BY id DESC")
    semua_tx = cursor.fetchall()

    if len(semua_tx) == 0:
        print("\nBelum ada riwayat transaksi!\n")
    else:
        print("\n================ RIWAYAT TRANSAKSI ================")
        print("ID Tx   | Tanggal             | Total Bayar ")
        print("---------------------------------------------------")
        for t in semua_tx:
            print(f"TX{t[0]:<5} | {t[1]:<19} | Rp{t[2]}")
        print("===================================================\n")
