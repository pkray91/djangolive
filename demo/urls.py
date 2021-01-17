from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from demo import views

urlpatterns = [
	path('form/',views.form),
	path('',views.home),
	path('news/',views.get_news),
	path('about/',views.about),
	path('contact/',views.contact),
	path('add/',views.adddata),
	path('get-data/',views.get_data),
	path('delete/<int:id>',views.delete),
	path('getdataforedit/<int:id>',views.getdataforedit),
	path('update/<int:id>',views.updatedata),
	path('get-category/<str>',views.get_category),
	

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)