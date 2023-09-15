from . import views
from django.urls import path


urlpatterns = [
    path('', views.CourseList.as_view(), name='home'),
    # path('search-courses/', views.CourseSearch.as_view(), name='search_courses'),
    path('', views.CourseList.as_view(), name='course_list'),
    path('<slug:slug>/', views.CourseDetail.as_view(), name='course_detail'),
    path('star/<slug:slug>', views.CourseStar.as_view(), name='course_star'),

]
