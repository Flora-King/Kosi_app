from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Course, Review
from .forms import ReviewForm


class CourseList(generic.ListView):
    """
    This view displays the course list with related images
    Also displays the course excerpt which links user to the course content
    """

    model = Course
    queryset = Course.objects.filter(status=1).order_by("-delivery_from")
    template_name = "index.html"
    paginate_by = 9


def course_detail(request, slug, *args, **kwargs):
    """
    This view displays the course title, content, reviews and stars
    """

    queryset = Course.objects.filter(status=1)
    course = get_object_or_404(queryset, slug=slug)
    reviews = course.reviews.all().order_by("-created_on")
    review_count = course.reviews.filter(approved=True).count()
    stars = False
    reviewed = False

    if course.stars.filter(id=request.user.id).exists():
        stars = True

    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review_form.instance.email = request.user.email
            review_form.instance.name = request.user.username
            review = review_form.save(commit=False)
            review.course = course
            review.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Review awaiting check.')
        else:
            review_form = ReviewForm()
    else:
        review_form = ReviewForm()

    return render(
        request,
        "course_detail.html",
        {
            "course": course,
            "reviews": reviews,
            "review_count": review_count,
            "stars": stars,
            "review_form": review_form
        },
    )


def course_star(request, slug, *args, **kwargs):
    """
    This view enables user to update the stars.
    """

    course = get_object_or_404(Course, slug=slug)

    if request.method == "POST" and request.user.is_authenticated:
        if course.stars.filter(id=request.user.id).exists():
            course.stars.remove(request.user)
        else:
            course.stars.add(request.user)

    return HttpResponseRedirect(reverse('course_detail', args=[slug]))


def review_delete(request, slug, review_id, *args, **kwargs):
    """
    This view allows user to delete own reviews
    """

    review = get_object_or_404(Review, id=review_id)
    review_form = ReviewForm(data=request.POST, instance=review)
    if review.name == request.user.username:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
    else:
        messages.add_message(
            request, messages.ERROR,
            'You can only delete your own reviews!')

    return HttpResponseRedirect(reverse('course_detail', args=[slug]))


def review_edit(request, slug, review_id, *args, **kwargs):
    """
    view to edit reviews
    """
    if request.method == "POST":

        queryset = Course.objects.filter(status=1)
        course = get_object_or_404(queryset, slug=slug)
        review = course.reviews.filter(id=review_id).first()
        review_form = ReviewForm(data=request.POST, instance=review)
        if review_form.is_valid() and review.name == request.user.username:
            review = review_form.save(commit=False)
            review.course = course
            review.approved = False
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review Updated!')
        else:
            messages.add_message(
                request, messages.ERROR,
                'Error updating review!'
                )

    return HttpResponseRedirect(reverse('course_detail', args=[slug]))
