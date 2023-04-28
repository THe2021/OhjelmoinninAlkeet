import math
import cmath
import piiristo as piir
import ikkunasto as ik

valinta = {
    "r": "r",
    "c": "c",
    "l": "l"
}

tila = {
    "syote_1": None,
    "syote_2": None,
    "laatikko_1": None,
    "laatikko_2": None,
    "piiri": None,
    "komponentti": None,
    "komponentit": [],
    "komponentit_2": [],
    "arvo": 0,
    "jannite": 0,
    "taajuus": 0,
    "impedanssi": 0
}

def aloita():
    lause = "Aseta piirin jännite ja taajuus syöttämällä\ntiedot ylempään tekstikenttään ja paina kyseisen\ntiedon tallentavaa nappia. Toimi samoin\nkomponentin valinnan ja komponentin arvon kanssa.\n-Vastuksen resistanssi (R)\n-Kondensaattorin kapasitanssi (C)\n-Kelan induktanssi (I)"  

    ik.kirjoita_tekstilaatikkoon(tila["laatikko_1"], lause, tyhjaa=True)


def aseta_jannite():
    jannite = ik.lue_kentan_sisalto(tila["syote_1"])
    
    
    try:
        if float(jannite):
            tila["jannite"] = float(jannite)
    
            lause = ("Jännite (U) {} V".format(jannite))
            ik.kirjoita_tekstilaatikkoon(tila["laatikko_2"], lause, tyhjaa=False)
            ik.tyhjaa_kentan_sisalto(tila["syote_1"])
    
    except ValueError:
        otsikko = "Virhe"
        viesti = "Syöte ei ollut liukuluku"
    
        ik.avaa_viesti_ikkuna(otsikko, viesti, virhe=True)
        ik.tyhjaa_kentan_sisalto(tila["syote_1"])

def aseta_taajuus():
    taajuus = ik.lue_kentan_sisalto(tila["syote_1"])
    
    try:
        if float(taajuus):
            tila["taajuus"] = float(taajuus)
    
            lause = ("Taajuus (f) {} Hz".format(taajuus))
            ik.kirjoita_tekstilaatikkoon(tila["laatikko_2"], lause, tyhjaa=False)
            ik.tyhjaa_kentan_sisalto(tila["syote_1"])
    except ValueError:
        otsikko = "Virhe"
        viesti = "Syöte ei ollut liukuluku"
    
        ik.avaa_viesti_ikkuna(otsikko, viesti, virhe=True)
        ik.tyhjaa_kentan_sisalto(tila["syote_1"])

def aseta_komponentti():
    komponentti = ik.lue_kentan_sisalto(tila["syote_1"]).lower()
    try:
        if valinta[komponentti]:    
            tila["komponentti"] = komponentti
            lause = ("Valittu: {}".format(komponentti))
            ik.kirjoita_tekstilaatikkoon(tila["laatikko_2"], lause, tyhjaa=False)
            ik.tyhjaa_kentan_sisalto(tila["syote_1"])
        
    except KeyError:
        otsikko = "Virhe"
        viesti = "Syöte ei ollut R, C tai L"
    
        ik.avaa_viesti_ikkuna(otsikko, viesti, virhe=True)
        ik.tyhjaa_kentan_sisalto(tila["syote_1"])
        

def lisaa_arvo():
    arvo = ik.lue_kentan_sisalto(tila["syote_1"])
    komponentti = tila["komponentti"]
    
    try:
        if float(arvo):
            luku = float(arvo)
            tila["arvo"] = luku
            tila["komponentit"].append((komponentti, luku))           
          
            ik.tyhjaa_kentan_sisalto(tila["syote_1"])
            ik.tyhjaa_kentan_sisalto(tila["syote_2"])
            laske_osoitinmuoto()
            ik.kirjoita_tekstilaatikkoon(tila["laatikko_1"], "Syötä tarvittaessa lisää komponentteja!", tyhjaa=True)
            ik.kirjoita_tekstilaatikkoon(tila["laatikko_1"], "Syötä rinnankytkettävien komponenttien\narvot alempaan tekstikenttään!", tyhjaa=False)
            ik.kirjoita_tekstilaatikkoon(tila["laatikko_1"], "Paina Piirrä rinnankytkentä-nappia vasta kun\nkaikki rinnankytkettävät komponentit on syötetty.", tyhjaa=False)
            piir.piirra_jannitelahde(tila["piiri"], tila["jannite"], tila["taajuus"], v_asetteluvali=2)
            piir.piirra_haara(tila["piiri"], tila["komponentit"], h_asetteluvali=6, v_asetteluvali=2, viimeinen=True)
            piir.piirra_piiri(tila["piiri"])
    
    except ValueError:
        otsikko = "Virhe"
        viesti = "Syöte ei ollut liukuluku"
    
        ik.avaa_viesti_ikkuna(otsikko, viesti, virhe=True)
        ik.tyhjaa_kentan_sisalto(tila["syote_1"])
        ik.tyhjaa_kentan_sisalto(tila["syote_2"])

def rinnan_kytkenta():
    arvo = ik.lue_kentan_sisalto(tila["syote_2"])
    komponentti = tila["komponentti"] 
    
    try:
        if float(arvo):
            luku = float(arvo)
            tila["arvo"] = luku
            tila["komponentit_2"].append((komponentti, luku))
            ik.tyhjaa_kentan_sisalto(tila["syote_2"])
            lause_1 = ("Valittu: {}, {}".format(komponentti, luku))
            lause_2 = ("Arvo: {}".format(luku))
            ik.kirjoita_tekstilaatikkoon(tila["laatikko_1"], lause_1, tyhjaa=True)
            ik.kirjoita_tekstilaatikkoon(tila["laatikko_2"], lause_2, tyhjaa=False)
                    
    except ValueError:
        otsikko = "Virhe"
        viesti = "Syöte ei ollut liukuluku"
    
        ik.avaa_viesti_ikkuna(otsikko, viesti, virhe=True)
        ik.tyhjaa_kentan_sisalto(tila["syote_2"])

def lisaa_rinnankytkenta():
    tila["komponentit"].append(tila["komponentit_2"])
    
    piir.piirra_jannitelahde(tila["piiri"], tila["jannite"], tila["taajuus"], v_asetteluvali=2)
    piir.piirra_haara(tila["piiri"], tila["komponentit"], h_asetteluvali=6, v_asetteluvali=2, viimeinen=True)
    piir.piirra_piiri(tila["piiri"])


def laske_virta():
    impedanssi = tila["impedanssi"]
    jannite = tila["jannite"]
    
    I = jannite / impedanssi
    
    return I
        
def laske_jannite():
    pass
    
    
      
def laske_osoitinmuoto():
    arvo = tila["arvo"]
    taajuus = tila["taajuus"]
    
    if  tila["komponentti"] == "r":
        impedanssi = arvo
        tila["impedanssi"] = impedanssi
        ximp, bimp = cmath.polar(impedanssi)
        yimp = math.degrees(bimp)
        xvir, bvir = cmath.polar(laske_virta())
        yvir = math.degrees(bvir)
        lause_1 = ("Vastuksen {}Ω impedanssi(Z):\n{} < {:.2f}°".format(arvo, ximp, yimp)) 
        lause_2 = ("Vastuksen {}Ω virta(I):\n{} < {:.2f}°".format(arvo, xvir, yvir))  
        ik.kirjoita_tekstilaatikkoon(tila["laatikko_2"], lause_1, tyhjaa=False)
        ik.kirjoita_tekstilaatikkoon(tila["laatikko_2"], lause_2, tyhjaa=False)
   
    elif tila["komponentti"] == "l":
        impedanssi = 2 * math.pi * taajuus * arvo * 1j
        tila["impedanssi"] = impedanssi
        ximp, bimp = cmath.polar(impedanssi)
        yimp = math.degrees(bimp)
        xvir, bvir = cmath.polar(laske_virta())
        yvir = math.degrees(bvir)
        lause_1 = ("Kelan {}H impedanssi(Z):\n{} < {:.2f}°".format(arvo, ximp, yimp)) 
        lause_2 = ("Kelan {}H virta(I):\n{} < {:.2f}°".format(arvo, xvir, yvir))         
        ik.kirjoita_tekstilaatikkoon(tila["laatikko_2"], lause_1, tyhjaa=False)   
        ik.kirjoita_tekstilaatikkoon(tila["laatikko_2"], lause_2, tyhjaa=False)
       
    elif tila["komponentti"] == "c":
        impedanssi = 1 / (2 * math.pi * taajuus * arvo * 1j)
        tila["impedanssi"] = impedanssi
        ximp, bimp = cmath.polar(impedanssi)
        yimp = math.degrees(bimp)
        xvir, bvir = cmath.polar(laske_virta())
        yvir = math.degrees(bvir)
        lause_1 = ("Kondensaattorin {}F impedanssi (Z):\n{} < {:.2f}°".format(arvo, ximp, yimp))
        lause_2 = ("Kondensaattorin {}F virta (I):\n{} < {:.2f}°".format(arvo, xvir, yvir))
        ik.kirjoita_tekstilaatikkoon(tila["laatikko_2"], lause_1, tyhjaa=False)
        ik.kirjoita_tekstilaatikkoon(tila["laatikko_2"], lause_2, tyhjaa=False)

def main():

    testi_ikkuna = ik.luo_ikkuna("Hemuli")
    luku_kehys = ik.luo_kehys(testi_ikkuna, ik.VASEN)
    
    teksti_kehys = ik.luo_kehys(testi_ikkuna, ik.OIKEA)
   
    ik.luo_nappi(luku_kehys, "Aloitusohjeet (paina)", aloita)
    teksti_kentta_1 = ik.luo_tekstikentta(luku_kehys)
    ik.luo_kehys(luku_kehys) 
    ik.luo_nappi(luku_kehys, "Tallenna jännite", aseta_jannite)
    ik.luo_nappi(luku_kehys, "Tallenna taajuus", aseta_taajuus)
    ik.luo_nappi(luku_kehys, "Valitse komponentti: R, C tai L", aseta_komponentti)
    ik.luo_nappi(luku_kehys, "Lisää komponentin arvo", lisaa_arvo) 
    teksti_kentta_2 = ik.luo_tekstikentta(luku_kehys)    
    ik.luo_nappi(luku_kehys, "Lisää komponentin arvo rinnankytkentänä", rinnan_kytkenta)
    ik.luo_nappi(luku_kehys, "Piirrä rinnankytkentä", lisaa_rinnankytkenta)
    ik.luo_nappi(luku_kehys, "Lopeta", ik.lopeta)
    
    piiri_ikkuna = piir.luo_piiri(teksti_kehys)      
    
    teksti_laatikko_1 = ik.luo_tekstilaatikko(luku_kehys, leveys=50, korkeus=10)
    teksti_laatikko_2 = ik.luo_tekstilaatikko(luku_kehys, leveys=50, korkeus=10) 
   
    tila["syote_1"] = teksti_kentta_1 
    tila["syote_2"] = teksti_kentta_2
    tila["laatikko_1"] = teksti_laatikko_1
    tila["laatikko_2"] = teksti_laatikko_2
    tila["piiri"] = piiri_ikkuna
      
    ik.kaynnista()

if __name__ == "__main__":

    main()
    
    
    