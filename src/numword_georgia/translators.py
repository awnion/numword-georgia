# SPDX-FileCopyrightText: 2023-present Sergei Blinov <blinovsv@gmail.com>
#
# SPDX-License-Identifier: MIT OR Apache-2.0

from numbers import Integral

BASE = {
    0: "ნულ",
    1: "ერთ",
    2: "ორ",
    3: "სამ",
    4: "ოთხ",
    5: "ხუთ",
    6: "ექვს",
    7: "შვიდ",
    8: "რვა",
    9: "ცხრა",
    10: "ათ",
    11: "თერთმეტ",
    12: "თორმეტ",
    13: "ცამეტ",
    14: "თოთხმეტ",
    15: "თხუთმეტ",
    16: "თექვსმეტ",
    17: "ჩვიდმეტ",
    18: "თვრამეტ",
    19: "ცხრამეტ",
}

_MINUS = "მინუს"  # mi-nus
_I = "ი"  # -i at the end of a number
_DA = "და"  # da, before 1-19
_M = "მ"  # m, before 20s
_20 = "ოც"  # =20, the base number
_H1 = "ას"  # as-i
_T1 = "ათას"  # at-as
_SCALES = (
    (10**12, "ტრილიონ"),  # trilion-i
    (10**9, "მილიარდ"),  # miliard-i
    (10**6, "მილიონ"),  # milion-i
)
_LIMIT_EXP = 15
_LIMIT = 10**_LIMIT_EXP


def translate(number: int) -> str:
    """
    Translate numbers into georgian numbers in words

    Any integral type is accepted: int and its subclasses (bool, IntEnum)
    as well as numpy integers. Floats and strings are not.

    >>> translate(9)
    'ცხრა'
    >>> translate(True)
    'ერთი'
    >>> translate(False)
    'ნული'
    >>> import numpy
    >>> translate(numpy.int64(9))
    'ცხრა'
    >>> translate(numpy.uint8(28))
    'ოცდარვა'
    >>> translate(9.0)
    Traceback (most recent call last):
    TypeError: expected an integer

    Raises TypeError for non-integers and ValueError for abs(number) >= 10**15.

    See: http://en.wikipedia.org/wiki/Georgian_numerals
    """
    if not isinstance(number, Integral):
        msg = "expected an integer"
        raise TypeError(msg)
    number = int(number)
    if abs(number) >= _LIMIT:
        msg = f"expected an integer between -10**{_LIMIT_EXP} + 1 and 10**{_LIMIT_EXP} - 1"
        raise ValueError(msg)

    result = ""

    if number < 0:
        result += _MINUS + " "
        number = -number

    if number == 0:
        return BASE[0] + _I

    # handle 1'000'000 and above
    for scale, name in _SCALES:
        m, number = divmod(number, scale)
        if m > 0:
            result += translate(m) + " " + name
            if number == 0:
                return result + _I
            result += " "

    # handle 1'000
    t, number = divmod(number, 1000)
    if t > 0:
        if t > 1:
            result += translate(t) + " "
        result += _T1
        if number == 0:
            return result + _I
        result += " "

    # handle 100
    h, number = divmod(number, 100)
    if h > 0:
        if h > 1:
            result += BASE[h]
        result += _H1
        if number == 0:
            return result + _I
        result += " "

    # handle 20
    d, n = divmod(number, 20)
    if d > 0:
        if d > 1:
            # 60 is sam-otsi: the stem already ends in m
            result += BASE[d] if BASE[d].endswith(_M) else BASE[d] + _M
        result += _20
        if n == 0:
            return result + _I
        result += _DA

    # 8 and 9 end in a vowel and take no -i
    if n in (8, 9):
        return result + BASE[n]
    return result + BASE[n] + _I
