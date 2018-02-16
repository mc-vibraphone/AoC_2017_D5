import unittest
from aoc_trampolines import trampolines

results = [{'input':list(map(int, '''0
    3
    0
    1
    -3'''.split())),
            'output':5},
          ]

class TrampolineTest(unittest.TestCase):
    def test_results(self):
        print('results are {}'.format(results))
        for r in results:
            print('Checking \n[{}]\n exits in {} steps'.format(r['input'], r['output']))
            self.assertEqual(r['output'], trampolines(r['input']))

if __name__ == '__main__':
    print('hello world')
    unittest.main()
