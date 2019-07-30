from django.test import TestCase, Client
from django.urls import reverse
from budget.models import Project, Category, Expense
import json


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.list_url = reverse('list')
        self.detail_url = reverse('detail', args=['project1'])
        Project.objects.create(
                name='project1',
                budget=10000)

    def test_project_list_GET(self):
        response = self.client.get(reverse(self.list_url))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'budget/project-list.html')

    def test_project_detail_GET(self):
        response = self.client.get(self.detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'budget/project-detail.html')


    def test_projetc_detail_POST_adds_new_expense(self):
        Category.objects.create(
                project=self.project1,
                name='development'
                )

        response = self.client.post(self.detail_url, {
                'title': 'expense1',
                'amount': 1000,
                'category':'development'
                })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.project1.expense.first().title, 'expense1')




