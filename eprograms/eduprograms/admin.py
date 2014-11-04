from django.contrib import admin
from .models import ProgramFor, ProgramChapter, ProgramCategory, Program


class ProgramForAdmin(admin.ModelAdmin):
    pass


class ProgramCategoryAdmin(admin.ModelAdmin):
    pass


class ProgramChapterAdmin(admin.TabularInline):
    model = ProgramChapter


class ProgramAdmin(admin.ModelAdmin):
    inlines = (ProgramChapterAdmin,)


admin.site.register(ProgramFor, ProgramForAdmin)
admin.site.register(ProgramCategory, ProgramCategoryAdmin)
admin.site.register(ProgramAdmin, ProgramAdmin)
