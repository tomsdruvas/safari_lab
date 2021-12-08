import unittest
from models.staff import Staff

class TestStaff(unittest.TestCase):
    
    def setUp(self):
        self.staff1 = Staff("Jack", "03.03.2020", 4)

    def test_staff_have_name(self):
        self.assertEqual("Jack", self.staff1.name)