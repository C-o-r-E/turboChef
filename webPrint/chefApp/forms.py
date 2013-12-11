from django import forms

class CADForm(forms.Form):
    cadfile = forms.FileField(
        label='Select a file',
        help_text='max. 2 megabytes'
    )
