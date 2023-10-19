from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Contact,  RawContact, Lead

@admin.register(RawContact)
class RawContactAdmin(admin.ModelAdmin):
    list_display = ['value', 'category', 'platform', 'note', 'status']

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ['origin','category', 'name', 'email', 'subject', 'time', 'status']  # make sure this import is correct

class ContactInline(admin.StackedInline):
    model = Contact
    can_delete = False
    verbose_name_plural = 'Contact'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ContactInline, )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_telephone')
    list_select_related = ('contact', )

    def get_telephone(self, instance):
        return instance.contact.telephone
    get_telephone.short_description = 'Telephone'

# Unregister the provided model admin then register the customized model admin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
# Also register the Contact model
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('user', 'telephone', 'adresse', 'business', 'job', 'status')
