from ...utils import W3CTestCase

class TestOrder(W3CTestCase):
    vars().update(W3CTestCase.find_tests(__file__, 'order-'))

