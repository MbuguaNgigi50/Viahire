from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import CreateView
from .models import PostCV
from django.contrib.auth.decorators import login_required
from .forms import PostCVForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def jobseeker(request):
    return render(request, 'jobseeker/jobseeker.html', {'title': 'Job Seeker'})

def postCV(request):
    return render(request, 'jobseeker/postCV.html', {'title': 'Post A CV'})

def profile(request):
    return render(request, 'jobseeker/profile.html', {'title': 'My Profile'})

class PostCV(LoginRequiredMixin, CreateView):
    model = PostCV
    fields = ['Username','First_Name', 'Last_Name', 'Current_Job', 'Age', 'Email_Address', 'Telephone_Number', 'Employment_History', 'Education',
    'Skills', 'Hobbies', 'Internships', 'Referress']

def postCV(request):
    if request.method == 'POST':
        form = PostCVForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'CV Posted Successfully!')
            return redirect('viahire-availablejobs')
    else:
        form = PostCVForm()
    return render(request, 'jobseeker/postCV.html', {'form': form})
