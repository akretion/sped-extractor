#!/usr/bin/env python

# we used a patched camelot
# see https://github.com/socialcopsdev/camelot/issues/217
import camelot

START = 0
STEP = 10


def extract_csv(module, max_pages):
    print("extracting tables from pdf for module %s (%s pages)..." % (module,
          max_pages))
    print("WARNING! It can take a while (easily 20 minutes)")
    # we process the pages 10 by 10 to avoid malloc errors
    i = START
    while i < max_pages:
        limit = min(i + STEP, max_pages)
        print('extracting pages %s to %s...' % (i, limit))
        tables = camelot.read_pdf('../specs/%s.pdf' % (module,),
                                  pages='%s-%s' % (i, limit),
                                  line_size_scaling=80,
                                  strip_text=' .\n')
        tables.export('../specs/%s/%s.csv' % (module, module), f='csv',
                      compress=False)
        i += STEP


# TODO improve tables:
# - remove empty lines
# - if table has the same num of columns as table from previous page
#   and seems to have no header and seems continuation of previous table,
#   then append it at the end of table of previous page.

if __name__ == '__main__':
    extract_csv('ecd', 190)
    extract_csv('ecf', 575)
    extract_csv('efd_icms_ipi', 262)
    extract_csv('efd_pis_cofins', 381)
