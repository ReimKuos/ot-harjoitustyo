import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti),"saldo: 0.1")

    def test_kortille_ladattu_summa_on_oikea(self):
        self.maksukortti.lataa_rahaa(20)
        self.assertEqual(str(self.maksukortti),"saldo: 0.3")

    def test_maksu_toimii_kun_rahaa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti),"saldo: 0.05")

    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(11)
        self.assertEqual(str(self.maksukortti),"saldo: 0.1")

    def test_metodi_palauttaa_true_jos_saldo_riittaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(5),True)

    def test_metodi_palauttaa_false_jos_saldo_ei_riita(self):
        self.assertEqual(self.maksukortti.ota_rahaa(20),False)

    def test_saldo_voi_paasta_nollaan(self):
        self.maksukortti.ota_rahaa(10)
        self.assertEqual(str(self.maksukortti),"saldo: 0.0")

    