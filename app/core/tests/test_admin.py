""" Tests for the Django admin modifications """

from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from problem.models import Problem


class AdminSiteTests(TestCase):
    """ Tests for django admin """

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@example.com", password="sample123")
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='samplepass123',
            name='Test User'
        )

    def test_users_list(self):
        """ Test that users are listed """
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_edit_user_page(self):
        """ Test the edit user page works """
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """ Test the create user page works """
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)


class AdminSiteProblemTests(TestCase):
    """ Tests for problems model in django admin """

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@example.com", password="sample123")
        self.client.force_login(self.admin_user)
        self.problem = Problem.objects.create(
            name="Problem 1", statement="XYZ", difficulty=Problem.Difficulty.EASY)

    def test_problems_list(self):
        """ Test that problems are listed """
        url = reverse('admin:problem_problem_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.problem.name)
        self.assertContains(res, self.problem.difficulty)

    def test_edit_user_page(self):
        """ Test the edit problem page works """
        url = reverse('admin:problem_problem_change', args=[self.problem.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """ Test the create user page works """
        url = reverse('admin:problem_problem_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
