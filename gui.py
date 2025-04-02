import tkinter as tk
from hangman import HangmanGame  # Tuodaan pelilogiikka

class HangmanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman")
        self.show_start_screen()

    def show_start_screen(self): #Määritellään aloitusruutu
        self.clear_screen()
        
        self.label_title = tk.Label(self.root, text="Hangman", font=("Arial", 30))
        self.label_title.pack(pady=20)

        self.button_start = tk.Button(self.root, text="Aloita peli", command=self.start_game)
        self.button_start.pack(pady=5)

        self.button_instructions = tk.Button(self.root, text="Käyttöohjeet", command=self.show_instructions)
        self.button_instructions.pack(pady=5)

        self.button_suljepeli = tk.Button(self.root, text="Sulje peli", command=self.sulje_peli)
        self.button_suljepeli.pack(pady=5)

    def start_game(self): #Pelin aloitus ja pelin sisällä oleva tilanne
        self.clear_screen()
        self.peli = HangmanGame()
        
        self.label_word = tk.Label(self.root, text=self.peli.hae_tilanne(), font=("Arial", 24))
        self.label_word.pack(pady=20)

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.button = tk.Button(self.root, text="Arvaa", command=self.arvaa)
        self.button.pack()

        self.label_info = tk.Label(self.root, text="Elämiä jäljellä: 6")
        self.label_info.pack(pady=10)
    
    def show_instructions(self): #Pelin käyttohjeet
        self.clear_screen()
        
        käyttöohjeet = ("Tervetuloa Hangman-peliin!\n" 
                        "1. Arvaa sana kirjain kerrallaan.\n"
                        "2. Sinulla on kuusi elämää.\n"
                        "3. Ala pelaamaan.")
        
        self.label_käyttöohjeet = tk.Label(self.root, text=käyttöohjeet, font=("Arial", 14), justify="left")
        self.label_käyttöohjeet.pack(pady=20)
        
        self.button_back = tk.Button(self.root, text="Takaisin", command=self.show_start_screen)
        self.button_back.pack(pady=10)

    def sulje_peli(self): #Sulje peli
        self.root.destroy()
    

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def arvaa(self): #Arvaa nappi
        kirjain = self.entry.get().lower()
        self.entry.delete(0, tk.END)

        if len(kirjain) != 1 or not kirjain.isalpha():
            self.label_info.config(text="Syötä vain yksi kirjain!")
            return

        tulos = self.peli.arvaa_kirjain(kirjain)
        self.label_word.config(text=self.peli.hae_tilanne())

        if self.peli.peli_ohi(): #Pelin lopputilanne
            if self.peli.voititko():
                self.label_info.config(text="🎉 Onneksi olkoon! Voitit!")
            else:
                self.label_info.config(text=f"💀 Hävisit! Sana oli: {self.peli.sana}")
            self.button.config(state=tk.DISABLED)
        else:
            self.label_info.config(text=f"{tulos} | Elämiä jäljellä: {self.peli.max_virheet - self.peli.virheiden_maara}")

if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanGUI(root)
    root.mainloop()
