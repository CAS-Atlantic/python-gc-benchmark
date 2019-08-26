"""
 * This program and the accompanying materials are made available under
 * the terms of the Eclipse Public License 2.0 which accompanies this
 * distribution and is available at https://www.eclipse.org/legal/epl-2.0/
 * or the Apache License, Version 2.0 which accompanies this distribution and
 * is available at https://www.apache.org/licenses/LICENSE-2.0.

Test the performance of the Django template system.

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
