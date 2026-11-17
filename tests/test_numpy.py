# SPDX-FileCopyrightText: 2023-present Sergei Blinov <blinovsv@gmail.com>
#
# SPDX-License-Identifier: MIT OR Apache-2.0

import pytest

from numword_georgia import translate

# numpy is not installed on PyPy: there it would be built from source
np = pytest.importorskip("numpy")


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (np.int64(9), "ცხრა"),
        (np.uint8(28), "ოცდარვა"),
        (np.int8(-128), "მინუს ას ოცდარვა"),
    ],
)
def test_translate_accepts_numpy_integers(number: int, expected: str) -> None:
    assert translate(number) == expected


def test_translate_rejects_numpy_floats() -> None:
    with pytest.raises(TypeError, match="expected an integer"):
        translate(np.float64(3.0))
