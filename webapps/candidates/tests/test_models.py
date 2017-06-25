from django.test import TestCase
from candidates.models import Evaluation 
from django.core.exceptions import ValidationError

class EvaluationModelTest(TestCase):
    def setUp(self):
        self.evaluation = Evaluation(name="CandidateEvaluation", email="candidateEvaluation@mp.com")

    def test_create_one_evaluation(self):
        self.evaluation.save()
        candidateEvaluation = Evaluation.objects.get(name="CandidateEvaluation")
        self.assertEqual(candidateEvaluation.name, 'CandidateEvaluation')
        self.assertEqual(candidateEvaluation.email, 'candidateEvaluation@mp.com')

    def test_name_is_required(self):
        self.evaluation.name = "";
        try:
            self.evaluation.clean_fields()
        except ValidationError:
            return
        self.fail('Field Name must be required!')

    def test_email_is_required(self):
        self.evaluation.email = "";
        try:
            self.evaluation.clean_fields()
        except ValidationError:
            return
        self.fail('Field Email must be required!')

    def check_one_field_skill_tec_rating_negative(self, skill_tec_field_name):
        setattr(self.evaluation, skill_tec_field_name, -1)
        try:
            self.evaluation.clean_fields()
            setattr(self.evaluation, skill_tec_field_name, 0)
        except ValidationError:
            return
        self.fail('Field "{p[field]}" can not be Negative!'.format(p={'field': skill_tec_field_name }))

    def check_one_field_skill_tec_rating_greater_than_ten(self, skill_tec_field_name):
        setattr(self.evaluation, skill_tec_field_name, 11)
        try:
            self.evaluation.clean_fields()
            setattr(self.evaluation, skill_tec_field_name, 0)
        except ValidationError:
            return
        self.fail('Field "{p[field]}" can not be greater than ten!'.format(p={'field': skill_tec_field_name }))

    def test_all_fields_skill_tec_rating_negative(self):
        for skill_tec_field in self.evaluation._meta.get_fields():
            if ( skill_tec_field.name.startswith( 'skill_tec_' ) ):
                self.check_one_field_skill_tec_rating_negative(skill_tec_field.name)

    def test_all_fields_skill_tec_rating_greater_than_ten(self):
         for skill_tec_field in self.evaluation._meta.get_fields():
            if ( skill_tec_field.name.startswith( 'skill_tec_' ) ):
                self.check_one_field_skill_tec_rating_greater_than_ten(skill_tec_field.name)

    def test_is_or_not_developer_front_end(self):
        for rating in range(7, 11):
            msg_rating = ' On rating: %s.' %(rating)
            self.evaluation.skill_tec_html_rating = rating
            self.evaluation.skill_tec_css_rating  = rating
            self.evaluation.skill_tec_javascript_rating = rating
            self.assertEqual(self.evaluation.is_developer_front_end(), True, msg_rating)
            self.evaluation.skill_tec_javascript_rating = 6
            self.assertEqual(self.evaluation.is_developer_front_end(), False, msg_rating)
            self.evaluation.skill_tec_javascript_rating = rating
            self.assertEqual(self.evaluation.is_developer_front_end(), True, msg_rating)
            self.evaluation.skill_tec_css_rating  = 6
            self.assertEqual(self.evaluation.is_developer_front_end(), False, msg_rating)
            self.evaluation.skill_tec_css_rating  = rating
            self.assertEqual(self.evaluation.is_developer_front_end(), True, msg_rating)
            self.evaluation.skill_tec_html_rating = 6
            self.assertEqual(self.evaluation.is_developer_front_end(), False, msg_rating)
            self.evaluation.skill_tec_html_rating = rating
            self.assertEqual(self.evaluation.is_developer_front_end(), True, msg_rating)

    def test_is_or_not_developer_back_end(self):
        for rating in range(7, 11):
            msg_rating = ' On rating: %s.' %(rating)
            self.evaluation.skill_tec_python_rating = rating
            self.evaluation.skill_tec_django_rating  = rating
            self.assertEqual(self.evaluation.is_developer_back_end(), True)
            self.evaluation.skill_tec_django_rating  = 6
            self.assertEqual(self.evaluation.is_developer_back_end(), False)
            self.evaluation.skill_tec_django_rating  = rating
            self.assertEqual(self.evaluation.is_developer_back_end(), True)
            self.evaluation.skill_tec_python_rating = 6 
            self.assertEqual(self.evaluation.is_developer_back_end(), False)
            self.evaluation.skill_tec_python_rating = rating
            self.assertEqual(self.evaluation.is_developer_back_end(), True)

    def test_is_or_not_developer_mobile(self):
        for rating in range(7, 11):
            msg_rating = ' On rating: %s.' %(rating)
            self.evaluation.skill_tec_ios_rating = rating
            self.evaluation.skill_tec_android_rating  = rating
            self.assertEqual(self.evaluation.is_developer_mobile(), True, msg_rating)
            self.evaluation.skill_tec_android_rating  = 6
            self.assertEqual(self.evaluation.is_developer_mobile(), False, msg_rating)
            self.evaluation.skill_tec_android_rating = rating
            self.assertEqual(self.evaluation.is_developer_mobile(), True, msg_rating)
            self.evaluation.skill_tec_ios_rating = 6
            self.assertEqual(self.evaluation.is_developer_mobile(), False, msg_rating)
            self.evaluation.skill_tec_ios_rating = rating
            self.assertEqual(self.evaluation.is_developer_mobile(), True, msg_rating)

    def test_is_or_not_developer_generic(self):
        for rating in range(7, 11):
            msg_rating = ' On rating: %s.' %(rating)
            self.evaluation.skill_tec_html_rating = 6 
            self.evaluation.skill_tec_css_rating  = 6
            self.evaluation.skill_tec_javascript_rating = 6
            self.evaluation.skill_tec_python_rating = 6
            self.evaluation.skill_tec_django_rating  = 6
            self.evaluation.skill_tec_ios_rating = 6 
            self.evaluation.skill_tec_android_rating  = 6
            self.assertEqual(self.evaluation.is_developer_generic(), True, msg_rating)
            self.evaluation.skill_tec_html_rating = rating 
            self.evaluation.skill_tec_css_rating  = rating
            self.evaluation.skill_tec_javascript_rating = rating
            self.evaluation.skill_tec_python_rating = rating
            self.evaluation.skill_tec_django_rating  = rating
            self.evaluation.skill_tec_ios_rating = rating
            self.evaluation.skill_tec_android_rating  = rating
            self.assertEqual(self.evaluation.is_developer_generic(), False, msg_rating)
 

