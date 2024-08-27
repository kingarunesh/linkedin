from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.db.models import Q, Count
from django.contrib.auth.models import User

from dashboard.models import FollowerFollowing, Profile

from explore.forms import SearchForm


@login_required
def explore_view(request):
    
    #NOTE :         top 10 followers
    top_followers = []
    users = User.objects.all()
    
    for user in users:
        total_followers = FollowerFollowing.objects.filter(following=user).count()
        count_followers = {
            "user": user,
            "total_followers": total_followers
        }

        top_followers.append(count_followers)
    
    top_followers = sorted(top_followers, key=lambda item: item['total_followers'], reverse=True)

    context = {
        "top_followers": top_followers
    }

    return render(request=request, template_name="explore/explore.html", context=context)


def search_user_view(request):

    query = request.GET.get("q")

    search_result = User.objects.filter(Q(username__icontains=query) | Q(first_name__icontains=query) | Q(last_name__icontains=query))

    context = {
        "search_result": search_result
    }

    return render(request=request, template_name="explore/user_search.html", context=context)
    

    



# def search(request):
#     if request.method == 'GET':
#         form = LocForm(request.POST)
#         if form.is_valid():
#             search_query = request.GET.get('search_box', None)
#             if search_query:
#                 FirstLoc_list_obj = FirstLoc_List.objects.filter(address__icontains=search_query)
#                 SecondLoc_list_obj= SecondLoc_list.objects.filter(address__icontains=search_query)

# #NOTE :         search
#     search_result = None
#     if request.method == "GET":
#         form = SearchForm(request.POST)

#         if form.is_valid():
#             query = request.GET.get("q", None)

#             if query:
#                 search_result = User.objects.filter(username__icontains=query)

#         print("\n\n\n")
#         print(search_result)
#         print("\n\n\n")
#     else:
#         form = SearchForm()