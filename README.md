# Numword Georgia

[![PyPI - Version](https://img.shields.io/pypi/v/numword-georgia.svg)](https://pypi.org/project/numword-georgia/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/numword-georgia.svg)](https://pypi.org/project/numword-georgia/)

- [Numword Georgia](#numword-georgia)
  - [Usage](#usage)
  - [Installation](#installation)
  - [Development](#development)
  - [Changelog](#changelog)
  - [License](#license)

## Usage

Converts numbers to words

```python
from numword_georgia import translate

for number in [5909, 9999, 7000, 7707, 91]:
    print(f"Number {number} is '{translate(number)}'")
```

```text
Number 5909 is 'ხუთი ათას ცხრაას ცხრა'
Number 9999 is 'ცხრა ათას ცხრაას ოთხმოცდაცხრამეტი'
Number 7000 is 'შვიდი ათასი'
Number 7707 is 'შვიდი ათას შვიდას შვიდი'
Number 91 is 'ოთხმოცდათერთმეტი'
```

Supported range is from `-10**15 + 1` to `10**15 - 1`, numbers outside of it raise `ValueError`.

Any integral type is accepted: `int`, `bool`, `IntEnum`, numpy integers.
Anything else, including floats and numeric strings, raises `TypeError`.

```python
translate(-16)  # 'მინუს თექვსმეტი'
translate(2 * 10**9 + 5)  # 'ორი მილიარდ ხუთი'
translate(10**15)  # ValueError: expected an integer between -10**15 + 1 and 10**15 - 1
translate(3.7)  # TypeError: expected an integer
```

## Installation

```console
pip install numword-georgia
```

## Development

The project is managed with [uv](https://docs.astral.sh/uv/).

```console
uv sync                       # create the environment
uv run pytest                 # run tests
uv run coverage run -m pytest && uv run coverage report
uv run --python 3.14 pytest   # run tests on a specific Python
uv run ruff check .           # lint
uv run ruff format .          # format
uv run ty check               # type check
uv run taplo fmt              # format TOML
```

## Changelog

See [CHANGELOG.md](https://github.com/awnion/numword-georgia/blob/main/CHANGELOG.md).

## License

`numword-georgia` is distributed under the terms of either the [MIT](https://github.com/awnion/numword-georgia/blob/main/LICENSE-MIT) license or the
[Apache License 2.0](https://github.com/awnion/numword-georgia/blob/main/LICENSE-APACHE), at your option.
