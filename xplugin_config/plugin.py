# coding: utf-8
from django import forms
from django.template.loader import render_to_string
from xadmin.plugins.utils import get_context_dict
from xadmin.views import BaseAdminPlugin


class ConfigPlugin(BaseAdminPlugin):
    """Configuration plugin for other plugins"""
    component_settings = False

    def init_request(self, *args, **kwargs):
        return self.component_settings

    def block_top_toolbar(self, context, nodes):
        """toobar"""
        context = get_context_dict(context)
        nodes.append(render_to_string("xplugin_config/blocks/comm.top.config.html",
                                      context=context))

    def block_extrabody(self, context, nodes):
        context = get_context_dict(context)
        nodes.append(render_to_string("xplugin_config/includes/config.html",
                                      context=context))

    def get_media(self, media):
        media += forms.Media(js=(
            'xplugin_config/js/modal_config.js',
        ))
        return media
