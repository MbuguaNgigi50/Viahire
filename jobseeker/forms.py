from django import forms
from django.contrib.auth.models import User
from .models import PostCV

class PostCVForm(forms.ModelForm):

    class Meta:
        model = PostCV
        fields = ['Username','First_Name', 'Last_Name', 'Current_Job', 'Age', 'Email_Address', 'Telephone_Number', 'Employment_History', 'Education',
        'Skills', 'Hobbies', 'Internships', 'Referress']
