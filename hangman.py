import random

class HangmanGame:
    def __init__(self):
        self.sanat = self.lataa_sanat_tiedostosta()
        self.sana = random.choice(self.sanat)
        self.arvatut_kirjaimet = []
        self.virheiden_maara = 0
        self.max_virheet = 6

    def lataa_sanat_tiedostosta(self): # Sanat haetaan tiedostosta sanat.txt
        try:
            with open("sanat.txt", "r", encoding="utf-8") as tiedosto:
                sanat = [rivi.strip() for rivi in tiedosto if rivi.strip()]
            if not sanat:
                raise ValueError("Sanatiedosto on tyhjä.")
            return sanat
        except FileNotFoundError:
            print("Virhe: Tiedostoa 'sanat.txt' ei löytynyt.")
            exit(1)
        except ValueError as e:
            print(f"Virhe: {e}")
            exit(1)


    def hae_tilanne(self):
        return " ".join([kirjain if kirjain in self.arvatut_kirjaimet else "_" for kirjain in self.sana]) # Palauttaa sanan, jossa arvaamattomat kirjaimet ovat '_' 

    def arvaa_kirjain(self, kirjain): # Käsittelee käyttäjän arvauksen ja palauttaa viestin
        if kirjain in self.arvatut_kirjaimet:
            return "Olet jo arvannut tämän kirjaimen."
        
        self.arvatut_kirjaimet.append(kirjain)

        if kirjain in self.sana:
            if self.hae_tilanne().replace(" ", "") == self.sana:  # Poistetaan välit vertailua varten
                return "Onneksi olkoon! Arvasit sanan oikein."
            return "Oikein!"
        else:
            self.virheiden_maara += 1
            if self.virheiden_maara >= self.max_virheet:
                return f"Hävisit! Sana oli: {self.sana}"
            return "Väärin!"

    def peli_ohi(self): # Tarkistaa, onko peli ohi
        return self.virheiden_maara >= self.max_virheet or self.hae_tilanne().replace(" ", "") == self.sana

    def voititko(self): # Tarkistaa, voitettiinko peli
        return self.hae_tilanne().replace(" ", "") == self.sana
    
# Testausskripti:
if __name__ == "__main__":
    peli = HangmanGame()
    print(f"Arvattava sana on: {peli.sana}")  # Testausta varten, pelissä tätä ei näytettäisi

    while not peli.peli_ohi():
        print("\nSana:", peli.hae_tilanne())
        kirjain = input("Arvaa kirjain: ").lower()
        
        if len(kirjain) != 1 or not kirjain.isalpha():
            print("Syötä yksi kirjain!")
            continue
        
        tulos = peli.arvaa_kirjain(kirjain)
        print(tulos)

    if peli.voititko():
        print("Voitit pelin!")
    else:
        print("Hävisit!")


