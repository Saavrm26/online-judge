from django.test import TestCase, Client
from problem.models import Problem
from django.contrib.auth import get_user_model
from rest_framework import status
from django.urls import reverse

PROBLEM_URL = reverse('problem')


class ProblemUnauthorizedTests(TestCase):
    def setUp(self):
        """ Creates a new user for testing """
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            name="Test user", email="user@example.com", password="abcde")
        self.client.force_login(user=self.user)

    def test_regular_user_cannot_upload_problem(self):
        problem = Problem(name="sample test", statement="Sample statement",
                          difficulty=Problem.Difficulty.EASY)
        self.client.post(PROBLEM_URL, problem)

# Tests to create: CRUD tests for testcase and tags, Tests for the problem ecosystem -- queries, Tests for unauthenticated users


class ProblemPrivateTests(TestCase):
    """ Tests for the problem model """

    def setUp(self):
        """ Creates a new user for testing """
        self.client = Client()
        self.staff = get_user_model().objects.create_user(
            email="staff@example.com", password="abcde")
        self.staff.is_staff = True
        self.staff.save()

    def test_create_problem(self):
        problem = {'name': "sample test", "statement": "Sample statement",
                   "difficulty": Problem.Difficulty.EASY}
        res = self.client.post(PROBLEM_URL, problem)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(problem, res.data)

    def test_update_problem(self):
        """ Test updating a problem """
        problem = Problem.objects.create(
            name="sample test", statement="Sample statement", difficulty=Problem.Difficulty.EASY)
        problem.save()
        pk = problem.pk

        updated_problem = {"name": "updated sample test",
                           "statement": "updated sample statement"}
        self.client.patch(PROBLEM_URL, {'pk': pk, 'data': updated_problem})

    # def test_delete_problem(self):
