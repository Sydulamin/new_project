from django.contrib import admin
from .models import *
# Register your models here.

class ClassNameAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = ('name',)

class SubjectNameAdmin(admin.ModelAdmin):
    list_display = ('name', 'className')
    search_fields = ('name', 'className__name')
    list_filter = ('className',)
    ordering = ('name',)

admin.site.register(Students)
admin.site.register(ClassName, ClassNameAdmin)
admin.site.register(SubjectName, SubjectNameAdmin)
admin.site.register(TeacherName)
admin.site.site_header = "School Management"
admin.site.site_title = "School Management Admin"
admin.site.index_title = "Welcome to School Management Admin"
admin.site.empty_value_display = "-empty-"

# admin.site.site_url = None
# admin.site.unregister(Group)  # Unregister the Group model from admin
# admin.site.disable_action('delete_selected')  # Disable the bulk delete action
# admin.site.enable_nav_sidebar = False  # Disable the navigation sidebar
# admin.site.login_template = 'admin/login.html'  # Custom login template
# admin.site.logout_template = 'admin/logout.html'  # Custom logout template
# admin.site.index_template = 'admin/index.html'  # Custom index template
# admin.site.app_index_template = 'admin/app_index.html'  # Custom app index template
# admin.site.login_form = None  # Custom login form
# admin.site.has_permission = lambda request: request.user.is_active and request.user.is_staff  # Custom permission check
# admin.site.has_module_perms = lambda request, app_label: request.user.is_active and request.user.is_staff
# admin.site.get_app_list = lambda request: []  # Custom app list
# admin.site.get_urls = lambda: []  # Custom URLs
# admin.site.get_app_list = lambda request: []