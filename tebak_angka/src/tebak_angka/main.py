from random import randint

kesempatan = 7

def print_art(teks):
    from art import tprint
    tprint(teks)

def is_guessed(tebakan, angka):
    if tebakan < angka:
        print("Tebakan terlalu rendah!")
    elif tebakan > angka:
        print("Tebakan terlalu tinggi ")
    else:
        print()

    return tebakan == angka

def main():
    print_art("Tebak Angka")
    angka = randint(1,100)
    print("Saya memikirkan satu angka di antara 1 sampai 100 ")
    print(f"Kamu diberi kesempatan menebak {kesempatan} kali")
    giliran = 0
    sukses = False
    while giliran < kesempatan:
        print("Coba tebak: ", end=" ")
        tebakan = int(input())
        if is_guessed(tebakan, angka):
            sukses = True
            break
        else:
            giliran = giliran + 1

    if sukses:
        print_art("Anda Berhasil!")
    else:
        print("Angka yang saya pikirkan: ", angka)
        print_art("Game Over!")

if __name__ == "__main__":
    main()


