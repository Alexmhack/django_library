from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime


class RenewBookForm(forms.Form):
	renewal_date = forms.DateField("Enter a date between today and four weeks later (default is 3 weeks).")

	def clean_renewal_date(self):
		data = self.cleaned_data['renewal_date']

		# check if date is in past
		if data < datetime.datetime.today():
			raise ValidationError(_('Invalid date - renewal in past'))

		# check if date is more than 4 weeks
		if data > datetime.date.today() + datetime.timedelta(weeks=4):
			raise ValidationError(_('Invalid date - date more than 4 weeks ahead'))

		# remember to always return the cleaned data
		return data