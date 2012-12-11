# coding: utf-8
__author__ = 'awnion'

import unittest
from numword_georgia import translate

class MyTestCase(unittest.TestCase):

    def test0(self):
        self.assertEqual(translate(0), u'ნული')

    def test16(self):
        self.assertEqual(translate(16), u'თექვსმეტი')

    def test20(self):
        self.assertEqual(translate(20), u'ოცი')

    def test21(self):
        self.assertEqual(translate(21), u'ოცდაერთი')

    def test30(self):
        self.assertEqual(translate(30), u'ოცდაათი')

    def test36(self):
        self.assertEqual(translate(38), u'ოცდათვრამეტი')

    def test47(self):
        self.assertEqual(translate(47), u'ორმოცდაშვიდი')

    def test80(self):
        self.assertEqual(translate(80), u'ოთხმოცი')

    def test99(self):
        self.assertEqual(translate(99), u'ოთხმოცდაცხრამეტი')

    def test120(self):
        self.assertEqual(translate(120), u'ას ოცი')

    def test250(self):
        self.assertEqual(translate(250), u'ორას ორმოცდაათი')

    def test415(self):
        self.assertEqual(translate(415), u'ოთხას თხუთმეტი')

    def test1000(self):
        self.assertEqual(translate(1000), u'ათასი')

    def test1001(self):
        self.assertEqual(translate(1001), u'ათას ერთი')

    def test1200(self):
        self.assertEqual(translate(1200), u'ათას ორასი')

    def test1999(self):
        self.assertEqual(translate(1999), u'ათას ცხრაას ოთხმოცდაცხრამეტი')

    def test2000(self):
        self.assertEqual(translate(2000), u'ორი ათასი')

    def test2010(self):
        self.assertEqual(translate(2010), u'ორი ათას ათი')

    def test5909(self):
        self.assertEqual(translate(5909), u'ხუთი ათას ცხრაას ცხრაი')

    def test9999(self):
        # WARNING: this test may be wrong, in Babel first word is `ცხრა` w/o `ი`
        self.assertEqual(translate(9999), u'ცხრაი ათას ცხრაას ოთხმოცდაცხრამეტი')

    def test10000(self):
        self.assertEqual(translate(10000), u'ათი ათასი')

    def test10001(self):
        self.assertEqual(translate(10001), u'ათი ათას ერთი')

    def test1000000(self):
        self.assertEqual(translate(1000000), u'ერთი მილიონი')

    def test1000001(self):
        self.assertEqual(translate(1000001), u'ერთი მილიონ ერთი')

    def test99000000(self):
        self.assertEqual(translate(99000000), u'ოთხმოცდაცხრამეტი მილიონი')

    def test999999999(self):
        self.assertEqual(translate(999999999),
                         u'ცხრაას ოთხმოცდაცხრამეტი მილიონ ცხრაას '
                         u'ოთხმოცდაცხრამეტი ათას ცხრაას ოთხმოცდაცხრამეტი')


if __name__ == '__main__':
    unittest.main()
