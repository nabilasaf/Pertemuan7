import tkinter as tk  # Mengimpor modul tkinter untuk membuat GUI
from tkinter import messagebox  # Mengimpor messagebox untuk menampilkan pesan kesalahan

# Fungsi untuk memvalidasi input dan menampilkan hasil prediksi
def hasil_prediksi():
    try: 
        # Loop untuk memeriksa setiap entry (input nilai)
        for entry in entries:
            nilai = int(entry.get())  # Mengambil nilai dari entry dan mengonversinya menjadi integer
            # Memeriksa apakah nilai berada dalam rentang yang valid (0-100)
            if not (0 <= nilai <= 100):
                raise ValueError("Nilai harus antara 0 dan 100.")  # Mengangkat kesalahan jika nilai tidak valid
        # Jika semua nilai valid, tampilkan hasil prediksi
        hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")
    except ValueError as ve:
        # Menampilkan pesan kesalahan jika ada input yang tidak valid
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100.")

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")  # Menetapkan judul jendela
root.geometry("400x600")  # Menetapkan ukuran jendela
root.configure(bg="#D4F6FF")  # Mengatur latar belakang jendela

# Label Judul
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 18, "bold"), bg="#CBDCEB")
judul_label.pack(pady=20)  # Menambahkan label judul ke jendela dengan padding vertikal

# Frame untuk input nilai mata pelajaran
frame_input = tk.Frame(root, bg="#CBDCEB")  # Membuat frame untuk menampung input
frame_input.pack(pady=10)  # Menambahkan frame ke jendela dengan padding vertikal

entries = []  # Daftar untuk menyimpan referensi ke entry input
for i in range(10):
    # Membuat label untuk setiap mata pelajaran
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i + 1}:", font=("Arial", 12), bg="#CBDCEB")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")  # Menempatkan label dalam grid
    # Membuat entry untuk input nilai
    entry = tk.Entry(frame_input, width=10, font=("Arial", 12))
    entry.grid(row=i, column=1, padx=10, pady=5)  # Menempatkan entry dalam grid
    entries.append(entry)  # Menambahkan entry ke daftar entries

# Tombol untuk hasil prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, font=("Arial", 12, "bold"), bg="#4CAF50", fg="black")
prediksi_button.pack(pady=30)  # Menambahkan tombol ke jendela dengan padding vertikal

# Label untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="", font=("Arial", 14, "italic", "bold"), fg="blue", bg="#f0f0f0")
hasil_label.pack(pady=20)  # Menambahkan label hasil ke jendela dengan padding vertikal

# Menjalankan aplikasi
root.mainloop()  # Memulai loop utama aplikasi