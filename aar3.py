nilai = int(input("Masukkan nilai ujian anda (0-100): "))

kehadiran = input("Apakah anda hadir dalam ujian? (hadir/tidak hadir): ")
if nilai >= 75 and kehadiran. lower() == "hadir" :
   print("Kategori : lulus")
elif nilai < 75 and kehadiran.lower() == "hadir":
   print ( " Kategori: Remedial")
else:
    print("Kategori: Tidak Lulus")
    