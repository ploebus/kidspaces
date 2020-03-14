from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Trees
from django import forms

STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
)

class TreeForm(forms.ModelForm):
    
    class Meta:
        model = Trees
        fields = ("__all__")
        widgets = {'lat': forms.HiddenInput(),'lng':forms.HiddenInput()}
    
    def __init__(self, *args, **kwargs):
        super(TreeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'tree_form'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'home'

        self.helper.add_input(Submit('submit', 'Save Tree'))