from . import views
from django.urls import path


urlpatterns = [
    path('', views.CourseList.as_view(), name='home'),
    path('<slug:slug>/', views.course_detail, name='course_detail'),
    # path('star/<slug:slug>', views.course_star, name='course_star'),
    path('<slug:slug>/delete_review/<int:review_id>', views.review_delete, name='review_delete'),
    path('<slug:slug>/edit_review/<int:review_id>', views.review_edit, name='review_edit')
]
