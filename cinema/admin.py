from django.contrib import admin
from .models import VideoProduct, OriginalTitle

# Register the cinema models so they appear in the admin site
admin.site.register(VideoProduct)
admin.site.register(OriginalTitle)
