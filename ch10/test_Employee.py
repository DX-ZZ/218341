import unittest


class EmployeeTestCase(unittest.TestCase):

    def setUp(self):
        self.formatted_default = Employee('ding', 'yuanxue', 1000)

    def test_give_default_raise(self):
        self.formatted_default.give_raise()
        self.assertEqual(self.formatted_default.salary, 6000)

    def test_give_coustom_raise(self):
        self.formatted_default.give_raise(8000)
        self.assertEqual(self.formatted_default.salary, 9000)

    if __name__ == 'main':
     unittest.main()
