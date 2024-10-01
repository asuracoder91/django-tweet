from django.contrib import admin

# Register your models here.
from .models import Tweet, Like


class ElonMuskFilter(admin.SimpleListFilter):
    title = "Contains Elon Musk or not"
    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("contain", "Contain"),
            ("not_contain", "Not Contain"),
        ]

    def queryset(self, request, tweets):
        is_contain = self.value()
        if is_contain == "contain":
            return tweets.filter(payload__contains="Elon Musk")
        if is_contain == "not_contain":
            return tweets.exclude(payload__contains="Elon Musk")
        else:
            return tweets


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = (
        "payload",
        "user",
        "like_count",
        "created_at",
        "updated_at",
    )

    list_filter = (
        ElonMuskFilter,
        "created_at",
    )
    search_fields = (
        "payload",
        "user__username",
    )


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = (
        "tweet",
        "user",
        "created_at",
        "updated_at",
    )
    list_filter = ("created_at",)
    search_fields = ("user__username",)
