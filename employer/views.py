from django.shortcuts import render, get_object_or_404
from .models import Post
from jobseeker.models import PostCV
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.conf import settings

# Create your views here.

def postJOB(request):
    return render(request, 'employer/postJOB.html', {'title': 'Post A Job'})

def availablejobs(request):
    return render(request, 'employer/availablejobs.html', {'title': 'Available Jobs'})

    content = {
        'posts': Post.objects.all()
    }
    return render(request, 'employer/availablejobs.html', content)

def applicant_view(request):
    return render(request, 'employer/applicants.html', {'title': 'All Applicants'})

    context = {
        'applicants':PostCV.objects.all()
    }
    return render(request, 'employer/applicants.html', context, {'title': 'All Applicants'})

class ApplicantsView(ListView):
    model = PostCV
    template_name = 'employer/applicants.html'
    context_object_name = 'applicants'
    paginate_by = 5

class ApplicantsDetailView(DetailView) :
    model = PostCV
    template_name = 'employer/applicant_detail.html'

class SearchView(ListView):
    model = PostCV
    template_name = 'employer/sort.html'

class PostListViews(ListView):
    model = Post
    template_name = 'employer/availablejobs.html'
    context_object_name = 'posts'
    paginate_by = 5

class UserPostListViews(ListView):
    model = Post
    template_name = 'employer/user_jobs.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username= self.kwargs.get('username'))
        return Post.objects.filter(Employer=user).order_by('-Job_Date')

class PostDetailViews(DetailView):
    model = Post

class PostCreateViews(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['Job_Name', 'Job_Description', 'Job_Requirements', 'Job_Qualifications']

    def form_valid(self, form):
        form.instance.Employer= self.request.user
        return super().form_valid(form)

class PostUpdateViews(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['Job_Name', 'Job_Description', 'Job_Requirements', 'Job_Qualifications']

    def form_valid(self, form):
        form.instance.Employer= self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.Employer:
            return True
        return False

class PostDeleteViews(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.Employer:
            return True
        return False
