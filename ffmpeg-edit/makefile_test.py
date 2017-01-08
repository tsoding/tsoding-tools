import unittest
from makefile import stopwatch_to_parts

class TestMakefile(unittest.TestCase):
    def test_stopwatch_to_parts(self):
        stopwatch = [["foo", 1],
                     ["bar", 100],
                     ["hello", 101],
                     ["world", 232],
                     ["derp", 404]]
        expected_parts = [
            {
                'begin': 1,
                'length': 100,
                'filename': 'part-1.ts'
            },
            {
                'begin': 101,
                'length': 132,
                'filename': 'part-2.ts'
            }
        ]
        self.assertEqual(stopwatch_to_parts(stopwatch), expected_parts)

if __name__ == '__main__':
    unittest.main()
