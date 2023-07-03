from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    attach = forms.FileField(widget=forms.ClearableFileInput(attrs={"allow_multiple_selected": True}), required=False)
    message = forms.CharField(widget = forms.Textarea )


class dialog_forms(forms.Form):
    # Define the form fields here
    field1 = forms.CharField(label='Field 1', max_length=100)
    field2 = forms.IntegerField(label='Field 2')
    # Add other fields as needed

    