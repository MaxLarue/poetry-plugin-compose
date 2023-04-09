from poetry.plugins.application_plugin import ApplicationPlugin

from poetry_plugin_compose.compose_command import compose_command_factory


class MultiPackagePlugin(ApplicationPlugin):
    def activate(self, application):
        print("plugin activated")
        application.command_loader.register_factory("compose", compose_command_factory)
