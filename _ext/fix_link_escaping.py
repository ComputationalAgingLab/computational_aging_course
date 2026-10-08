"""Undo the HTML escaping that myst-parser 3.x applies to link URLs.

myst-parser 3.0 stores links as ``escapeHtml(uri)``, and the HTML writer escapes
them again, so ``?a=1&b=2`` ends up as ``?a=1&amp;amp;b=2`` and the link breaks.
"""
import html

from docutils import nodes
from sphinx.transforms import SphinxTransform


class UnescapeReferenceUris(SphinxTransform):
    default_priority = 900

    def apply(self, **kwargs):
        for ref in self.document.findall(nodes.reference):
            uri = ref.get("refuri")
            if uri and "&" in uri:
                ref["refuri"] = html.unescape(uri)


def setup(app):
    app.add_transform(UnescapeReferenceUris)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
