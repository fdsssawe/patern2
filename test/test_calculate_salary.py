from unittest import TestCase
from main import  QualityAssurance


class TestQualityAssurance(TestCase):
	def test_calculate_salary(self):
		p1 = QualityAssurance
		self.assertEqual(QualityAssurance.calculate_salary(p1,employee_salary=1000,task_number=1),1000)
