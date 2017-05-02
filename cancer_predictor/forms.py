from django import forms
from django.forms import Field
from django.core.validators import MaxValueValidator


class RegistrationForm(forms.Form):

    def validate(self, value):
        if value < 1 and value > 10:
            raise ValidationError(_('%(value)s is not between 1 and 10.'), params={'value': value},)

    f1 = forms.IntegerField(label = 'Clump Thickness' , label_suffix = "", min_value = 1 , max_value = 10, widget=forms.TextInput(attrs={'size': '50'}), required = True)
    f2 = forms.IntegerField(label = 'Uniformity of Cell Size' , label_suffix = "", min_value = 1 , max_value = 10, widget=forms.TextInput(attrs={'size': '50'}), required = True)
    f3 = forms.IntegerField(label = 'Uniformity of Cell Shape' , label_suffix = "", min_value = 1 , max_value = 10, widget=forms.TextInput(attrs={'size': '50'}), required = True)
    f4 = forms.IntegerField(label = 'Marginal Adhesion' , label_suffix = "", min_value = 1 , max_value = 10, widget=forms.TextInput(attrs={'size': '50'}), required = True)
    f5 = forms.IntegerField(label = 'Single Epithelial Cell Size' , label_suffix = "", min_value = 1 , max_value = 10, widget=forms.TextInput(attrs={'size': '50'}), required = True)
    f6 = forms.IntegerField(label = 'Bare Nuclei' , label_suffix = "", min_value = 1 , max_value = 10, widget=forms.TextInput(attrs={'size': '50'}), required = True)
    f7 = forms.IntegerField(label = 'Bland Chromatin' , label_suffix = "", min_value = 1 , max_value = 10, widget=forms.TextInput(attrs={'size': '50'}), required = True)
    f8 = forms.IntegerField(label = 'Normal Nucleoli' , label_suffix = "", min_value = 1 , max_value = 10, widget=forms.TextInput(attrs={'size': '50'}), required = True)
    f9 = forms.IntegerField(label = 'Mitoses' , label_suffix = "", min_value = 1 , max_value = 10, widget=forms.TextInput(attrs={'size': '50'}), required = True)
