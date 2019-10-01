import unittest
import time
from atcommand import AtCommand, defaultAt

class DemoAtTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_case1(self):       
        defaultAt.send_at('ATE0')
        self.assertIsNotNone(defaultAt.check_at_resp('OK'))

        defaultAt.send_at('AT')
        self.assertIsNotNone(defaultAt.check_at_resp('OK'))

        defaultAt.send_at('ATI')
        at_resp = defaultAt.check_at_resp('OK')
        self.assertIsNotNone(at_resp)
        fw_ver = defaultAt.parse_at_resp('Revision:', at_resp)
        print fw_ver.split()[0] # To be check with expected fw version
        



        
