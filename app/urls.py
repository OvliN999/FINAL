from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

# Import views from controller (authview, book, admins)
from app.controller import authview, book, admins

urlpatterns = [
    path('', views.home, name="home"),
    path('category/', views.category, name="category"),
    path('category/<str:id>', views.categoryview, name="categoryview"),
    path('category/<str:categ_id>/<str:car_id>', views.carview, name="carview"),

    path('book/', book.addtobook, name="addtobook"),

    path('register/', authview.register, name="register"),
    path('login/', authview.loginpage, name="loginpage"),
    path('logout/', authview.logoutpage, name="logout"),

    path('admin-panel/', admins.dashboard, name="dashboard"),
    path('addcar/', admins.addcar, name="addcar"),
    path('deletecar/<int:id>', admins.deletecar, name="deletecar"),  # unique for deleting cars

    path('adduser/', admins.adduser, name="adduser"),
    path('viewuser/', admins.viewuser, name="viewuser"),
    path('deleteuser/<int:id>', admins.deleteuser, name="deleteuser"),  # unique for deleting users

    path('bookview/', admins.bookview, name="bookview"),
]

# Serve static and media files during development (only for DEBUG=True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

