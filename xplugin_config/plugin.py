# coding: utf-8
from django import forms
from django.template.loader import render_to_string
from django.utils.functional import cached_property
from xadmin.plugins.utils import get_context_dict
from xadmin.views import BaseAdminPlugin


class Storage:
    def __init__(self, namespace, request):
        self.namespace = namespace
        self.request = request

    @cached_property
    def options(self):
        return (self.request.GET if self.request.method == 'GET' else
                self.request.POST)

    @cached_property
    def cookies(self):
        return self.request.COOKIES

    def get(self, key, default=None):
        """get value key"""
        value = self.options.get(key)
        value = value or self.cookies.get(self.namespace + "." + key)
        value = value or default
        return value

    def set(self, key, value, **kwargs):
        """Set key value"""
        self.cookies.set(key, value, **kwargs)


class ConfigPlugin(BaseAdminPlugin):
    """Configuration plugin for other plugins"""
    component_store = None
    __order__ = 50

    def init_request(self, *args, **kwargs):
        is_active = isinstance(self.component_store, str)
        if is_active:
            self._init()
        return is_active

    def _init(self):
        av = self.admin_view
        # armazenamento da view
        av.storage = Storage(self.component_store,
                             self.request)

    def block_top_toolbar(self, context, nodes):
        """toolbar"""
        context = get_context_dict(context)
        nodes.append(render_to_string("xplugin_config/blocks/comm.top.config.html",
                                      context=context))

    block_top_toolbar.priority = 0

    def get_context(self, context):
        context['config_modal'] = {
            'button_text': "Configuration",
            'title': "Configuration",
            'storage': self.admin_view.storage
        }
        return context

    get_context.priority = 100

    def block_extrabody(self, context, nodes):
        context = get_context_dict(context)
        nodes.append(render_to_string("xplugin_config/includes/config.html",
                                      context=context))

    def get_media(self, media):
        media += forms.Media(js=(
            'xplugin_config/js/storage.js',
            'xplugin_config/js/modal_config.js',
        ))
        return media

    get_media.priority = 100