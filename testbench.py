"""
A class for packaging multiple tests into one testbench.
"""
class TestBench:
    """
    Class constructor.

    description: A string description of the testbench as a whole.
    """
    def __init__(self, description: str):
        self.__description = description
        self.__num_tests = 0

        # Rep. Invariant: The elems of __test are dictionary with the following key/value pairs:
        # "description": string description of test
        # "function": Pointer to the function for this test
        # "Inputs": The parameters to pass to this function
        self.__tests = []

    """
    Add a test to the testbench.

    descripion: A string description of this particular test
    funct: A pointer to a function to run as part of the testbench. It may have any output, but the output will be ignored when running the testbench. The function should *not* have any parameters.
    """
    def add_test(self, description: str, funct):
        test = {'description': description, 'function': funct}
        self.__tests.append(test)
        self.__num_tests += 1

    """
    Add multiple tests to the testbench.

    The tests should be in the form of a list of tuples (description, function), where description and function satisfy the preconditions in add_test.
    """
    def add_tests(self, tests: list):
        for test in tests:
            self.add_test(test[0], test[1])

    """
    Runs all of the tests in the testbench

    Every test will be run, even if some fail.

    The function provided for each test will be run as-is, and the test will be defined as passing if the function does not throw an exception.
    """
    def run_bench(self):
        num_passed = 0
        print("{}\n".format(self.__description))

        # ID is simply the order in which the test was added
        for test_id in range(len(self.__tests)):
            # Test encoded as a dictionary
            test = self.__tests[test_id]
            test_description, test_function = test['description'], test['function']

            print("Running test {}".format(test_id))
            print("Description: {}".format(test_description))

            try:
                # Precondition: function takes no parameters
                test_function()
                # If no assertion error raised:
                print("Test {} passed\n".format(test_id))
                num_passed += 1

            # Otherwise assertion error was raised
            except Exception as msg:
                print(msg)
                print("Test {} failed\n".format(test_id))
        
        print('{} tests passed, {} tests failed'.format(num_passed, self.__num_tests - num_passed))
