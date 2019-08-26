from django import forms

from .models import Address


class AddressForm(forms.ModelForm):
    """
    User-related CRUD form
    """
    name = forms.CharField(label='Name', required=False, widget=forms.TextInput(attrs={"class": 'form-control' , "placeholder": "Your full name"}))
    address_type = forms.CharField(label='Address type', required=False, widget=forms.TextInput(attrs={"class": 'form-control' , "placeholder": "Home/Business Address"}))
    address_line_1 = forms.CharField(label='Address line 1', required=False, widget=forms.TextInput(attrs={"class": 'form-control' , "placeholder": "Address"}))
    address_line_2 = forms.CharField(label='Address line 2', required=False, widget=forms.TextInput(attrs={"class": 'form-control' , "placeholder": "Aparment Number/Floor Number"}))
    city = forms.CharField(label='City', required=False, widget=forms.TextInput(attrs={"class": 'form-control' , "placeholder": "City"}))
    country = forms.CharField(label='Country', required=False, widget=forms.TextInput(attrs={"class": 'form-control' , "placeholder": "Country"}))
    state = forms.CharField(label='State', required=False, widget=forms.TextInput(attrs={"class": 'form-control' , "placeholder": "State"}))
    postal_code = forms.IntegerField(label='Postal code', required=False, widget=forms.TextInput(attrs={"class": 'form-control' , "placeholder": "Postal code"}))
    class Meta:
        model = Address
        fields = [
            'name',
            #'billing_profile',
            'address_type',
            'address_line_1',
            'address_line_2',
            'city',
            'country',
            'state',
            'postal_code'
        ]




class AddressCheckoutForm(forms.ModelForm):
    """
    User-related checkout address create form
    """
    name = forms.CharField(label='Name', required=False, widget=forms.TextInput(attrs={"class": 'form-control' , "placeholder": "Your full name"}))
    address_line_1 = forms.CharField(label='Address line 1', required=False, widget=forms.TextInput(attrs={"class": 'form-control' , "placeholder": "Address"}))
    address_line_2 = forms.CharField(label='Address line 2', required=False, widget=forms.TextInput(attrs={"class": 'form-control' , "placeholder": "Aparment Number/Floor Number"}))
    city = forms.CharField(label='City', required=False, widget=forms.TextInput(attrs={"class": 'form-control' , "placeholder": "City"}))
    country = forms.CharField(label='Country', required=False, widget=forms.TextInput(attrs={"class": 'form-control' , "placeholder": "Country"}))
    state = forms.CharField(label='State', required=False, widget=forms.TextInput(attrs={"class": 'form-control' , "placeholder": "State"}))
    postal_code = forms.IntegerField(label='Postal code', required=False, widget=forms.TextInput(attrs={"class": 'form-control' , "placeholder": "Postal code"}))


    class Meta:
        model = Address
        fields = [
            'name',
            #'billing_profile',
            #'address_type',
            'address_line_1',
            'address_line_2',
            'city',
            'country',
            'state',
            'postal_code'
        ]

