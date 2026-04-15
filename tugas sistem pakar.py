def diagnosa_kerusakan():
    # 1. KNOWLEDGE BASE (nama kerusakan -> gejala & solusi)
 
    knowledge_base = {
        "RAM Rusak": {
            "gejala": ["blue screen (BSOD)", "komputer sering restart sendiri", "program sering not responding"],
            "solusi": "Coba bersihkan pin RAM dengan penghapus karet lalu pasang kembali. Jika masih bermasalah, ganti RAM baru."
        },
        "Overheat / Prosesor Kepanasan": {
            "gejala": ["komputer mati mendadak", "kipas berbunyi keras", "badan laptop terasa sangat panas"],
            "solusi": "Bersihkan kipas dan heatsink dari debu, ganti thermal paste, dan pastikan ventilasi laptop tidak tertutup."
        },
        "Hardisk Rusak": {
            "gejala": ["booting sangat lama", "file tiba-tiba hilang atau tidak bisa dibuka", "muncul suara klik-klik dari dalam laptop"],
            "solusi": "Jalankan CHKDSK untuk cek bad sector. Segera backup data penting dan ganti hardisk jika perlu."
        },
        "VGA / Kartu Grafis Bermasalah": {
            "gejala": ["layar berkedip-kedip", "muncul kotak-kotak aneh di layar", "tampilan layar tiba-tiba blank/hitam"],
            "solusi": "Update atau reinstall driver VGA. Jika menggunakan VGA eksternal, coba lepas dan pasang kembali."
        },
        "Baterai / Adaptor Bermasalah": {
            "gejala": ["laptop tidak mau menyala", "baterai tidak mau mengisi daya", "laptop mati saat charger dicabut"],
            "solusi": "Coba ganti charger/adaptor dengan yang baru sesuai spesifikasi. Kalibrasi atau ganti baterai jika sudah drop."
        },
        "Infeksi Virus / Malware": {
            "gejala": ["komputer tiba-tiba sangat lambat", "muncul iklan atau popup terus-menerus", "program membuka diri sendiri tanpa sebab"],
            "solusi": "Jalankan full scan antivirus (Windows Defender / Malwarebytes). Jika parah, lakukan install ulang sistem operasi."
        },
        "Sistem Operasi Corrupt": {
            "gejala": ["muncul pesan error saat booting", "komputer tidak bisa masuk ke Windows", "aplikasi bawaan Windows tidak bisa dibuka"],
            "solusi": "Gunakan fitur Startup Repair di Windows Recovery. Jika gagal, lakukan install ulang sistem operasi."
        }
    }

    # Mengambil semua gejala unik dari knowledge base
    semua_gejala = set()
    for info in knowledge_base.values():
        for g in info["gejala"]:
            semua_gejala.add(g)

    semua_gejala = sorted(list(semua_gejala))

    # Proses Tanya Jawab dengan pengguna
    print("=" * 55)
    print("   SISTEM PAKAR DIAGNOSA KERUSAKAN KOMPUTER / LAPTOP")
    print("=" * 55)
    print("Jawablah dengan 'y' untuk Ya atau 't' untuk Tidak.\n")

    gejala_pengguna = []

    for gejala in semua_gejala:
        jawab = input(f"  Apakah terjadi '{gejala}'? (y/t): ").strip().lower()
        if jawab == 'y':
            gejala_pengguna.append(gejala)

    print("\n" + "=" * 55)
    print("              HASIL ANALISIS SISTEM")
    print("=" * 55)

    # 2. MESIN INFERENSI
    hasil_diagnosa = []

    for nama_kerusakan, info in knowledge_base.items():
        gejala_kerusakan = info["gejala"]
        total_gejala     = len(gejala_kerusakan)

        # Hitung gejala yang cocok antara input pengguna & aturan
        gejala_cocok = [g for g in gejala_kerusakan if g in gejala_pengguna]
        jumlah_cocok = len(gejala_cocok)

        if jumlah_cocok > 0:
            # Certainty Factor = (gejala cocok / total gejala kerusakan) * 100
            cf = round((jumlah_cocok / total_gejala) * 100)
            hasil_diagnosa.append({
                "nama"   : nama_kerusakan,
                "cf"     : cf,
                "cocok"  : gejala_cocok,
                "solusi" : info["solusi"]
            })

    # Urutkan dari keyakinan tertinggi ke terendah
    hasil_diagnosa.sort(key=lambda x: x["cf"], reverse=True)

    # 3. OUTPUT — Tampilkan hasil diagnosa + solusi
    if not gejala_pengguna:
        print("\n  Anda tidak memasukkan gejala apapun.")
        print("  Silakan coba lagi dan jawab dengan jujur.\n")

    elif not hasil_diagnosa:
        # Gejala diinput tapi tidak cocok dengan kerusakan manapun
        print("\n  Tidak terdeteksi kerusakan berdasarkan gejala yang dimasukkan.")
        print("  Disarankan untuk membawa perangkat ke teknisi komputer.\n")

    else:
        print(f"\nGejala yang terdeteksi : {', '.join(gejala_pengguna)}\n")
        print("  Kemungkinan Kerusakan :")

        for i, hasil in enumerate(hasil_diagnosa, start=1):
            if hasil["cf"] == 100:
                label_cf = "Sangat Yakin"
            elif hasil["cf"] >= 75:
                label_cf = "Kemungkinan Besar"
            elif hasil["cf"] >= 50:
                label_cf = "Kemungkinan"
            else:
                label_cf = "Kemungkinan Kecil"

            print(f"\n  [{i}] {hasil['nama']}")
            print(f"      Keyakinan : {hasil['cf']}% ({label_cf})")
            print(f"      Gejala    : {', '.join(hasil['cocok'])}")
            print(f"      Solusi    : {hasil['solusi']}")

        # Tampilkan diagnosa utama
        utama = hasil_diagnosa[0]
        print("\n  " + "=" * 54)
        print(f"  >> DIAGNOSA UTAMA : {utama['nama']}")
        print(f"  >> KEYAKINAN      : {utama['cf']}%")
        print(f"  >> SOLUSI         : {utama['solusi']}")
        print("  " + "=" * 54)
        print("\n  *Catatan: Segera bawa ke teknisi jika masalah berlanjut.\n")

# Entry point program
if __name__ == "__main__":
    diagnosa_kerusakan()