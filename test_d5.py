import unittest
from aoc_trampolines import trampolines, trampolines_2

results = [{'input':list(map(int, '''0
    3
    0
    1
    -3'''.split())),
    'output':5},]

results2 = [{'input':list(map(int,
    '''0
        3
        0
        1
        -3'''.split())),
            'output':10},
            ]

class TrampolineTest(unittest.TestCase):
    def test_results(self):
        print('results are {}'.format(results))
        for r in results:
            print('Checking \n[{}]\n exits in {} steps'.format(r['input'], r['output']))
            self.assertEqual(r['output'], trampolines(r['input']))
        for r in results2:
            print('Checking \n[{}]\n exits in {} steps'.format(r['input'], r['output']))
            self.assertEqual(r['output'], trampolines_2(r['input']))

if __name__ == '__main__':
    print('hello world')
    unittest.main()
