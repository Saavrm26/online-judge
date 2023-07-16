from django.test import TestCase, Client
from problem.models import Problem
from django.contrib.auth import get_user_model
from rest_framework import status
from django.urls import reverse

PROBLEM_CREATE_URL = reverse('problem:problem_create')


def PROBLEM_GET_URL(pk):
    return reverse('problem:problem', kwargs={'pk': pk})


def PROBLEM_MODIFY_URL(pk):
    return reverse('problem:problem_modify', kwargs={'pk': pk})


PROBLEM_LIST_URL = reverse('problem:problem_list')


class ProblemUnauthorizedTests(TestCase):
    def setUp(self):
        """ Creates a new user for testing """
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            name="Test user", email="user@example.com", password="abcde")
        self.client.force_login(user=self.user)

    def test_regular_user_cannot_upload_problem(self):
        """ Test a normal user cannot create a new problem """

        problem = {'name': "sample test", 'statement': "Sample statement",
                   'difficulty': Problem.Difficulty.EASY}
        res = self.client.post(PROBLEM_CREATE_URL, problem)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
# Tests to create: CRUD tests for testcase and tags,
# Tests for the problem ecosystem -- queries,
# Tests for unauthenticated users


class ProblemPrivateTests(TestCase):
    """ Tests for the problem model """

    def setUp(self):
        """ Creates a new user for testing """
        self.client = Client()
        self.staff = get_user_model().objects.create_user(
            email="staff@example.com", password="abcde")
        self.staff.is_staff = True
        self.staff.save()
        self.client.force_login(user=self.staff)

    def test_create_problem(self):
        """ Test staff memebers can create a new problem """
        problem = {
            'name': 'sample test',
            'statement': 'Sample statement',
            'difficulty': 'Easy'
        }
        res = self.client.post(PROBLEM_CREATE_URL, problem)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        for key in problem.keys():
            self.assertEqual(res.data[key], problem[key])

    def test_get_all_problems(self):
        """ Test get all problems """
        problem = {
            'name': 'sample test',
            'statement': 'Sample statement',
            'difficulty': 'Easy'
        }
        self.client.post(PROBLEM_CREATE_URL, problem)
        res = self.client.get(PROBLEM_LIST_URL)
        for key in problem.keys():
            self.assertEqual(res.data[0][key], problem[key])

    def test_update_problem(self):
        """ Test updating a problem """
        problem = Problem.objects.create(name="sample test",
                                         statement="Sample statement",
                                         difficulty=Problem.Difficulty.EASY)

        problem.save()
        pk = problem.pk
        updated_problem = {"name": "updated sample test",
                           "statement": "updated sample statement"}

        self.client.patch(PROBLEM_MODIFY_URL(pk), {'data': updated_problem})

    # def test_delete_problem(self):
