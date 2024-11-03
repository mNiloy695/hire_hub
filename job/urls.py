from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('',views.CompanyView)

urlpatterns = [
    path('list/',views.JobListView.as_view(),name='job_list'),
    path("<int:pk>/",views.JobDetailView.as_view()),
    path("apply/",views.ApplyListView.as_view(),name="apply"),
    path("apply/<int:pk>/",views.ApplyDetailView.as_view()),
    path('companies/', include(router.urls)),
      
]