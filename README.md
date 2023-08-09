# Praktikum-4-DasPro
Praktikum 4 Dasar Pemrograman Institut Teknologi Bandung yang menggunakan bahasa Python
## Soal 1
Buatlah program yang menentukan ada berapa banyak bilangan bulat yang tidak lebih kecil dari X tetapi tidak lebih besar dibandingkan Y yang habis dibagi 3 dan atau 4. Jika tidak ada bilangan bulat yang memenuhi maka tampilkan “Tidak Ada”. X dan Y merupakan bilangan bulat positif yang kurang dari 1000.
Untuk membaca input dalam satu baris dan mengubahnya menjadi array, gunakan kode berikut
a = list(map(int, input("").split()))
## Soal 2
Diberikan dua buah bilangan yaitu  N dan M serta list yang berisi N buah bilangan integer yaitu a. Anda ingin mengetahui ada berapa banyak bilangan pada list tersebut yang merupakan Bilangan Best. Sebuah bilangan a[i] termasuk ke dalam Bilangan Best jika terdapat bilangan lain yang nilainya sama dengan a[i] dan jaraknya dari indeks i maksimal sebesar M. Tentukanlah ada berapa banyak elemen dari list a yang termasuk ke dalam bilangan best. N  dan M merupakan bilangan bulat positif.
Hint:
Untuk membaca input dalam satu baris dan mengubahnya menjadi array, gunakan kode berikut
a = list(map(int, input("").split()))
## Soal 3
Buatlah sebuah program yang menerima masukan sebuah bilangan bulat N dan sebuah array a yang berisi bilangan bulat sebanyak N. N harus divalidasi terlebih dahulu apakah N bernilai valid, yaitu 0 < N <= 100. Jika N valid, program akan menerima bilangan bulat sebanyak N yang nilainya berada di antara -1000 dan 1000 (-1000 dan 1000 juga termasuk ke dalam kemungkinan nilai) dan tidak terurut serta tidak dijamin unik. Program kemudian menerima input bilangan X. Keluarkan elemen pada array yang nilainya terkecil kedua dari keseluruhan elemen pada array yang lebih besar dari X. Jika tidak ada, keluarkan -1. 
Note : Dilarang menggunakan fungsi sort python
Hint:
Untuk membaca input dalam satu baris dan mengubahnya menjadi array, gunakan kode berikut
a = list(map(int, input("").split()))
## Soal 4
Diberikan sebuah bilangan N dan sebuah list yang berisi N buah bilangan bulat non negatif yaitu a. Karena Anda menyukai bilangan berdigit 1 (bilangan yang nilainya kurang dari 10) maka Anda ingin membuat seluruh elemen pada list berdigit 1. Pada sebuah operasi anda dapat mengubah nilai dari suatu bilangan menjadi jumlah dari setiap digitnya, misalnya yaitu 123 diubah menjadi 1+2+3 = 6. Tentukan jumlah operasi minimum yang diperlukan untuk membuat seluruh bilangan pada list menjadi berdigit 1. N dijamin positif dan nilai dari sebuah bilangan pada list dijamin tidak lebih dari 10^9 (Note : "^" menyatakan operasi perpangkatan).
Hint:
Untuk membaca input dalam satu baris dan mengubahnya menjadi array, gunakan kode berikut
a = list(map(int, input("").split()))
## Soal 5
Diberikan dua buah bilangan N dan M yang merupakan bilangan positif. Buatlah program yang menggambarkan segitiga pascal dengan total baris sebesar N dan elemen pada baris pertama merupakan M. Segitiga pascal yang digambarkan cukup dalam bentuk segitiga siku-siku. Hint : simpan array dari baris sebelumnya untuk membuat array pada baris selanjutnya.
