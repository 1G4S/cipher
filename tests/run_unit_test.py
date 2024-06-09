import unittest

loader1 = unittest.TestLoader()
tests_files = loader1.discover("files")
unittest.TextTestRunner().run(tests_files)

loader2 = unittest.TestLoader()
tests_hashers = loader2.discover("hashers")
unittest.TextTestRunner().run(tests_hashers)

loader3 = unittest.TestLoader()
tests_helpers = loader3.discover("helpers")
unittest.TextTestRunner().run(tests_helpers)

loader4 = unittest.TestLoader()
tests_managers = loader4.discover("managers")
unittest.TextTestRunner().run(tests_managers)

loader5 = unittest.TestLoader()
tests_menus = loader5.discover("menus")
unittest.TextTestRunner().run(tests_menus)