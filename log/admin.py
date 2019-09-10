# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from log.models import UserProfileInfo, User, department, ticket

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(department)
admin.site.register(ticket)
