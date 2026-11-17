# SPDX-FileCopyrightText: 2023-present Sergei Blinov <blinovsv@gmail.com>
#
# SPDX-License-Identifier: MIT OR Apache-2.0

import importlib.util

import pytest


def pytest_collection_modifyitems(items: list[pytest.Item]) -> None:
    """Skip docstring examples when numpy, which they use, is not installed."""
    if importlib.util.find_spec("numpy") is not None:
        return
    skip = pytest.mark.skip(reason="numpy is not installed")
    for item in items:
        if isinstance(item, pytest.DoctestItem):
            item.add_marker(skip)
