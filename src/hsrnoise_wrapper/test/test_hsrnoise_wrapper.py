
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
        for filename in ['test.input', 'test.output', 'hsr.dump']:
            if os.path.exists(filename):
                os.remove(filename)
        
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
    
            with open('base.input', 'r') as inp:
                result1 = inp.read()
            with open('test.input', 'r') as inp:
                result2 = inp.read()
            
            lnum = 1
            for line1, line2 in zip(result1, result2):
                # Omit lines with objects, because memory location differs
                if 'object at' not in line1:
                    try:
                        self.assertEqual(line1, line2)
                    except AssertionError as err:
                        raise AssertionError("line %d doesn't match file %s: %s"
                                             % (lnum, 'base.input', err))
                    lnum += 1
            
            # Check output file parsing
                
            shutil.copyfile('base.output', 'test.output')
            print comp.SPL
            comp.parse_output()
            print comp.SPL
            
            with open('hsr.dump', 'w') as out:
                dump(comp, stream=out, recurse=True)
            
            with open('base_hsr.dump', 'r') as inp:
                result1 = inp.readlines()
            with open('hsr.dump', 'r') as inp:
                result2 = inp.readlines()
            
            lnum = 1
            for line1, line2 in zip(result1, result2):
                # Omit lines with objects, because memory location differs
                if 'object at' not in line1:
                    try:
                        self.assertEqual(line1, line2)
                    except AssertionError as err:
                        raise AssertionError("line %d doesn't match file %s: %s"
                                             % (lnum, 'base_hsr.dump', err))
                    lnum += 1

        finally:
            os.chdir(basename)
        
if __name__ == "__main__":
    unittest.main()
    
