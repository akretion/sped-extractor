#!/usr/bin/env python3

import logging

# we used a patched camelot
# see https://github.com/socialcopsdev/camelot/issues/217
import camelot

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)

START = 0
STEP = 10


def extract_csv(module, max_pages):
    logger.info(
        "extracting tables from pdf for module {} ({} pages)...".format(
            module, max_pages
        )
    )
    logger.warning("WARNING! It can take a while (easily 20 minutes)")
    # we process the pages 10 by 10 to avoid malloc errors
    i = START
    while i < max_pages:
        limit = min(i + STEP, max_pages)
        logger.info("extracting pages {} to {}...".format(i, limit))
        tables = camelot.read_pdf(
            "../specs/{}.pdf".format(module), pages="{}-{}".format(i, limit),
        )
        tables.export(
            "../specs/{}/raw/{}.csv".format(module, module), f="csv", compress=False
        )
        i += STEP


# TODO improve tables:
# - remove empty lines
# - if table has the same num of columns as table from previous page
#   and seems to have no header and seems continuation of previous table,
#   then append it at the end of table of previous page.

if __name__ == "__main__":
    extract_csv("ecd", 12)
    extract_csv("ecf", 12)
    extract_csv("efd_icms_ipi", 12)
    extract_csv("efd_pis_cofins", 12)
