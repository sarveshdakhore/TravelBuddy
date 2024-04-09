from django.core.management.commands.runserver import Command as RunServerCommand

class Command(RunServerCommand):
    def handle(self, *args, **options):
        options['port'] = options.get('port', '8080')
        super(Command, self).handle(*args, **options)