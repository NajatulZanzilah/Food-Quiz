import random
import time

makanan_indonesia = {
    "Rawon": "Jawa Timur",
    "Gudeg": "Yogyakarta",
    "Pempek": "Palembang",
    "Rendang": "Sumatera Barat",
    "Papeda": "Papua",
    "Sate Lilit": "Bali",
    "Coto Makassar": "Sulawesi Selatan",
    "Soto Banjar": "Kalimantan Selatan",
    "Ayam Taliwang": "Nusa Tenggara Barat",
    "Sate Madura": "Jawa Timur",
    "Soto Betawi": "DKI Jakarta",
    "Otak-otak": "Kepulauan Riau",
    "Tinutuan": "Sulawesi Utara",
    "Ayam Woku": "Sulawesi Utara",
    "Bika Ambon": "Sumatera Utara",
    "Lontong Balap": "Jawa Timur",
    "Tahu Sumedang": "Jawa Barat",
    "Soto Kudus": "Jawa Tengah",
    "Mie Aceh": "Aceh",
    "Ikan Bakar Manokwari": "Papua Barat",
    "Serabi": "Jawa Barat",
    "Gado-Gado": "DKI Jakarta",
    "Ayam Betutu": "Bali",
    "Sop Konro": "Sulawesi Selatan",
    "Gulai Ikan Patin": "Riau",
    "Kerak Telor": "DKI Jakarta",
    "Soto Lamongan": "Jawa Timur",
    "Nasi Kucing": "Yogyakarta",
    "Ayam Rica-Rica": "Sulawesi Utara",
    "Tempoyak": "Sumatera Selatan",
    "Sate Padang": "Sumatera Barat",
    "Nasi Liwet": "Jawa Tengah",
}

def show_trophy():
    print("\n")
    print("                █████████████████████")
    print("                █░░░░░░░░░░░░░░░░░░░█")
    print("                █    🏆  🏆  🏆     █")
    print("                █░░░░░░░░░░░░░░░░░░░█")
    print("                █████████████████████")
    print("                     ██████████")
    print("                   ██████████████")
    print("                 ██████████████████")
    print("                 █                █")
    print("                 █    CONGRATS    █")
    print("                 █                █")
    print("                 ██████████████████")
    print("\n")

def show_game_over():
    print("\n")
    print("██████   █████  ███    ███ ███████      ███████  ██      ██ ███████ ██████ ")
    print("██      ██   ██ ████  ████ ██          ██     ██ ██      ██ ██      ██   ██")
    print("██      ███████ ██ ████ ██ █████       ██     ██ ██      ██ █████   ██████ ")
    print("██  ███ ██   ██ ██  ██  ██ ██          ██     ██ ██      ██ ██      ██   ██")
    print("███████         ██  ██  ██ ███████     █████████ ██████████ ███████ ██")
    print("")
    print("            ███████████████████████████████████")
    print("            █░░░░░░░░░░░  GAME OVER  ░░░░░░░░░█")
    print("            ███████████████████████████████████")
    print("\n")

def main_sendiri():
    print("\n=== MODE MAIN SENDIRI ===")
    nama = input("Masukkan nama player: ")

    nyawa = 3
    score = 0
    soal_total = 10

    keys = list(makanan_indonesia.keys())
    random.shuffle(keys)  

    for i in range(soal_total):
        makanan = keys[i]
        jawaban_benar = makanan_indonesia[makanan]

        print(f"\nSoal {i+1}/{soal_total}")
        print(f"➡ Dari daerah mana makanan **{makanan}** berasal?")
        jawab = input("Jawaban: ")

        if jawab.lower() == jawaban_benar.lower():
            print("✔ BENAR!")
            score += 10
        else:
            print("❌ SALAH!")
            print(f"Jawaban benar: {jawaban_benar}")
            nyawa -= 1

        print(f"Nyawa: {nyawa} | Score: {score}")
        print("----------------------------------")

        if nyawa == 0:
            break

    if nyawa == 0:
        show_game_over()
    else:
        print("\nSELESAI! Semua soal sudah dijawab.")

    print(f"Score Akhir: {score}")

    if score >= 80:
        show_trophy()

def main_bersama():
    print("\n=== MODE MAIN BERSAMA TEMAN ===")
    player1 = input("Nama Player 1: ")
    player2 = input("Nama Player 2: ")

    nyawa1 = 3
    nyawa2 = 3
    score1 = 0
    score2 = 0
    soal_total = 10

    keys = list(makanan_indonesia.keys())
    random.shuffle(keys)

    giliran = 0 
    players = [player1, player2]

    for i in range(soal_total):
        pemain = players[giliran]
        makanan = keys[i]
        jawaban_benar = makanan_indonesia[makanan]

        print(f"\nSoal {i+1}/{soal_total}")
        print(f"GILIRAN: {pemain}")
        print(f"➡ Dari daerah mana makanan **{makanan}** berasal?")
        jawab = input("Jawaban: ")

        if pemain == player1:
            if jawab.lower() == jawaban_benar.lower():
                score1 += 10
                print("✔ BENAR!")
            else:
                nyawa1 -= 1
                print("❌ SALAH! Jawaban benar:", jawaban_benar)
        else:
            if jawab.lower() == jawaban_benar.lower():
                score2 += 10
                print("✔ BENAR!")
            else:
                nyawa2 -= 1
                print("❌ SALAH! Jawaban benar:", jawaban_benar)

        print(f"{player1}: Nyawa {nyawa1} | Score {score1}")
        print(f"{player2}: Nyawa {nyawa2} | Score {score2}")
        print("----------------------------------")

        if nyawa1 == 0 or nyawa2 == 0:
            break

        giliran = 1 - giliran  

    print("\n=== HASIL ===")

    if nyawa1 == 0 and nyawa2 > 0:
        print(f"Pemenang: {player2}")
        show_trophy()
    elif nyawa2 == 0 and nyawa1 > 0:
        print(f"Pemenang: {player1}")
        show_trophy()
    else:
        if score1 > score2:
            print(f"Pemenang: {player1}")
            show_trophy()
        elif score2 > score1:
            print(f"Pemenang: {player2}")
            show_trophy()
        else:
            print("Hasil SERI!")
            show_game_over()

def main():
    while True:
        print("\n==============================")
        print(" GAME TEBAK MAKANAN INDONESIA")
        print("==============================")
        print("1. Main Sendiri")
        print("2. Main Bersama Teman")
        print("3. Keluar")
        print("==============================")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            main_sendiri()
        elif pilihan == "2":
            main_bersama()
        elif pilihan == "3":
            print("Keluar dari game...")
            break
        else:
            print("Pilihan tidak valid!")

main()