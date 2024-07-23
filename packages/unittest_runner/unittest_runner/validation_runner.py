
from unittest import TextTestResult

class ValidationTestResult(TextTestResult):
  # The default behavior is to display the test name and short description.
  # We want to display only the short description if it exists, otherwise just the test name.
  # Students don't see the tests, so we don't need to display the test name.
  def getDescription(self, test):
    doc_first_line = test.shortDescription()
    if doc_first_line:
      return doc_first_line
    else:
      return str(test)
