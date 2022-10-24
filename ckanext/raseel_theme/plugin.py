import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
pconfig = toolkit.config
from ckan.common import config
from ckan.lib.app_globals import set_app_global
from ckan.lib.plugins import DefaultTranslation
import ckan.logic as logic
import ckan.lib.helpers as h
from datetime import datetime


class RaseelThemePlugin(plugins.SingletonPlugin, DefaultTranslation):
    plugins.implements(plugins.ITranslation)
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    def update_config(self, config_):
        set_app_global('ckan.raseel_url',
                   pconfig.get('%s.raseel_url' % __name__))
        set_app_global('ckan.raseel_portal_url',
                   pconfig.get('%s.raseel_portal_url' % __name__))
        set_app_global('ckan.raseel_ckan_app_id',
                   pconfig.get('%s.raseel_ckan_app_id' % __name__))
        set_app_global('ckan.raseel_global_login_organization_name',
                   pconfig.get('%s.raseel_global_login_organization_name' % __name__))

        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('assets', 'theme')

    # ITemplateHelpers
    def get_helpers(self):
        return {
            'raseel_theme_get_last_datasets': lambda: logic.get_action('package_search')({}, {"rows": 8})['results'],
            'raseel_theme_get_resource_number': raseel_theme_get_resource_number,
            'raseel_theme_get_showcase_number': raseel_theme_get_showcase_number,
            'raseel_theme_get_popular_datasets': lambda: logic.get_action('package_search')({}, {"rows": 4, 'sort': 'views_total desc'})['results'],
            'raseel_theme_display_date': raseel_theme_display_date,
            'raseel_theme_get_map': raseel_theme_get_map,
            'raseel_theme_get_groups': lambda: logic.get_action('group_list')({}, {"all_fields": True}),
            'raseel_theme_spatial_installed': lambda: config.get('ckanext.raseel_theme.spatial_installed', 'False'),
            'raseel_theme_osmnames_key': lambda: config.get('ckanext.raseel_theme.osmnames_key', '')
        }


def raseel_theme_display_date(strDate):
    return datetime.strptime(strDate, "%Y-%m-%dT%H:%M:%S.%f").strftime('%d/%m/%Y')


def raseel_theme_get_resource_number():
    return logic.get_action('resource_search')({}, {'query': {'name:': ''}})['count']


def raseel_theme_get_showcase_number():
    return len(logic.get_action('ckanext_showcase_list')({}, {}))


def raseel_theme_get_map(view_id, resource_id, package_id):
    resource_view = None
    try:
        resource_view = logic.get_action('resource_view_show')({}, {'id': view_id})
    except ():
        return 'View not found'

    resource = logic.get_action('resource_show')({}, {'id': resource_id})
    package = logic.get_action('package_show')({}, {'id': package_id})

    return h.rendered_resource_view(resource_view, resource, package, True)
