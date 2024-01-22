from django.contrib import admin

from Main.models import *


class PostAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Meta', {
            'fields': ('meta_title', 'meta_keywords', 'meta_image', 'meta_description')
        }),

        ('Post', {
            'fields': ('title', 'photo', 'body', 'slug')
        }),)

    list_display = ('date_added','title',)
  
    def active(self, obj):
        return obj.is_active == 1
  
    active.boolean = True
admin.site.register(Post, PostAdmin)


class CareerAdmin(admin.ModelAdmin):
    list_display = ('date_added','title','experience')
    def active(self, obj):
        return obj.is_active == 1
admin.site.register(Career, CareerAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('date_added','name','phone_no')
    def active(self, obj):
        return obj.is_active == 1
admin.site.register(Contact, ContactAdmin)


class cadidateAdmin(admin.ModelAdmin):
    list_display = ('date_added','name','job')
    def active(self, obj):
        return obj.is_active == 1
admin.site.register(cadidate, cadidateAdmin)