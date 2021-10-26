from django.forms import ModelForm
from .models import Employee
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class EmployeeForm(ModelForm):
    class Meta:
        model=Employee
        fields="__all__"
class NewUserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ("username", "password1", "password2")
    def save(self,commit=True):
        user=super(NewUserForm,self).save(commit=False)
        if commit:
            user.save()
        return user
