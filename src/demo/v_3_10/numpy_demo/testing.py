import unittest

from numpy import array, floor, log10, all
from numpy.testing import assert_allclose
from pytest import raises, approx


class AssertSignificantDigits:

    @staticmethod
    def base10_exponent(number):
        if number == 0:
            return 0
        else:
            return int(floor(log10(abs(number))))

    @staticmethod
    def absolute_tolerance_for_n_digits(desired, significant_digits=3):
        return 0.5 * 10**(AssertSignificantDigits.base10_exponent(desired) - (significant_digits - 1))

    @staticmethod
    def assert_significant_digits_match(computed, expected, significant_digits=3):
        for a, b in zip(computed, expected):
            atol = AssertSignificantDigits.absolute_tolerance_for_n_digits(b, significant_digits)
            assert a == approx(b, abs=atol)


class TestAssertClose(unittest.TestCase):

    expected = array([0.0123000, 0.456, 0.789])

    # Counterintuitively, assert_allclose() sets the tolerance to absolute *plus* rtol * abs(desired), rather than
    # testing for absolute tolerance only in the case of small values, as in MATLAB and pytest. Generally, just use one
    # or the other. Relative tolerance is always measured with 'desired' as the denominator value, not
    # min(actual, desired). Therefore, rtol is a threshold on abs(actual - desired) / abs(desired). Unfortunately,
    # it also doesn't report which element failed.
    def test_relative_tolerance(self):

        computed = array([0.0123012, 0.456, 0.789])
        assert_allclose(computed, self.expected, rtol=1e-4, atol=0)

        with raises(AssertionError, match=r"Not equal to tolerance rtol="):
            computed = array([0.0123013, 0.456, 0.789])
            assert_allclose(computed, self.expected, rtol=1e-4, atol=0)  # fails

    def test_absolute_tolerance(self):

        computed = array([0.0123012, 0.456, 0.789])

        atol = AssertSignificantDigits.absolute_tolerance_for_n_digits(self.expected[0], 4)
        assert_allclose(computed, self.expected, rtol=0, atol=atol)

        with raises(AssertionError, match=r"Not equal to tolerance rtol="):
            atol = AssertSignificantDigits.absolute_tolerance_for_n_digits(self.expected[0], 5)
            assert_allclose(computed, self.expected, rtol=0, atol=atol)  # fails

    def test_pytest_approx(self):

        # If you specify both ``abs`` and ``rel``, the numbers will be considered equal if either tolerance is met.
        assert 1 + 1e-8 == approx(1)  # defaults are rel=1e-6 and abs=1e-12, must pass either
        assert 1 + 1e-8 == approx(1, rel=1e-6, abs=1e-12)  # same
        with raises(AssertionError):
            assert 1 + 1e-8 == approx(1, abs=1e-12)

        computed = array([0.0123012, 0.456, 0.789])

        # Use numpy.all() to test all components. The output is nice, but you can't vary the tolerance by component.
        with raises(AssertionError):
            assert all(computed == approx(self.expected))

        # Brute force method
        AssertSignificantDigits.assert_significant_digits_match(computed, self.expected, 4)
        with raises(AssertionError):
            AssertSignificantDigits.assert_significant_digits_match(computed, self.expected, 5)
