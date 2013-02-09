from pyramid.config import Configurator

from security import RequestWithAttributes

from plonejenkins.middleware.db import ReposDB


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings,
                          request_factory=RequestWithAttributes)

    # adds cornice
    config.include("cornice")

    config.registry.settings['api_key'] = settings['api_key']

    config.registry.settings['core'] = ReposDB(settings['core_repos_db'])

    # adds cornice
    config.include("cornice")

    config.scan("plonejenkins.middleware.views")

    config.end()

    return config.make_wsgi_app()
