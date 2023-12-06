from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static



urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('items/', include('item.urls')),
    path('users/', include('users.urls')), 
    path('checkout/', include('checkout.urls')),
    path('inbox/', include('conversation.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('', include('paypal.standard.ipn.urls')),
    path('transaction/', include('transactions.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),  # <-- here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


