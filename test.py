target = __import__("sprints.py")

import unittest
from sprints import myfun

class Testmyfun(unittest.TestCase):
    def test_list_int(self):

        test1 = [1, 2, 3,4,5,6]
        result1 = myfun(test1)
        self.assertEqual(result1, [4.0,0.0])
        
        
        test2 = [1, 2, 3,4,5,6,5.6,2.3]
        result1 = myfun(test1)
        self.assertEqual(result1, [4.0,5.6])
        
        
        test3 = [1.2, 3, 4,2.4,9.8,5,6,7,8,9]
        result1 = myfun(test1)
        self.assertEqual(result1, [6.0,9.8])

if __name__ == '__main__':
    unittest.main()
