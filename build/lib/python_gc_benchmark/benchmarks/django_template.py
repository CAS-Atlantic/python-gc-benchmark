"""Test the performance of the Django template system.

This will have Django generate a 150x150-cell HTML table.
"""

from six.moves import xrange

import django.conf
from django.template import Context, Template


DEFAULT_SIZE = 100


def run_django_template(size):
    template = Template("""<table>
{% for row in table %}
<tr>{% for col in row %}<td>{{ col|escape }}</td>{% endfor %}</tr>
{% endfor %}
</table>
    """)
    table = [xrange(size) for _ in xrange(size)]
    context = Context({"table": table})

    template.render(context)


if __name__ == "__main__":
    django.conf.settings.configure(TEMPLATES=[{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
    }])
    django.setup()

    run_django_template(DEFAULT_SIZE)
