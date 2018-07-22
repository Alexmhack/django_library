from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

import datetime

from .models import BookInstance

# form using forms.ModelForm
class RenewBookModelForm(ModelForm):
	class Meta:
		model = BookInstance
		fields = ['due_back', ]
		labels = {'due_back': _('Renewal Date')}
		help_texts = {'due_back': 'Enter a date between today and four weeks later (default is 3 weeks)'}

	def clean_due_back(self):
		data = self.cleaned_data['due_back']

		if data < datetime.date.today():
			raise ValidationError(_('Invalid date - renewal in past'))

		if data > datetime.date.today() + datetime.timedelta(weeks=4):
			raise ValidationError(_('Invalid date - date more than 4 weeks ahead'))

		return data

# form using forms.Form
# class RenewBookForm(forms.Form):
# 	renewal_date = forms.DateField(help_text="Enter a date between today and four weeks later (default is 3 weeks).")

# 	def clean_renewal_date(self):
# 		data = self.cleaned_data['renewal_date']

# 		# check if date is in past
# 		if data < datetime.date.today():
# 			raise ValidationError(_('Invalid date - renewal in past'))

# 		# check if date is more than 4 weeks
# 		if data > datetime.date.today() + datetime.timedelta(weeks=4):
# 			raise ValidationError(_('Invalid date - date more than 4 weeks ahead'))

# 		# remember to always return the cleaned data
# 		return data