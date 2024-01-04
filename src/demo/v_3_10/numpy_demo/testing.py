import unittest

from numpy import array, floor, log10
from numpy.testing import assert_allclose


class TestCloseArrays(unittest.TestCase):

    computed = array([0.0123012, 0.456, 0.789])
    expected = array([0.0123000, 0.456, 0.789])

    # Counterintuitively, assert_allclose() sets the tolerance to absolute *plus* rtol * abs(desired), rather than
    # testing for absolute tolerance only in the case of small values, as in MATLAB. Generally, just use one or
    # the other. Relative tolerance is always measured with 'desired' as the denominator value, not
    # min(actual, desired). Therefore, rtol is a threshold on abs(actual - desired) / abs(desired). Unfortunately,
    # it also doesn't report which element failed.

    @staticmethod
    def base10_exponent(number):
        if number == 0:
            return 0
        else:
            return int(floor(log10(abs(number))))

    @staticmethod
    def absolute_tolerance_for_n_digits(desired, significant_digits=3):
        return 0.5 * 10**(TestCloseArrays.base10_exponent(desired) - (significant_digits - 1))

    def test(self):

        assert_allclose(self.computed, self.expected, rtol=1e-4, atol=0)

        atol = self.absolute_tolerance_for_n_digits(self.expected[0], 4)
        # atol = self.absolute_tolerance_for_n_digits(self.expected[0], 5)  # fails
        assert_allclose(self.computed, self.expected, rtol=0, atol=atol)
