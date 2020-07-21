from django.contrib import admin
from django.forms import Textarea
from django.db import models
from games.models import *


admin.site.register([Team, Profile, CheckerType, HTMLPage, AttemptsInfo])


class TaskInline(admin.TabularInline):
    model = Task
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 3, 'cols': 40})},
    }


@admin.register(TaskGroup)
class TaskGroupAdmin(admin.ModelAdmin):
    inlines = [
        TaskInline,
    ]


class TaskGroupInline(admin.TabularInline):
    model = TaskGroup


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    inlines = [
        TaskGroupInline
    ]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 3, 'cols': 40})},
    }


@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 3, 'cols': 40})},
    }


@admin.register(ProxyAttempt)
class PendingAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 3, 'cols': 40})},
    }

    def get_queryset(self, request):
        qs = super(PendingAdmin, self).get_queryset(request)
        return qs.filter(status='Pending')
