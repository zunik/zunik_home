from zunik_home import settings


def global_settings(request):
    return {
        'SITE_DOMAIN' : settings.SITE_DOMAIN
    }