# SPDX-FileCopyrightText: 2023-present Sergei Blinov <blinovsv@gmail.com>
#
# SPDX-License-Identifier: MIT
# coding: utf-8

import unittest

from numword_georgia import translate


class MyTestCase(unittest.TestCase):
    def test0(self):
        self.assertEqual(translate(0), "ნული")

    def test16(self):
        self.assertEqual(translate(16), "თექვსმეტი")

    def testminus16(self):
        self.assertEqual(translate(-16), "მინუსი თექვსმეტი")

    def test20(self):
        self.assertEqual(translate(20), "ოცი")

    def test21(self):
        self.assertEqual(translate(21), "ოცდაერთი")

    def test30(self):
        self.assertEqual(translate(30), "ოცდაათი")

    def test36(self):
        self.assertEqual(translate(38), "ოცდათვრამეტი")

    def test47(self):
        self.assertEqual(translate(47), "ორმოცდაშვიდი")

    def test80(self):
        self.assertEqual(translate(80), "ოთხმოცი")

    def test99(self):
        self.assertEqual(translate(99), "ოთხმოცდაცხრამეტი")

    def test120(self):
        self.assertEqual(translate(120), "ას ოცი")

    def test250(self):
        self.assertEqual(translate(250), "ორას ორმოცდაათი")

    def test415(self):
        self.assertEqual(translate(415), "ოთხას თხუთმეტი")

    def test1000(self):
        self.assertEqual(translate(1000), "ათასი")

    def test1001(self):
        self.assertEqual(translate(1001), "ათას ერთი")

    def test1200(self):
        self.assertEqual(translate(1200), "ათას ორასი")

    def test1999(self):
        self.assertEqual(translate(1999), "ათას ცხრაას ოთხმოცდაცხრამეტი")

    def test2000(self):
        self.assertEqual(translate(2000), "ორი ათასი")

    def test2010(self):
        self.assertEqual(translate(2010), "ორი ათას ათი")

    def test5909(self):
        self.assertEqual(translate(5909), "ხუთი ათას ცხრაას ცხრაი")

    def test9999(self):
        # WARNING: this test may be wrong, in Babel first word is `ცხრა` w/o `ი`
        self.assertEqual(translate(9999), "ცხრაი ათას ცხრაას ოთხმოცდაცხრამეტი")

    def test10000(self):
        self.assertEqual(translate(10000), "ათი ათასი")

    def test10001(self):
        self.assertEqual(translate(10001), "ათი ათას ერთი")

    def test1000000(self):
        self.assertEqual(translate(1000000), "ერთი მილიონი")

    def test1000001(self):
        self.assertEqual(translate(1000001), "ერთი მილიონ ერთი")

    def test99000000(self):
        self.assertEqual(translate(99000000), "ოთხმოცდაცხრამეტი მილიონი")

    def test999999999(self):
        self.assertEqual(
            translate(999999999),
            "ცხრაას ოთხმოცდაცხრამეტი მილიონ ცხრაას ოთხმოცდაცხრამეტი ათას ცხრაას ოთხმოცდაცხრამეტი",
        )


if __name__ == "__main__":
    unittest.main()
