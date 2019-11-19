from django.urls import path
from .views import (PostListViews, PostDetailViews, PostCreateViews, PostUpdateViews, PostDeleteViews, UserPostListViews, ApplicantsView, ApplicantsDetailView
                    )
from . import views

urlpatterns = [
    path('postjob/', views.postJOB, name = 'viahire-postJOB'),
    path('post/<int:pk>/', PostDetailViews.as_view(),name = 'post_detail' ),
    path('post/<int:pk>/update/', PostUpdateViews.as_view(),name = 'post_update' ),
    path('post/<int:pk>/delete/', PostDeleteViews.as_view(),name = 'post_delete' ),
    path('post/new/', PostCreateViews.as_view(),name = 'viahire-postJOB' ),
    path('availablejobs/', PostListViews.as_view(), name = 'viahire-availablejobs'),
    path('user/<str:username>/', UserPostListViews.as_view(), name = 'viahire-userjobs'),
    path('applicants/', ApplicantsView.as_view(), name = 'viahire-applicants'),
    path('job-post/applicant_detail/<int:pk>/', ApplicantsDetailView.as_view(), name = 'applicant_detail'),
]
