import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    #kateis testit

    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_luotu_kassapaate_on_oikeanlainen(self):
        myydyt = self.kassapaate.maukkaat + self.kassapaate.edulliset
        self.assertEqual((self.kassapaate.kassassa_rahaa,myydyt),(100000,0))

    def test_rahamaara_kasvaa_oikein_ostettaessa_edullinen_kateisella(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_rahamaara_kasvaa_oikein_ostettaessa_maukas_kateisella(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_vaihtorahan_suuruus_on_oikea_ostettessa_edullinen_kateisella(self):
        takaisin = self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(takaisin,260)
    
    def test_vaihtorahan_suuruus_on_oikea_ostettessa_maukas_kateisella(self):
        takaisin = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(takaisin,100)

    def test_edullisten_maara_kasvaa_ostettaessa_kateisella(self):
        self.kassapaate.syo_maukkaasti_kateisella(600)
        self.assertEqual(self.kassapaate.maukkaat,1)

    def test_maukkaiden_maara_kasvaa_ostettaessa_kateisella(self):
        self.kassapaate.syo_maukkaasti_kateisella(600)
        self.assertEqual(self.kassapaate.maukkaat,1)

    def test_kassan_rahamaara_ei_kasva_jos_maksu_on_liian_pieni_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(10)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)

    def test_kassan_rahamaara_ei_kasva_jos_maksu_on_liian_pieni_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(10)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)

    def test_edullisten_maara_ei_kasva_jos_maksu_on_liian_pieni(self):
        self.kassapaate.syo_edullisesti_kateisella(180)
        self.assertEqual(self.kassapaate.edulliset,0)

    def test_maukkaiden_maara_ei_kasva_jos_maksu_on_liian_pieni(self):
        self.kassapaate.syo_maukkaasti_kateisella(180)
        self.assertEqual(self.kassapaate.maukkaat,0)

    #kortti testit

    def test_edullinen_maksu_kortilla_palauttaa_true(self):
        kortti = Maksukortti(1000)
        tila = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(tila,True)

    def test_maukas_maksu_kortilla_palauttaa_true(self):
        kortti = Maksukortti(1000)
        tila = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(tila,True)


    def test_kortilta_veloitetaan_rahaa_kun_saldo_riittaa_edullinen(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(str(kortti),"saldo: 7.6")

    def test_kortilta_veloitetaan_rahaa_kun_saldo_riittaa_maukas(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(str(kortti),"saldo: 6.0")


    def test_edullinen_maksu_kortilla_palauttaa_false_kun_raha_ei_riita(self):
        kortti = Maksukortti(1)
        tila = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(tila,False)

    def test_maukas_maksu_kortilla_palauttaa_false_kun_raha_ei_riita(self):
        kortti = Maksukortti(1)
        tila = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(tila,False)


    def test_kortilta_ei_veloiteta_rahaa_kun_saldo_ei_riita_edullinen(self):
        kortti = Maksukortti(1)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(str(kortti),"saldo: 0.01")

    def test_kortilta_ei_veloiteta_rahaa_kun_saldo_ei_riita_riittaa_maukas(self):
        kortti = Maksukortti(1)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(str(kortti),"saldo: 0.01")

        
    def test_myytyjen_maara_kasvaa_kun_edullinen_ostetaan(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_myytyjen_maara_kasvaa_kun_maukas_ostetaan(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)


    def test_myytyjen_maara_ei_kasva_kun_saldo_ei_riita_edulliset(self):
        kortti = Maksukortti(1)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset,0)

    def test_myytyjen_maara_ei_kasva_kun_saldo_ei_riita_maukkaat(self):
        kortti = Maksukortti(1)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat,0)


    def test_tila_kortilta_veloitettu_raha_ei_siirry_kassaan_edulliset(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_tila_kortilta_veloitettu_raha_ei_siirry_kassaan_maukkaat(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)


    def test_tila_kortilta_veloittamaton_raha_ei_siirry_kassaan_edulliset(self):
        kortti = Maksukortti(1)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_tila_kortilta_veloittamaton_raha_ei_siirry_kassaan_maukkaat(self):
        kortti = Maksukortti(1)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)


    def test_kortille_laataaminen_nostaa_kassan_rahamaaraa(self):
        kortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(kortti,500)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100500)

    def test_kortille_laataaminen_nostaa_kortin_saldoa(self):
        kortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(kortti,500)
        self.assertEqual(kortti.saldo,1500)

    def test_kortille_ei_voi_ladata_kortille_negatiivista_rahaa(self):
        kortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(kortti,-500)
        self.assertEqual(kortti.saldo,1000)

