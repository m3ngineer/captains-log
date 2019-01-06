from django import forms

class DailyForm(forms.Form):
    prompt = forms.CharField(
            widget=forms.TextInput(attrs={'placeholder': 'Prompt text',
                                        'class': 'form-control input-lg'
                                        })
            )
    response = forms.CharField(
            widget=forms.TextInput(attrs={'placeholder': 'Answer prompt',
                                        'class': 'form-control input-lg'
                                        })
            )
