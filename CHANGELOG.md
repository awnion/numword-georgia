# Changelog

All notable changes to this project are documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## 0.4.0 - 2026-11-17

### Changed

- **Breaking:** Python 3.11 or newer is required; 3.8, 3.9 and 3.10 are no longer supported.
- **Breaking:** only integral types are accepted (`int`, `bool`, `IntEnum`, numpy integers).
  Floats, strings and other types raise `TypeError` instead of being converted with `int()`.
- **Breaking:** numbers outside `-10**15 + 1 .. 10**15 - 1` raise `ValueError`.
- The project is now dual-licensed under MIT or Apache-2.0, at your option.

### Added

- Billions (`მილიარდი`) and trillions (`ტრილიონი`).
- PyPy 3.11 is tested in CI.
- The package ships type information (`py.typed`).

### Fixed

- 8 and 9 no longer get a spurious `-ი` ending: `რვა`, `ცხრა`, `ოცდარვა`, `რვა ათასი`
  instead of `რვაი`, `ცხრაი`, `ოცდარვაი`, `რვაი ათასი`.
- 60 to 79 are spelled with a single `მ`: `სამოცი`, `სამოცდაშვიდი` instead of `სამმოცი`, `სამმოცდაშვიდი`.
- Negative numbers start with `მინუს` instead of `მინუსი`.
- Numbers from `10**9` no longer produce forms like `ათასი მილიონი`.

## 0.3.4 - 2026-11-17

### Added

- Python 3.14 support.
