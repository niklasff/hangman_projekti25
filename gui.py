import tkinter as tk
from hangman import HangmanGame  # Tuodaan pelilogiikka

class HangmanGUI:
    def __init__(self, root):
        # Alustetaan graafinen käyttöliittymä:
        self.root = root
        self.root.title("Hangman") # Otsikko
        self.show_start_screen() # Näytetään aloitusruutu

    # Määritellään aloitusruutu ja siihen kuuluvat otsikot ja napit:
    def show_start_screen(self): 
        self.clear_screen() # Tyhjennetään mahdollinen edellinen ruutu
        
        # Pelin nimi otsikkona
        self.label_title = tk.Label(self.root, text="Hangman", font=("Arial", 30))
        self.label_title.pack(pady=20)

        # Aloita peli -nappi
        self.button_start = tk.Button(self.root, text="Aloita peli", command=self.start_game)
        self.button_start.pack(pady=5)

        # Käyttöohjeet -nappi
        self.button_instructions = tk.Button(self.root, text="Käyttöohjeet", command=self.show_instructions)
        self.button_instructions.pack(pady=5)

        # Sulje peli -nappi
        self.button_suljepeli = tk.Button(self.root, text="Sulje peli", command=self.sulje_peli)
        self.button_suljepeli.pack(pady=5)

        # Lisää sana sanalistaan -nappi
        self.button_add_word = tk.Button(self.root, text="Lisää sana sanalistaan", command=self.show_add_word_screen)
        self.button_add_word.pack(pady=5)

    # Aloitetaan peli ja näytetään pelitilanne:
    def start_game(self): 
        self.peli = HangmanGame() # Luodaan uusi HangmanGame-olio, joka hallinnoi peliä
        
        # Näytetään sanan arvaustilanne
        self.label_word = tk.Label(self.root, text=self.peli.hae_tilanne(), font=("Arial", 24))
        self.label_word.pack(pady=20)

        # Käyttäjä syöttää arvauksen tähän
        self.entry = tk.Entry(self.root)
        self.entry.pack()

        # Arvausnappi
        self.button = tk.Button(self.root, text="Arvaa", command=self.arvaa)
        self.button.pack()

        # Näytetään käyttäjän elämät
        self.label_info = tk.Label(self.root, text="Elämiä jäljellä: 6")
        self.label_info.pack(pady=10)
    
    def show_instructions(self): #Pelin käyttohjeet
        self.clear_screen() # Tyhjennetään peliruudun sisältö
        
        # Käyttöohjeiden teksti
        käyttöohjeet = ("Tervetuloa Hangman-peliin!\n" 
                        "Tehtävänäsi on arvata sana kirjain kerrallaan.\n"
                        "Väärä kirjain vie sinulta yhden elämän.\n"
                        "Elämiä on yhteensä kuusi.\n"
                        "Jos arvaat sanan oikein, voitat pelin.\n\n"
                        "Voit myös lisätä omia sanojasi sanalistaan.")
        # Teksti ja sen muotoilu  
        self.label_käyttöohjeet = tk.Label(self.root, text=käyttöohjeet, font=("Arial", 14
                    ), justify="center", anchor="center")
        self.label_käyttöohjeet.pack(pady=20)
        
        # Takaisin -nappi
        self.button_back = tk.Button(self.root, text="Takaisin", command=self.show_start_screen)
        self.button_back.pack(pady=10)

    # Sanan lisäämisruutu
    def show_add_word_screen(self):
        self.clear_screen()
        self.label_add = tk.Label(self.root, text="Lisää uusi sana sanalistaan", font=("Arial", 18))
        self.label_add.pack(pady=10)

        # Kenttä uuden sanan lisäämiseen
        self.entry_new_word = tk.Entry(self.root)
        self.entry_new_word.pack(pady=5)

        # Lisää sana -nappi
        self.button_submit_word = tk.Button(self.root, text="Lisää sana", command=self.lisaa_sana)
        self.button_submit_word.pack(pady=5)

        self.label_feedback = tk.Label(self.root, text="", font=("Arial", 12))
        self.label_feedback.pack(pady=10)

        # Takaisin -nappi
        self.button_back = tk.Button(self.root, text="Takaisin", command=self.show_start_screen)
        self.button_back.pack(pady=10)
    
    # Lisää sana-toiminto
    def lisaa_sana(self):
        uusi_sana = self.entry_new_word.get()
        peli = HangmanGame()
        if not uusi_sana.isalpha(): # Sana pelkkiä kirjaimia
            self.label_feedback.config(text="Anna vain kirjaimia sisältävä sana.")
            return

        if uusi_sana.lower() in peli.sanat: # Jos sana on jo listassa
            self.label_feedback.config(text=f"Sana '{uusi_sana}' on jo sanalistassa.")
        else:
            peli.lisaa_sana_sanalistaan(uusi_sana) # Lisätään sana sanalistaan
            self.label_feedback.config(text=f"Sana '{uusi_sana}' lisättiin onnistuneesti!")
            self.entry_new_word.delete(0, tk.END) # Tekstikenttä tyhjennetään



    def sulje_peli(self): #Sulje peli
        # Sulkee pelin ja ikkunan
        self.root.destroy()
    

    def clear_screen(self):
        # Tyhjentää näytön
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def arvaa(self):
        # Käsittelee käyttäjän arvauksen
        kirjain = self.entry.get().lower()
        self.entry.delete(0, tk.END) # Tyhjennetään syöttökenttä

        # Käyttäjä saa syöttää vain yhden kirjaimen
        if len(kirjain) != 1 or not kirjain.isalpha(): 
            self.label_info.config(text="Syötä vain yksi kirjain!")
            return

        tulos = self.peli.arvaa_kirjain(kirjain) # Arvauksen käsittely
        # Päivitetään tilanne ruudulle:
        self.label_word.config(text=self.peli.hae_tilanne())

        if self.peli.peli_ohi(): #Pelin lopputilanne (voitto vai häviö)
            if self.peli.voititko():
                self.label_info.config(text="🎉 Onneksi olkoon! Voitit!")
            else:
                self.label_info.config(text=f"💀 Hävisit! Sana oli: {self.peli.sana}")
            self.button.config(state=tk.DISABLED) #  Ei saa tehdä uusia arvauksia
        else:
            # Päivitetään elämiä jäljellä -tilanne
            self.label_info.config(text=f"{tulos} | Elämiä jäljellä: {self.peli.max_virheet - self.peli.virheiden_maara}")
# Käynnistetään peli
if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanGUI(root)
    root.mainloop()
