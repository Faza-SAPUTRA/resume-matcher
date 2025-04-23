# Resume Matcher ✨

**Resume Matcher** adalah aplikasi pintar untuk mencocokkan resume dengan deskripsi pekerjaan secara cepat dan akurat. Dibuat dengan Flask dan Bootstrap 5, aplikasi ini membantu rekruter atau siapa saja yang ingin menemukan kandidat terbaik dengan mudah! 🚀

## 🎯 Apa Itu Resume Matcher?

Resume Matcher mempermudah proses seleksi kandidat dengan fitur berikut:

- **Unggah Resume Mudah**: Klik atau drag-and-drop file resume (format .pdf, .doc, .docx).
- **Analisis Kecocokan**: Menggunakan algoritma TF-IDF dan Cosine Similarity untuk membandingkan resume dengan deskripsi pekerjaan.
- **Hasil Jelas**: Skor kecocokan ditampilkan dalam persentase dengan label seperti "Sangat Cocok", "Cukup Cocok", atau "Tidak Cocok".
- **Desain Responsif**: Tampilan modern dan intuitif menggunakan Bootstrap 5.

**Lihat Cara Kerjanya**\
Berikut demo singkat penggunaan aplikasi:\
![Demo Resume Matcher]([https://via.placeholder.com/600x300?text=Demo+Resume+Matcher](https://imgur.com/a/pfsffDJ))  
*(Catatan: Ganti URL di atas dengan GIF asli, misalnya pakai ScreenToGif atau LICEcap, untuk menunjukkan proses unggah file dan hasil pencocokan.)*

## 📂 Struktur Proyek

Karena repository ini tidak mendukung folder, semua file ada di root direktori. Namun, untuk menjalankan proyek Flask, kamu perlu atur ulang ke struktur berikut:

```
project/
├── main.py
├── requirements.txt
├── README.md
├── static/
│   ├── styles.css
│   ├── scripts.js
├── templates/
│   ├── index.html
│   ├── matcher.html
├── Uploads/
```

**Penjelasan File**:

- `main.py`: File utama aplikasi Flask untuk backend dan pemrosesan resume.
- `requirements.txt`: Daftar dependensi Python untuk proyek ini.
- `index.html`: Halaman beranda (landing page) aplikasi.
- `matcher.html`: Halaman untuk unggah resume dan deskripsi pekerjaan.
- `styles.css`: File CSS tambahan untuk styling.
- `scripts.js`: File JavaScript untuk unggah file dan drag-and-drop.
- `Uploads/`: Folder untuk menyimpan file resume yang diunggah (dibuat otomatis).

## 🛠️ Prasyarat

Sebelum mulai, pastikan kamu punya:

- Python 3.6 atau lebih tinggi 🐍
- `pip` untuk install package Python
- Git (opsional, kalau kamu clone repo)

## ⚙️ Cara Install

Ikuti langkah berikut untuk setup proyek di lokal:

1. **Clone Repository** (opsional):

   ```bash
   git clone <URL_REPOSITORY_KAMU>
   cd <NAMA_FOLDER_REPOSITORY>
   ```

2. **Atur Struktur Folder**\
   Karena file di repository ada di root, kamu perlu buat folder dan pindah file:

   - Buat folder `static` dan `templates`.
   - Pindahkan:
     - `styles.css` dan `scripts.js` ke `static/` (namakan ulang `script.js` menjadi `scripts.js`).
     - `index.html` dan `matcher.html` ke `templates/`.
   Struktur akhir harus sesuai seperti di atas.

3. **Install Dependensi**\
   Gunakan `requirements.txt` untuk install semua package:

   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan Aplikasi**\
   Setelah semua siap, jalankan aplikasi:

   ```bash
   python main.py
   ```

   Kalau berhasil, kamu akan lihat pesan:

   ```
   * Running on http://127.0.0.1:5000
   ```

## 🚀 Cara Menggunakan

Berikut langkah-langkah pakai Resume Matcher:

1. **Buka Aplikasi**\
   Buka browser dan kunjungi `http://127.0.0.1:5000/`. Kamu akan lihat halaman beranda dengan tombol "Mulai Resume Matcher".

2. **Ke Halaman Matcher**\
   Klik tombol **"Mulai Resume Matcher"**, kamu akan masuk ke `http://127.0.0.1:5000/matcher`.

3. **Masukkan Deskripsi Pekerjaan**\
   Di bagian "Deskripsi Pekerjaan", masukkan deskripsi pekerjaan yang ingin dicocokkan dengan resume.

4. **Unggah Resume**\
   Di bagian "Unggah Resume":

   - Klik area bertulisan "Seret & letakkan file resume di sini atau klik untuk cari file" untuk pilih file, atau langsung drag-and-drop.
   - File yang didukung: `.pdf`, `.doc`, `.docx`.
   - File yang diunggah akan muncul di daftar di bawah area unggah, dengan tombol `×` untuk hapus jika salah pilih.

5. **Proses Pencocokan**\
   Klik tombol **"Proses Pencocokan Resume"**. Aplikasi akan memproses dan menampilkan hasil seperti ini:

   ```
   Resume dengan kecocokan tertinggi:
   - resume1.pdf: 46% (Cukup Cocok)
   - resume2.docx: 32% (Cukup Cocok)
   ```

**Catatan**: Kamu perlu unggah minimal 5 resume untuk melihat hasil. Kalau kurang, aplikasi akan menampilkan pesan error.

## 💡 Fitur Tambahan

**Klik untuk Lihat Fitur yang Bisa Ditambahkan**

- **Loading Spinner**: Tambah animasi loading saat proses pencocokan.
- **Validasi Client-Side**: Cek jumlah file minimal sebelum submit.
- **Dukungan Format Lain**: Tambah dukungan untuk file .txt.
- **Hasil Visual**: Tampilkan grafik untuk skor kecocokan.

## 🐞 Troubleshooting

**Klik untuk Lihat Solusi Masalah Umum**

- **Aplikasi Tidak Berjalan?**\
  Cek log di terminal. Pastikan folder `Uploads/` bisa ditulis. Kalau error permission, buat folder manual: `mkdir Uploads`.

- **File Tidak Bisa Diunggah?**\
  Pastikan format file `.pdf`, `.doc`, atau `.docx`. Buka F12 di browser, cek tab Console untuk error JavaScript.

- **Hasil Tidak Muncul?**\
  Cek Network tab (F12) untuk lihat POST request ke `/matcher`. Kalau gagal, periksa log Flask di terminal.

## 🛠️ Teknologi yang Digunakan

- **Backend**: Flask (Python) 🐍
- **Frontend**: Bootstrap 5, HTML, CSS, JavaScript 🌐
- **Pemrosesan File**: PyPDF2 (PDF), docx2txt (DOC/DOCX) 📜
- **Analisis Data**: scikit-learn (TF-IDF, Cosine Similarity) 📊
- **Pengelola File**: Werkzeug (secure filename) 🔒

## 🤝 Kontribusi

Pengen bantu kembangkan proyek ini? Yuk, ikutan! Caranya:

1. Fork repo ini.
2. Buat branch baru (`git checkout -b fitur-baru`).
3. Commit perubahan (`git commit -m "Tambah fitur X"`).
4. Push ke branch (`git push origin fitur-baru`).
5. Buat Pull Request.

Ide kontribusi:

- Tambah validasi file di client.
- Bikin loading animation.
- Dukungan format file baru.

## 📜 Lisensi

Proyek ini dilisensikan di bawah MIT License. Bebas digunakan dan dimodifikasi! 🙏

## 📬 Kontak

Punya pertanyaan atau butuh bantuan? Hubungi saya di:\
📧 email@example.com\
🐙 Atau buka issue di repo ini.

---

**Resume Matcher** - Seleksi kandidat jadi lebih mudah dan cerdas! 🌟\
Made with ❤️ by Resume Matcher Team
