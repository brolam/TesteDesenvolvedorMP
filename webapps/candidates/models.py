from django.db import models
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError

SKILL_TECHNOLOGY_RATING_CHOICES = [(0,0), (1,1), (2,2), (3,3), (4,4) ,(5,5) ,(6,6), (7,7) , (8,8), (9,9), (10,10)]

class SkillTecRatingField(models.IntegerField):
		def validate_skill_tec_rating(self, value):
			if ( value, value ) in SKILL_TECHNOLOGY_RATING_CHOICES :  return
			raise ValidationError(_('This skill rating should be between 1 and 10.'))

		def __init__(self, *args, **kwargs):
			kwargs['choices'] = SKILL_TECHNOLOGY_RATING_CHOICES
			kwargs['blank']=True 
			kwargs['default']=0
			kwargs['validators']=[self.validate_skill_tec_rating]
			super(models.IntegerField, self).__init__(*args, **kwargs)

class Evaluation(models.Model):
 	name = models.CharField(_("name"), max_length=60, null=False, blank=False)
 	email = models.EmailField(_("email"), max_length=60, null=False, blank=False)
 	skill_tec_html_rating = SkillTecRatingField( _("HTML") )
 	skill_tec_css_rating = SkillTecRatingField( _("CSS"))
	skill_tec_javascript_rating = SkillTecRatingField( _("Javascript") )
	skill_tec_python_rating = SkillTecRatingField( _("Python") )
	skill_tec_django_rating = SkillTecRatingField( _("Django") )
	skill_tec_ios_rating = SkillTecRatingField( _("Developer iOS") )
	skill_tec_android_rating = SkillTecRatingField( _("Developer Android") )

	def is_developer_front_end(self):
		return (
			7 <= self.skill_tec_html_rating <= 10 and 
			7 <= self.skill_tec_css_rating <= 10 and
			7 <= self.skill_tec_javascript_rating <= 10
		)

	def is_developer_back_end(self):
		return (
			7 <= self.skill_tec_python_rating <= 10 and 
			7 <= self.skill_tec_django_rating <= 10
		)

	def is_developer_mobile(self):
		return (
			7 <= self.skill_tec_ios_rating <= 10 and 
			7 <= self.skill_tec_android_rating <= 10
		)

	def is_developer_generic(self):
		return (
			not self.is_developer_front_end() and 
			not self.is_developer_back_end() and 
			not self.is_developer_mobile() 
		)

 	def __unicode__(self):
 		return u'%s / %s' % (self.name, self.email)
