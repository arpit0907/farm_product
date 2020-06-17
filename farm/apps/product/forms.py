from django import forms 
from product.models import Product, User, CustomeDetailBill
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
# from bootstrap_datepicker_plus import DatePickerInput


    
class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name','prize','quantity','product_img')


# from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name','last_name', 'email', 'password1', 'password2','address','phone_number','profile_img')
    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        name = User.objects.filter(username=username)
        if name.count():
            raise  ValidationError("Username already exists")
        return username

class CustomerBillForm(forms.ModelForm):

    class Meta:
        model = CustomeDetailBill
        fields = ('__all__')