from django.forms import ModelForm
from candidates.models import Evaluation
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from webapps import settings
from django.utils.translation import ugettext as _

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

	def send_all_emails_with_evaluation(self):
		if self.instance.is_developer_front_end(): self.send_one_email_with_evaluation(_("Front-End"))
		if self.instance.is_developer_back_end(): self.send_one_email_with_evaluation(_("Back-End")) 
		if self.instance.is_developer_mobile(): self.send_one_email_with_evaluation(_("Mobile")) 
		if self.instance.is_developer_generic(): self.send_one_email_with_evaluation("")

	def send_one_email_with_evaluation(self, developer_title):
		from_email = settings.ADMINS[0][1]
		to_email = self.instance.email
		subject = _("Thank you for applying")
		parames = { 'name': self.instance.name , 'developer_title': developer_title}
		html_content = render_to_string('evaluation/email.html', parames)
		text_content = strip_tags(html_content)
		msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
		msg.attach_alternative(html_content, "text/html")
		msg.send()