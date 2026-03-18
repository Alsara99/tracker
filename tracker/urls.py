from django.urls import path
from .views import (
    HabitListCreateView,
    HabitRetrieveUpdateDestroyView,
    PublicHabitListView,
)

urlpatterns = [
    path("tracker/", HabitListCreateView.as_view(), name="habit-list-create"),
    path(
        "tracker/<int:pk>/",
        HabitRetrieveUpdateDestroyView.as_view(),
        name="habit-detail",
    ),
    path("tracker/public/", PublicHabitListView.as_view(), name="habit-public"),
]
