"""pandoc-beamer-notes is a panflute pandoc filter to add notes to latex beamer
presentations."""

import panflute as pf


def prepare(doc):
    pass


def action(elem, doc):
    if isinstance(elem, pf.elements.RawInline) and elem.format == 'tex':
        if elem.text.startswith('\\note{') and elem.text.endswith('}'):
            body = pf.convert_text(elem.text[6:-1], output_format='latex')
            para = pf.convert_text('\\note{{{}}}'.format(body))[0]
            return para.content[0]
    return elem


def finalize(doc):
    pass


def main(doc=None):
    return pf.run_filter(action,
                         prepare=prepare,
                         finalize=finalize,
                         doc=doc)


if __name__ == '__main__':
    main()
