import tkinter as tk
from tkinter import messagebox, scrolledtext

# Fungsi untuk mengenkripsi dan mendekripsi teks menggunakan Caesar Cipher
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

# Fungsi untuk mengolah teks
def process_text(encrypt=True):
    try:
        shift = int(shift_entry.get())
        text = input_text.get("1.0", tk.END).strip()
        processed_text = caesar_cipher(text, shift if encrypt else -shift)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, processed_text)
    except ValueError:
        messagebox.showerror("Input Error", "Nilai pergeseran harus berupa angka.")

# Fungsi untuk menyalin hasil ke clipboard
def copy_to_clipboard():
    output = output_text.get("1.0", tk.END).strip()
    root.clipboard_clear()
    root.clipboard_append(output)
    messagebox.showinfo("Disalin", "Hasil telah disalin ke clipboard!")

# Setup GUI
root = tk.Tk()
root.title("Caesar Cipher")
root.geometry("600x400")
root.configure(bg="#f0f0f0")

# Judul
tk.Label(root, text="Caesar Cipher", font=("Helvetica", 16), bg="#f0f0f0", fg="#333").pack(pady=10)

# Input Teks
tk.Label(root, text="Input Teks:", bg="#f0f0f0", fg="#333").pack()
input_text = scrolledtext.ScrolledText(root, height=8, width=70, wrap=tk.WORD, bg="#ffffff", fg="#000000")
input_text.pack(pady=5)

# Nilai Pergeseran
tk.Label(root, text="Nilai Pergeseran:", bg="#f0f0f0", fg="#333").pack()
shift_entry = tk.Entry(root, width=10, bg="#ffffff", fg="#000000")
shift_entry.pack(pady=5)

# Tombol
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

# Tombol untuk enkripsi dan dekripsi
tk.Button(button_frame, text="Enkripsi", command=lambda: process_text(True), bg="#4CAF50", fg="white").pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Dekripsi", command=lambda: process_text(False), bg="#F44336", fg="white").pack(side=tk.LEFT, padx=5)

# Tombol untuk menyalin hasil
tk.Button(button_frame, text="Salin", command=copy_to_clipboard, bg="#2196F3", fg="white").pack(side=tk.LEFT, padx=5)

# Output Teks
tk.Label(root, text="Output Teks:", bg="#f0f0f0", fg="#333").pack()
output_text = scrolledtext.ScrolledText(root, height=8, width=70, wrap=tk.WORD, bg="#ffffff", fg="#000000")
output_text.pack(pady=5)

# Jalankan aplikasi
root.mainloop()