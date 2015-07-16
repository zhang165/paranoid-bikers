from django.test import TestCase
from parkingApp.models import Placemark

# selenium imports
from django.test import LiveServerTestCase
from django.contrib.auth.models import User
from selenium import webdriver


class PlacemarkTestCase(TestCase):

	def setUp(self):
		Placemark.objects.create(placemark_id="1234", name="metered_parking", credit_card="no", location="smith street", intersection="yes", time="3 hours", link="yes", lat="40.12345678", lon="06.0123456")
		Placemark.objects.create(placemark_id="5678", name="metered_parking", credit_card="no", location="10th street", intersection="no", time="4 hours", link="yes", lat="40.567890", lon="06.123456")
		Placemark.objects.create(placemark_id="1122", name="non_metered_parking", credit_card="no", location="Joffre Ave", intersection="yes", time="no time",link="yes", lat="50.1234567", lon="06.1234567")
	
	def test_retrieve(self):
		test1 = Placemark.objects.get(placemark_id="1234")
		test2 = Placemark.objects.get(placemark_id="1122")
		self.assertEqual(test1.name, 'metered_parking')
		self.assertEqual(test2.name, 'non_metered_parking')


class AdminTestCase(LiverServerTestCase):
    def setUp(self):
        # setUp is where you instantiate the selenium webdriver and loads the browser.
        User.objects.create_superuser(
            username='admin',
            password='admin',
            email='admin@example.com'
        )
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        super(AdminTestCase, self).setUp()
            
    def tearDown(self):
        # Call tearDown to close the web browser
        self.selenium.quit()
        super(AdminTestCase, self).tearDown()
            
    def test_create_user(self):
        """
        Django admin create user test
        This test will create a user in django admin and assert that
        page is redirected to the new user change form.
        """
        # Open the django admin page.
        # DjangoLiveServerTestCase provides a live server url attribute
        # to access the base url in tests
        self.selenium.get(
            '%s%s' % (self.live_server_url,  "/admin/")
        )
        # Fill login information of admin
        username = self.selenium.find_element_by_id("id_username")
        username.send_keys("admin")
        password = self.selenium.find_element_by_id("id_password")
        password.send_keys("admin")
        # Locate Login button and click it
        self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()
        self.selenium.get(
            '%s%s' % (self.live_server_url, "/admin/auth/user/add/"))
        # Fill the create user form with username and password
        self.selenium.find_element_by_id("id_username").send_keys("test")
        self.selenium.find_element_by_id("id_password1").send_keys("test")
        self.selenium.find_element_by_id("id_password2").send_keys("test")
        # Forms can be submitted directly by calling its method submit
        self.selenium.find_element_by_id("user_form").submit()
        self.assertIn("Change user", self.selenium.title)

