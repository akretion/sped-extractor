#!/usr/bin/env python3

import logging
import os

import click
import requests
from PyPDF2 import PdfFileReader

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)

URL = {
    2020: {
        # Leiaute 8 - Novembro de 2019
        "ecd": "http://sped.rfb.gov.br/arquivo/download/4210",
        # Leiaute 6 - Dezembro de 2019
        "ecf": "http://sped.rfb.gov.br/arquivo/download/4272",
        # Leiaute 14 - Versão 3.0.3 - Outubro de 2019
        "efd_icms_ipi": "http://sped.rfb.gov.br/arquivo/download/4202",
        # Versão 1.33 - Dezembro de 2019
        "efd_pis_cofins": "http://sped.rfb.gov.br/arquivo/download/4263",
    },
    2019: {
        #  Leiaute 7 - Dezembro de 2018
        "ecd": "http://sped.rfb.gov.br/arquivo/download/2911",
        # Leiaute 5 - Fevereiro de 2019
        "ecf": "http://sped.rfb.gov.br/arquivo/download/2908",
        # Versão 3.0.1 - Janeiro de 2019
        "efd_icms_ipi": "http://sped.rfb.gov.br/arquivo/download/4222",
        # Versão 1.31 - Abril de 2019
        "efd_pis_cofins": "http://sped.rfb.gov.br/estatico/20/6E34811D4F98083196E2A09880F048189788FC/Guia_Pratico_EFD_Contribuicoes_Versao_1_31%20-%2029_04_2019.pdf",
    },
    2018: {
        # Leiaute 6 - Agosto de 2018
        "ecd": "http://sped.rfb.gov.br/arquivo/download/2417",
        # Leiaute 4 - Agosto de 2018
        "ecf": "http://sped.rfb.gov.br/arquivo/download/2422",
        # Versão 2.0.22 - Novembro de 2017
        "efd_icms_ipi": "http://sped.rfb.gov.br/arquivo/download/3057",
        # Versão 1.27 - Julho de 2018
        "efd_pis_cofins": "http://sped.rfb.gov.br/estatico/43/2F5A22D2A58F51DB2F40AF5501DAC4A45F74AE/Guia_Pratico_EFD_Contribuicoes_Versao_1_27.pdf",
    },
    2017: {
        # Leiaute 5 - Maio de 2017
        "ecd": "http://sped.rfb.gov.br/arquivo/download/2078",
        # Leiaute 3 - Maio de 2017
        "ecf": "http://sped.rfb.gov.br/arquivo/download/2102",
        # Versão 2.0.20 - Dezembro de 2016
        "efd_icms_ipi": "http://sped.rfb.gov.br/arquivo/download/3056",
        # Versão 1.23 - Setembro de 2017
        "efd_pis_cofins": "http://sped.rfb.gov.br/estatico/1D/5B40578A64FD1B6DE7BC9705D82AC59D4EC0BD/Guia_Pratico_EFD_Contribuicoes_Versao_1_23.pdf",
    },
    2016: {
        # Leiaute 4 - Maio de 2016
        "ecd": "http://sped.rfb.gov.br/arquivo/download/1640",
        # Leiaute 2 - Junho de 2016
        "ecf": "http://sped.rfb.gov.br/arquivo/download/1654",
        # Versão 2.0.19 - Maio de 2016
        "efd_icms_ipi": "http://sped.rfb.gov.br/arquivo/download/3055",
        # Versão 1.21 - Outubro de 2015
        "efd_pis_cofins": "http://sped.rfb.gov.br/estatico/C3/A5008A6AEC8AA7BF117AFDDCDDB8569D4B5B9D/Guia_Pratico_EFD_Contribuicoes_Versao_1.21-%20De%2015.10.2015.pdf",
    },
}

MOST_RECENT_YEAR = max(URL, key=int)
OLDEST_YEAR = min(URL, key=int)


def _download(mod, year):
    pdf = "../specs/{}.pdf".format(mod)
    url = URL[year].get(mod)
    try:
        r = requests.get(url)
    except requests.exceptions.MissingSchema:
        logger.warning(
            "  Cannot download {}'s pdf because '{}' is not a valid URL.".format(
                mod.upper(), url
            )
        )
        pass
    else:
        if not r or r.headers.get('content-type') != "application/pdf":
            logger.warning("  No pdf found at '{}' for {}.".format(url, mod.upper()))
        else:
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
            logger.info("Downloading {} pdf from {}...".format(module.upper(), year))
            _download(module, year)


if __name__ == "__main__":
    main()
