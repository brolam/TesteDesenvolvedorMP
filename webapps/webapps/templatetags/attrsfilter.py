from django import template
from django.contrib.messages import constants as messages
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='form_group_class')
def  form_group_class(value):
	form_group = 'form-group ' + 'has-error' if value.errors else '' 
	return form_group

@register.filter(name='form_input')
def  form_input(value):	
	return value.as_widget(attrs={'class':'form-control', 'placeholder':value.label , })

@register.filter(name='url_query')
def  url_query(value):	
	return  u'?%s' % (value) if value else '' 

@register.filter(name='form_button_radio')
def form_button_radio(value, item):
	isCheckBoxSelected = (str(value.data) == str(item)) or is_form_button_radio_none( value.data, item )
	checked = 'checked' if isCheckBoxSelected else ''
	cssClass = 'btn btn-primary active' if isCheckBoxSelected else 'btn btn-primary'
	params = {'name': value.name, 'value': str(item), 'checked': checked, 'cssClass': cssClass }
	htmlStr = '<label class="{p[cssClass]}"><input type="radio" id="{p[name]}_{p[value]}" name="{p[name]}" value="{p[value]}" autocomplete="off"  {p[checked]} >{p[value]}</label>'
	return mark_safe(htmlStr.format(p=params))

def is_form_button_radio_none(value, item):
	return ( value == None  and item == 0 )

@register.filter('startswith')
def startswith(text, starts):
    if isinstance(text, basestring):
        return text.startswith(starts)
    return False