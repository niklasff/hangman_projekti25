import tkinter as tk
from hangman import HangmanGame  # Tuodaan pelilogiikka

class HangmanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman")

        self.peli = HangmanGame()  # Luodaan peliolio

        # Sana-tekstikenttä
        self.label_word = tk.Label(root, text=self.peli.hae_tilanne(), font=("Arial", 24))
        self.label_word.pack(pady=20)

        # Kirjainkenttä
        self.entry = tk.Entry(root)
        self.entry.pack()

        # Arvaa-nappi
        self.button = tk.Button(root, text="Arvaa", command=self.arvaa)
        self.button.pack()

        # Info-teksti
        self.label_info = tk.Label(root, text="Elämiä jäljellä: 6")
        self.label_info.pack(pady=10)

    def arvaa(self):
        """Käsittelee käyttäjän arvauksen"""
        kirjain = self.entry.get().lower()
        self.entry.delete(0, tk.END)  # Tyhjennetään syöttökenttä

        if len(kirjain) != 1 or not kirjain.isalpha():
            self.label_info.config(text="Syötä vain yksi kirjain!")
            return

        tulos = self.peli.arvaa_kirjain(kirjain)
        self.label_word.config(text=self.peli.hae_tilanne())  # Päivitetään sana

        if self.peli.peli_ohi():
            if self.peli.voititko():
                self.label_info.config(text="🎉 Onneksi olkoon! Voitit!")
            else:
                self.label_info.config(text=f"💀 Hävisit! Sana oli: {self.peli.sana}")
            self.button.config(state=tk.DISABLED)  # Estetään lisäarvaukset
        else:
            self.label_info.config(text=f"{tulos} | Elämiä jäljellä: {self.peli.max_virheet - self.peli.virheiden_maara}")

def kaynnista_peli():
    root = tk.Tk()
    HangmanGUI(root)
    root.mainloop()

if __name__ == "__main__":
    kaynnista_peli()
