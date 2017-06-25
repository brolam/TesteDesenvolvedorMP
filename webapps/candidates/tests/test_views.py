from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test import Client
from candidates.models import Evaluation
from django.core import mail
from django.utils.translation import ugettext as _

class EvaluationViewTest(TestCase):
    def setUp(self):
        self.evaluation_new_url = "/candidates/evaluation/new"
     
    def test_home_request(self):
    	response = self.client.get('/')
    	self.assertEqual(response.status_code, 302)

    def test_new_request(self):
    	response = self.client.get(self.evaluation_new_url)
    	self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'name="name"')
        self.assertContains(response, 'name="email"')
        self.assertContains(response, 'name="skill_tec_html_rating"')
        self.assertContains(response, 'name="skill_tec_css_rating"')
        self.assertContains(response, 'name="skill_tec_javascript_rating"')
        self.assertContains(response, 'name="skill_tec_python_rating"')
        self.assertContains(response, 'name="skill_tec_django_rating"')
        self.assertContains(response, 'name="skill_tec_ios_rating"')
        self.assertContains(response, 'name="skill_tec_android_rating"')

    def test_name_required(self):
        response = self.client.post(self.evaluation_new_url , {'name': ''})
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'name', u'Este campo \xe9 obrigat\xf3rio.')

    def test_email_required(self):
        response = self.client.post(self.evaluation_new_url , {'email': ''})
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'name', u'Este campo \xe9 obrigat\xf3rio.')

    def test_email_invalid(self):
        response = self.client.post(self.evaluation_new_url , {'name': 'CandidateEvaluation', 'email': 'Candidate Evaluation@mp'})
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'email', u'Introduza um endere\xe7o de e-mail v\xe1lido.')

    def check_one_field_skill_tec_rating_negative(self, skill_tec_field_name ):
        response = self.client.post(self.evaluation_new_url , {skill_tec_field_name: -1})
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', skill_tec_field_name, u'Selecione uma op\xe7\xe3o v\xe1lida. -1 n\xe3o se encontra nas op\xe7\xf5es dispon\xedveis.')  

    def check_one_field_skill_tec_rating_greater_than_ten(self, skill_tec_field_name):
        response = self.client.post(self.evaluation_new_url , {skill_tec_field_name: 11})
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', skill_tec_field_name, u'Selecione uma op\xe7\xe3o v\xe1lida. 11 n\xe3o se encontra nas op\xe7\xf5es dispon\xedveis.') 

    def test_all_fields_skill_tec_rating_negative(self):
        for skill_tec_field in Evaluation._meta.get_fields():
            if ( skill_tec_field.name.startswith( 'skill_tec_' ) ):
                self.check_one_field_skill_tec_rating_negative(skill_tec_field.name)

    def test_all_fields_skill_tec_rating_greater_than_ten(self):
        for skill_tec_field in Evaluation._meta.get_fields():
            if ( skill_tec_field.name.startswith( 'skill_tec_' ) ):
                self.check_one_field_skill_tec_rating_greater_than_ten(skill_tec_field.name)

    def test_submit_is_frontEnd_backEnd_and_mobile_developer(self):
        params = { 
            'name': 'One Developer', 
            'email': 'cndidateEvaluation@mp.com',
            'skill_tec_html_rating': 7, 
            'skill_tec_css_rating': 7, 
            'skill_tec_javascript_rating': 7, 
            'skill_tec_python_rating': 7,
            'skill_tec_django_rating': 7, 
            'skill_tec_ios_rating': 7, 
            'skill_tec_android_rating': 7, }
        response = self.client.post(self.evaluation_new_url , params)
        self.assertContains(response, 'your evaluation has been successfully registered!')
        evaluation = candidateEvaluation = Evaluation.objects.get(name="One Developer")
        self.assertEqual(evaluation.name, 'One Developer')
        self.assertEqual(evaluation.email, 'cndidateEvaluation@mp.com')
        self.assertEqual(evaluation.is_development_front_end(), True, 'Must be One Developer Front-End.')
        self.assertEqual(evaluation.is_development_back_end(), True, 'Must be One Developer Back-End.')
        self.assertEqual(evaluation.is_development_mobile(), True, 'Must be One Developer Mobile.')
        self.assertEqual(evaluation.is_development_generic(), False, 'Must not be One Developer Generic.')
        self.assertEqual(len(mail.outbox), 3, 'Three emails should be sent')
        self.assertIn( _("Front-End"), mail.outbox[0].body )
        self.assertIn( _("Back-End"), mail.outbox[1].body )
        self.assertIn( _("Mobile"), mail.outbox[2].body )
        # Empty the test outbox
        mail.outbox = []

    
    def test_submit_is_one_generic_developer(self):
        params = { 
            'name': 'One Developer Generic', 
            'email': 'cndidateEvaluation@mp.com',
            'skill_tec_html_rating': 7, 
            'skill_tec_css_rating': 6, 
            'skill_tec_javascript_rating': 7, 
            'skill_tec_python_rating': 7,
            'skill_tec_django_rating': 6, 
            'skill_tec_ios_rating': 6, 
            'skill_tec_android_rating': 7, }
        response = self.client.post(self.evaluation_new_url , params)
        self.assertContains(response, 'your evaluation has been successfully registered!')
        evaluation = candidateEvaluation = Evaluation.objects.get(name="One Developer Generic")
        self.assertEqual(evaluation.name, 'One Developer Generic')
        self.assertEqual(evaluation.email, 'cndidateEvaluation@mp.com')
        self.assertEqual(evaluation.is_development_front_end(), False, 'Must not be One Developer Front-End.')
        self.assertEqual(evaluation.is_development_back_end(), False, 'Must not be One Developer Back-End.')
        self.assertEqual(evaluation.is_development_mobile(), False, 'Must not be One Developer Mobile.')
        self.assertEqual(evaluation.is_development_generic(), True, 'Must be One Developer Generic.')
        self.assertEqual(len(mail.outbox), 1, 'Should send an email')
        self.assertNotIn( _("Front-End"), mail.outbox[0].body )
        self.assertNotIn( _("Back-End"), mail.outbox[0].body )
        self.assertNotIn( _("Mobile"), mail.outbox[0].body )
        # Empty the test outbox
        mail.outbox = []
  


