import random

class HangmanGame:
    def __init__(self):
        self.sanat = ["python", "ohjelmointi", "tietokone", "kehitys", "projekti"]
        self.sana = random.choice(self.sanat)
        self.arvatut_kirjaimet = []
        self.virheiden_maara = 0
        self.max_virheet = 6

    def hae_tilanne(self):
        """Palauttaa sanan, jossa arvaamattomat kirjaimet ovat '_' """
        return " ".join([kirjain if kirjain in self.arvatut_kirjaimet else "_" for kirjain in self.sana])

    def arvaa_kirjain(self, kirjain):
        """Käsittelee käyttäjän arvauksen ja palauttaa viestin"""
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

    def peli_ohi(self):
        """Tarkistaa, onko peli ohi"""
        return self.virheiden_maara >= self.max_virheet or self.hae_tilanne().replace(" ", "") == self.sana

    def voititko(self):
        """Tarkistaa, voititko pelin"""
        return self.hae_tilanne().replace(" ", "") == self.sana
    
    nisse on vammanen
