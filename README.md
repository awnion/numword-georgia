# Numword Georgia

[![PyPI - Version](https://img.shields.io/pypi/v/numword-georgia.svg)](https://pypi.org/project/numword-georgia/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/numword-georgia.svg)](https://pypi.org/project/numword-georgia/)

- [Numword Georgia](#numword-georgia)
  - [Usage](#usage)
  - [Installation](#installation)
  - [Development](#development)
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

## License

`numword-georgia` is distributed under the terms of either the [MIT](https://github.com/awnion/numword-georgia/blob/main/LICENSE-MIT) license or the
[Apache License 2.0](https://github.com/awnion/numword-georgia/blob/main/LICENSE-APACHE), at your option.
