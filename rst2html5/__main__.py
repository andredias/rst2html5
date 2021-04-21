from docutils.core import default_description, publish_cmdline

from . import HTML5Writer


def main():
    description = 'Generates (X)HTML5 documents from standalone ' 'reStructuredText sources.' + default_description
    publish_cmdline(writer=HTML5Writer(), description=description)


if __name__ == '__main__':
    main()
