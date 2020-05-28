#!/usr/bin/env python3

import logging

import camelot
from PyPDF2 import PdfFileReader

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)

START = 0
STEP = 10


def extract_csv(module, limit=False):
    """Extract tables from module's pdf with camelot.
    If a limit is given, on the first pages will be parsed until the limit number."""
    pdf_path = "../specs/{}.pdf".format(module)
    export_csv_path = "../specs/{}/raw/{}.csv".format(module, module)

    pdf = PdfFileReader(pdf_path)
    max_pages = limit if limit else pdf.getNumPages()

    logger.info(
        """extracting tables from pdf for module {} ({} pages)...\
        \nWARNING! It can take a while (easily 20 minutes)""".format(
            module, max_pages
        )
    )

    # we process the pages 10 by 10 to avoid malloc errors
    i = START
    while i < max_pages:
        limit = min(i + STEP, max_pages)
        logger.info("\nextracting pages {} to {}...".format(i, limit))
        tables = camelot.read_pdf(pdf_path, pages="{}-{}".format(i, limit),)
        tables.export(export_csv_path, f="csv", compress=False)
        i += STEP


# TODO improve tables:
# - remove empty lines
# - if table has the same num of columns as table from previous page
#   and seems to have no header and seems continuation of previous table,
#   then append it at the end of table of previous page.

if __name__ == "__main__":
    extract_csv("ecd")
    extract_csv("ecf")
    extract_csv("efd_icms_ipi")
    extract_csv("efd_pis_cofins")
