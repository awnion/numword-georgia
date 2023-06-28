# Numword Georgia

[![PyPI - Version](https://img.shields.io/pypi/v/numword-georgia.svg)](https://pypi.org/project/numword-georgia/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/htest.svg)](https://pypi.org/project/numword-georgia/)

- [Numword Georgia](#numword-georgia)
  - [Usage](#usage)
  - [Installation](#installation)
  - [License](#license)

## Usage

Converts numbers to words

```python
from numword_georgia import translate

for number in [5909, 9999, 7000, 7707, 91]:
    print(f"Number {number} is '{translate(number)}'")
```

```text
Number 5909 is 'ხუთი ათას ცხრაას ცხრაი'
Number 9999 is 'ცხრაი ათას ცხრაას ოთხმოცდაცხრამეტი'
Number 7000 is 'შვიდი ათასი'
Number 7707 is 'შვიდი ათას შვიდას შვიდი'
Number 91 is 'ოთხმოცდათერთმეტი'
```

## Installation

```console
pip install numword-georgia
```

## License

`numword-georgia` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
