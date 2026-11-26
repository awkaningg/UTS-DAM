#### Proyek UTS - Data Acquisition & Management (DAM)

Repositori ini disusun untuk memenuhi Ujian Tengah Semester (UTS) mata kuliah **Data Acquisition & Management (DAM)**. Proyek ini mencakup proses akuisisi data dari tiga sumber berbeda (*Download CSV/Excel*, *REST API*, dan *Web Scraping*), verifikasi etika pengambilan data (robots.txt), pembersihan data (*data cleaning*), hingga penggabungan data ke dalam format tabel terstruktur. 

#### 1. Data Diri Mahasiswa

KeteranganDetail
****Nama Lengkap****
Clementin Christianingsi Mune Harum
****NIM****
2501010363
****Kelas****
F
****Program Studi****
Informatika - Manajemen Data Analisis
****Email Pribadi****
clementincmharum@gmail.com

#### 2. Sumber Data & URL

Seluruh data yang dikumpulkan berfokus pada informasi kebudayaan, berita, dan koleksi museum di Indonesia. Pengecekan kepatuhan robots.txt telah dilakukan menggunakan identitas email pribadi dan menghasilkan status **True** (diizinkan untuk diakses).

| No | Metode Akuisisi | Nama Sumber Data | URL Sumber | Format Raw | Format Process | Status Etika (robots.txt) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | **Download** | Dataset Koleksi Museum Nasional Indonesia | https://museumnasional.or.id | .xlsx | .csv (Tabel) | Resmi / Terbuka |
| **2** | **API** | WordPress REST API - Museum Nasional Indonesia | https://museumnasional.or.id | .json | .csv & .json (Tabel) | True (Diizinkan) |
| **3** | **Scraping** | Website Resmi Museum Nasional Indonesia | https://museumnasional.or.id | .html | .csv & .html (Tabel) | True (Diizinkan) |

#### 3. Checklist Etika & Tata Kelola Data

| No | Aspek | Status (Ya/Tidak/NA) | Bukti / Catatan |
| :--- | :--- | :---: | :--- |
| **1** | Sumber data dan URL dicantumkan | **Ya** | Sumber berasal dari website resmi Museum Nasional (https://museumnasional.or.id). URL dicantumkan di metadata. |
| **2** | Lisensi data diperiksa dan dicatat | **Ya** | Data bersifat publik (artikel berita website resmi pemerintah/museum). Diperuntukkan untuk tujuan akademis/studi. |
| **3** | robots.txt / Terms of Service diperiksa | **Ya** | Pengecekan robots.txt telah dilakukan menggunakan RobotFileParser. Hasil menunjukkan akses diizinkan (`boleh_diakses: True`). |
| **4** | Kolom PII diidentifikasi | **Ya** | Kolom PII (Personally Identifiable Information) dianalisis. Tidak ditemukan data personal sensitif pada artikel publik. |
| **5** | PII dihapus, di-mask, atau di-pseudonimisasi | **Ya** | Identitas penulis artikel yang berupa nama staf umum tidak diproses lebih jauh untuk menjaga privasi. |
| **6** | Prinsip minimalisasi data diterapkan | **Ya** | Hanya kolom penting yang diambil: ID, Tanggal Terbit, Judul, dan URL untuk menghindari penumpukan data tidak perlu. |
| **7** | Potensi bias sampel dianalisis | **Ya** | Bias sampel dianalisis: data terbatas pada artikel publikasi online Museum Nasional saja, tidak mewakili seluruh arsip fisik. |
| **8** | Tujuan penggunaan data dinyatakan eksplisit | **Ya** | Pengambilan data dilakukan khusus untuk keperluan analisis data dan tugas akademik (UTS DAM). |
| **9** | Rencana retensi dan penghapusan data ada | **Ya** | Data disimpan secara lokal di repositori proyek dan akan dihapus setelah evaluasi akademik selesai. |


#### 4. Tujuan (*Goal*) Proyek

1. **Multi-Source Data Acquisition:** Mengumpulkan minimal 100 baris data dari berbagai metode pengambilan data modern (*Download*, *API*, dan *Web Scraping*).
2. **Etika & Kepatuhan Data:** Memastikan proses *scraping* mematuhi aturan situs target melalui pengecekan file robots.txt dengan menyertakan identitas User-Agent dan email pribadi.
3. **Data Cleaning & Structuring:** Mengubah format data mentah tidak terstruktur (JSON dan HTML) menjadi format tabel yang bersih, bebas duplikat, dan mudah dibaca.
4. **Data Integration:** Menggabungkan seluruh dataset yang telah dibersihkan dari ketiga sumber ke dalam satu tabel terpadu (**Data Gabungan**) untuk siap digunakan pada tahap analisis selanjutnya.

#### 5. Struktur Repositori

```text
UTS-DAM/
├── Data/
│   ├── Raw/                         # Menyimpan data mentah asli dari 3 sumber
│   │   ├── data_museum_raw.csv
│   │   ├── api_museum_raw.json
│   │   └── scraping_museum_raw.html
│   └── Process/                     # Menyimpan data bersih berbentuk tabel & gabungan
│       ├── download_museum_process.csv
│       ├── api_museum_process.csv
│       ├── scraping_museum_process.html
│       └── data_gabungan_process.csv
├── Download_CSV.ipynb               # Notebook proses pembersihan data CSV/Excel
├── API.ipynb                        # Notebook akuisisi & pembersihan data REST API
├── Scrapping.ipynb                  # Notebook cek etika dan robots.txt
└── README.md                        # Dokumentasi utama proyek UTS
```
