pandoc-beamer-notes
===================

Warning: This package only exists for legacy reasons, do not use it anymore!

Instead, use pandoc's built-in mechanism for note slides:

.. code-block:: markdown

    # My frame
    <div class="notes">
    My **Notes**:

    - Don't use any filters, unless they are useful!
    - This is all still in *pandoc*

    </div>

    # My next Frame ...

And compile with

.. code-block:: shell

    pandoc -t beamer -V classoption=notes ...

Thanks to `Norman Markgraf`_ to make me aware of this and providing the simple
example above.

For more information check out `shoeffner/pandoc-beamer-notes#3`_.


Legacy usage
------------
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
.. _`Norman Markgraf`: https://github.com/NMarkgraf
.. _`shoeffner/pandoc-beamer-notes#3`: https://github.com/shoeffner/pandoc-beamer-notes/issues/3
