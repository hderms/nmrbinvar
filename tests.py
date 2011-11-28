import unittest
import tktest
class TestXIntersection(unittest.TestCase):
    def setUp(self):
        groupCont = tktest.groupContainer()
        groupCont.group_hash = {'0': tktest.group('test.csv', '0').read_spectra()}
        groupCont.group_hash['1'] =  tktest.group('test1.csv', '1').read_spectra()
        
    def test_choice(self):

        self.assertTrue(groupCont.group_xvalue_intersection().issubset(set['herp', 'derp']))
        
if __name__ == '__main__':

    groupCont = tktest.groupContainer('derp')
    groupCont.group_hash = {'0': tktest.group(['test.csv'], '0').read_spectra()}
    groupCont.group_hash['1'] =  tktest.group(['test1.csv'], '1').read_spectra()
    print groupCont.group_xvalue_intersection()
