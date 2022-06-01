# Hier bookradmin site; deze is site specifiek en niet
# per se gerelateerd aan review app

from django.contrib import admin


class BookrAdminSite(admin.AdminSite):
    title_header = 'Bookr Admin'
    site_header = 'Bookr administrtion'
    index_title = 'Bookr site admin'
