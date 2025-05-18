import os
import time
import sys

def warna(teks, warna):
    warna_kode = {
        # Warna dasar terang
        'merah': '\033[91m',
        'hijau': '\033[92m',
        'kuning': '\033[93m',
        'biru': '\033[94m',
        'ungu': '\033[95m',
        'cyan': '\033[96m',
        'putih': '\033[97m',
        'hitam': '\033[90m',
        
        # Warna terang versi muda / light
        'merah_muda': '\033[95m',
        'hijau_muda': '\033[92m',
        'kuning_muda': '\033[93m',
        'biru_muda': '\033[94m',
        'ungu_muda': '\033[95m',
        'cyan_muda': '\033[96m',

        # Efek teks
        'bold': '\033[1m',
        'underline': '\033[4m',
        'blink': '\033[5m',
        'reversed': '\033[7m',
        
        # Reset / normal
        'reset': '\033[0m',
    }

    return warna_kode.get(warna, '\033[0m') + teks + warna_kode['reset']

def banner():
    os.system("clear")
    
    print(warna("""Dibuat Oleh Po1OsS♤""", 'biru'))
    print(warna("""
⠀⠀⣿⠲⠤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣸⡏⠀⠀⠀⠉⠳⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⠀⠀⠀⠀⠀⠀⠀⠉⠲⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⣄⠀⠀⠀⡰⠋⢙⣿⣦⡀⠀⠀⠀⠀⠀
⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣙⣦⣮⣤⡀⣸⣿⣿⣿⣆⠀⠀⠀⠀
⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⠀⣿⢟⣫⠟⠋⠀⠀⠀⠀
⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣷⣷⣿⡁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⢸⣿⣿⣧⣿⣿⣆⠙⢆⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⣿⣤⣿⣿⣿⡟⠹⣿⣿⣿⣿⣷⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣧⣴⣿⣿⣿⣿⠏⢧⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠈⢳⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡏⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⢳
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠸⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇⢠⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣼⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠛⠻⠿⣿⣿⣿⡿⠿⠿⠿⠿⠿⢿⣿⣿⠏⠀⠀⠀⠀⠀⠀
""", 'merah'))
    print(warna("Advanced Toolkit by Po1OsS♤", 'kuning'))

def info_user():
    print(warna("""
╭──────────[ INFO USER ]──────────╮
│  Pemilik Script : Po1OsS♤       │
│  Status VIP        : ∞ Days     │
│  Hak Akses      : Penuh         │
│  Termux Support : YES           │
│  Version : 0.1                  │
╰─────────────────────────────────╯
""", 'cyan_muda'))

def menu():
    print(warna("""    

 [1]. DOOS VL
   
""", 'hijau'))

def main():
    banner()
    info_user()
    menu()
    choice = input(warna("Pilih opsi: ", 'ungu')).lower()
    if choice == '0':
        print(warna("Keluar dari script...", 'merah'))
        exit()
    elif choice == '1':
        os.system("python3 PolossSc/DDOSV1[vl].py")
    elif choice == '2':
        os.system("python3 PolossSc/DDOSV2[Samp].py")
    elif choice == '3':
        os.system("python3 PolossSc/DDOSV3[God].py")
    elif choice == '4':
        os.system("python3 PolossSc/DDOSV4[UDP].py")
    elif choice == '5':
        os.system("python3 PolossSc/ALL.py")
    elif choice == 'endd':
        print(warna("Restarting script...", 'kuning'))
        time.sleep(1)
        os.execv(sys.executable, ['python'] + sys.argv)
    else:
        print(warna("Fitur ini belum diaktifkan atau sedang dikembangkan.", 'merah'))
        input(warna("Tekan Enter untuk kembali ke menu...", 'kuning'))
        main()

if __name__ == "__main__":
    main()