import unittest
from .validation_runner import ValidationTestResult

# Run the tests in the given file pattern and display the results to the user.
# Validation tests use the ValidationTestResult class to display only the short description of the test.
# This also returns simplified results for the caller to use. Simplified results is a list of the form:
# [{'name': 'test_name', 'result': 'PASS/FAIL/ERROR/EXPECTED_FAILURE/UNEXPECTED_SUCCESS'}, ...]
def run_validation_tests(file_pattern):
  result = run_tests(file_pattern, ValidationTestResult)
  return result.simplified_results

# Run the tests in the given file pattern and display the results to the user.
# Student tests use the standard TextTestResult class to display the test name and short description.
def run_student_tests(file_pattern):
  run_tests(file_pattern, unittest.TextTestResult)

def run_tests(file_pattern, resultclass):
  loader = unittest.TestLoader()
  test_suite = loader.discover('.', file_pattern)
  runner = unittest.TextTestRunner(verbosity=2, resultclass=resultclass)
  return runner.run(test_suite)
