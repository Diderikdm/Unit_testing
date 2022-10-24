import sys
import inspect
import traceback
import logging
from types import ModuleType
from typing import Union, Optional

def test_unit_tests(test_modules: Union[ModuleType, list], 
                    explicit_raise: bool = False,
                    explicit_return: bool = False, 
                    verbose_logging: bool = False) -> Optional[list]:
    """
    Use:
    --------
    Iterates through given test modules, finds the classes and functions within
    these classes that start with test and runs the tests. Logs errors in the log
    in all cases and returns error variables when explitit_return = True

    Args:
    --------
    test_modules : Union[ModuleType, list]
        module(s) you want to run the tests of.
    explicit_raise: bool = (optional)
        flag raises an error if any unittest did not pass (for DAG purposes)
    explicit_return : bool (optional)
        flag return a list of values to show in the portal, defaults to False
    verbose_logging : bool (optional)
        flag to dump the entire traceback to the logs, defaults to False

    Returns:
    --------
    out_data : Optional[list]
        Returns None or a list of errors (module name, function name, error message) 
                        per index depending on the flag explicit_return
    """

    if isinstance(test_modules, ModuleType):
        test_modules = [test_modules]

    failed_tests_to_return = []
    
    for test_module in test_modules:
        failed_tests = {}
        #finds all classes in module that start with test, x[0] = name, x[1] = class
        class_members = [x[1] for x in inspect.getmembers(sys.modules[test_module.__name__], inspect.isclass) if x[0].lower().startswith('test')]

        #build class ManualTest with above classes as parents 
        ManualTest = type('ManualTest', tuple(class_members), {})

        test_object = ManualTest()

        #find test functions in class(es)
        test_functions = [x for x in dir(test_object) if x.lower().startswith('test')]

        #run every test and collect exceptions
        for test_function in test_functions:
            test = getattr(test_object, test_function)
            try:
                test()
            except Exception as e:
                func_name = str(test_function)
                if verbose_logging:
                    failed_tests[func_name] = traceback.format_exc()
                else:
                    failed_tests[func_name] = e

                failed_tuple = (test_module.__name__, func_name, failed_tests[func_name])

                logging.warn('FAILED: {} : {}\n{}\n'.format(*failed_tuple))
                failed_tests_to_return.append(failed_tuple)

                
        if not failed_tests:
            logging.warn(f"All {len(test_functions)} unit tests for {test_module.__name__} passed.\n")
        else:
            logging.warn(get_fail_message_for_unit_test(failed_tests, test_module, len(test_functions)))

    #print a warn message in the log or returns a list of errors
    names_of_tested_modules = [test_module.__name__ for test_module in test_modules]
    if failed_tests_to_return:
        logging.warn(get_fail_message_for_all_unit_tests(failed_tests_to_return, names_of_tested_modules))

        if explicit_raise:
            raise Exception(f"{len(failed_tests_to_return)} failed: {get_raise_message(failed_tests_to_return)}")

    else:
        logging.warn(f"All unit tests for {names_of_tested_modules} passed.\n")

    if explicit_return:
        return failed_tests_to_return


def get_fail_message_for_unit_test(failed_tests, test_module, total_tests):

    message = f"{len(failed_tests)} unit test{'s' if len(failed_tests) > 1 else ''} out of {total_tests} for"

    message += f"{test_module.__name__} did not pass: {[test_name for test_name in failed_tests]}\n"

    return message
  

def get_fail_message_for_all_unit_tests(failed_tests, names_of_tests):

    message =  "\n\nA total of {} unit test{} for\n".format(len(failed_tests), 's' if len(failed_tests) > 1 else '')

    message += "\n{}\n\ndid not pass:".format('\n'.join(names_of_tests))

    message += "\n\n{}\n".format("\n".join(["{}.{} : {}".format(*failed) for failed in failed_tests]))

    return message


def get_raise_message(failed_tests_to_return):

    return "\n" + "\n".join([str(x) for x in failed_tests_to_return])
