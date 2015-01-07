from django.test import TestCase, Client
from coaches.models import Coach
from django.contrib.auth.models import User
from datetime import date

# Create your tests here.


class CoachTest(TestCase):
    def test_coach_pages(self):
        client = Client()
        user_1 = User.objects.create()

        response = client.get('/coaches/')
        self.assertEqual(response.status_code, 200)

        response = client.get('/coaches/1/')
        self.assertEqual(response.status_code, 404)

        coach_1 = Coach.objects.create(name='Petr',
                                       surname='Ivanov',
                                       date_of_birth=date(1996, 2, 16),
                                       email="example@example.com",
                                       user=user_1,
                                       )
        response = client.get('/coaches/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Petr")

        response = client.get('/coaches/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "example@example.com")

    def test_coach_create(self):
        user_1 = User.objects.create()

        coach_1 = Coach.objects.create(name='Petr',
                                       surname='Ivanov',
                                       date_of_birth=date(1996, 2, 16),
                                       email="example@example.com",
                                       user=user_1,
                                       )
        coach_2 = Coach.objects.create(name='Ivan',
                                       surname='Petrov',
                                       date_of_birth=date(1996, 3, 16),
                                       email="notexample@example.com",
                                       user=user_1,
                                       )
        self.assertEqual(Coach.objects.all().count(), 2)

    def test_coach_edit(self):
        client = Client()
        user_1 = User.objects.create()

        coach_1 = Coach.objects.create(name='Petr',
                                       surname='Ivanov',
                                       date_of_birth=date(1996, 2, 16),
                                       email="example@example.com",
                                       user=user_1,
                                       )
        coach_1 = Coach.objects.update(name='Ivan',
                                       surname='Petrov',
                                       date_of_birth=date(1996, 3, 16),
                                       email="notexample@example.com",
                                       user=user_1
                                       )
        self.assertEqual(Coach.objects.all().count(), 1)

        response = client.get('/coaches/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "notexample@example.com")

        response = client.get('/coaches/2/')
        self.assertEqual(response.status_code, 404)