"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from candidates.models import Evaluation 
from django.core.exceptions import ValidationError

class CandidateEvaluationModelTest(TestCase):

    def test_create_one_evaluation(self):
        evaluation = Evaluation(name="CandidateEvaluation", email="candidateEvaluation@mp.com")
        evaluation.save()
        candidateEvaluation = Evaluation.objects.get(name="CandidateEvaluation")
        self.assertEqual(candidateEvaluation.name, 'CandidateEvaluation')
        self.assertEqual(candidateEvaluation.email, 'candidateEvaluation@mp.com')

    def test_evaluation_name_is_required(self):
        evaluation = Evaluation(email="candidateEvaluation@mp.com")
        try:
            evaluation.clean_fields()
        except ValidationError:
            return
        self.fail('Field Name must be required!')

    def test_evaluation_email_is_required(self):
        evaluation = Evaluation(name="CandidateEvaluation")
        try:
            evaluation.clean_fields()
        except ValidationError:
            return
        self.fail('Field Email must be required!')
   