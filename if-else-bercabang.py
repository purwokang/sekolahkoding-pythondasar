# LATIHAN: Putri raja sedang mencari jodoh
# syaratnya: Baik dan Rajin

tamu = "pria"
baik = True
rajin = True

if baik & rajin:
    if tamu == "pria":
        print("kita nikah yuk!")
    else:
        print("kita jadi saudara")

else:
    print("Hush! pergi sana!")


# Kode Alternatif:
# if baik & rajin & (tamu == "pria"):
#     print("kita nikah yuk!")
# elif baik & rajin & (tamu == "cewek"):
#     print("kita saudaraan")
# else:
#     print("Hush! pergi sana!")
