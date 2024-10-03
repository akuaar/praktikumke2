nilai = int(input("Masukkan nilai ujian anda (0-100): "))

if 90 <= nilai<= 100:
    print("Sangat Baik")
elif 80 <= nilai<= 89:
    print("Baik")
elif 70 <= nilai<= 79:
    print("Cukup")
elif 60 <= nilai<= 69:
    print("Kurang")
else:
    print("Sangat Kurang")

