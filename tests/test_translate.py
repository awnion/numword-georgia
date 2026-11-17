# SPDX-FileCopyrightText: 2023-present Sergei Blinov <blinovsv@gmail.com>
#
# SPDX-License-Identifier: MIT OR Apache-2.0

from enum import IntEnum

import pytest

from numword_georgia import translate


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (0, "ნული"),
        (8, "რვა"),
        (9, "ცხრა"),
        (16, "თექვსმეტი"),
        (-16, "მინუს თექვსმეტი"),
        (20, "ოცი"),
        (21, "ოცდაერთი"),
        (28, "ოცდარვა"),
        (29, "ოცდაცხრა"),
        (30, "ოცდაათი"),
        (38, "ოცდათვრამეტი"),
        (47, "ორმოცდაშვიდი"),
        (60, "სამოცი"),
        (67, "სამოცდაშვიდი"),
        (79, "სამოცდაცხრამეტი"),
        (80, "ოთხმოცი"),
        (99, "ოთხმოცდაცხრამეტი"),
        (120, "ას ოცი"),
        (250, "ორას ორმოცდაათი"),
        (415, "ოთხას თხუთმეტი"),
        (1000, "ათასი"),
        (1001, "ათას ერთი"),
        (1200, "ათას ორასი"),
        (1999, "ათას ცხრაას ოთხმოცდაცხრამეტი"),
        (2000, "ორი ათასი"),
        (2010, "ორი ათას ათი"),
        (5909, "ხუთი ათას ცხრაას ცხრა"),
        (9999, "ცხრა ათას ცხრაას ოთხმოცდაცხრამეტი"),
        (8000, "რვა ათასი"),
        (-9, "მინუს ცხრა"),
        (10000, "ათი ათასი"),
        (10001, "ათი ათას ერთი"),
        (1000000, "ერთი მილიონი"),
        (1000001, "ერთი მილიონ ერთი"),
        (99000000, "ოთხმოცდაცხრამეტი მილიონი"),
        (999999999, "ცხრაას ოთხმოცდაცხრამეტი მილიონ ცხრაას ოთხმოცდაცხრამეტი ათას ცხრაას ოთხმოცდაცხრამეტი"),
        # examples from the Georgian Wikipedia article on numerals
        (101, "ას ერთი"),
        (340, "სამას ორმოცი"),
        (1730, "ათას შვიდას ოცდაათი"),
        (1901, "ათას ცხრაას ერთი"),
        (20780, "ოცი ათას შვიდას ოთხმოცი"),
        (200533, "ორასი ათას ხუთას ოცდაცამეტი"),
        (2003700, "ორი მილიონ სამი ათას შვიდასი"),
        (5500731, "ხუთი მილიონ ხუთასი ათას შვიდას ოცდათერთმეტი"),
        (3500400800, "სამი მილიარდ ხუთასი მილიონ ოთხასი ათას რვაასი"),
        # amounts written out in Georgian official documents
        (1120000, "ერთი მილიონ ას ოცი ათასი"),
        (1867060, "ერთი მილიონ რვაას სამოცდაშვიდი ათას სამოცი"),
        (2200000, "ორი მილიონ ორასი ათასი"),
        (10**9, "ერთი მილიარდი"),
        (2 * 10**9 + 5, "ორი მილიარდ ხუთი"),
        (8 * 10**9, "რვა მილიარდი"),
        (10**12, "ერთი ტრილიონი"),
        (40 * 10**12 + 10**6, "ორმოცი ტრილიონ ერთი მილიონი"),
    ],
)
def test_translate(number: int, expected: str) -> None:
    assert translate(number) == expected


@pytest.mark.parametrize("number", [3.7, 3.0, "12", None])
def test_translate_rejects_non_integers(number: object) -> None:
    with pytest.raises(TypeError, match="expected an integer"):
        translate(number)  # ty: ignore[invalid-argument-type]


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (True, "ერთი"),
        (False, "ნული"),
        (IntEnum("Digit", {"NINE": 9}).NINE, "ცხრა"),
    ],
)
def test_translate_accepts_integral_types(number: int, expected: str) -> None:
    assert translate(number) == expected


@pytest.mark.parametrize("number", [10**15, -(10**15), 10**30])
def test_translate_rejects_out_of_range(number: int) -> None:
    with pytest.raises(ValueError, match="expected an integer between"):
        translate(number)


def test_translate_range_limits() -> None:
    assert translate(10**15 - 1).startswith("ცხრაას ოთხმოცდაცხრამეტი ტრილიონ ")
    assert translate(-(10**15) + 1).startswith("მინუს ცხრაას ")
