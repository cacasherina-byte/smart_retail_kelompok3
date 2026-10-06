#                      inisialisasi_proyek.py
import sqlite3
from datetime import datetime
#BUAT DATABASE DAN KONEKSI
conn = sqlite3.connect("smart_retail.db")
cursor = conn.cursor()
#BUAT TABEL USER (UNTUK SISTEM LOGIN)
def buat_tabel():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT,
            role TEXT)""")
    #BUAT TABEL PRODUK (UNTUK KELOLA PRODUK)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produk (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_produk TEXT,
            harga_modal INTEGER,
            harga_jual INTEGER,
            stok INTEGER)""")
    #BUAT TABEL TRANSAKSI (UNTUK MODUL TRANSAKSI)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transaksi (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            tanggal TEXT,
            total_bayar INTEGER)""")
    #BUAT TABEL (UNTUK RIWAYAT TRANSAKSI)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS detail_transaksi (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            ID_transaksi INTEGER,
            ID_produk INTEGER,
            jumlah INTEGER,
            subtotal INTEGER)""")
    conn.commit()
    #MASUKKAN DATA RECORDS KE TABEL USER
    cursor.execute("SELECT * FROM users")
    data_user = cursor.fetchall()
    if len(data_user) == 0:
        cursor.execute("INSERT INTO users (username, password, role) VALUES ('Admin', '1234', 'Admin')")
        cursor.execute("INSERT INTO users (username, password, role) VALUES ('Kasir', '4321', 'Kasir')")
        conn.commit()
    #MASUKKAN DATA RECORDS KE TABEL PRODUK
    cursor.execute("SELECT * FROM produk")
    data_produk = cursor.fetchall()
    if len(data_produk) == 0:
        cursor.execute("INSERT INTO produk (nama_produk, harga_modal, harga_jual, stok) VALUES ('Beras 5 Kg', 65000, 75000, 20)")
        cursor.execute("INSERT INTO produk (nama_produk, harga_modal, harga_jual, stok) VALUES ('Gula 1 Kg', 15000, 18000, 30)")
        cursor.execute("INSERT INTO produk (nama_produk, harga_modal, harga_jual, stok) VALUES ('Minyak Goreng', 18000, 22000, 25)")
        cursor.execute("INSERT INTO produk (nama_produk, harga_modal, harga_jual, stok) VALUES ('Mie Instan', 2500, 3500, 100)")
        cursor.execute("INSERT INTO produk (nama_produk, harga_modal, harga_jual, stok) VALUES ('Kopi Sachet', 1000, 1500, 50)")
        conn.commit()
