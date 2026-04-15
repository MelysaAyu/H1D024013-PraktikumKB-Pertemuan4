H1D024013-PraktikumKB-Pertemuan4
DESKRIPSI PROGRAM
Program ini adalah Sistem Pakar berbasis Python yang mampu mendiagnosa kerusakan pada komputer atau laptop berdasarkan gejala-gejala yang dimasukkan oleh pengguna. Program menggunakan metode Certainty Factor (CF) untuk mengukur tingkat keyakinan dari setiap kemungkinan kerusakan, lalu menampilkan hasil diagnosa beserta solusi penanganannya.

KRITERIA TUGAS
1. Knowledge Base (Minimal 5 Kerusakan)
   Di sinilah semua pengetahuan tentang kerusakan komputer disimpan. Pada program ini terdapat 7 kerusakan yaitu RAM rusak, Overheat, Hardisk rusak, VGA, Baterai, Malware,   Sistem operasi corrupt. Program menggunakan struktur data Dictionary Python (bukan if else panjang) agar mudah dikembangkan.
2. Mesin Inferensi (Inference Engine)
   Bagian yang bertugas mencocokkan gejala dari pengguna dengan aturan di Knowledge Base, lalu menghitung tingkat keyakinan.
   - Mengumpulkan Semua Gejala Unik
Program mengambil semua gejala unik dari seluruh kerusakan yang ada di Knowledge Base, lalu mengurutkannya agar ditampilkan secara konsisten ke pengguna.
   - Tanya Jawab dengan 
Program menanyakan satu per satu setiap gejala. Jika pengguna menjawab y, gejala tersebut ditambahkan ke dalam list gejala_pengguna
   - Perhitungan Certainty Factor (CF)
RUMUS => CF = (Jumlah Gejala Cocok / Total Gejala Kerusakan) × 100%
CONTOH => CF = (2 / 3) × 100 = 67% → label "Kemungkinan" artinya kerusakan RAM punya 3 gejala dan jika pengguna cocok 2 gejala
  - Penanganan Kondisi Tidak Cocok
Program menangani dua kondisi edge case agar tidak error

3. Output Program
   Hasil diagnosa ditampilkan dengan jelas dan terurut dari keyakinan tertinggi ke terendah.
   CONTOH :
==========================================================
   SISTEM PAKAR DIAGNOSA KERUSAKAN KOMPUTER / LAPTOP
==========================================================
Jawablah dengan 'y' untuk Ya atau 't' untuk Tidak.
  Apakah terjadi 'blue screen (BSOD)'? (y/t): y
  Apakah terjadi 'booting sangat lama'? (y/t): y
  Apakah terjadi 'komputer mati mendadak'? (y/t): t
  ...
==========================================================
              HASIL ANALISIS SISTEM
==========================================================
  Gejala yang terdeteksi : blue screen (BSOD), booting sangat lama
  Kemungkinan Kerusakan :
  [1] RAM Rusak
      Keyakinan : 33% (Kemungkinan Kecil)
      Gejala    : blue screen (BSOD)
      Solusi    : Coba bersihkan pin RAM dengan penghapus karet...

  [2] Hardisk Rusak
      Keyakinan : 33% (Kemungkinan Kecil)
      Gejala    : booting sangat lama
      Solusi    : Jalankan CHKDSK untuk cek bad sector...
  
  ======================================================
  >> DIAGNOSA UTAMA : RAM Rusak
  >> KEYAKINAN      : 33%
  >> SOLUSI         : Coba bersihkan pin RAM dengan penghapus karet...
  ======================================================
  *Catatan: Segera bawa ke teknisi jika masalah berlanjut.
