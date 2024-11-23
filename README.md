# Mini E-commerce - Kelompok 2  

Proyek ini adalah sistem mini e-commerce yang dibangun menggunakan arsitektur **microservices**. Sistem terdiri dari tiga layanan utama: **User-Service**, **Product-Service**, dan **Order-Service**, yang saling berkomunikasi melalui API RESTful.

---

## Arsitektur Sistem  

### 1. User-Service  
**Deskripsi**:  
Layanan untuk mengelola data pengguna, termasuk registrasi, login, dan pengelolaan profil.  

**Teknologi yang Digunakan**:  
- **Framework**: Node.js dengan Express  
- **Database**: MongoDB  

**Fitur Utama**:  
- Registrasi pengguna baru.  
- Login dan autentikasi dengan JWT atau OAuth.  
- Pengelolaan profil pengguna (edit data, ganti password).  

**Komunikasi Antar Layanan**:  
- Menyediakan data pengguna ke Order-Service untuk validasi saat memproses pesanan.  

---

### 2. Product-Service  
**Deskripsi**:  
Layanan untuk mengelola data produk, seperti menambah, mengedit, dan menghapus produk.  

**Teknologi yang Digunakan**:  
- **Framework**: Laravel 10  
- **Database**: MySQL  

**Fitur Utama**:  
- CRUD produk (buat, baca, perbarui, hapus).  
- Menyediakan data produk berdasarkan filter atau pencarian.  
- Otomatis memperbarui stok berdasarkan pesanan di Order-Service.  

**Komunikasi Antar Layanan**:  
- Menyediakan data produk ke Order-Service untuk validasi pesanan, termasuk harga dan stok.  

---

### 3. Order-Service  
**Deskripsi**:  
Layanan untuk memproses pesanan dari pengguna, mulai dari pembuatan hingga pelacakan status pesanan.  

**Teknologi yang Digunakan**:  
- **Framework**: FastAPI  
- **Database**: MySQL  

**Fitur Utama**:  
- Membuat pesanan baru berdasarkan data dari User-Service dan Product-Service.  
- Melacak status pesanan (dalam proses, dikirim, selesai).  
- Integrasi dengan gateway pembayaran (opsional).  

**Komunikasi Antar Layanan**:  
- Mengambil data pengguna dari User-Service untuk memverifikasi identitas.  
- Mengambil data produk dari Product-Service untuk memvalidasi stok dan harga sebelum memproses pesanan.  
- Memberikan notifikasi status pesanan kepada User-Service.  

---

## Keuntungan Arsitektur Microservices  
1. **Independensi Layanan**:  
   Setiap layanan dapat dikembangkan, diperbarui, dan di-deploy secara terpisah.  

2. **Skalabilitas**:  
   Layanan dapat diskalakan sesuai kebutuhan, misalnya Product-Service untuk menangani banyak permintaan data produk.  

3. **Kemandirian Teknologi**:  
   Setiap layanan menggunakan teknologi yang paling sesuai, seperti Node.js, Laravel, dan FastAPI.  

4. **Reliabilitas**:  
   Kegagalan pada satu layanan tidak secara langsung memengaruhi layanan lain.  

---

## Cara Menjalankan Layanan  

### User-Service  
1. **Persiapan**:  
   - Pastikan Node.js dan MongoDB telah terinstal.  
2. **Menjalankan**:  
   ```bash
   cd user-service
   npm install
   npm start

### LINK VIDEO
Link Video Demonstrasi : https://drive.google.com/file/d/1t9BCCivdXahjB-3vMEqssRf4YjPIzQbh/view?usp=drivesdk
