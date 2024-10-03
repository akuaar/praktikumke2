usia= int(input("Masukkan usia anda: "))
tekanandarah = int(input("Masukkan tekanan darah anda:"))

if usia  >= 60 and tekanandarah >140 :
   print ("Status Kesehatan : Tinggi")
elif usia >=60 and tekanandarah <=140 :
   print ("Status Kesehatan : Normal ")
elif usia <60 and tekanandarah >130 :
   print ("Status Kesehatan : Tinggi")
elif usia <60 and tekanandarah <=130 :
   print ("Status Kesehatan : Normal")
   