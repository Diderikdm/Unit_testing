import unittest
from pathlib import Path

class TestClassOne(unittest.TestCase):


    def test_correct(self):

        from _massarius.caching_tools.caching_tools import get_path_for_airflow_cache

        path_to_verify = Path.home() / "gcs/data/cache"

        function_return_path = get_path_for_airflow_cache()

        self.assertEqual(path_to_verify, function_return_path)


    def test_false(self):

        from _massarius.caching_tools.caching_tools import get_path_for_airflow_cache
        
        path_to_verify = "/wrong/path"

        function_return_path = get_path_for_airflow_cache()

        self.assertEqual(path_to_verify, function_return_path)

    def test_three_compare_different_ints_as_equal(self):
        self.assertEqual(1, 2)


if __name__ == '__main__':
    import sys
    sys.path.append("/home/diderik/cloud/dags/")
    unittest.main(verbosity=2)
