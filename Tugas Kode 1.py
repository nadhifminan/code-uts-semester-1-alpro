Nama:Nadhif Fajrul Minan <br>
NIM:220411100060

# 1 Konsep
### 1.1 Materi
  Tulis ringkasan (1 sampai dengan 4 paragraf, jika memungkinkan berikan contoh dalam Python) tentang :
  * 1.Tipe Data
  * 2.Algoritma (Definisi, Jenis-jenis algoritma, bagaimana menulis algoritma)

### jawab:
<br>di dalam bahasa pemrograman ada beberapa bentuk data yaitu:1.data numerik: adalah data yang berupa angka yang terdiri dari bilangan bulat dan bilangan pecahan.
Tipe angka bilangan bulat disebut integer contoh 1,3,4,53,6,43, dll
dan sedangkan angka yang berupa bilangan pecahan yang disebut tipe data Float contoh 1.5, 2.5, 2.3 ,7.1 ,dll<br>
    <br>Selanjutnya yang ke-2. Yaitu data yang berupa text/huruf maupun angka yang penulisannya diapit oleh tanda petik baik satu ('_') maupun petik dua("_")  itu disebut tipe data String contohnya adalah:'angsa', "Indonesia", 'angka', "5", '6' ,'17' ,dll.,selain 3 data itu kita juga mengenal data boolean yaitu data yang menyatakan nilai benar atau salah (true/false).<br>
    <br>algoritma merupakan sebuah urutan langkah-langkah yang diciptakan guna menyelesaikan suatu problem yang diimplementasikan sebagai sebuah instruksi/syntax ke dalam bahasa pemrograman secara berurutan.<br>
    <br>jenis-jenis algoritma sendiri dibagi menjadi 3 yaitu:
*Sequence: adalah sebuah algoritma yang dikerjakan secara lurus dari awal sampai akhir.
sebelum saya menyebutkan jenis-jenis algoritma lainnya perlu kita ketahui bahwa sebuah algoritma tidak selalu dalam keadaan lurus(Sequence)tetapi juga ada percabangan dan di sinilah kita kenal dengan yang namanya ekspressi boolean yang bernilai true atau false,ada juga relational operator,dan juga logical operator.
*Branches (selection) yaitu suatu kondisi algoritma yang memungkinkan untuk memilih mengerjakan bagian x atau y maupun yang lainnya antara kondisi true dan false
*Iteration (looping) yaitu suatu kondisi algoritma yang dimungkinkan menginstruksikan perintah secara berulang sampai jumlah tertentu. di sini kita mengenal syntax yang namanya for dan while untuk perulangan ini.
    <br>langakah-langkah menulis algoritma:<br>
1.Definisikan masalah yang akan diuraikan
2.merumuskan masalah/problem
3.menginisialisasikan variabel yang sesuai dengan value
4.membuat code perumusan masalah
5.membuat inputaan data
6.mencetak hasil

### 1.2 Algoritma-1
Tuliskan algoritma (tiap tahap, diberikan nomor tahapan) untuk menyelesaikan Persamaan Matematika : <br>
 $y=\sum_{(i=1)}^n(i^2+2i)$ ,dimana n adalah inputan dari user

### Jawab:
1.masukkan nilai dari n <br>
2.buat inisialisai temporal=0 dan i =1 <br>
3.masukkan rumus y=$y=\sum_{(i=1)}^n(i^2+2i)$<br>
4.inisialisaikan lagi temporal=temporal+y<br>
5.tampilkan hasil yang tersimpan dalam variabel temporal yang terakhir

###  1.3 Algoritma-2
Tuliskan algoritma (tiap tahap, diberikan nomor tahapan) untuk permasalahan berikut ini :
1.	Terdapat (Diketahui) dua buah titik, yaitu (x1,y1) dan (x2,y2)
2.	Jika terdapat titik baru yang hanya diketahui nilai koordinat x nya, misal (x3,...), maka cari nilai y3
3.	Petunjuk : Gunakan Persamaan Garis seperti yang ditunjukkan pada Gambar 1, dan![image.png](attachment:image.png)
![image-2.png](attachment:image-2.png)
Gambar 1: Persamaan Garis y = mx + c

#### Jawab:
1.inisialisasikan nilai dari (x1 dan y1),(x2 dan y2) <br>
2.masukkan dalam rumus   untuk mengetahui nilai dari M <br>
3.masukkan nilai ke dalam rumus persamaan garis y3=x3-x1)<br>
4.tampilkan hasil dari y3

### 1.4	Algoritma-3
Tulis tahapan-tahapan (algoritma) untuk menampilkan sejumlah n bilangan ganjil, dimana n adalah inputan dari user, dan jumlahkan semua bilangan ganjil tersebut.

### Jawab:
1.buat variabel inputan untuk n dan juga inisialisasi variabel lainya<br>
2.gunakan iteration(while/for)<br>
3.moduluskan bilangan dengan 2 dan equal kan nilai dengan 1<br>
4.kemudian inisialisasikan kembali temp dengan temp+a,agar menjadi penamabahan dari hasil akhir iterasi<br>
5.kemudian tampilkan hasil dari bilangan ke-n dan hasilnya<br>
6.berikan batas/stoping condition dari iterasinya while<br>
7.tampilkan hasil dari bilangan ganjil iterasi ke-n<br>

### 1.5 Algoritma-4
Tulis algoritma untuk menampilkan sejumlah bilangan dan total jumlah dari bilangan-bilangan tersebut, berdasarkan persamaan deret aritmatika.
$$Un=a+(n-1)b$$
$$Sn=\frac{n}{2}(2^a + (n-1)b)$$
dimana
Un : suku ke-n (n input dari user) 
a : suku awal(input dari user) 
b : beda(input dari user), and
Sn : Total jumlah seluruh suku, mulai dari suku pertama sampai suku ke-n

### Jawab:
1.cara pertama buat inputan/angka yang harus dimasukkan user untuk menyatakan suku ke berapa? ,suku pertama?,interval/bedanya? .<br>

2.keumdian kita gunakan iteration samapai suku ke -n.(for/while)<br>

3.kemudian kita ganti nilai n=i+1,dimana di setiap iterasinya yang berubah ditambahkan 1<br>

4.Tentukan rumus dan pola bilanganya yaitu kita memakai Un =a+(n-1)*b dan jumlah semua suku-Sn=n/2*(2*a+(n-1)*b).<br>

5.kemudian print/lakukan perintah cetak dari  Un dan Sn

# 2  Implementasi
### 2.1 Program Bilangan Ganjil
Konversi algoritma yang sudah ditulis sebelumnya dengan menggunakan bahasa Pemrograman Python. Contoh hasil eksekusi dapat dilihat di Gambar.2a or Gambar.2b :

### 2.2 Program Deret Aritmatika
Konversi algoritma yang sudah ditulis sebelumnya dengan menggunakan bahasa Pemrograman Python, seperti yang ditunjukkan pada Gambar 3a or Gambar3b.
![image.png](attachment:image.png)
        (a)n=5
        (b)n=10
Gambar Bilangan Ganjil dan jumlahnya
![image-2.png](attachment:image-2.png)
(a) n = 3,a = 4,b = 6  . (b) n = 5,a = 6,b = 7
Gambar 3: Arithmetic Series
### Jawab:
"""

n=int(input('masukkan jumlah bilangan='))
a=0
c=1
jumlah=0
while c<=n:
    if a%2 ==1:
        jumlah=jumlah+a
        print('bilangan ke-',c,':',a)
        c+=1
    a+=1
print('Total=',jumlah)

n=int(input('masukkan nilai n ='))
a=int(input('masukkan nilai a ='))
b=int(input('masukkan nilai b ='))
for i in range(n):
    n=i+1
    Un=a+(n-1)*b
    sn=n/2*(2*a+(n-1)*b)
    print('U-',i+1,'=',Un)
print('sn=',sn)
