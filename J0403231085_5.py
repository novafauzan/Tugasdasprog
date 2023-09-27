#Alat BMI dibuat oleh Fauzan Fuadiansyah dengan NIM J0403231085
tinggi = int(input('masukkan tinggi badan: ')) / 100
berat = int(input('masukkan berat badan: '))
IMT = berat/tinggi**2
print(IMT)
if IMT <= 18.5 :
    print('kurus')
elif IMT <= 25 :
    print('normal')
elif IMT <= 30 :
    print('gemuk')
elif IMT > 30 :
    print ('kegemukan')