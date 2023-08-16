from django.urls import path
from myTools import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.homePageView.as_view(), name="home"),
    path('tools/', views.tool_list),
    path('tools/<int:id>', views.tool_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)
