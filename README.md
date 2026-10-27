# Python Exhaustive Search

Program Python yang mencari rute terpendek dengan metode exhaustive search. Seluruh kemungkinan urutan kunjungan dicoba satu per satu, lalu rute dengan total jarak terkecil dipilih. Program ini merupakan tugas mata kuliah Strategi Algoritma.

Kasus yang diselesaikan adalah perjalanan keliling dari titik awal Q yang mengunjungi lima titik lain (R, S, T, U, P) tepat satu kali, lalu kembali ke Q. Setiap pasangan titik memiliki bobot jarak yang sudah ditentukan di dalam kode.

## Fitur

- Matriks jarak antar titik dicetak ke terminal.
- Semua permutasi rute dihitung dan ditampilkan beserta total jaraknya.
- Rute tercepat dan total jaraknya ditampilkan sebagai hasil akhir.
- Visualisasi graf sebelum dan sesudah pencarian. Pada tampilan sesudah, rute terbaik disorot dengan garis biru tebal.

## Teknologi

- Python 3
- NetworkX untuk membangun graf dan membaca bobot sisi
- Matplotlib untuk visualisasi graf
- Itertools dari pustaka standar untuk membangkitkan permutasi

## Cara Instalasi

Prasyarat: Python 3 sudah terpasang.

Pasang dependensi yang dibutuhkan:

```bash
pip install networkx matplotlib
```

## Cara Menjalankan

Jalankan berkas utama dari folder repositori:

```bash
python exhaustive.py
```

Program akan mencetak matriks jarak, daftar semua rute beserta total jaraknya, dan rute tercepat. Dua jendela grafik Matplotlib akan muncul sesudahnya. Jendela pertama menampilkan semua koneksi antar titik, jendela kedua menampilkan rute terbaik.

Catatan: jumlah permutasi tumbuh sangat cepat mengikuti jumlah titik, jadi metode ini hanya praktis untuk jumlah titik yang kecil.

## Lisensi

Proyek ini memakai lisensi MIT. Lihat berkas [LICENSE](LICENSE) untuk teks lengkapnya.
