from django.test import TestCase
from candidates.models import Evaluation 
from django.core.exceptions import ValidationError

class CandidateEvaluationModelTest(TestCase):
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

    def test_all_field_skill_tec_rating_greater_than_ten(self):
         for skill_tec_field in self.evaluation._meta.get_fields():
            if ( skill_tec_field.name.startswith( 'skill_tec_' ) ):
                self.check_one_field_skill_tec_rating_greater_than_ten(skill_tec_field.name)
