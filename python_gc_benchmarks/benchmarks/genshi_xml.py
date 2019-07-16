"""
Render a template using Genshi module.
"""

from six.moves import xrange

from genshi.template import MarkupTemplate, NewTextTemplate


BIGTABLE_XML = """\
<table xmlns:py="http://genshi.edgewall.org/">
<tr py:for="row in table">
<td py:for="c in row.values()" py:content="c"/>
</tr>
</table>
"""


def run_genshi(loops, tmpl_cls, tmpl_str):
    tmpl = tmpl_cls(tmpl_str)
    table = [dict(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8, i=9, j=10)
             for _ in range(1000)]
    range_it = xrange(loops)

    for _ in range_it:
        stream = tmpl.generate(table=table)
        stream.render()

BENCHMARKS = {
    'xml': (MarkupTemplate, BIGTABLE_XML),
}


if __name__ == "__main__":
    
    benchmarks = sorted(BENCHMARKS)

    for bench in benchmarks:
        name = 'genshi_%s' % bench
        tmpl_cls, tmpl_str = BENCHMARKS[bench]
        run_genshi(100, tmpl_cls, tmpl_str)
