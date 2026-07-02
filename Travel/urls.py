from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login_view,name='login'),
    path('register',views.register_view,name='register'),
    path('logout',views.logout_view,name='logout'),
    path('Admin',views.admin_view,name='Admin'),
    path('dashboard',views.dashboard_view,name='Adashboard'),
    path('Recommendation',views.Udashboard_view,name='udashboard'),
    path('add-destination',views.add_destination,name='adddestination'),
    path('Save-destination/<int:pk>/',views.save_Destination,name='Save_destination'),
    path('Saved-list',views.saved_list,name='Save_list'),
    path('delete-saved/<int:pk>/',views.delete_saved,name='delete_Save'),
    path('delete-destination/<int:pk>/',views.delete_destionation,name='delete_destination'),
]

