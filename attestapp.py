import unittest
from demotestcase import DemoAtTestCase
from atcommand import AtCommand, defaultAt

class AtTestApp:
    def __init__(self):
        pass

    def start(self):
        defaultAt.open('COM12')
        
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(DemoAtTestCase)
        unittest.TextTestRunner(verbosity=2).run(suite)

        defaultAt.close()

if __name__ == "__main__":
    AtTestApp().start()
