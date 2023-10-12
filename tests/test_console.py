#!/usr/bin/python3

"""
all unittests for console.py, all features!
"""

import inspect
import unittest
import console
import pep8
HBNBCommand = console.HBNBCommand


class TestConsoleDocs(unittest.TestCase):
    """It's a class for testing TestConsoleDocs of the Console"""

    def test_HBNBCommand_class_docstring(self):
        """It tests that the HBNBCommand_class Comply docstring"""

        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand class needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class needs a docstring")

    def test_pep8_conformance_console(self):
        """It tests that the conformance console Comply to PEP8."""

        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """It tests that the console module Comply docstring"""

        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_pep8_conformance_test_console(self):
        """It tests that the conformance console test Comply to PEP8."""

        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
