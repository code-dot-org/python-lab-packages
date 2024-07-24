import unittest
from .validation_runner import ValidationTestResult

# Run the tests in the given file pattern and display the results to the user.
# Validation tests use the ValidationTestResult class to display only the short description of the test.
def run_validation_tests(file_pattern):
  run_tests(file_pattern, ValidationTestResult)

# Run the tests in the given file pattern and display the results to the user.
# Student tests use the standard TextTestResult class to display the test name and short description.
def run_student_tests(file_pattern):
  run_tests(file_pattern, unittest.TextTestResult)

def run_tests(file_pattern, resultclass):
  loader = unittest.TestLoader()
  test_suite = loader.discover('.', file_pattern)
  runner = unittest.TextTestRunner(verbosity=2, resultclass=resultclass)
  result = runner.run(test_suite)
