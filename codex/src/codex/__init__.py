
from sphinx.application import Sphinx

from codex.extension import setup_extension


def setup(app: Sphinx):
    setup_extension(app)
    return {"version": "0.1", "parallel_read_safe": True}
