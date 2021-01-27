import unittest
import tests.testCases.CardTest
import tests.testCases.DeckTest

# initialize the test suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(tests.testCases.DeckTest))
suite.addTests(loader.loadTestsFromModule(tests.testCases.CardTest))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)