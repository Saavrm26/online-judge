""" URL Mappings for problems """
from django.urls import path
from problem.views import (
    ModifyProblem,
    CreateProblemView,
    GetProblemListView,
    GetProblemView
)

app_name = 'problem'


urlpatterns = [
    path('', GetProblemListView.as_view(), name='problem_list'),
    path('create', CreateProblemView.as_view(), name='problem_create'),
    path('<int:pk>', GetProblemView.as_view(), name='problem'),
    path('modify/<int:pk>', ModifyProblem.as_view(), name='problem_modify')
]
