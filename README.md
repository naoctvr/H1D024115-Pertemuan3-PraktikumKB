#H1D024115 – Pertemuan 3 Praktikum KB

Dokumen ini berisi pengumpulan tugas praktikum Kecerdasan Buatan pada pertemuan ke-3.

Implementasi Logika Fuzzy dengan Library scikit-fuzzy

Program yang dibuat menerapkan Fuzzy Inference System (FIS) menggunakan metode Mamdani untuk dua studi kasus yang berbeda.

1. Studi Kasus 1 – Penentuan Stok Makanan (main.py)

Program ini bertujuan untuk menentukan jumlah stok makanan yang optimal berdasarkan empat variabel input menggunakan logika fuzzy.

a. Variabel Input (Antecedent)
Barang Terjual [0–100] → kategori: Rendah, Sedang, Tinggi
Permintaan [0–300] → kategori: Rendah, Sedang, Tinggi
Harga per Item [0–100.000] → kategori: Murah, Sedang, Mahal
Profit [0–4.000.000] → kategori: Rendah, Sedang, Banyak
b. Variabel Output (Consequent)
Stok Makanan [0–1000] → kategori: Sedang, Banyak
c. Aturan Fuzzy (Rules)

Terdapat 6 aturan IF-THEN yang digunakan untuk menentukan output berdasarkan kombinasi input.

d. Data Input yang Digunakan
Barang Terjual = 80
Permintaan = 255
Harga per Item = Rp 25.000
Profit = Rp 3.500.000
e. Membership Function
Sebagian besar menggunakan fungsi segitiga (trimf)
Untuk kategori Profit “Banyak” menggunakan fungsi trapesium (trapmf)
2. Studi Kasus 2 – Kepuasan Pelayanan Masyarakat (studi2.py)

Program ini digunakan untuk menghitung tingkat kepuasan masyarakat terhadap pelayanan berdasarkan empat variabel input.

a. Variabel Input (Antecedent)
Kejelasan Informasi [0–100] → Tidak, Cukup, Memuaskan
Kejelasan Persyaratan [0–100] → Tidak, Cukup, Memuaskan
Kemampuan Petugas [0–100] → Tidak, Cukup, Memuaskan
Ketersediaan Sarpas [0–100] → Tidak, Cukup, Memuaskan
b. Variabel Output (Consequent)
Kepuasan Pelayanan [0–400] → Tidak, Kurang, Cukup, Memuaskan, Sangat
c. Aturan Fuzzy (Rules)

Terdapat 81 aturan IF-THEN, yang merupakan kombinasi dari:
4 variabel input × 3 kategori → 3⁴ = 81 aturan

d. Data Input yang Digunakan
Kejelasan Informasi = 80
Kejelasan Persyaratan = 60
Kemampuan Petugas = 50
Ketersediaan Sarpas = 90
e. Membership Function
Trapmf digunakan untuk kategori “Tidak” dan “Memuaskan”
Trimf digunakan untuk kategori “Cukup”
Output seluruhnya menggunakan trapmf
3. Library yang Digunakan
a. numpy

Digunakan untuk membuat array numerik sebagai dasar semesta pembicaraan pada variabel fuzzy.

b. matplotlib

Berfungsi untuk menampilkan grafik membership function serta hasil defuzzifikasi.

c. scikit-fuzzy (skfuzzy)

Merupakan library utama untuk membangun sistem fuzzy, meliputi:

Definisi variabel input dan output
Pembuatan membership function (trimf, trapmf)
Penyusunan aturan fuzzy
Pembuatan sistem kontrol dan simulasi
Proses perhitungan output (defuzzifikasi)
4. Cara Menjalankan Program

Install terlebih dahulu library yang dibutuhkan:

pip install numpy matplotlib scikit-fuzzy

Jalankan program:

# Studi Kasus 1
python main.py

# Studi Kasus 2
python studi2.py
