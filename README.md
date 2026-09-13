Nama : Regina Gunadi

NPM : 2506542852

Kelas : PBP E

### Tugas 1
<div align="justify">

1. Iya, saya menggunakan beberapa semantik web yaitu section, article, dan figure. 
Berdasarkan informasi yang saya dapat di internet (W3School: https://www.w3schools.com/html/html5_semantic_elements.asp), semantik web digunakan untuk memberikan hierarki pada website sehingga hal ini dapat membantu SEO untuk lebih mudah mencari kata kunci saat website dipublikasikan. Saya memilih beberapa semantik web tersebut karena: 
- **section**: digunakan apabila kita ingin mengelompokkan konten dengan tema spesifik tertentu. Sebelumnya template terdiri dari About Me saja, dan tugas meminta untuk ditambahkan minimal satu section baru. Section baru ini (Experiences) isi kontennya tidak berkaitan dengan isi About Me. Section dapat diibaratkan sebagai sebuah kontainer yang berisi berbagai macam barang dalam kategori tertentu. Secara intuitif, pemisahan konten About Me dan Experiences harus dilakukan.
- **article**: digunakan apabila kita ingin menulis konten yang dapat independen. Berdasarkan ketentuan tugas, section baru akan memiliki minimal tiga konten di dalamnya. Setiap isi konten dalam section baru tersebut bersifat independen karena keberadaannya tidak mempengaruhi isi konten lainnya dalam section yang sama. Contoh: konten penjelasan pengalaman saya sebagai akademik DDP0 bila dihapus tidak akan mempengaruhi isi konten penjelasan lainnya. 
- **figure**: digunakan apabila kita ingin membungkus media pendukung (yang bersifat independen) untuk sebuah informasi, contoh gambar pendukung tiap experience. 
Walaupun tampilan website bisa dibuat hanya dengan menggunakan *div* atau *span*, namun penggunaan semantik web membuat hierarki struktur web lebih deskriptif sehingga struktur website dapat lebih mudah direvisi/diubah seiring berjalannya waktu. Contoh: sebuah header akan lebih jelas apabila menggunakan header dibandingkan dengan div.


2. Tantangan tata letak yang saya temukan adalah bagaimana caranya membuat informasi masih dapat dibaca dan terstruktur dengan baik walaupun tampilannya menyempit. Pada section Experience, informasinya bersifat memanjang ke samping. Pada awalnya, saya telah mengatur tata letak tampilan mobile dengan: @media (max-width: 600px) dan mengisinya dengan beberapa styling di styles.css. Namun saat dijalankan, penjelasan experiences menjadi berantakan (keluar dari kotak kontainer abu-abu). Saya sempat bingung, namun setelah mencari di internet (W3Schools: https://www.w3schools.com/css/css3_flexbox_container.asp), saya mencoba untuk menambahkan display flex pada container utama (abu-abu) dan flex-direction pada styling media mobile, dan akhirnya berhasil. 
Dalam menentukan elemen yang harus diubah posisi/ukurannya, saya melakukan beberapa pertimbangan: 
- **Keterbacaan teks**: Menurut saya, penjelasan experiences adalah informasi yang penting, sehingga harus tetap bisa dibaca dengan baik dalam tampilan mobile. 
- **Balance visual antara teks dan gambar pendukung**: Walaupun teks penjelasan adalah hal yang penting, saya juga tidak ingin mengorbankan ukuran gambar. 
Maka, atas dua pertimbangan ini, saya memilih untuk membuatnya vertikal turun ke bawah dengan menggunakan flex-direction: column.


3. Secara umum, batasan yang saya rasakan saat mencoba untuk menyajikan informasi pada website statis portofolio ini adalah tampilan website terasa seperti satu dimensi saja dan "tidak hidup" sehingga website terasa kurang interaktif bagi user. Maka, ada beberapa hal yang ingin saya coba terapkan di iterasi tugas selanjutnya, yaitu: 
- *Scroll animation*: membuat setiap section muncul (fade in) secara perlahan saat user menurunkan halaman ke bawah.
- *Typing effect*: membuat tulisan seperti dityping pada bagian section About Me.  
- *Toggle dark/light mode*: warna website saya sekarang cenderung dark mode, namun mungkin ada beberapa user yang lebih nyaman untuk membaca informasi dalam kondisi light mode. 


### Setup Mingguan: 
Minggu ini saya melakukan: 
- Melakukan penyesuaian styling CSS template Tutorial 1
- Menambahkan section baru: Experiences dan styling CSSnya


### Penggunaan AI (AI Disclosure)
Strategi saya untuk mengerjakan tugas ini adalah menggunakan Google untuk mencari hal-hal yang bersifat umum, dan menggunakan AI untuk pertanyaan yang khusus, contoh: Google -> apa perbedaan penggunaan *article* dan *aside* pada web? AI: apakah penggunaan *article* pada bagian ini *blok kode* tepat?
Saya menggunakan AI (Gemini) untuk membantu saya memahami kode template terutama bagian CSS, mengecek pemahaman dan/atau keputusan saya terkait suatu hal tertentu (apakah hal tersebut best practices/tidak), dan melakukan debugging ringan. 
Strategi prompting yang saya gunakan adalah: 
- **Membantu/mengecek pemahaman**: mengirimkan blok kode yang kurang saya pahami, lalu dilanjutkan dengan pertanyaan terkait mengapa hal tersebut butuh ada/dilakukan. Contoh: pertanyaan terkait mengapa style * dan root tidak menjadi satu saja. 
- **Mengecek keputusan**: mengirimkan blok kode keputusan saya, lalu dilanjutkan dengan pertanyaan apakah keputusan saya tersebut benar atau butuh penyesuaian. Contoh: pertanyaan terkait keputusan saya untuk menggunakan article untuk section experiences.
- **Melakukan debugging ringan**: mengirimkan apa yang sudah saya lakukan, lalu dilanjutkan dengan pertanyaan kenapa tidak dapat sesuai dengan apa yang saya inginkan. Contoh: pertanyaan terkait penggunaan display: flex namun gambarnya malah jadi kecil sekali --> harus ditentukan ukuran pakem fotonya.
Untuk selengkapnya, dapat dilihat pada log chat berikut: https://share.gemini.google/rhbE58CHtlO0
</div>


### Tugas 2
<div align = "justify">

1. Alur ketika pengguna membuka portofolio baru adalah sebagai berikut:  
Pengguna yang ingin melihat suatu halaman web akan mengirim request dan request ini akan diarahkan ke urls.py di projek Django kita. Di file urls.py dalam projek terdapat kode: 'path("", include("main.urls"))' yang akan mengakses file urls.py yang ada di aplikasi kita. Di file urls.py aplikasi, terdapat kode 'path("experience/", show_experience, name="show_experience")' di mana kita mendeklarasikan tambahan alamat pada halaman website terkait (contoh: "https://regina-gunadi-myportofolio.pws.cs.ui.ac.id/experience/"), lalu memanggil suatu fungsi (contoh: show_experience) yang ada di views.py. Pada views.py, fungsi kita akan memanggil model yang telah didefinisikan dalam models.py. Models.py akan mengakses database untuk mencari data yang diperlukan, lalu bila ada datanya, maka ia akan mengembalikannya melalui views.py dalam bentuk context untuk ditampilkan pada template websitenya.

2. Data untuk bagian portofolio baru sebaiknya disimpan pada model bukan ditulis manual di template agar kodingan pada template tidak redundan dan menjadi sangat panjang seiring bertambahnya data/informasi yang ingin ditampilkan.
Bila kita ingin memelihara dan mengembangkan aplikasi lebih lanjut, praktik seperti ini meningkatkan keterbacaan dari kodingan yang kita buat di tengah penambahan data/informasi.  

3. Perbedaan fungsi makemigrations dan migrate adalah: 
    *    **Makemigrations**: dilakukan bila kita ingin melakukan migrasi model. Hal ini dilakukan bila kita ingin mendaftarkan model baru atau melakukan perubahan terhadap model, contoh: mengganti atau menghapus atribut. Django akan membandingkan model saat ini dengan file migrasi yang telah dibuat, bila ada perbedaan maka akan dibuat migrasi. Instruksi ini belum mengubah basis data kita, file migrasi hanya menyiapkan instruksi apa yang perlu dilakukan selanjutnya. 
    *    **Migrate**: dilakukan setelah kita melakukan makemigrations. Karena instruksi ini membaca file migrasi tersebut dan membandingkan model yang ada di dalamnya dengan basis data yang sudah ada. Bila terdapat perbedaan, maka hal tersebut akan diterapkan dalam basis data kita.
*Contoh kasus:* di awal, kita telah mendaftarkan model Experience dengan fields: nama, deskripsi, lokasi dan mengisi datanya ke dalam basis data dengan menggunakan makemigrations dan migrate. Lalu di tengah pengerjaan website, kita menyadari bahwa field lokasi tidak diperlukan dan ingin dihapus, maka kita melakukan perubahan lalu melakukan makemigrations dan migrate lagi. 

### Setup Mingguan: 
Minggu ini saya melakukan: 
- Melakukan penyesuaian styling pada experience.html
- Membuat model baru: Award, dan mengintegrasikannya dengan urls.py, views.py
- Menambahkan template baru: award.html dan styling CSSnya juga 

### Penggunaan AI (AI Disclosure)
Strategi saya untuk mengerjakan tugas minggu ini adalah sama seperti minggu sebelumnya. Namun, ada sedikit tambahan, dimana saya menggunakan AI untuk mendebug tampilan website yang tidak sesuai keinginan saya. Contoh: gambar tidak dapat dilihat saat urlnya telah dimasukkan ke Django model, pada saat filtering dijalankan ternyata moduleError, dan sebagainya. Mungkin kebanyakan pertanyaan saya terkait dengan error. 
Strategi prompting yang saya gunakan adalah:
- **Menunjukkan/menceritakan apa yang telah saya lakukan** : saya menunjukkan bagaimana saya melakukan sesuatu dengan panduan mencari di Google atau Youtube namun menghasilkan error. Lalu saya tanyakan mengapa hal tersebut error dan bagaimana cara memperbaikinya.
- **Meminta untuk tidak diberikan solusi kodenya dahulu** : saya ingin mencoba sendiri terlebih dahulu mengerjakan suatu hal tersebut. Bila terjadi error, barulah saya bertanya di mana letak kesalahannya. 

Untuk selengkapnya dapat dilihat di: https://share.gemini.google/KVRQw4bDiGq6
</div>