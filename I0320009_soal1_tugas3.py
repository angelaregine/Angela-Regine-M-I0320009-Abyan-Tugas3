#Menampilkan list 10 teman
Nama_teman = ['Adrian', 'Audrey', 'Evelyn', 'Candrika', 'Funny', 'Aratia', 'Divana', 'Ayu', 'Gea', 'Hana']

#Menampilkan isi list indeks nomor 4,6,7
print("List indeks nomor 4,6,7 yaitu", Nama_teman[4], ",", Nama_teman[6], ", dan", Nama_teman[7])

#Mengganti nama teman di list 3,5,9
Nama_teman[3] = 'Elisa'
Nama_teman[5] = 'Bagus'
Nama_teman[9] = 'Dendy'

#Menambahkan 2 nama teman
Nama_teman.append('Afiq')
Nama_teman.append('Fadhila')

#Menampilkan semua nama teman dengan pengulangan
friend = 0
for teman in range (0,12) :
    print (Nama_teman[friend])
    friend+=1

#Menampilkan panjang list
print("Panjang indeks list yaitu", len(Nama_teman))