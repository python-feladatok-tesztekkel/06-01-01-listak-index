from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestKodolas(TestCase):
    def test_feladat01(self):
        keresett="alma"
        aktualis = feladatok.titkositas(keresett)
        elvart = "eöőe"
        self.assertEqual(elvart, aktualis, keresett+" szót nem jól titkosította")
    def test_feladat02(self):
        keresett = "az"
        aktualis = feladatok.titkositas(keresett)
        elvart = "ed"
        self.assertEqual(elvart, aktualis, keresett + " szót nem jól titkosította")
    def test_feladat03(self):
        keresett = "eltöredezettségmentesítőtleníttethetetlenségtelenítőtlenkedhetnétek"
        aktualis = feladatok.titkositas(keresett)
        elvart = "iövsüihidivvűíkőipviűnvtvöipnvvivlivivöipűíkviöipnvtvöipóihlivpívió"
        self.assertEqual(elvart, aktualis, keresett + " szót nem jól titkosította")
    def test_feladat04(self):
        keresett = "elkelkáposztástalaníthatatlanságoskodásaitokért"
        aktualis = feladatok.titkositas(keresett)
        elvart = "iöóiöóéuqűdvéűveöepnvlevevöepűékqűóqhéűemvqóíüv"
        self.assertEqual(elvart, aktualis, keresett + " szót nem jól titkosította")
    def test_feladat05(self):
        keresett = ""
        aktualis = feladatok.titkositas(keresett)
        elvart = ""
        self.assertEqual(elvart, aktualis, keresett + " szót nem jól titkosította")
