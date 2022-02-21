from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestEUTag(TestCase):
    def test_feladat01(self):
        keresett="Észtország"
        aktualis = feladatok.eu_tag_e(keresett)
        elvart = True
        self.assertEqual(elvart, aktualis, keresett+" EU tagságát rosszul határozta meg")
    def test_feladat02(self):
        keresett="Magyarország"
        aktualis = feladatok.eu_tag_e(keresett)
        elvart = True
        self.assertEqual(elvart, aktualis, keresett+" EU tagságát rosszul határozta meg")
    def test_feladat03(self):
        keresett="Szlovákia"
        aktualis = feladatok.eu_tag_e(keresett)
        elvart = True
        self.assertEqual(elvart, aktualis, keresett+" EU tagságát rosszul határozta meg")
    def test_feladat04(self):
        keresett="USA"
        aktualis = feladatok.eu_tag_e(keresett)
        elvart = False
        self.assertEqual(elvart, aktualis, keresett+" EU tagságát rosszul határozta meg")