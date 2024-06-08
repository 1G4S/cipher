import unittest

loader1 = unittest.TestLoader()
tests_files = loader1.discover("/Users/igorsarnowski/PycharmProjects/cipher/tests/files")
unittest.TextTestRunner().run(tests_files)

loader2 = unittest.TestLoader()
tests_hashers = loader2.discover("/Users/igorsarnowski/PycharmProjects/cipher/tests/hashers")
unittest.TextTestRunner().run(tests_hashers)

loader3 = unittest.TestLoader()
tests_helpers = loader3.discover("/Users/igorsarnowski/PycharmProjects/cipher/tests/helpers")
unittest.TextTestRunner().run(tests_helpers)

loader4 = unittest.TestLoader()
tests_managers = loader4.discover("/Users/igorsarnowski/PycharmProjects/cipher/tests/managers")
unittest.TextTestRunner().run(tests_managers)

loader5 = unittest.TestLoader()
tests_menus = loader5.discover("/Users/igorsarnowski/PycharmProjects/cipher/tests/menus")
unittest.TextTestRunner().run(tests_menus)