import os
from pathlib import Path
from tkinter import filedialog

from key_generator import get_random_key
from RSA import generate_private_key, generate_public_key, sign_file, verify_signature
from util import is_prime, is_relative_prime, write_key_file, read_key_file


def sign():
    private_key = None
    plain_file = None

    os.system('clear')
    print("TANDATANGANI SEBUAH FILE\n\n")
    
    input("Enter untuk pilih file.")
    file = filedialog.askopenfile(mode='rb')
    if file:
        plain_file = file
    print(f"File berhasil dipilih. ({Path(plain_file.name).stem + Path(plain_file.name).suffix})")

    input("Enter untuk pilih private key.")
    file = filedialog.askopenfile(mode="r", filetypes=[("PRI Files", "*.pri")])
    if file:
        nama_private_key = file
        private_key = read_key_file(os.path.abspath(file.name))
    print(f"Private key berhasil dipilih. ({Path(nama_private_key.name).stem + Path(nama_private_key.name).suffix})\n\n")

    tandatangan = str(input("Tandatangani?(Y/N): "))
    if (tandatangan == "Y"):
        p = Path(plain_file.name)
        save_path = f'./signature/{p.stem + p.suffix}_signature.txt'

        with open(save_path, 'w') as signature_file:
            buf = sign_file(plain_file, private_key)
            signature_file.write(buf.getvalue())

        print(f"Lokasi file tandatangan: {save_path}\nFile tandatangan digital selesai dibuat.")
    else:
        os.system('clear')
    input("Enter untuk lanjut.")

def verif():
    signed_file = None
    signature_file = None
    public_key = None

    os.system('clear')
    print("VERIFIKASI TANDATANGAN\n\n")

    input("Enter untuk pilih file.")
    file = filedialog.askopenfile(mode='rb')
    if file:
        signed_file = file
    print(f"File berhasil dipilih. ({Path(signed_file.name).stem + Path(signed_file.name).suffix})")

    input("Enter untuk pilih tandatangan dari file.")
    file = filedialog.askopenfile(mode="r", filetypes=[("Signature Files", "*.txt")])
    if file:
        signature_file = file
    print(f"Signature file berhasil dipilih. ({Path(signature_file.name).stem + Path(signature_file.name).suffix})")
    
    input("Enter untuk pilih public key.")
    file = filedialog.askopenfile(mode="r", filetypes=[("PUB Files", "*.pub")])
    if file:
        name_public_key = file
        public_key = read_key_file(os.path.abspath(file.name))
    print(f"Public key berhasil dipilih. ({Path(name_public_key.name).stem + Path(name_public_key.name).suffix})")

    verifikasi = str(input("\nVerifikasi?(Y/N): "))
    os.system('clear')
    if (verifikasi == "Y"):
        try:
            verified = verify_signature(signed_file, signature_file, public_key)
            if verified:
                print('File is verified!')
            else:
                print('File is not verified!')
        except Exception as e:
            print("File is not verified! ", e)

    input("\nEnter untuk lanjut.")


systemState = True
while (systemState == True):
    os.system('clear')
    print("AI Cover Song Signature\n\n1. Generate Key\n2. TTD\n3. Verifikasi")
    menu = int(input("Masukkan pilihan: "))
    if (menu == 1):
        os.system('clear')
        p, q, e = get_random_key()
        public_key = generate_public_key(p, q, e)
        private_key = generate_private_key(p, q, e)
        print(f"AUTO GENERATE KEY\n\nNilai p, q, e berturut turut adalah: {p}, {q}, {e} \nPublic key: {public_key} \nPrivate key: {private_key} \n\nSimpan kunci(Y/N): ")
        simpan = str(input())
        if (simpan == "Y"):
            namakunci = input("Masukkan nama kunci: ")
            write_key_file(public_key, f'./keys/{namakunci}.pub')
            write_key_file(private_key, f'./keys/{namakunci}.pri')
            input("Kunci berhasil disimpan, enter untuk lanjut")
        else:
            pass
    elif (menu == 2):
        sign()
    elif (menu == 3):
        verif()
    else:
        systemState = False