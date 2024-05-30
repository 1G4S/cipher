import unittest

loader = unittest.TestLoader()
tests = loader.discover('/Users/igorsarnowski/PycharmProjects/cipher/tests/hashers')
testRunner = unittest.TextTestRunner()
testRunner.run(tests)
