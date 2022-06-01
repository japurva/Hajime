"""
Setup url patterns
"""
from django.urls import path, include, re_path

from rest_framework import routers
from .views import auth_views, leave_views, employee_views, attendance_views
from django.views.decorators.csrf import csrf_exempt


# Router settings
router = routers.DefaultRouter()
router.register(r'users', employee_views.EmployeeViewSet, basename='users')
#router.register(r'attendance', attendance_views.AttendanceViewSet, basename='attendance')

#leave = routers.DefaultRouter()
#leave.register(r'detail',leave_views.LeaveViewSet,basename='details')


urlpatterns = [
    path(r'', include((router.urls, 'backend'), namespace='default')),
    #path(r'leave/', include((leave.urls, 'leave'), namespace='leave')),
    path('csrf/', auth_views.get_csrf, name='api-csrf'), 
    path('login/', csrf_exempt(auth_views.login_view), name='api-login'),
    path('logout/', auth_views.logout_view, name='api-logout'),
    path('session/', auth_views.SessionView.as_view(), name='api-session'),
    path('profile/', auth_views.WhoAmIView.as_view(), name='api-whoami'),
]

