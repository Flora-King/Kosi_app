from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Course
from .forms import ReviewForm
from django.views.generic import ListView, DetailView
from django.db.models import Q


# class CourseSearch(ListView):
#     model = Course
#     queryset = Course.objects.all()

#     def get_queryset(self, slug, *args, **kwargs):
#         q = request.GET.get('q')

#         if q:
#             courses = Course.objects.filter(title__search=q)

#         else:
#             courses = None

#         context = {'courses': courses}
#         return render(request, 'base.html', context)


class CourseList(generic.ListView):
    model = Course
    queryset = Course.objects.filter(status=1).order_by('-delivery_from')
    template_name = 'index.html'
    paginate_by = 9


class CourseDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Course.objects.filter(status=1)
        course = get_object_or_404(queryset, slug=slug)
        reviews = course.reviews.filter(approved=True).order_by("created_on")
        stars = False
        if course.stars.filter(id=self.request.user.id).exists():
            stars = True

        return render(
            request,
            "course_detail.html",
            {
                "course": course,
                # "slug": slug,
                "reviews": reviews,
                "commented": False,
                "stars": stars,
                "review_form": ReviewForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Course.objects.filter(status=1)
        course = get_object_or_404(queryset, slug=slug)
        reviews = course.reviews.filter(approved=True).order_by("created_on")
        stars = False
        if course.stars.filter(id=self.request.user.id).exists():
            stars = True

        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            review_form.instance.email = request.user.email
            review_form.instance.name = request.user.username
            review = review_form.save(commit=False)
            review.course = course
            review.save()
        else:
            review_form = ReviewForm()

        return render(
            request,
            "course_detail.html",
            {
                "course": course,
                "reviews": reviews,
                "reviewed": True,
                "stars": stars,
                "review_form": ReviewForm()
            },
        )


class CourseStar(View):
    def post(self, request, slug):
        course = get_object_or_404(Course, slug=slug)

        if course.stars.filter(id=request.user.id).exists():
            course.stars.remove(request.user)
        else:
            course.stars.add(request.user)

        return HttpResponseRedirect(reverse('course_detail', args=[slug]))
