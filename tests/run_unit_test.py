import unittest

loader = unittest.TestLoader()
tests = loader.discover("/Users/igorsarnowski/PycharmProjects/cipher/tests/helpers")
testRunner = unittest.TextTestRunner()
testRunner.run(tests)
