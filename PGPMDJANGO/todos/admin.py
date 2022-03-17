from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Utente

# Register your models here.
from compressor.filters import CompilerFilter

class PostCSSFilter(CompilerFilter):
	command = 'postcss'


admin.site.register(Utente, UserAdmin)