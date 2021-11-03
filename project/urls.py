import traceback

import django
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from project import settings
from project.logger import logger

urlpatterns = [
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    if settings.DEBUG_TOOLS:
        import debug_toolbar

        urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns

    try:
        urlpatterns += [
            url(r'^media/(?P<path>.*)$', django.views.static.serve,
                {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ]
    except:
        logger.error(traceback.format_exc())
