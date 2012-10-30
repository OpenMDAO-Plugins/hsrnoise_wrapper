
import unittest
import os
import sys
import shutil

from hsrnoise_wrapper.hsrnoise import HSRNOISE
from openmdao.main.container import dump

class Hsrnoise_wrapperTestCase(unittest.TestCase):

    def setUp(self):
        pass
        
    def tearDown(self):
        pass
        
    def test_Hsrnoise_wrapper(self):
        
        comp = HSRNOISE()

        dirname = os.path.abspath(os.path.dirname(__file__))

        basename = os.getcwd()
        os.chdir(dirname)

        try:
            # Check input file generation
            
            comp.load_model(filename='base.input')
            comp.setup()
            comp.generate_input()
    
            file1 = open('base.input', 'r')
            result1 = file1.read()
            file1.close()
            file1 = open('test.input', 'r')
            result2 = file2.read()
            file2.close()
            
            self.assertEqual(result1, result2)
            
            # Check output file parsing
                
            shutil.copyfile('base_ejectd.out', 'ejectd.out')
            comp.parse_output('Subsonic')
            
            file1 = open('drea.dump', 'w')
            dump(comp, stream=file1, recurse=True)
            file1.close()
            
            file1 = open('base_drea.dump', 'r')
            result1 = file1.readlines()
            file1.close()
            file2 = open('drea.dump', 'r')
            result2 = file2.readlines()
            file2.close()
            
            for line1, line2 in zip(result1, result2):
                # Omit lines with objects, because memory location differs
                if 'object at' not in line1:
                    self.assertEqual(line1, line2)

        finally:
            os.chdir(basename)
        
if __name__ == "__main__":
    unittest.main()
    