import unittest
from makefile import stopwatch_to_parts, seconds_to_timestamp

class TestMakefile(unittest.TestCase):
    def test_stopwatch_to_parts(self):
        stopwatch = [["foo", 1],
                     ["bar", 100],
                     ["hello", 150],
                     ["world", 232],
                     ["derp", 404]]
        expected_parts = [
            {
                'begin': 1,
                'length': 100,
                'filename': 'part-1.ts',
                'timestamp': '0:0:0'
            },
            {
                'begin': 150,
                'length': 83,
                'filename': 'part-2.ts',
                'timestamp': '0:1:40'
            }
        ]
        self.assertEqual(stopwatch_to_parts(stopwatch), expected_parts)

    def test_seconds_to_timestamp(self):
        self.assertEqual(seconds_to_timestamp(0), "0:0:0")
        self.assertEqual(seconds_to_timestamp(60), "0:1:0")
        self.assertEqual(seconds_to_timestamp(92), "0:1:32")
        self.assertEqual(seconds_to_timestamp(92), "0:1:32")
        self.assertEqual(seconds_to_timestamp(5036), "1:23:56")


if __name__ == '__main__':
    unittest.main()
