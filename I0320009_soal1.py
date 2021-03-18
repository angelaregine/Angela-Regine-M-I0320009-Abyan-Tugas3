#Menampilkan list 10 teman
list = ['Adrian', 'Audrey', 'Evelyn', 'Candrika', 'Funny', 'Aratia', 'Divana', 'Ayu', 'Gea', 'Hana']

#Menampilkan isi list indeks nomor 4,6,7
print("List indeks nomor 4,6,7 yaitu", list[4], ",", list[6], ", dan", list[7])

#Mengganti nama teman di list 3,5,9
list[3] = 'Elisa'
list[5] = 'Bagus'
list[9] = 'Dendy'

#Menambahkan 2 nama teman
list.append('Afiq')
list.append('Fadhila')

#Menampilkan semua nama teman dengan pengulangan
print(list*2)

#Menampilkan panjang list
print(len(list))
