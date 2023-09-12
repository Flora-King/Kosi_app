from django.shortcuts import render
from django.views import generic
from .models import Course
from .forms import ReviewForm


class CourseList(generic.ListView):
    model = Course
    queryset = Course.objects.filter(status=1).order_by('-delivery_date')
    template_name = 'index.html'
    paginate_by = 10


class CourseDetail(generic.ListView):

    def get(self, request, slug, *args, **kwargs):
        queryset = Course.objects.filter(status=1)
        course = get_object_or_404(queryset, slug=slug)
        reviews = course.reviews.filter(approved=True).order_by("delivery_date")
        liked = False
        if course.stars.filter(id=self.request.user.id).exists():
            stared = True

        return render(
            request,
            "course_detail.html",
            {
                "course": course,
                "reviews": reviews,
                "stared": stared,
                "Review_form": ReviewForm()
            },
        )
