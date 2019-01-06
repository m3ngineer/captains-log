from django import forms

class DailyForm(forms.Form):

    prompt = forms.CharField(
            widget=forms.TextInput(attrs={
                                        'class': 'form-control input-lg'
                                        })
            )
    response = forms.CharField(
            widget=forms.Textarea(attrs={'placeholder': 'Answer prompt',
                                        'class': 'form-control form-answer'
                                        })
            )
