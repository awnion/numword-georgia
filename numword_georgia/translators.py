# coding: utf-8
__author__ = 'awnion'

base = {
    0: u"ნულ",
    1: u"ერთ",
    2: u"ორ",
    3: u"სამ",
    4: u"ოთხ",
    5: u"ხუთ",
    6: u"ექვს",
    7: u"შვიდ",
    8: u"რვა",
    9: u"ცხრა",
    10: u"ათ",
    11: u"თერთმეტ",
    12: u"თორმეტ",
    13: u"ცამეტ",
    14: u"თოთხმეტ",
    15: u"თხუთმეტ",
    16: u"თექვსმეტ",
    17: u"ჩვიდმეტ",
    18: u"თვრამეტ",
    19: u"ცხრამეტ",
}

_minus = u'მინუსი' # mi-nu-si
_i = u"ი"  # -i at the end of a number
_da = u"და"  # da, before 1-19
_m = u"მ"  # m, before 20s
_20 = u"ოც"  # =20, the base number
_h1 = u"ას"  # as-i
_t1 = u"ათას"  # at-as
_m1 = u"მილიონ"  # milion-i


def translate(number):
    """
    Translate numbers into georgian numbers in words

    See: http://en.wikipedia.org/wiki/Georgian_numerals
    """
    number = int(number)
    result = u''

    if number < 0:
        result += _minus + u' '
        number = -number

    if number == 0:
        return base[0] + _i

    # handle 1'000'000
    m, number = divmod(number, 1000000)
    if m > 0:
        result += translate(m) + u' ' + _m1
        if number == 0:
            return result + _i
        result += u' '

    # handle 1'000
    t, number = divmod(number, 1000)
    if t > 0:
        if t > 1:
            result += translate(t) + u' '
        result += _t1
        if number == 0:
            return result + _i
        result += u' '

    # handle 100
    h, number = divmod(number, 100)
    if h > 0:
        if h > 1:
            result += base[h]
        result += _h1
        if number == 0:
            return result + _i
        result += u' '

    # handle 20
    d, n = divmod(number, 20)
    if d > 0:
        if d > 1:
            result += base[d] + _m
        result += _20
        if n == 0:
            return result + _i
        result += _da

    return result + base[n] + _i


def main():
    print translate(5909)
    print translate(9999)
    print translate(7000)
    print translate(7707)

if __name__ == "__main__":
    main()