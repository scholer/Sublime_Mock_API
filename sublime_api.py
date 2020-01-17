# Copyright 2019, Rasmus Sorensen <rasmusscholer@gmail.com>

"""

Mocks the sublime_api functions provided by Sublime Text execution environment.

This currently only provides function interfaces, but no actual functionality.
That is, the functions when called, will not do anything, and will just return a dummy value,
typically simply 1.

"""

from sublime_mock_api.mock_api import *


print("sublime_api module imported (mocked version).")
print("version():", version())
