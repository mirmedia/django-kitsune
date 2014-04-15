# -*- coding: utf-8 -
'''
Created on Mar 3, 2012

@author: Raul Garreta (raul@tryolabs.com)

Based on django-chronograph.

Changes for Django 1.6
@author: Anderson Santos (me@andersonsantos.info)

'''

__author__      = "Raul Garreta (raul@tryolabs.com)"


from django.conf import settings
import os
try:
	from django.core.management import setup_environ
except ImportError:
	setup_environ = os.environ.setdefault 

from django.utils.importlib import import_module


def get_manage_py():
    module = import_module(settings.SETTINGS_MODULE)
    return os.path.join(setup_environ(module, settings.SETTINGS_MODULE), 'manage.py')