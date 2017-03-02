"""pandoc-beamer-notes is a panflute pandoc filter to add notes to latex beamer
presentations."""

__version__ = '0.1.1'


from .pandoc_beamer_notes import prepare, action, finalize, main  # noqa
