#Membuat program dictionary
dict = {'Nama':'Angela','Hobi1':'Menari','Hobi2':'Mendengarkan lagu','Hobi3':'Menonton youtube','Sosmed1':'line: angelarms','Sosmed2':'ig:angela.rms','Sosmed3':'twitter:geminsme','Lagu1':'My Everything','Lagu2':'Kidult','Lagu3':'Crossroads','Makanan1':'Fettucine', 'Makanan2':'Burger','Makanan3':'Nasi goreng'}

#Mengubah salah satu hobi dan sosmed, menghapus 2 makanan, dan menambah 1 hobi
dict['Hobi2'] = 'Makan'
dict['Sosmed2'] = 'ig: angelareginem'
del dict['Makanan1']
del dict['Makanan2']
dict['Hobi4'] = 'Jalan-jalan'

print(dict)