from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = "home"),
    path('accounts/', include("accounts.urls")),
    path('profile/', include("profiles.urls")),
    path('admins/', include("admins.urls"))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#Change Site Title, Index Title and Site Title
admin.site.site_header = "MWANGA HAKIKA BANK"
admin.site.site_title = "MWANGA HAKIKA BANK"
admin.site.index_title = "Welcome to MWANGA HAKIKA BANK"
