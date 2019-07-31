from django.test import SimpleTestCase
from budget.forms import ExpenseForm

class TestForms(SimpleTestCase):

  def test_expense_form_valid_data(self):
    form = ExpenseForm(date={
      'title': 'expense1',
      'amount': 1000,
      'category': 'development'
    })

    self.assertTrue(forms.is_valid())

  
  def test_expense_form_no_data(self):
    form = ExpenseForm(data={})

    self.assertFalse(form.is_valid())
    self.assertEquals(len(form.erros), 3)

    
