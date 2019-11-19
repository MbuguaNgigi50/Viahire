from django.shortcuts import render
from employer.models import Post
from jobseeker.models import PostCV
from django.views.generic import ListView

# Create your views here.

def SortView(request):

    qs = PostCV.objects.all()
    Employment_History_contains_query = request.GET.get('Employment_History_contains')
    education_contains_query = request.GET.get('education_contains')
    skills_contains_query = request.GET.get('skills_contains')
    hobbies_contains_query = request.GET.get('hobbies_contains')
    internships_contains_query = request.GET.get('internships_contains')
    referees_contains_query = request.GET.get('referees_contains')

    if Employment_History_contains_query != '' and Employment_History_contains_query is not None:
        qs = qs.filter(Employment_History__icontains = Employment_History_contains_query)

    elif education_contains_query != '' and education_contains_query is not None:
        qs = qs.filter(Education__icontains = employment_history_contains_query)

    elif skills_contains_query != '' and skills_contains_query is not None:
        qs = qs.filter(Skills__icontains = employment_history_contains_query)

    elif hobbies_contains_query != '' and hobbies_contains_query is not None:
        qs = qs.filter(Hobbies__icontains = hobbies_contains_query)

    elif internships_contains_query != '' and internships_contains_query is not None:
        qs = qs.filter(Internships__icontains = internships_contains_query)

    elif referees_contains_query != '' and referees_contains_query is not None:
        qs = qs.filter(Referees__icontains = referees_contains_query)

        return qs

    content = {
        "list":qs
    }

    return render(request, 'search/sorting.html', content)
