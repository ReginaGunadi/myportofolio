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


### Tugas 3
<div align = "justify">

1. Berdasarkan informasi yang saya dapatkan di internet (https://shahmirprogrammer.medium.com/when-to-use-simple-form-or-model-form-in-django-python-8d6ee4aa769e), kita lebih baik menggunakan ModelForm pada Django karena memiliki beberapa manfaat bawaan, yaitu: 
- Terintegrasi dengan model yang telah dibuat: Pada model yang telah dibuat di models.py, kita dapat menentukan requirements dari input user, contoh: input harus bentuk URL, tanggal, ada panjang maksimum tertentu, dan sebagainya. ModelForm terintegrasi dengan model, sehingga kita dapat secara otomatis mengecek apakah input user memenuhi kriteria. 
- Menjaga keamanan data dari SQL Injection dan cross site scripting (XSS): SQL injection adalah peretasan web yang dilakukan dengan cara memasukkan kode SQL yang berbahaya yang dapat menghapus dan mengubah database ke dalam kolom input pengguna website. Hal ini dapat dicegah, karena Django akan menganggap perintah di luar keywords Django sebagai suatu string dan tidak mengeksekusinya. Sementara, cross site scripting adalah melakukan penyisipan kode berbahaya (biasanya kode JavaScript) ke dalam halaman web publik. Django juga mempunyai kemampuan untuk mengubah sintaks HTML yang berbahaya tersebut menjadi tampilan string biasa saja.
- Mengurangi repetisi kode: dengan membuat ModelForm, bila di masa depan form dibutuhkan di beberapa tempat yang berbeda di halaman web, kita tidak perlu menuliskan kode panjang berulang. 

Untuk meningkatkan keamanan web, kita wajib menambahkan {% csrf_token %} pada form. CSRF token adalah suatu token yang digenerate oleh Django untuk setiap sesi akses user website. Pada saat user melakukan sesi pengisian form, token ini akan menjadi tanda pengenal yang akan dicek oleh server. Bila token yang terdata di server dengan token user session sama, maka data input user akan diterima dan disimpan dalam database.

2. Berdasarkan informasi yang saya dapatkan di internet (https://medium.com/javarevisited/xml-vs-json-why-json-dominates-the-modern-web-7082f8c2edec), JSON lebih diminati karena beberapa keunggulan: 
- Keterbacaan dan kemudahan penulisan: Sintaks JSON lebih mudah untuk dibaca baik oleh orang awam maupun developer pemula, karena mengadaptasi penulisan dari bahasa-bahasa pemrograman lainnya, contoh Python, Java, dan sebagainya. Sementara penulisan XML menggunakan tag, sehingga mungkin tidak begitu mudah dipahami. 
- Beberapa program menyediakan built in support untuk JSON: Beberapa bahasa pemrograman seperti Python, Java, dan Go menyediakan built-in functions untuk melakukan parsing dan serialisasi (mengekstrak data dari JSON) sehingga pemrosesan data lebih mudah dilakukan dibandingkan dengan XML. 
- Lebih cepat diproses: Sintaks JSON minimalis dan sederhana, sehingga dapat meminimalisasi pemrosesan bila digunakan dalam website atau aplikasi yang butuh pemrosesan cepat.  Sementara adanya tag pada XML memperlambat pemrosesan tersebut. 

3. Di database, kita menyimpan data dalam bentuk objects. Pada saat user mengirimkan request untuk mengakses data, views.py akan menerima requestnya dan mengakses database. Database akan mengembalikan sekumpulan objek, contoh: experience = Experience.objects.all(). Namun web sisi user tidak bisa secara mandiri mengakses unsur tiap objek kembalian tersebut lalu menampilkannya di halaman web. Maka, kita memerlukan proses serialization terlebih dahulu. Proses ini adalah proses mengubah unsur-unsur tiap objek ke dalam bentuk text yang dapat dibaca dan ditampilkan. Setelah diserialisasi, JSON hasil akan dikirimkan melalui jaringan kepada user untuk ditampilkan pada web user. 

### Setup Mingguan: 
Minggu ini saya melakukan: 
- Merefactor codingan header dan footer menjadi base.html 
- Menambahkan form dengan fitur add, delete, edit dan delete modal (secara generic) pada Experience dan Award
- Merefactor search form pada Experience dan Award menjadi generic_search_form.html
- Menambahkan fitur sort by title ascending dan descending pada Experience dan Award
- Merapikan styling CSS beberapa fitur baru tambahan yang telah dilist di atas

### Penggunaan AI (AI Disclosure)
Untuk mengerjakan tugas minggu ini, AI saya gunakan sebagai teman diskusi: validator keputusan, teman debugging dan menjelaskan. Karena minggu ini tugas berfokus pada refactoring kode yang sudah ada, saya cukup banyak bertanya tentang apakah keputusan refactoring saya tepat atau tidak. Contoh: untuk section Experience dan Award sama-sama menggunakan fitur search, dan saya memutuskan bahwa hal tersebut harus direfactor menjadi satu html generic. Namun saya cukup bingung apakah hal tersebut dapat memunculkan error atau tidak karena kedua hal akan mengakses database yang berbeda. 
Strategi prompting yang saya gunakan adalah:
- **Mengecek kebenaran keputusan saya**: Saya memberi tahu keputusan saya tentang sesuatu dan bertanya kepada AI untuk memastikan apakah keputusan tersebut benar dan butuh dilakukan (best practice) atau tidak. 
- **Membantu debugging**: Saya mengirimkan kode yang error disertai dengan hipotesis/analisis mengapa hal tersebut error. Lalu saya meminta AI untuk mengecek apakah pemahaman saya benar atau tidak. 
- **Membantu menjelaskan**: Setelah mengirimkan kode error, AI memberikan solusi untuk mengatasinya. Saya bertanya kembali ke AI mengapa hal tersebut butuh dilakukan.

Untuk selengkapnya dapat dilihat di: https://share.gemini.google/ewFLojuAo7Z3
</div>