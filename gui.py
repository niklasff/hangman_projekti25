import tkinter as tk
from hangman import HangmanGame  # Tuodaan pelilogiikka

class HangmanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman")
        self.show_start_screen()

    def show_start_screen(self): #Määritellään aloitusruutu ja siihen kuuluvat otsikot ja napit
        self.clear_screen()
        
        self.label_title = tk.Label(self.root, text="Hangman", font=("Arial", 30))
        self.label_title.pack(pady=20)

        self.button_start = tk.Button(self.root, text="Aloita peli", command=self.start_game)
        self.button_start.pack(pady=5)

        self.button_instructions = tk.Button(self.root, text="Käyttöohjeet", command=self.show_instructions)
        self.button_instructions.pack(pady=5)

        self.button_suljepeli = tk.Button(self.root, text="Sulje peli", command=self.sulje_peli)
        self.button_suljepeli.pack(pady=5)

        self.button_add_word = tk.Button(self.root, text="Lisää sana sanalistaan", command=self.show_add_word_screen)
        self.button_add_word.pack(pady=5)


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
                        "Tehtävänäsi on arvata sana kirjain kerrallaan.\n"
                        "Väärä kirjain vie sinulta yhden elämän.\n"
                        "Elämiä on yhteensä kuusi.\n"
                        "Jos arvaat sanan oikein, voitat pelin.\n\n"
                        "Voit myös lisätä omia sanojasi sanalistaan.")
        
        self.label_käyttöohjeet = tk.Label(self.root, text=käyttöohjeet, font=("Arial", 14), justify="center", anchor="center")
        self.label_käyttöohjeet.pack(pady=20)
        
        self.button_back = tk.Button(self.root, text="Takaisin", command=self.show_start_screen)
        self.button_back.pack(pady=10)

    def show_add_word_screen(self):
        self.clear_screen()
        self.label_add = tk.Label(self.root, text="Lisää uusi sana sanalistaan", font=("Arial", 18))
        self.label_add.pack(pady=10)

        self.entry_new_word = tk.Entry(self.root)
        self.entry_new_word.pack(pady=5)

        self.button_submit_word = tk.Button(self.root, text="Lisää sana", command=self.lisaa_sana)
        self.button_submit_word.pack(pady=5)

        self.label_feedback = tk.Label(self.root, text="", font=("Arial", 12))
        self.label_feedback.pack(pady=10)

        self.button_back = tk.Button(self.root, text="Takaisin", command=self.show_start_screen)
        self.button_back.pack(pady=10)
    
    def lisaa_sana(self):
        uusi_sana = self.entry_new_word.get()
        peli = HangmanGame()
        if not uusi_sana.isalpha():
            self.label_feedback.config(text="Anna vain kirjaimia sisältävä sana.")
            return

        if uusi_sana.lower() in peli.sanat:
            self.label_feedback.config(text=f"Sana '{uusi_sana}' on jo sanalistassa.")
        else:
            peli.lisaa_sana_sanalistaan(uusi_sana)
            self.label_feedback.config(text=f"Sana '{uusi_sana}' lisättiin onnistuneesti!")
            self.entry_new_word.delete(0, tk.END)



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
