from django.contrib import admin

from system.models import ConfigUser, LegalUser, Role, SocialUser

# Register your models here.
admin.site.register(SocialUser)
admin.site.register(ConfigUser)
admin.site.register(LegalUser)
admin.site.register(Role)
