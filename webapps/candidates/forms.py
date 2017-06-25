from django.forms import ModelForm
from candidates.models import Evaluation

class EvaluationForm(ModelForm):
	class Meta:
		model = Evaluation
		fields = [
		 'id',
		 'name', 
		 'email',
		 'skill_tec_html_rating', 
		 'skill_tec_css_rating', 
		 'skill_tec_javascript_rating', 
		 'skill_tec_python_rating', 
		 'skill_tec_django_rating', 
		 'skill_tec_ios_rating', 
		 'skill_tec_android_rating' 
		 ]