# Wunki's Django Template

**Table of Contents**

- [Wunki's Django Template](#wunki's-django-template)
	- [Usage](#usage)
	- [Author](#author)

After doing a gazillion Django projects I saw some recurring patterns. This
project template for Django is the template I use for new projects. It
contains the configuration and setup for the following packages:

- [South]
- [Celery]
- [Django Extensions]
- [Django Debug toolbar] (in development)
- [Django Compressor]
- [Django Configurations]

Besides that the above packages are setup with sensible defaults, you also get
the following benefits by using this package:

1. In development you can surf to [/500.html] and [/404.html] to view your
   404 and 500 templates.

2. Static and media files are served correctly in development.

3. You receive a *pong* when you visit the [/ping] page. This view can be used
   in load balancer to see if your application is still up. Think [ELB].

4. Celery runs on your development database while in development so you don't
   have to setup RabbitMQ on your development machine.

5. Sensible directory layout. Your _media_ and _static_ files will be copied
   into the `public` directory. They already contain a `.gitignore` because
   those files should not be in Git.

6. Email is setup for you. Error mails are sent with an actual sender and you
   can debug on port `1025` with the Python `smptd` server.

## Usage

Start a new Django project with this template:

    django-admin.py startproject <project_name> --template=https://github.com/wunki/wunki-django-template/archive/master.zip

Go to the <project_name> directory and install the requirements:

    pip install -r requirements.txt

Sync and migrate:

    ./manage.py syncdb
    ./manage.py migrate

Run the server and you can find your new project at:
[http://localhost:8000](http://localhost:8000).

## Author

This is written by Petar Radosevic who used a similar template at [Gibbon]. If
you like programming as much as he does, you should follow him on Twitter:
[@wunki].

[South]: http://south.aeracode.org/
[Celery]: http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html
[Django Extensions]: https://github.com/django-extensions/django-extensions
[Django Debug toolbar]: https://github.com/django-debug-toolbar/django-debug-toolbar
[Django Compressor]: https://django_compressor.readthedocs.org/
[Django Configurations]: http://django-configurations.readthedocs.org/
[/500.html]: http://localhost:8000/500.html
[/404.html]: http://localhost:8000/404.html
[/ping]: http://localhost:8000/ping
[ELB]: http://aws.amazon.com/elasticloadbalancing/
[Gibbon]: http://blog.gibbon.co
[What Every Django Project Needs]: http://blog.gibbon.co/posts/2013-09-19-what-every-django-project-needs.html
[Gibbon]: http://gibbon.co
[@wunki]: https://twitter.com/wunki
