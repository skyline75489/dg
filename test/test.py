import unittest
import shutil

from pathlib import Path

import dg


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.json = dg.read_json("test/test.json")

    def tearDown(self):
        shutil.rmtree('./test/hello')

    def test_1(self):
        dg.generate_dir_with_json(self.json, './test')
        self.assertTrue(Path('./test/hello').is_dir())
        self.assertTrue(Path('./test/hello/123.txt').is_file())
        self.assertTrue(Path('./test/hello/ok').is_dir())
        self.assertTrue(Path('./test/hello/ok/abc.md').is_file())
        self.assertTrue(Path('./test/hello/ok/good.js').is_file())

if __name__ == '__main__':
    unittest.main()
