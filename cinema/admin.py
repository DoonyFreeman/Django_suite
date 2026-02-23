from django.contrib import admin
from .models import VideoProduct, OriginalTitle, ProductType, Director, DirectorVideoProduct

# Register the cinema models so they appear in the admin site
admin.site.register(ProductType)
admin.site.register(VideoProduct)
admin.site.register(OriginalTitle)
admin.site.register(Director)
admin.site.register(DirectorVideoProduct)
