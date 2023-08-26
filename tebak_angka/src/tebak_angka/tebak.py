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
