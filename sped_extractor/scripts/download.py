#!/usr/bin/env python3

import logging
import os

import click
import requests

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)

URL = {
    2019: {
        "ecd": "http://sped.rfb.gov.br/estatico/2A/D6DD917199D4DE9B01C0D406778DA7A8E2E05D/Manual_de_Orienta%c3%a7%c3%a3o_da_ECD_2019_Dezembro_Leiaute_8.pdf",
        "ecf": "http://sped.rfb.gov.br/estatico/06/0372A38AD8F1D2AAEA6B65FF02E2BE7624A30C/Manual_de_Orienta%c3%a7%c3%a3o_da_ECF_Dezembro_2019.pdf",
        "efd_icms_ipi": "http://sped.rfb.gov.br/estatico/0D/434EFF065B893AB70D59AD102A946DC9237680/2019.05.21_GUIA%20PR%c3%81TICO%20DA%20EFD%20-%20Vers%c3%a3o%203.0.3%20-%20v3%20para%20publica%c3%a7%c3%a3o.pdf",
        "efd_pis_cofins": "http://sped.rfb.gov.br/estatico/21/752D4028C877B5B71F3B1A850C32317A36B5AC/Guia_Pratico_EFD_Contribuicoes_Versao_1_33%20-%2016_12_2019.pdf",
    }
}

MOST_RECENT_YEAR = max(URL, key=int)
OLDEST_YEAR = min(URL, key=int)


def _download(mod, year):
    pdf = "../specs/{}.pdf".format(mod)
    url = URL[year].get(mod)
    r = requests.get(url)
    try:
        os.remove(pdf)
    except OSError:
        pass
    with open(pdf, "wb") as f:
        f.write(r.content)


@click.command()
@click.option(
    "--year",
    default=MOST_RECENT_YEAR,
    show_default=True,
    type=int,
    help="Specify a SPED specification year between {} and {}".format(
        OLDEST_YEAR, MOST_RECENT_YEAR
    ),
)
def main(year):
    """Download SPED specifications pdf from http://sped.rfb.gov.br/"""
    for module in ["ecd", "ecf", "efd_icms_ipi", "efd_pis_cofins"]:
        if not URL.get(year):
            logger.warning(
                "An integer between {} and {} is required for year's option, not '{}'.\
                ".format(
                    OLDEST_YEAR, MOST_RECENT_YEAR, year
                )
            )
            break
        else:
            logger.info("Downloading {} pdf from {}...".format(module, year))
            _download(module, year)


if __name__ == "__main__":
    main()
