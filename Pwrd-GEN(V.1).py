# Created by: ShiDdos
# Password Maker V.1

import random
import os

os.system('clear')

banner = """
  /$$$$$$  /$$       /$$ /$$$$$$$        /$$                    
 /$$__  $$| $$      |__/| $$__  $$      | $$                    
| $$  \__/| $$$$$$$  /$$| $$  \ $$  /$$$$$$$  /$$$$$$   /$$$$$$$
|  $$$$$$ | $$__  $$| $$| $$  | $$ /$$__  $$ /$$__  $$ /$$_____/
 \____  $$| $$  \ $$| $$| $$  | $$| $$  | $$| $$  \ $$|  $$$$$$ 
 /$$  \ $$| $$  | $$| $$| $$  | $$| $$  | $$| $$  | $$ \____  $$
|  $$$$$$/| $$  | $$| $$| $$$$$$$/|  $$$$$$$|  $$$$$$/ /$$$$$$$/
 \______/ |__/  |__/|__/|_______/  \_______/ \______/ |_______/
"""

print(banner)

os.system('sleep 1')

media = '\33[31mSocial Media: \nInstagram: https://www.instagram.com/shidoreal/ \nYoutube: https://www.youtube.com/@shiddos \nGithub: https://github.com/ShiDdos\33[0m'

print(media)

print()
print("######################################################################################")
print()

print("~~~~~~~~~~~~~~~~~~~~~~~~BAŞLANGIÇTA 3 SANİYE BEKLE!~~~~~~~~~~~~~~~~~~~~~~~~")

os.system('sleep 4')

os.system('clear')

banner = """
  /$$$$$$  /$$       /$$ /$$$$$$$        /$$                    
 /$$__  $$| $$      |__/| $$__  $$      | $$                    
| $$  \__/| $$$$$$$  /$$| $$  \ $$  /$$$$$$$  /$$$$$$   /$$$$$$$
|  $$$$$$ | $$__  $$| $$| $$  | $$ /$$__  $$ /$$__  $$ /$$_____/
 \____  $$| $$  \ $$| $$| $$  | $$| $$  | $$| $$  \ $$|  $$$$$$ 
 /$$  \ $$| $$  | $$| $$| $$  | $$| $$  | $$| $$  | $$ \____  $$
|  $$$$$$/| $$  | $$| $$| $$$$$$$/|  $$$$$$$|  $$$$$$/ /$$$$$$$/
 \______/ |__/  |__/|__/|_______/  \_______/ \______/ |_______/
"""

print(banner)

os.system('sleep 1')

media = '\33[31mSocial Media: \nInstagram: https://www.instagram.com/shidoreal/ \nYoutube: https://www.youtube.com/@shiddos \nGithub: https://github.com/ShiDdos\33[0m'
print(media)

print()
print("######################################################################################")
print()


karakter = 'abcçdefgğhıijklmnoöprsştuüvyz1234567890ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ!@#$%^&*'

psayi = input('Sistem[?]> Kaç şifre üretmek istiyorsunuz?: ')
psayi = int(psayi)

uzunluk = input('Sistem[?]> Şifrenin uzunluğu? : ')
uzunluk = int(uzunluk)

print("Sistem[!]>Şifre hazırlanıyor!")

os.system('Sleep 3')

print("~~~~~~~~~~~~~~~~~~~~~~~~Şifre Hazır!~~~~~~~~~~~~~~~~~~~~~~~~")

for password in range(psayi):
	sifre = ''
	for char in range(uzunluk):
	    sifre += random.choice(karakter)        
	print("[*]Şifren:",sifre)
input()	