from django.db import models
from django.utils.translation import ugettext as _

class Evaluation(models.Model):
 	name = models.CharField(_("name"), max_length=60, null=False, blank=False)
 	email = models.EmailField(_("email"), max_length=60, null=False, blank=False)

 	def __unicode__(self):
 		return u'%s / %s' % (self.name, self.email)
