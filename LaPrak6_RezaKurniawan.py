# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 19:26:01 2021

@author: rezakurniawan
"""

import math

def kubus(rusuk):
	luas = 6 * rusuk**2
	print(f"Luas permukaan kubus tersebut adalah {luas} cm²")
	
def balok(panjang, lebar, tinggi):
	luas = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))
	print(f"Luas permukaan balok tersebut adalah {luas} cm²")
	
def tabung(jari_jari, tinggi):
	if jari_jari % 7 == 0:
		luas = 2 * (22/7) * jari_jari * (jari_jari + tinggi)
	else:
		luas = 2 * math.pi * jari_jari * (jari_jari + tinggi)
	print(f"Luas permukaan tabung tersebut adalah {luas} cm²")
	
def kerucut(jari_jari, garis_lukis):
	if jari_jari % 7 == 0:
		luas = (22/7) * jari_jari * (jari_jari + garis_lukis)
	else:
		luas = math.pi * jari_jari * (jari_jari + garis_lukis)
	print(f"Luas permukaan kerucut tersebut adalah {luas} cm²")

def bola(jari_jari):
	if jari_jari % 7 == 0:
		luas = 4 * (22/7) * jari_jari **2
	else:
		luas = 4 * math.pi * jari_jari **2
	print(f"Luas permukaan bola tersebut adalah {luas} cm²")

while True:
	print("\nKalkulator Luas Permukaan Bangun Ruang\n1. Kubus\t| 4. Kerucut\n2. Balok\t| 5. Bola\n3. Tabung\t| 6. Exit")
	
	menu = int(input("Pilih menu yang tersedia: "))
	if menu == 1:
		rusuk = int(input("Masukkan nilai rusuk: "))
		kubus(rusuk)
	elif menu == 2:
		panjang, lebar, tinggi = int(input("Masukkan nilai panjang: ")), int(input("Masukkan nilai lebar: ")), int(input("Masukkan nilai tinggi: "))
		balok(panjang, lebar, tinggi)
	elif menu == 3:
		jari_jari, tinggi = int(input("Masukkan nilai jari-jari: ")), int(input("Masukkan nilai tinggi: "))
		tabung(jari_jari, tinggi)
	elif menu == 4:
		jari_jari, garis_lukis = int(input("Masukkan nilai jari-jari: ")), int(input("Masukkan nilai garis lukis: "))
		kerucut(jari_jari, garis_lukis)
	elif menu == 5:
		jari_jari = int(input("Masukkan nilai jari-jari: "))
		bola(jari_jari)
	elif menu == 6:
		print('\nT E R I M A  K A S I H  ! !')
		break