from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestAngolOraNevsor(TestCase):
    def test_feladat01(self):
        keresett="Halass Mónika"
        aktualis = feladatok.nevsorban_hanyadik(keresett)
        elvart = 1
        self.assertEqual(elvart, aktualis, keresett+" személy esetén rosszul határoza meg, hogy a névsorban hanyadik.")
    def test_feladat02(self):
        keresett="Márton Kinga"
        aktualis = feladatok.nevsorban_hanyadik(keresett)
        elvart = 3
        self.assertEqual(elvart, aktualis, keresett+" személy esetén rosszul határoza meg, hogy a névsorban hanyadik.")
    def test_feladat03(self):
        keresett="Nagy András"
        aktualis = feladatok.nevsorban_hanyadik(keresett)
        elvart = 4
        self.assertEqual(elvart, aktualis, keresett+" személy esetén rosszul határoza meg, hogy a névsorban hanyadik.")
    def test_feladat04(self):
        keresett="Zsóka Tibor"
        aktualis = feladatok.nevsorban_hanyadik(keresett)
        elvart = 7
        self.assertEqual(elvart, aktualis, keresett+" személy esetén rosszul határoza meg, hogy a névsorban hanyadik.")
    def test_feladat04(self):
        keresett="Ismeretlen"
        aktualis = feladatok.nevsorban_hanyadik(keresett)
        elvart = -1
        self.assertEqual(elvart, aktualis, keresett+" személy esetén rosszul határoza meg, hogy a névsorban hanyadik.")