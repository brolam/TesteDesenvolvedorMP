from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

class EvaluationAcceptanceTest(StaticLiveServerTestCase):
    evaluation_new_url = "/candidates/evaluation/new"

    @classmethod
    def setUpClass(cls):
        super(EvaluationAcceptanceTest, cls).setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(20)
        
    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(EvaluationAcceptanceTest, cls).tearDownClass()

    def test_submit_front_end_developer(self):
        self.selenium.get('%s%s' % (self.live_server_url, self.evaluation_new_url))
        name_input = self.selenium.find_element_by_name("name")
        name_input.send_keys('One Developer Front-End')
        email_input = self.selenium.find_element_by_name("email")
        email_input.send_keys('candidateEvaluation@mp.com')
        self.selenium.find_element_by_id("skill_tec_html_rating_7").click()
        self.selenium.find_element_by_id("skill_tec_css_rating_7").click()
        self.selenium.find_element_by_id("skill_tec_javascript_rating_7").click()
        self.selenium.find_element_by_id("button_submit").click()

    def test_submit_back_end_developer(self):
        self.selenium.get('%s%s' % (self.live_server_url, self.evaluation_new_url))
        name_input = self.selenium.find_element_by_name("name")
        name_input.send_keys('One Developer Back-End')
        email_input = self.selenium.find_element_by_name("email")
        email_input.send_keys('candidateEvaluation@mp.com')
        self.selenium.find_element_by_id("skill_tec_python_rating_7").click()
        self.selenium.find_element_by_id("skill_tec_django_rating_7").click()
 
    def test_submit_mobile_developer(self):
        self.selenium.get('%s%s' % (self.live_server_url, self.evaluation_new_url))
        name_input = self.selenium.find_element_by_name("name")
        name_input.send_keys('One Developer Mobile')
        email_input = self.selenium.find_element_by_name("email")
        email_input.send_keys('candidateEvaluation@mp.com')
        self.selenium.find_element_by_id("skill_tec_ios_rating_7").click()
        self.selenium.find_element_by_id("skill_tec_android_rating_7").click()
        self.selenium.find_element_by_id("button_submit").click()

    def test_submit_generic_developer(self):
        self.selenium.get('%s%s' % (self.live_server_url, self.evaluation_new_url))
        name_input = self.selenium.find_element_by_name("name")
        name_input.send_keys('One Developer Generic')
        email_input = self.selenium.find_element_by_name("email")
        email_input.send_keys('candidateEvaluation@mp.com')
        self.selenium.find_element_by_id("skill_tec_html_rating_7").click()
        self.selenium.find_element_by_id("skill_tec_css_rating_6").click()
        self.selenium.find_element_by_id("skill_tec_javascript_rating_7").click()
        self.selenium.find_element_by_id("skill_tec_python_rating_6").click()
        self.selenium.find_element_by_id("skill_tec_django_rating_7").click()
        self.selenium.find_element_by_id("skill_tec_ios_rating_6").click()
        self.selenium.find_element_by_id("skill_tec_android_rating_7").click()
        self.selenium.find_element_by_id("button_submit").click()



