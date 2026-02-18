from django.urls import path
from .views import HabitListCreateView, HabitRetrieveUpdateDestroyView

urlpatterns = [
    path("tracker/", HabitListCreateView.as_view(), name="habit-list-create"),
    path(
        "tracker/<int:pk>/",
        HabitRetrieveUpdateDestroyView.as_view(),
        name="habit-retrieve-update-destroy",
    ),
]
