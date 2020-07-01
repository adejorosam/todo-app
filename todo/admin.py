from django.contrib import admin
from todo.models import Category,Task

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    pass

class TaskAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category,CategoryAdmin)
admin.site.register(Task,TaskAdmin)


