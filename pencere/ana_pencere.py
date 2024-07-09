import tkinter as tk
from tkinter import ttk, messagebox
import os

class AnaPencere(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.initUI()

    def __sifirEkle(self, sayi):
        metin = str(sayi)
        metin = "0" + metin if len(metin) == 1 else metin
        return metin

    def controls(self):
        self.lbSaat = tk.Label(text="Saat:")
        self.lbSaat.grid(row=0, column=0)
        self.lbSaat.configure(font=self.Font_tuple, padx=10, pady=10)

        self.tSaat = ttk.Combobox(textvariable=tk.StringVar())
        self.tSaat["values"] = [self.__sifirEkle(i) for i in range(0, 24)]
        self.tSaat.grid(row=0, column=1)
        self.tSaat.configure(font=self.Font_tuple)

        self.lbDakika = tk.Label(text="Dakika:")
        self.lbDakika.grid(row=1, column=0)
        self.lbDakika.configure(font=self.Font_tuple, padx=10, pady=10)

        self.tDakika = ttk.Combobox(textvariable=tk.StringVar())
        self.tDakika["values"] = [self.__sifirEkle(i) for i in range(0, 60)]
        self.tDakika.grid(row=1, column=1)
        self.tDakika.configure(font=self.Font_tuple)

        self.btnAyarla = tk.Button(text="Kapat", command=self.__zamanAyarla)
        self.btnAyarla.grid(row=2, column=1, sticky='nesw')
        self.btnAyarla.configure(font=self.Font_tuple)

    def initUI(self):
        self.title("Uykucu v1.0")
        self.geometry("400x200")
        self.eval('tk::PlaceWindow . center')

        self.fontSettings()
        self.controls()

    def fontSettings(self):
        self.Font_tuple = ("Comic Sans MS", 20, "bold")

    def __zamanAyarla(self):
        komut = f"shutdown -h {self.tSaat.get()}:{self.tDakika.get()}"
        geriDonen = os.popen(komut).read()
        messagebox.showinfo("Dikkat", geriDonen + " Kapatma saati işlendi.")
