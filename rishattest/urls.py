from django.contrib import admin
from django.urls import path
from paypage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index_html"),
    path('success', views.success),
    path('cancel', views.cancel),
    path('buy/<int:pk>', views.CreateCheckoutSessionView),
    path('item/<int:pk>', views.goods_info),
]
