from django.test import TestCase, Client
from students.models import Student
from datetime import date

# Create your tests here.


class StudentTest(TestCase):
    def test_student_pages(self):
        client = Client()

        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)

        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 404)

        student_1 = Student.objects.create(name='Student_Vasya',
                                           surname='Prosto_Vasya',
                                           date_of_birth=date(1996, 2, 16),
                                           email="example@example.com",
                                           )
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Student_Vasya")

        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "example@example.com")

    def test_student_create(self):
        student_1 = Student.objects.create(name='Student_Vasya',
                                           surname='Prosto_Vasya',
                                           date_of_birth=date(1996, 2, 16),
                                           email="example@example.com",
                                           )
        student_2 = Student.objects.create(name='Student_Petya',
                                           surname='Prosto_Petya',
                                           date_of_birth=date(1996, 3, 16),
                                           email="notexample@example.com",
                                           )
        self.assertEqual(Student.objects.all().count(), 2)

    def test_student_edit(self):
        client = Client()

        student_1 = Student.objects.create(name='Student_Vasya',
                                           surname='Prosto_Vasya',
                                           date_of_birth=date(1996, 2, 16),
                                           email="example@example.com",
                                           )
        student_1 = Student.objects.update(name='Student_Petya',
                                           surname='Prosto_Petya',
                                           date_of_birth=date(1996, 3, 16),
                                           email="notexample@example.com",
                                           )
        self.assertEqual(Student.objects.all().count(), 1)

        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "notexample@example.com")

        response = client.get('/students/2/')
        self.assertEqual(response.status_code, 404)