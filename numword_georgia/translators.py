# coding: utf-8
__author__ = "awnion"

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

_MINUS = "მინუსი"  # mi-nu-si
_I = "ი"  # -i at the end of a number
_DA = "და"  # da, before 1-19
_M = "მ"  # m, before 20s
_20 = "ოც"  # =20, the base number
_H1 = "ას"  # as-i
_T1 = "ათას"  # at-as
_M1 = "მილიონ"  # milion-i


def translate(number: int) -> str:
    """
    Translate numbers into georgian numbers in words

    See: http://en.wikipedia.org/wiki/Georgian_numerals
    """
    number = int(number)
    result = ""

    if number < 0:
        result += _MINUS + " "
        number = -number

    if number == 0:
        return BASE[0] + _I

    # handle 1'000'000
    m, number = divmod(number, 1000000)
    if m > 0:
        result += translate(m) + " " + _M1
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
            result += BASE[d] + _M
        result += _20
        if n == 0:
            return result + _I
        result += _DA

    return result + BASE[n] + _I


def main():
    for number in [5909, 9999, 7000, 7707, 91]:
        print(f"Number {number} is '{translate(number)}'")


if __name__ == "__main__":
    main()
