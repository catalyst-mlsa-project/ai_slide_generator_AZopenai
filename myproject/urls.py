from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin site URL
    path('admin/', admin.site.urls),
    
    # Include the URLs from the 'myapp' app
    path('', include('myapp.urls')),  # This will include all URLs defined in your 'myapp.urls'
]

# Serve static files during development (CSS, JS, images)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Serve media files (uploaded files like images)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




