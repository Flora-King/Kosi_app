from django.contrib import admin

from .models import Course, Review
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Course)
class CourseAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'delivery_from')
    summernote_fields = ('content',)
    search_fields = ['title', 'content']
    list_display = ('title', 'slug', 'status', 'delivery_from',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'course', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approved_reviews']

    def approve_reviews(self, request, queryset):
        queryset.updated(approved=True)
