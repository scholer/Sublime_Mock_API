# Copyright 2019, Rasmus Sorensen <rasmusscholer@gmail.com>

"""

This module allows you to re-create and test the mocked `sublime_api` module against

Unfortunately, getting the signature for the sublime_api built-in functions or methods
is not possible, because they don't provide a signature.

    inspect.signature(sublime_api.yes_no_cancel_dialog)  # Raises ValueError

But what we *can* do is getting the signature for the functions in the mock_api module,
and test if they have an interface that is compatible with the functions from
the built-in sublime_api module.

See also:

* https://www.python.org/dev/peps/pep-0362/



"""

# If run from inside Sublime Text, and assuming you haven't shadowned the built-in path,
# this will get the original sublime_api module provided by the Sublime Text execution environment.
import sublime_api
from . import mock_api
import inspect



def compare_mock_vs_original():
    for attr_name in dir(sublime_api):
        original = getattr(sublime_api, attr_name)
        mocked = getattr(mock_api, attr_name)
        if str(type(original)) == "<class 'builtin_function_or_method'>":
            sig = inspect.signature(mocked)
            argspec = inspect.getfullargspec(mocked)

        else:
            print(attr_name, ":", original, " <--> ", mocked, "       ",
                  "Matches" if mocked == original else "MISMATCH!")


def check_missing_mock_items():
    something_is_missing = False
    for attr_name in dir(sublime_api):
        original = getattr(sublime_api, attr_name)
        try:
            mocked = getattr(mock_api, attr_name)
        except AttributeError:
            print("{} ({}) is MISSING in mock_api!".format(attr_name, type(original)))
            something_is_missing = True
    if not something_is_missing:
        print("** All attributes in sublime_api appears to be present in mock_api - GREAT! **")


def create_updated_mock_api_module():
    pass


