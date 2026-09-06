Nama : Regina Gunadi
NPM : 2506542852
Kelas : PBP E

### Tugas 1
1.Iya, saya menggunakan beberapa semantik web yaitu section, article, dan figure. 
Berdasarkan informasi yang saya dapat di internet (W3School: https://www.w3schools.com/html/html5_semantic_elements.asp), semantik web digunakan untuk memberikan hierarki pada website sehingga hal ini dapat membantu SEO untuk lebih mudah mencari kata kunci saat website dipublikasikan.   

Saya memilih beberapa semantik web tersebut karena: 
- **section**: digunakan apabila kita ingin mengelompokkan konten dengan tema spesifik tertentu. Sebelumnya template terdiri dari About Me saja, dan tugas meminta untuk ditambahkan minimal satu section baru. Section baru ini (Experiences) isi kontennya tidak berkaitan dengan isi About Me. Section dapat diibaratkan sebagai sebuah kontainer yang berisi berbagai macam barang dalam kategori tertentu. Secara intuitif, pemisahan konten About Me dan Experiences harus dilakukan.
- **article**: digunakan apabila kita ingin menulis konten yang dapat independen. Berdasarkan ketentuan tugas, section baru akan memiliki minimal tiga konten di dalamnya. Setiap isi konten dalam section baru tersebut bersifat independen karena keberadaannya tidak mempengaruhi isi konten lainnya dalam section yang sama. Contoh: konten penjelasan pengalaman saya sebagai akademik DDP0 bila dihapus tidak akan mempengaruhi isi konten penjelasan lainnya. 
- **figure**: digunakan apabila kita ingin membungkus media pendukung (yang bersifat independen) untuk sebuah informasi, contoh gambar pendukung tiap experience. 

Walaupun tampilan website bisa dibuat hanya dengan menggunakan *div* atau *span*, namun penggunaan semantik web membuat hierarki struktur web lebih deskriptif sehingga struktur website dapat lebih mudah direvisi/diubah seiring berjalannya waktu. Contoh: sebuah header akan lebih jelas apabila menggunakan header dibandingkan dengan div.


2.Tantangan tata letak yang saya temukan adalah bagaimana caranya membuat informasi masih dapat dibaca dan terstruktur dengan baik walaupun tampilannya menyempit. Pada section Experience, informasinya bersifat memanjang ke samping. Pada awalnya, saya telah mengatur tata letak tampilan mobile dengan: @media (max-width: 600px) dan mengisinya dengan beberapa styling di styles.css. Namun saat dijalankan, penjelasan experiences menjadi berantakan (keluar dari kotak kontainer abu-abu). 

Saya sempat bingung, namun setelah mencari di internet (W3Schools: https://www.w3schools.com/css/css3_flexbox_container.asp), saya mencoba untuk menambahkan display flex pada container utama (abu-abu) dan flex-direction pada styling media mobile, dan akhirnya berhasil. 

Dalam menentukan elemen yang harus diubah posisi/ukurannya, saya melakukan beberapa pertimbangan: 
- **Keterbacaan teks**: Menurut saya, penjelasan experiences adalah informasi yang penting, sehingga harus tetap bisa dibaca dengan baik dalam tampilan mobile. 
- **Balance visual antara teks dan gambar pendukung**: Walaupun teks penjelasan adalah hal yang penting, saya juga tidak ingin mengorbankan ukuran gambar. 
Maka, atas dua pertimbangan ini, saya memilih untuk membuatnya vertikal turun ke bawah dengan menggunakan flex-direction: column.

3.Secara umum, batasan yang saya rasakan saat mencoba untuk menyajikan informasi pada website statis portofolio ini adalah tampilan website terasa seperti satu dimensi saja dan "tidak hidup" sehingga website terasa kurang interaktif bagi user. Maka, ada beberapa hal yang ingin saya coba terapkan di iterasi tugas selanjutnya, yaitu: 
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