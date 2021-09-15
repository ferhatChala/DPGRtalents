from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User,Doctorant,Teacher,DThese,DLab,DPGRuser,CFDuser,CSuser,Grade


class UserAdmin(UserAdmin):
	list_display = ('email','username')
	search_fields = ('email','username',)
	readonly_fields=('date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


admin.site.register(User, UserAdmin)
admin.site.register(Doctorant)
admin.site.register(Teacher)
admin.site.register(DThese)
admin.site.register(DLab)
admin.site.register(DPGRuser)
admin.site.register(CFDuser)
admin.site.register(CSuser)
admin.site.register(Grade)

