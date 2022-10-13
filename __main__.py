from _massarius.unittesting.unittesting import test_unit_tests
from _massarius.unittesting import (
    test_unit_testing_one,
    test_unit_testing_two,
    test_unit_testing_three
)


def main():
    test_unit_tests([
        test_unit_testing_one,
        test_unit_testing_two,
        test_unit_testing_three
    ])

if __name__ == "__main__":
    main()
