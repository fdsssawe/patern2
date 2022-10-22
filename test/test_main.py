import datetime
import uuid
from unittest import TestCase
from main import QualityAssurance,AssignmentManager,Employee,Project,ProjectManager


class TestAssignmentManager(TestCase):
	def test_link(self):
		p1 = AssignmentManager()
		tempid = uuid.uuid4()
		project1 = "title"
		self.assertEqual(AssignmentManager.link(p1, tempid, project1), "['title']")


class TestQualityAssurance(TestCase):
	def test_ask_sick_leave(self):
		QA = QualityAssurance
		employee = Employee("test","test","test","test","test","test","test")
		project = Project("test",datetime.time,[1,5,7,8],5)
		PM = ProjectManager(1,"test","test","test","test",152,project)
		AM = AssignmentManager()
		AM.link(employee.id,project.title)
		self.assertEqual(QualityAssurance.ask_sick_leave(QA,PM,project,employee,AM),)
