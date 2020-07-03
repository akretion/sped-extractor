import pathlib

from setuptools import setup
from spedextractor import __version__

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.rst").read_text()

setup(
    name="sped-extractor",
    version=__version__,
    description=(
        "Extrai e interpreta os registros e os campos das tabelas dos manuais do SPED "
        "(Sistema Público de Escrituração Digital), para os módulos "
        "ECD, ECF, EFD Contribuições (PIS, COFINS) e EFD ICMS IPI."
    ),
    long_description=README,
    long_description_content_type="text/x-rst",
    url="https://github.com/akretion/sped-extractor",
    author="Akretion",
    author_email="contact@akretion.com.br",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["spedextractor"],
    include_package_data=True,
    install_requires=[r.strip() for r in open("requirements.txt").read().splitlines()],
    setup_requires=["setuptools_scm"],
)
