from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices
from django.conf import settings

PLUGIN_SETTINGS = settings.PLUGINS_CONFIG.get("netbox_healthcheck_plugin", dict())


PLUGIN_NAVIGATION = PLUGIN_SETTINGS.get('navigation',True)
if PLUGIN_NAVIGATION:
    menu_items = (
        PluginMenuItem(
            link='plugins:netbox_healthcheck_plugin:healthcheck_list',
            link_text='HealthCheck',
            buttons=None
        ),
    )