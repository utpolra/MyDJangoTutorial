from .views import search,filter,contact,postview,postcreate,PostDeleteView, subview,ContactView,PostEditView,PostCreateView,PostListView,PostDetailView
from .forms import ContactFormtwo
from django.urls import path
app_name='tuition'
urlpatterns = [
    # path('contact/',contact,name="contact"),
    path('search/',search,name="search"),
    path('filter/',filter,name="filter"),
    path('contact/',ContactView.as_view(),name="contact"),
    # path('contact2/',ContactView.as_view(form_class=ContactFormtwo, template_name="contact2.html"),name="contact2"),
    path('posts/',postview,name="posts"),
    path('subjects/',subview,name="subjects"),
    path('postlist/',PostListView.as_view(),name="postlist"),
    path('postdetail/<int:pk>/',PostDetailView.as_view(),name="postdetail"),
    path('delete/<int:pk>/',PostDeleteView.as_view(),name="delete"),
    path('edit/<int:pk>/',PostEditView.as_view(),name="edit"),
    # path('create/',postcreate,name="create"),
    path('create/',PostCreateView.as_view(),name="create"),
]