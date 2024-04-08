import unittest
from TrappingRainWater_test import TestWaterTrap as test_class # Modify the file and class name


class CustomTestResult(unittest.TextTestResult):
    def printErrors(self):
        """
        Override the printErrors method to customize the output of failed and errored tests.
        This method is called by the unittest framework to print the errors and failures.
        """
        self.stream.writeln("\nFailed Test Cases Summary:")
        for test, err in self.failures + self.errors:
            # Extracting the test method name using test.id() and printing it
            self.stream.writeln(f"- {test.id().split('.')[-1]}: Failed")

def run_tests_and_calculate_percentage():
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class) 
    # Using the CustomTestResult class to handle the test results
    runner = unittest.TextTestRunner(resultclass=CustomTestResult, verbosity=2)
    result = runner.run(suite)
    
    total_tests = result.testsRun
    failed_tests = len(result.failures) + len(result.errors)
    passed_tests = total_tests - failed_tests
    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0
    
    print("\nSummary:")
    print(f"Total tests run: {total_tests}")
    print(f"Passed tests: {passed_tests}")
    print(f"Failed tests: {failed_tests}")
    print(f"Pass percentage: {pass_percentage:.2f}%")

if __name__ == '__main__':
    run_tests_and_calculate_percentage()

