# your_project_name/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns # 1. Import i18n_patterns

# These are the patterns that WILL be prefixed with a language code (e.g., /af/ /xh/)
# We wrap them in the i18n_patterns function.
urlpatterns = i18n_patterns(
    path('', include('showcase.urls')),
    # You can add other app URLs here if they also need translation.
)

# You can add patterns that should NOT be translated here.
# For example, the admin site is often left untranslated.
urlpatterns += [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
]

# Add media and static file serving for development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)