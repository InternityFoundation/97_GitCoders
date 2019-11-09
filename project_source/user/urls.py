from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url
from .views import *
urlpatterns = [
    # path('login', login_page, name="login"),
    path('check', auth_check, name="check"),
    path('profile/edit', ProfileEdit.as_view(), name="profile_edit"),

    # path('invalid', invalid, name="invalid"),
    # path('profile', profile, name="profile"),
    # path('profile/edit/', edit_profile, name="profile_edit"),
    # path('profile/address', view_user_address, name="profile_address"),
    # path('profile/address/add', add_user_address, name="add_user_address"),
    # path('profile/address/edit/<int:address_id>', edit_user_address, name="edit_user_address"),
    path('logout', logout_user, name="logout"),
    path('register', register_user, name="register"),
    # path('add-companies-profile', add_companies_profile, name="add_companies_profile"),
    # path('edit-companies-profile', edit_companies_profile, name="edit_companies_profile"),
    # path('make-me-seller/', make_me_seller, name='make-seller'),
    # re_path(r'^activate/(?P<token>[-@$\w]+)/$', activate, name='activate'),
]
