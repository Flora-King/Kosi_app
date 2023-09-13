from django.db import models
from django.db.models import Model

# my models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))
# DELIVERY = ((1, "Classroom"), (2, "Online"), (3, "All"))
DELIVERY = (
    ('Classroom', '1'),
    ('Online', '2'),
    ('All', '3')
)


class Course(models.Model):
    delivery = models.CharField(max_length=20, null=True, blank=True, choices=DELIVERY, default=3)
    featured_image = CloudinaryField('image', default='placeholder')
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    excerpt = models.TextField(max_length=300)
    course_content = models.TextField(max_length=1500)
    delivery_from = models.DateTimeField(auto_now_add=True)
    delivery_to = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stars = models.ManyToManyField(User, related_name='stars', blank=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['price']

    def __str__(self):
        return self.title

    def number_of_stars(self):
        return self.stars.count()


class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Review {self.body} by {self.name}"
