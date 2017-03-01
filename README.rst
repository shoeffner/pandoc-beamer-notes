pandoc-beamer-notes
===================

``pandoc-beamer-notes`` is a `panflute`_ `pandoc`_ `filter`_.
It allows to use markdown in LaTeX notes.

Thus something like the following will be rendered nicely:

.. code-block:: markdown

    \note{**this is bold**}
    \note{
    * a list
    * is also possible
    }

See the `example <example>`_ for a simple presentation containing notes.

Remember to compile your documents with the notes enabled for beamer:

.. code-block:: shell

    pandoc -t beamer -V classoption=notes ...


Installation
------------

Just use pip to install it from `pypi`_.

.. code-block:: shell

    pip install pandoc-beamer-notes


.. _`filter`: https://pandoc.org/scripting.html
.. _`pandoc`: https://pandoc.org/index.html
.. _`panflute`: http://scorreia.com/software/panflute/index.html
.. _`pypi`: https://pypi.python.org/pypi/pandoc-beamer-notes
