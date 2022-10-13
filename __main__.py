from <<path.to.module>>.unittesting.unittesting import test_unit_tests
from <<path.to.module>>.unittesting import (
    test_unit_testing_one,
    test_unit_testing_two,
    test_unit_testing_three
)

# Example usage
def main():
    modules_to_test = [
        test_unit_testing_one,
        test_unit_testing_two,
        test_unit_testing_three
    ]
    
    failed_tests = test_unit_tests(modules_to_test, explicit_return=True)

    for failed_test in failed_tests:
        print(failed_test)

if __name__ == "__main__":
    main()
