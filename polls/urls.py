from django.urls import path
from polls.views import  results, vote
from polls.views import IndexView, DetailView
# , , ResultsView, vote



app_name = "polls"
urlpatterns = [
    # path("", index, name="index"),
    path("", IndexView.as_view(), name="index"),
    # path("specifics/<int:question_id>/", detail, name="detail"),
    path("<int:pk>/", DetailView.as_view(), name="detail"),
    path("<int:question_id>/vote/", vote, name="vote"),
    path("<int:question_id>/results/", results, name="results"),
]

# app_name = "polls"
# urlpatterns = [

#    
#     path("<int:pk>/results/", ResultsView.as_view(), name="results"),
#     path("<int:question_id>/vote/", vote, name="vote"),
# ]
