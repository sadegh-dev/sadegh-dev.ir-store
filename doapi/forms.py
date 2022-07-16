from django import forms


class UserApiForm(forms.Form):
    username = forms.CharField(
        max_length=254 ,
        required= True,
        label = 'ایمیل',
        widget= forms.EmailInput(attrs={
            'class':'form-control bg-light',
            'placeholder' : 'your-email@email.com' ,
        }))
    password = forms.CharField(
        max_length=20 ,
        required= True,
        label = 'رمز عبور',
        widget= forms.PasswordInput(attrs={
            'class':'form-control bg-light',
        }))
