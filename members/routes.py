"""
Members application API URL configuration
"""

from django.urls import path

from members import resources

urlpatterns = [
    path(
        "members/",
        resources.MemberListCreateAPIView.as_view(),
        name="members-list"
    ),
    path(
        "members/<int:pk>/",
        resources.MemberRetrieveUpdateDestroyAPIView.as_view(),
        name="members-detail"
    ),
    path(
        "teams/",
        resources.TeamListCrateAPIView.as_view(),
        name="teams-list"
    ),
    path(
        "teams/<int:pk>/",
        resources.TeamRetrieveUpdateDestroyAPIView.as_view(),
        name="teams-detail"
    )

]
