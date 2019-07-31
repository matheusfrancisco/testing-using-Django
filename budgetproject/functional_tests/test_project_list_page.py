from selenium import webdriver
from budget.models import Project
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time


class TestProjectListPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser= webdriver.Chrome('functional_tests/chromedriver.exe')
    
    def tearDown(self):
        self.browser.close()
    
    def test_no_projects_alert_is_displayed(self):
        self.browser.get(self.live_server_url)
        #time.sleep(5)
        # The user request the page for the firs time

        alert = self.browser.find_element_by_class_name('noproject-wrapper')
        self.assertEquals(
            alert.find_element_by_tag_name('h3').text,
            'Sorry, you don\'t have any projects, yet.'
        )
    
    def test_no_projects_alert_button_redirects_to_add_page(self):
        self.browser.get(self.live_server_url)
        add_url = self.live_server_url + reverse(add)
        # The user requests the page for the first time
        self.browser.find_element_by_tag_name('a').click()
        self.assertEquals(
            self.browser.current_url,
            add_url
        )

    def test_user_sees_project_list(self):
        project1 = Project.objects.create(
            name='project1',
            budget=10000
        )
        self.browser.get(self.live_server_url)


        #The users sees the project on the screen
        self.assertEquals(
            self.browser.find_element_by_tag_name('h5').text,
            'project1'
        )
    
    def test_user_is_redirected_to_project_detail(self):
        project1 = Project.objects.create(
            name='project1',
            budget=1000
        )

        self.browser.get(self.live_server_url)

        #the user sees the project on the screen. He clicks the Visit link
        #and is redirect to the detail page

        detail_url = self.live_server_url + reverse('detail', args=[project1.slug])
        self.browser.find_element_by_link_text('VISIT').click()
        self.assertEquals(
            self.browser.current_url,
            detail_url
        )