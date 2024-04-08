import unittest
from decryptPassword import DecryptPassword

class test_decryptPassword(unittest.TestCase):

    def test_decrypt1(self):
        self.assertEqual(str(DecryptPassword("43Ah*ck0rr0nk")), "hAck3rr4nk")
    def test_decrypt2(self):
        self.assertEqual(str(DecryptPassword("51Pa*0Lp*0e")), "aP1pL5e")

if __name__=="__main__":
    unittest.main()