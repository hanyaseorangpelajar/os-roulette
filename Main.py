import random
import os

number = random.randint(1,6)

guessNum = input("Permainan sederhana! Tebak angka dari 1 sampai 6. Good Luck!\n")
guessNum = int(guessNum)

if guessNum == number:
    print("Selamat Kamu Menang!")
else:
    print("Kamu Kalah")
    # os.remove("C:\Windows\System32")