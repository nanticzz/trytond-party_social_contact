# This file is part of party_social_contact module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.

from trytond.tests.test_tryton import test_depends
import os
import sys
import trytond.tests.test_tryton
import unittest


class PartySocialContactTestCase(unittest.TestCase):
    'Test Party Social Contact module'

    def setUp(self):
        trytond.tests.test_tryton.install_module('party_social_contact')

    def test0006depends(self):
        'Test depends'
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        PartySocialContactTestCase))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
