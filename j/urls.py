from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',views.hello, name='hello'),
    path('writetext/', views.writetext, name='writetext'),
    path('home/', views.home, name='home'),
    path('upload/', views.upload_image, name='upload_image'),
    path('delete_images/', views.delete_images, name='delete_images'),
    path('emaill_form/', views.email_form, name='email_form'),
    path('delete-text/<int:text_id>/', views.delete_text, name='delete_text'),
    # path('mantras/', views.mantra, name='mantras'),
]

     


from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




    

