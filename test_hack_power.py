import unittest
import hack_power

class TestHack(unittest.TestCase):

    def test_hack_calculator(self):
        self.assertEqual(hack_power.hack_calculator('baaca'), 31)
        self.assertEqual(hack_power.hack_calculator('babacaba'), 55)
        self.assertEqual(hack_power.hack_calculator('aabacabaaaca'), 81)
        self.assertEqual(hack_power.hack_calculator('abc'), 6)
        self.assertEqual(hack_power.hack_calculator('baad'), 0)



if __name__ == '__main__':
    unittest.main()
