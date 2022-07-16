from django import forms

class CartAddForm(forms.Form) :
    number = forms.IntegerField(
        min_value=1, 
        initial='1', 
        max_value=9, 
        label='تعداد', 
        widget= forms.NumberInput(attrs={
            'class':'form-control mx-auto bg-light text-center w-25 ',
        })) 