# Sistem Pakar Diagnosa Kerusakan Komputer

Sistem pakar berbasis Python untuk mendiagnosa kerusakan komputer/laptop berdasarkan gejala yang dipilih pengguna. Dibuat sebagai tugas praktikum mata kuliah Sistem Pakar.

---

## Deskripsi

Program ini meniru cara kerja seorang teknisi komputer dalam menganalisa kerusakan. Pengguna cukup mencentang gejala yang dialami, lalu sistem akan mencocokkannya dengan basis pengetahuan (*knowledge base*) dan menampilkan kemungkinan kerusakan beserta solusinya.

---

## Fitur

- Antarmuka GUI sederhana menggunakan **tkinter**
- **5 jenis kerusakan** yang dapat didiagnosa
- Menampilkan **nama kerusakan** dan **solusi** secara langsung
- Tombol **Reset** untuk mengulang diagnosa
- Menggunakan **Dictionary** sebagai struktur data knowledge base

---

## Knowledge Base

| No | Kerusakan | Gejala | Solusi |
|----|-----------|--------|--------|
| 1 | RAM Rusak | Blue screen, tidak bisa booting | Lepas RAM, bersihkan pin dengan penghapus karet, pasang kembali |
| 2 | Overheat | Komputer mati sendiri, terasa sangat panas | Bersihkan kipas dari debu, ganti pasta thermal prosesor |
| 3 | Hardisk Rusak | File hilang, tidak bisa booting | Jalankan `chkdsk` di Command Prompt, segera backup data |
| 4 | VGA Bermasalah | Layar bergaris, tidak ada tampilan | Update driver VGA atau pasang ulang ke slot berbeda |
| 5 | PSU Lemah | Komputer tidak mau menyala, mati sendiri | Periksa kabel power, ganti PSU jika tegangan tidak stabil |

---

## Struktur Kode

```
sistem_pakar.py
│
├── knowledge_base        → Dictionary berisi data kerusakan, gejala, solusi
├── daftar_gejala         → List semua gejala yang bisa dipilih pengguna
│
├── cari_kerusakan()      → Mesin inferensi (mencocokkan gejala dengan knowledge base)
├── tombol_diagnosa()     → Dipanggil saat tombol DIAGNOSA diklik
├── tombol_reset()        → Mengosongkan semua pilihan dan hasil
│
└── GUI (tkinter)
    ├── Judul & instruksi
    ├── Checkbox gejala
    ├── Tombol DIAGNOSA & RESET
    └── Label hasil diagnosa
```

---

## Cara Menjalankan

**Persyaratan:**
- Python 3 sudah terinstal
- Library `tkinter` (sudah bawaan Python, tidak perlu install terpisah)

**Langkah-langkah:**

```bash
# 1. Clone repositori ini
git clone https://github.com/username/sistem-pakar-komputer.git

# 2. Masuk ke folder
cd sistem-pakar-komputer

# 3. Jalankan program
python sistem_pakar.py
```

---

## 🔍 Cara Kerja Mesin Inferensi

Program menggunakan pendekatan **forward chaining** — mencocokkan fakta (gejala yang dipilih) dengan aturan di knowledge base.

```python
def cari_kerusakan(gejala_dipilih):
    hasil_diagnosa = []

    for nama_kerusakan, data in knowledge_base.items():
        cocok = True

        for gejala in data["gejala"]:
            if gejala not in gejala_dipilih:
                cocok = False
                break

        if cocok:
            hasil_diagnosa.append(nama_kerusakan)

    return hasil_diagnosa
```

> Sebuah kerusakan **terdeteksi** apabila **semua** gejala wajibnya ada dalam pilihan pengguna.

---

---

## Catatan

Program ini dibuat dengan tujuan **pembelajaran**. Knowledge base dapat dengan mudah diperluas dengan menambahkan entry baru pada dictionary `knowledge_base` tanpa perlu mengubah logika program.

```python
# Contoh menambah kerusakan baru:
"Motherboard Rusak": {
    "gejala": ["tidak ada tampilan", "komputer tidak mau menyala"],
    "solusi": "Bawa ke teknisi untuk pengecekan kapasitor dan jalur daya."
}
```
