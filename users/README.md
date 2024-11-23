# User Service dengan Docker

Proyek ini adalah sebuah layanan mikro (microservice) untuk manajemen pengguna yang dibangun menggunakan Node.js dan Express, serta dibungkus dengan Docker. Layanan ini menyediakan operasi CRUD (Create, Read, Update, Delete) untuk pengguna serta autentikasi dan otorisasi menggunakan JWT.

## Fitur

- **CRUD Pengguna**: Membuat, membaca, memperbarui, dan menghapus profil pengguna.
- **Autentikasi**: Login dan registrasi pengguna dengan JWT.
- **Otorisasi**: Rute yang dilindungi hanya dapat diakses oleh pengguna yang terautentikasi.
- **Penanganan Error**: Middleware untuk menangani error secara terpusat.
- **Dockerized**: Mudah dideploy menggunakan Docker dan Docker Compose.

## Endpoint API

### Rute Autentikasi

- **POST** `/auth/register` - Mendaftarkan pengguna baru.
- **POST** `/auth/login` - Mengautentikasi pengguna dan mendapatkan token JWT.
- **GET** `/auth/protected-route` - Contoh rute yang dilindungi.

### Rute Pengguna

- **POST** `/users` - Membuat profil pengguna baru.
- **GET** `/users` - Mendapatkan semua pengguna (dilindungi).
- **GET** `/users/{id}` - Mendapatkan pengguna berdasarkan ID (dilindungi).
- **PUT** `/users/{id}` - Memperbarui informasi pengguna berdasarkan ID (dilindungi).
- **DELETE** `/users/{id}` - Menghapus pengguna berdasarkan ID (dilindungi).
- **GET** `/users/protected-route` - Contoh rute yang dilindungi.

## Persyaratan Sistem

- **Docker**
- **Docker Compose**
- **Node.js & npm** (jika ingin menjalankan layanan secara lokal tanpa Docker)

## Instalasi

1. **Clone Repositori**

   ```bash
   git clone https://github.com/your-username/e-commerce-microservices.git
   cd e-commerce-microservices/user-service

2. **Jalankan Dengan DOCKER Compose**
- docker-compose up --build -d