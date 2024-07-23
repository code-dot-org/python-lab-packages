import unittest
from .validation_runner import ValidationTestResult

def run_validation_tests(file_pattern):
  run_tests(file_pattern, ValidationTestResult)

def run_student_tests(file_pattern):
  run_tests(file_pattern, unittest.TextTestResult)

def run_tests(file_pattern, resultclass):
  loader = unittest.TestLoader()
  test_suite = loader.discover('.', file_pattern)
  runner = unittest.TextTestRunner(verbosity=2, resultclass=resultclass)
  result = runner.run(test_suite)
