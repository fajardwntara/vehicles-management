# Vehicle Management Built in Django + Vue JS Rest API integrated. 

### Kebutuhan
1. Git
2. Docker (28.1.1 or supported version)
3. Node (v22.14.0 or supported version)
4. Python (3.9+ or supported version)

### Langkah Install
1. `git clone https://github.com/fajardwntara/vehicles-management.git` untuk clone repository
2. `sudo docker compose up --build` untuk membangun semua dependencies yang dibutuhkan.
3. `sudo docker compose exec backend python manage.py makemigrations` untuk melakukan pengecekan perubahan pada model database.
4. `sudo docker compose exec backend python manage.py migrate` untuk melakukan migrasi model database
5. `sudo docker compose exec backend python manage.py createsuperuser` untuk melakukan pembuatan superuser (Admin) untuk langkah awal dalam login
6. Pergi ke `http://localhost:5173` untuk menjalankan frontend (Vue JS) aplikasi dalam melakukan aktivitas dari sisi pengguna.
7. Pergi ke `http://localhost:8000` untuk menjalankan backend (Django REST Framework) dalam melakukan manajemen API. Berikut Link pada API Management: `https://drive.google.com/file/d/1r0V1HPcr9ERvsBAFIHu-Mexsdt-2E_aY/view?usp=sharing`

### NOTE
Apabila memiliki kendala dalam melakukan build pada docker lakukan penghapusan image dan lakukan build ulang.

`sudo docker compose down -v`

`sudo docker system prune -f`

`sudo docker compose build --no-cache`