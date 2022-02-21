from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestSzotar(TestCase):
    def test_feladat01(self):
        keresett="alma"
        aktualis = feladatok.szotar(keresett)
        elvart = "apple"
        self.assertEqual(elvart, aktualis, keresett+" szót nem jól fordította le!")
    def test_feladat02(self):
        keresett="dió"
        aktualis = feladatok.szotar(keresett)
        elvart = "walnut"
        self.assertEqual(elvart, aktualis, keresett+" szót nem jól fordította le!")
    def test_feladat03(self):
        keresett="narancs"
        aktualis = feladatok.szotar(keresett)
        elvart = "orange"
        self.assertEqual(elvart, aktualis, keresett+" szót nem jól fordította le!")
    def test_feladat04(self):
        keresett="ismeretlen"
        aktualis = feladatok.szotar(keresett)
        elvart = "A szót nem ismerem!"
        self.assertEqual(elvart, aktualis, keresett+" szót nem jól fordította le!")