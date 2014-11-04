"""
Developers base settings
"""
from .base import *  # noqa , Flake8 to ignore F403


DEBUG = True
TEMPLATE_DEBUG = DEBUG
THUMBNAIL_DEBUG = DEBUG

DEV_APPS = (
    'debug_toolbar.apps.DebugToolbarConfig',
    'django_extensions'
)

INSTALLED_APPS = tuple(list(INSTALLED_APPS) + list(DEV_APPS))