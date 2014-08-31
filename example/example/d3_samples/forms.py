__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'

from django import forms
from django.utils.translation import ugettext_lazy as _

from dash.base import DashboardPluginFormBase

class ChartForm(forms.Form, DashboardPluginFormBase):
    """
    Chart form for `ChartBasePlugin` plugin.
    """

    plugin_data_fields = [
        ("title", ""),
    ]

    title = forms.CharField(label=_("Title"), required=True)
