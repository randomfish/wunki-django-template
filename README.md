# Wunki's Django Template

After doing a gazillion Django projects I saw some recurring patterns. This
project template for Django is the template I use for new projects. It
contains the configuration and setup for the following packages:

- [South]
- [Celery]
- [Django extensions]
- [Django Debug toolbar] (in development)
- [Django Compressor]
- [Django Configurations]

## Usage

Start a new Django project with this template:

    django-admin.py startproject <project_name> --template=https://github.com/wunki/wunki-django-template/archive/master.zip

Go to the <project_name> directory and install the requirements:

    pip install -r requirements.txt

Sync and migrate:

    ./manage.py syncdb
    ./manage.py migrate

Run the server and you can find your new project at: [http://localhost:8000]

## Resources

TODO.

[South]: http://south.aeracode.org/
[Celery]: http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html
[Django extensions]: https://github.com/django-extensions/django-extensions
[Django Debug toolbar]: https://github.com/django-debug-toolbar/django-debug-toolbar
[Django Compressor]: https://django_compressor.readthedocs.org/
[Django Configurations]: http://django-configurations.readthedocs.org/
