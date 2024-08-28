import unittest
from jar import Jar

class TestJar(unittest.TestCase):

    def test_initialization(self):
        jar = Jar()
        self.assertEqual(jar.capacity, 12)
        self.assertEqual(jar.size, 0)

    def test_deposit(self):
        jar = Jar()
        jar.deposit(5)
        self.assertEqual(jar.size, 5)
        self.assertEqual(str(jar), "🍪🍪🍪🍪🍪")

        jar.deposit(6)
        self.assertEqual(jar.size, 11)

        with self.assertRaises(ValueError):
            jar.deposit(2)

    def test_withdraw(self):

        jar = Jar()
        jar.deposit(10)
        jar.withdraw(4)
        self.assertEqual(jar.size, 6)
        self.assertEqual(str(jar), "🍪🍪🍪🍪🍪🍪")

        with self.assertRaises(ValueError):
            jar.withdraw(7)

    def test_str_representation(self):
        jar = Jar()
        jar.deposit(3)
        self.assertEqual(str(jar), "🍪🍪🍪")
        jar.withdraw(2)
        self.assertEqual(str(jar), "🍪")

if __name__ == "__main__":
    result = unittest.main(exit=False)
    if result.result.wasSuccessful():
        sys.exit(0)
    else:
        sys.exit(1)
    unittest.main()
