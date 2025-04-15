import random

class HangmanGame:
    def __init__(self):
        # Alustetaan peli: sanat ladataan tiedostosta, valitaan satunnainen sana,
        # asetetaan tyhjät listat arvatuille kirjaimille ja virheille.
        self.sanat = self.lataa_sanat_tiedostosta() # Sanat tiedostosta
        self.sana = random.choice(self.sanat) # Valitaan satunnainen sana
        self.arvatut_kirjaimet = [] # Lista arvatuista kirjaimista
        self.virheiden_maara = 0 # Virheiden määrä on aluksi nolla
        self.max_virheet = 6 # Maksimivirheet, jolloin peli päättyy

    

    def lataa_sanat_tiedostosta(self): # Sanat haetaan tiedostosta sanat.txt
        try:
            # Yritetään avata tiedosto lukutilassa:
            with open("sanat.txt", "r", encoding="utf-8") as tiedosto: 
                # Luetaan tiedoston rivit ja poistetaan tyhjät rivit:
                sanat = [rivi.strip() for rivi in tiedosto if rivi.strip()]
            if not sanat: # Tulostetaan virheilmoitus, jos sanatiedosto on tyhjä
                raise ValueError("Sanatiedosto on tyhjä.")
            return sanat
        except FileNotFoundError: # Tulostetaan virheilmoitus, jos tiedostoa ei löydy
            print("Virhe: Tiedostoa 'sanat.txt' ei löytynyt.")
            exit(1) # Lopetetaan ohjelma
        except ValueError as e: # Tulostetaan virheilmoitus muista mahdollisista virheistä
            print(f"Virhe: {e}")
            exit(1) # Lopetetaan ohjelma


    def hae_tilanne(self):
        # Palauttaa tilanne, jossa sanan arvaamattomat kirjaimet ovat '_' 
        return " ".join([kirjain if kirjain in self.arvatut_kirjaimet
                          else "_" for kirjain in self.sana]) 

    def arvaa_kirjain(self, kirjain): # Käsittelee käyttäjän arvauksen ja palauttaa viestin
        # Jos kirjain on jo arvattu, ilmoitetaan siitä:
        if kirjain in self.arvatut_kirjaimet:
            return "Olet jo arvannut tämän kirjaimen."
        
        # Arvattu kirjain lisätään arvatut_kirjaimet-listaan.
        self.arvatut_kirjaimet.append(kirjain)

        if kirjain in self.sana: # Jos kirjain on oikein
            # Poistetaan välit vertailua varten:
            if self.hae_tilanne().replace(" ", "") == self.sana: 
                return "Onneksi olkoon! Arvasit sanan oikein." # Voitto
            return "Oikein!" # Kirjainarvaus oli oikein ja peli jatkuu
        else:
            self.virheiden_maara += 1 # Jos kirjain on väärä, lisätään virheisiin yksi
            if self.virheiden_maara >= self.max_virheet: # Jos virheitä on liikaa, peli hävitään
                return f"Hävisit! Sana oli: {self.sana}" # Häviö
            return "Väärin!" # Arvaus oli väärin, peli jatkuu

    def peli_ohi(self): # Tarkistaa, onko peli ohi
        # Palauttaa True, jos virheiden määrä on maksimi tai sana ollaan arvattu
        return self.virheiden_maara >= self.max_virheet or self.hae_tilanne(    
        ).replace(" ", "") == self.sana

    def voititko(self): # Tarkistaa, voitettiinko peli
        # Tarkistetaan, onko sana arvattu, jolloin palautuu True
        return self.hae_tilanne().replace(" ", "") == self.sana
    
    # Käyttäjä voi lisätä sanoja listaan
    def lisaa_sana_sanalistaan(self, uusi_sana): 
        # Poistetaan ylimääräiset välilyönnit ja muutetaan kirjaimet pieneksi
        uusi_sana = uusi_sana.strip().lower()

        if uusi_sana in self.sanat: # Jos sana on jo listassa
            print(f"Sana '{uusi_sana}' on jo sanalistassa.")
        else:
            # Avataan tiedosto lisäystilassa ja kirjoitetaan uusi sana:
            with open("sanat.txt", "a", encoding="utf-8") as tiedosto:
                tiedosto.write(f"{uusi_sana}\n")
            # Uusi sana lisätään myös sanalistaan
            self.sanat.append(uusi_sana)
            print(f"Sana '{uusi_sana}' lisättiin sanalistaan.")
    



