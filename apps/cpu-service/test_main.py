import unittest
from main import VERSION

class TestCPUService(unittest.TestCase):
    def test_version_format(self):
        # 驗證版號格式是否包含 "-cpu"
        self.assertTrue(VERSION.endswith("-cpu"))

    def test_version_value(self):
        # 驗證目前版號是否正確 (作為範例)
        self.assertEqual(VERSION, "1.0.0-cpu")

if __name__ == "__main__":
    unittest.main()
