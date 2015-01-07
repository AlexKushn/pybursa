from django.test import TestCase, Client
from courses.models import Course
from coaches.models import Coach
from django.contrib.auth.models import User
from datetime import date

# Create your tests here.


class CourseTest(TestCase):
    def test_course_pages(self):
        client = Client()
        user_1 = User.objects.create()

        response = client.get('/courses/')
        self.assertEqual(response.status_code, 200)

        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 404)

        coach_1 = Coach.objects.create(name='Petr',
                                       surname='Ivanov',
                                       date_of_birth=date(1996, 2, 16),
                                       email="example@example.com",
                                       user=user_1,
                                       )
        course_1 = Course.objects.create(name='PyBursa1',
                                         description='Course PyBursa',
                                         date_of_start=date(2015, 1, 16),
                                         date_of_end=date(2015, 3, 16),
                                         lecturer=coach_1,
                                         )
        response = client.get('/courses/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "PyBursa1")

        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Course PyBursa")

    def test_course_create(self):
        user_1 = User.objects.create()

        coach_1 = Coach.objects.create(name='Petr',
                                       surname='Ivanov',
                                       date_of_birth=date(1996, 2, 16),
                                       email="example@example.com",
                                       user=user_1,
                                       )

        course_1 = Course.objects.create(name='PyBursa1',
                                         description='Course PyBursa',
                                         date_of_start=date(2015, 1, 16),
                                         date_of_end=date(2015, 3, 16),
                                         lecturer=coach_1,
                                         )
        course_2 = Course.objects.create(name='PyBursa2',
                                         description='Course PyBursa',
                                         date_of_start=date(2015, 1, 16),
                                         date_of_end=date(2015, 3, 16),
                                         lecturer=coach_1,
                                         )
        self.assertEqual(Course.objects.all().count(), 2)

    def test_course_edit(self):
        client = Client()
        user_1 = User.objects.create()

        coach_1 = Coach.objects.create(name='Petr',
                                       surname='Ivanov',
                                       date_of_birth=date(1996, 2, 16),
                                       email="example@example.com",
                                       user=user_1,
                                       )
        course_1 = Course.objects.create(name='PyBursa1',
                                         description='Course PyBursa',
                                         date_of_start=date(2015, 1, 16),
                                         date_of_end=date(2015, 3, 16),
                                         lecturer=coach_1,
                                         )
        course_1 = Course.objects.update(name='PyBursa2',
                                         description='Course PyBursa2',
                                         date_of_start=date(2015, 2, 16),
                                         date_of_end=date(2015, 4, 16),
                                         lecturer=coach_1,
                                         )
        self.assertEqual(Course.objects.all().count(), 1)

        response = client.get('/courses/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Course PyBursa2")

        response = client.get('/courses/2/')
        self.assertEqual(response.status_code, 404)