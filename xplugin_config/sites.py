from xadmin.sites import site as xsite
from xadmin.views import CommAdminView


def register(site=None):
    """Register the configuration plugin"""
    if site is None:
        site = xsite
    from xplugin_config.plugin import ConfigPlugin
    site.register_plugin(ConfigPlugin, CommAdminView)
