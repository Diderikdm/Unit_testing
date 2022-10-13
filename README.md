# UnitTesting module

This module provides an easy way to centralize unittesting for certain functions you want to test. 
This module implements a dynamic approach to making the ManualTest class by extracting Test-classes from the provided module(s)
to the main function of this module and thus inheriting all test-functions connected to the Test-classes. It also adds a
runTest: pass function which is a mandatory function for unittests to run.

|WARNING: Be wary of using the same name for functions in multiple classes in the ***same*** module. Every consequal class with the same function name overrides the previously loaded function |
| --- |
 
# Writing a unit test

* Make a module and give it a name (for example tests.py)

* Inside the new module, import necessities:

```python
import unittest                                   # Main standard module for unittesting
from <path.to.module.to.test> import module       # module to test functions of
[...]
```

* And build a test class (starting with Test and inheriting unittest.TestCase) with (optional) fundamental functions needed for building given test-data:

```python
class TestFooBar(unittest.TestCase):
    
    [...]
    def make_stuff_that_helps_with_your_tests(self, parameters):
        return pd.DataFrame(dostuff)

    [...]
```

* Add functions (starting with test) to the test-class based on data you want to test the given module with:

```python
    def test_does_my_thing_work_1(self):
        # Build the variables (arguments that need to be passed to the function to be tested) with dummy-data 
        foo = {"key1" : "value1"}
        bar = ["values"]

        # Create an expected result
        expected = {"key1" : ["values"] + ["value"]}

        # Run the function of the module you want to test with the dummy-data as arguments
        actual = module.function(foo, bar)

        # Assert whether the result you got from running the function with dummy data is the same as the result you expected it to be or not
        self.assertEqual(expected, actual)
```

* At the bottom of the module, add the following snippet to run all the tests (when the code is inside this module, everything is loaded and ready to run):

```python
if __name__ == '__main__':
    unittest.main(verbosity=2)
```


# Usage
The UnitTesting module requires one module containing one or many* Test-classes (classes that start with Test) and these Test-classes require at least one or
many* test-functions (functions that start with test) combined. 

* The module will work regardless of amount, so a number of 0 would not cause an error; it would just not test anything.

three ways to use this module:

* import the module inside a jupyter notebook.
* use it inside a module you want to run tests of every time it's used.
* use it inside a unittest-DAG to run any/all tests at given times.

to see the tests and messages of the tests that failed:

```python
from path.to.module import test_module_name_containing_test_class_and_function

from path.to.module.unittesting import test_unit_tests

test_unit_tests(test_module_name_containing_test_class_and_function)
```

OR

```python
from path.to.module import test_module_name_containing_test_class_and_function
from path.to.module import test_module_name_containing_test_class_and_function_two

from path.to.module.unittesting import test_unit_tests

modules_to_test = [test_module_name_containing_test_class_and_function, test_module_name_containing_test_class_and_function_two]

test_unit_tests(modules_to_test)
```

# Parameters

There are three optional parameters you can use when using this module:

***

* explicit_return (boolean)

***

If True, this will return the failed unit tests in the form of:
tuple(module (dot notation path), name of the test that failed, actual errormessage)

For example:

```python
from path.to.module.unittesting import test_unit_testing_one, test_unit_testing_two

from path.to.module.unittesting.unittesting import test_unit_tests

modules_to_test = [test_unit_testing_one, test_unit_testing_two]
failed_tests = test_unit_tests(modules_to_test, explicit_return=True)

for failed_test in failed_tests:
    print(failed_test)
```

Output:

```python
>>> WARNING:root:FAILED: path.to.module.unittesting.test_unit_testing_one : test_false
>>> '/wrong/path' != PosixPath('/home/diderik/gcs/data/cache')
>>> 
>>> WARNING:root:FAILED: path.to.module.unittesting.test_unit_testing_one : test_three_compare_different_ints_as_equal
>>> 1 != 2
>>> 
>>> WARNING:root:2 unit tests forpath.to.module.unittesting.test_unit_testing_one did not pass: ['test_false', 'test_three_compare_different_ints_as_equal']
>>> 
>>> WARNING:root:All unit tests for path.to.module.unittesting.test_unit_testing_two passed.
>>> 
>>> WARNING:root:
>>> 
>>> A total of 2 unit tests for
>>> 
>>> path.to.module.unittesting.test_unit_testing_one
>>> path.to.module.unittesting.test_unit_testing_two
>>> 
>>> did not pass:
>>> 
>>> path.to.module.unittesting.test_unit_testing_one.test_false : '/wrong/path' != PosixPath('/home/diderik/gcs/data/cache')
>>> path.to.module.unittesting.test_unit_testing_one.test_three_compare_different_ints_as_equal : 1 != 2
>>> 
>>> ('path.to.module.unittesting.test_unit_testing_one', 'test_false', AssertionError("'/wrong/path' != PosixPath('/home/diderik/gcs/data/cache')"))
>>> ('path.to.module.unittesting.test_unit_testing_one', 'test_three_compare_different_ints_as_equal', AssertionError('1 != 2'))
```

***

* explicit_raise (boolean)

***

If True, raises an explicit error based on the same return variables in explicit_return at the end of all unit tests for these modules:

```python
>>> [2022-06-27 09:51:57,095] {taskinstance.py:1503} ERROR - Task failed with exception
>>> Traceback (most recent call last):
>>>   File "/opt/python3.8/lib/python3.8/site-packages/airflow/models/taskinstance.py", line 1158, in _run_raw_task
>>>     self._prepare_and_execute_task_with_callbacks(context, task)
>>>   File "/opt/python3.8/lib/python3.8/site-packages/airflow/models/taskinstance.py", line 1333, in _prepare_and_execute_task_with_callbacks
>>>     result = self._execute_task(context, task_copy)
>>>   File "/opt/python3.8/lib/python3.8/site-packages/airflow/models/taskinstance.py", line 1358, in _execute_task
>>>     result = task_copy.execute(context=context)
>>>   File "/opt/python3.8/lib/python3.8/site-packages/airflow/operators/python.py", line 150, in execute
>>>     return_value = self.execute_callable()
>>>   File "/opt/python3.8/lib/python3.8/site-packages/airflow/operators/python.py", line 161, in execute_callable
>>>     return self.python_callable(*self.op_args, **self.op_kwargs)
>>>   File "/home/airflow/gcs/dags/path.to.module/unittesting/unittesting.py", line 84, in test_unit_tests
>>>     raise Exception(f"{len(failed_tests_to_return)} failed: {get_raise_message(failed_tests_to_return)}")
>>> Exception: 1 failed: 
>>> ('etl_v2.unittests.test_automate_backfills', 'test_kwarg_mapping_fails', AssertionError("'-x' != '-x -i'\n- -x\n+ -x -i\n"))
```

***

* verbose_logging (boolean)

***

If True, this parameter will provide the full context of the error message in the logs.

For example:

```python
from path.to.module.unittesting import test_unit_testing_one, test_unit_testing_two

from path.to.module.unittesting.unittesting import test_unit_tests

modules_to_test = [test_unit_testing_one, test_unit_testing_two]
test_unit_tests(modules_to_test, verbose_logging=True)
```

Output:

```python
>>> WARNING:root:FAILED: path.to.module.unittesting.test_unit_testing_one : test_false
>>> Traceback (most recent call last):
>>>   File "/home/diderik/cloud/dags/path.to.module/unittesting/unittesting.py", line 56, in test_unit_tests
>>>     test()
>>>   File "/home/diderik/cloud/dags/path.to.module/unittesting/test_unit_testing_one.py", line 26, in test_false
>>>     self.assertEqual(path_to_verify, function_return_path)
>>>   File "/usr/lib/python3.8/unittest/case.py", line 912, in assertEqual
>>>     assertion_func(first, second, msg=msg)
>>>   File "/usr/lib/python3.8/unittest/case.py", line 905, in _baseAssertEqual
>>>     raise self.failureException(msg)
>>> AssertionError: '/wrong/path' != PosixPath('/home/diderik/gcs/data/cache')
>>> 
>>> 
>>> WARNING:root:FAILED: path.to.module.unittesting.test_unit_testing_one : test_three_compare_different_ints_as_equal
>>> Traceback (most recent call last):
>>>   File "/home/diderik/cloud/dags/path.to.module/unittesting/unittesting.py", line 56, in test_unit_tests
>>>     test()
>>>   File "/home/diderik/cloud/dags/path.to.module/unittesting/test_unit_testing_one.py", line 29, in test_three_compare_different_ints_as_equal
>>>     self.assertEqual(1, 2)
>>>   File "/usr/lib/python3.8/unittest/case.py", line 912, in assertEqual
>>>     assertion_func(first, second, msg=msg)
>>>   File "/usr/lib/python3.8/unittest/case.py", line 905, in _baseAssertEqual
>>>     raise self.failureException(msg)
>>> AssertionError: 1 != 2
>>> ...
>>>     raise self.failureException(msg)
>>> AssertionError: 1 != 2
```
