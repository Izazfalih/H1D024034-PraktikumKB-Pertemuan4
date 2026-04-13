import tkinter as tk
from tkinter import messagebox

knowledge_base = {
    "RAM Rusak": {
        "gejala": ["blue screen", "tidak bisa booting"],
        "solusi": "Lepas RAM lalu bersihkan pin-nya dengan penghapus karet, kemudian pasang kembali."
    },
    "Overheat": {
        "gejala": ["komputer mati sendiri", "terasa sangat panas"],
        "solusi": "Bersihkan kipas dari debu dan ganti pasta thermal pada prosesor."
    },
    "Hardisk Rusak": {
        "gejala": ["file hilang", "tidak bisa booting"],
        "solusi": "Jalankan perintah chkdsk di Command Prompt, lalu backup data penting segera."
    },
    "VGA Bermasalah": {
        "gejala": ["layar bergaris", "tidak ada tampilan"],
        "solusi": "Update driver VGA atau coba pasang ulang kartu VGA ke slot yang berbeda."
    },
    "PSU Lemah": {
        "gejala": ["komputer tidak mau menyala", "komputer mati sendiri"],
        "solusi": "Periksa semua kabel power, jika tegangan tidak stabil segera ganti PSU."
    }
}

daftar_gejala = [
    "blue screen",
    "tidak bisa booting",
    "komputer mati sendiri",
    "terasa sangat panas",
    "file hilang",
    "layar bergaris",
    "tidak ada tampilan",
    "komputer tidak mau menyala"
]

def cari_kerusakan(gejala_dipilih):
    hasil_diagnosa = []  # Menyimpan hasil yang ditemukan

    # Loop setiap kerusakan di knowledge base
    for nama_kerusakan, data in knowledge_base.items():

        gejala_kerusakan = data["gejala"]
        cocok = True

        # Cek apakah SEMUA gejala kerusakan ini ada di pilihan pengguna
        for gejala in gejala_kerusakan:
            if gejala not in gejala_dipilih:
                cocok = False
                break  # Kalau ada yang tidak cocok, langsung keluar loop

        # Kalau semua gejala cocok, tambahkan ke hasil
        if cocok:
            hasil_diagnosa.append(nama_kerusakan)

    return hasil_diagnosa

# TAMPILAN GUI (Graphical User Interface)
# Buat jendela utama
jendela = tk.Tk()
jendela.title("Sistem Pakar Kerusakan Komputer")
jendela.geometry("500x550")

# --- Judul ---
label_judul = tk.Label(
    jendela,
    text="Sistem Pakar Kerusakan Komputer",
    font=("Arial", 14, "bold")
)
label_judul.pack(pady=10)

label_instruksi = tk.Label(
    jendela,
    text="Centang gejala yang dialami komputer Anda:",
    font=("Arial", 10)
)
label_instruksi.pack()

# --- Checkboxes Gejala ---
# Dictionary untuk menyimpan status setiap checkbox (dicentang atau tidak)
status_gejala = {}

frame_gejala = tk.Frame(jendela)
frame_gejala.pack(pady=10)

for gejala in daftar_gejala:
    # Buat variabel untuk checkbox ini (True = dicentang, False = tidak)
    var = tk.BooleanVar()
    status_gejala[gejala] = var  # Simpan ke dictionary

    # Buat tampilan checkbox
    checkbox = tk.Checkbutton(
        frame_gejala,
        text=gejala,
        variable=var,
        font=("Arial", 10),
        anchor="w"
    )
    checkbox.pack(fill="x", padx=20, pady=2)


# --- Fungsi tombol Diagnosa ---
def tombol_diagnosa():
    # Kumpulkan gejala yang dicentang oleh pengguna
    gejala_dipilih = []
    for gejala, var in status_gejala.items():
        if var.get() == True:  # Kalau checkbox dicentang
            gejala_dipilih.append(gejala)

    # Cek apakah pengguna memilih minimal 1 gejala
    if len(gejala_dipilih) == 0:
        messagebox.showwarning("Peringatan", "Pilih minimal 1 gejala terlebih dahulu!")
        return

    # Jalankan mesin inferensi
    hasil = cari_kerusakan(gejala_dipilih)

    # Tampilkan hasil ke label
    if len(hasil) == 0:
        label_hasil.config(
            text="Tidak terdeteksi kerusakan.\nCoba pilih gejala yang lain.",
            fg="red"
        )
    else:
        teks_hasil = "Kerusakan terdeteksi:\n\n"
        for nama in hasil:
            solusi = knowledge_base[nama]["solusi"]
            teks_hasil += f"• {nama}\n  Solusi: {solusi}\n\n"
        label_hasil.config(text=teks_hasil, fg="green")


# --- Fungsi tombol Reset ---
def tombol_reset():
    # Kembalikan semua checkbox ke tidak dicentang
    for var in status_gejala.values():
        var.set(False)
    label_hasil.config(text="")


# --- Tombol ---
frame_tombol = tk.Frame(jendela)
frame_tombol.pack(pady=10)

tk.Button(
    frame_tombol,
    text="DIAGNOSA",
    font=("Arial", 11, "bold"),
    bg="navy", fg="white",
    width=12,
    command=tombol_diagnosa
).pack(side="left", padx=10)

tk.Button(
    frame_tombol,
    text="RESET",
    font=("Arial", 11),
    width=10,
    command=tombol_reset
).pack(side="left", padx=10)

# --- Label Hasil ---
label_hasil = tk.Label(
    jendela,
    text="",
    font=("Arial", 10),
    justify="left",
    wraplength=460
)
label_hasil.pack(padx=20, pady=10)

# --- Jalankan aplikasi ---
jendela.mainloop()