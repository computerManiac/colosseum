from ....utils import W3CTestCase

class TestBorderPaddingBleed(W3CTestCase):
    vars().update(W3CTestCase.find_tests(__file__, 'border-padding-bleed-'))

