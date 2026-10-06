#                   login_sistem.py
def login():
    print("=== MENU LOGIN ===")
    print("BOCORAN LOG IN:")
    print("1. Username : Admin, Password : 1234")
    print("2. Username : Kasir, Password : 4321")
    #INPUT
    user_input = input("Username: ")
    pass_input = input("Password: ")

    #HASIL EKSEKUSI DARI INPUT
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (user_input, pass_input))
    hasil = cursor.fetchone()
    #PERCABANGAN PADA INPUT
    if hasil is not None:
        user_id = hasil[0]
        username_login = hasil[1]
        role_login = hasil[3]
        print(f"\nLogin berhasil! Selamat datang {username_login}")
        return True, username_login, role_login
    else:
        print("\nUsername atau password salah, coba lagi!")
        return False, None, None
