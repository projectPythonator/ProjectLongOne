import os
import unittest

from InputClass import InputCLass

class TestInputCLass(unittest.TestCase):
    test_dir = os.path.dirname(os.path.abspath(__file__)).split(os.sep)[-1]+"/HelloWorkdd.c"
    def testinit(self):
        instancetest = InputCLass("int main()",self.test_dir)
        self.assertEqual(self.test_dir, instancetest.fid)
        self.assertEqual("int main()", instancetest.sig)
    def testthe_inputs(self):
        pass

if __name__ == '__main__':
    unittest.main()
