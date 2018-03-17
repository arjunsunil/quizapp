from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

User = get_user_model()
class UserLoginForm(forms.Form):
    username =forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)

    def clean(self ,*args , **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username,password=password)
            if not user:
                raise forms.ValidationError("Incorrect username/password")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")
            if not user.is_active:
                raise forms.ValidationError("This user no longer active")
        return super(UserLoginForm,self).clean(*args,**kwargs)

class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label="Email Address")
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model =User
        fields =  [
        'username',
        'email',
        'password',
        ]
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password']:
            self.fields[fieldname].help_text = None
    def clean_email2(self):
        email = self.cleaned_data.get("email")
        if email_qs.exists():
            raise forms.ValidationError("email already exists")
        return email
