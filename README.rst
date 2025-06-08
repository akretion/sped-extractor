.. image:: https://img.shields.io/pypi/v/sped-extractor.svg
    :target: https://pypi.org/project/sped-extractor/
    :alt: PyPI Version

.. image:: https://img.shields.io/github/actions/workflow/status/akretion/sped-extractor/main.yml?branch=master
    :target: https://github.com/akretion/sped-extractor/actions/workflows/main.yml
    :alt: Build Status

.. image:: https://img.shields.io/codecov/c/github/akretion/sped-extractor.svg
    :target: https://codecov.io/gh/akretion/sped-extractor
    :alt: Coverage Status

.. image:: https://img.shields.io/pypi/l/sped-extractor.svg
    :target: https://opensource.org/licenses/MIT
    :alt: License

==============
sped-extractor
==============


Esse package extrai as tabelas dos pdf das `especificações do SPED <http://sped.rfb.gov.br/pasta/show/9>`_ usando o package python `camelot-py`_ e cria arquivos CSV com as informações **dos registros e campos de cada módulo**, levemente formatados para ser utilizados por outros programas.

Os módulos da SPED tratados por esse package são :

- `ECD <http://sped.rfb.gov.br/pasta/show/1569>`_
- `ECF <http://sped.rfb.gov.br/pasta/show/1644>`_
- `EFD ICMS IPI <http://sped.rfb.gov.br/pasta/show/1573>`_
- `EFD Contribuições (PIS, COFINS) <http://sped.rfb.gov.br/pasta/show/1989>`_


📚  Para cada módulo estão gerados 4 arquivos :

- *registers.csv* : a lista detalhada dos **registros** do módulo ``MODULE``.
- *accurate_fields.csv* : a lista das linhas dos **campos** de cada registro *como eles aparecem no pdf* das especificações (para conferir e melhorar o resultado da extração).
- *fields.csv* : a lista dos mesmos campos porém **com atributos "interpretados"**, utilizáveis mais facilmente por outros programas.

📇 Uma vez ``sped-extractor`` for instalado, os campos, registros e blocos de cada módulo são facilmente accessiveis como **dicionários python**  :

>>> from spedextractor import get_fields, get_registers, get_blocks
>>> get_fields("ecd")
  [{'register': '0000', 'index': 2, 'code': 'LECD', 'desc': 'Texto fixo contendo “LECD”.', 'length': '004', 'type': 'char', 'required': True, [...]}, [...] ]



**Índice**

.. contents::
   :local:

Arquivos extraidos
==================

=============================  ==========================
Registros                      CSV utilizável
=============================  ==========================
ECD_registers.csv_             ECD_fields.csv_
ECF_registers.csv_             ECF_fields.csv_
EFD_ICMS_IPI_registers.csv_    EFD_ICMS_IPI_fields.csv_
EFD_PIS_COFINS_registers.csv_  EFD_PIS_COFINS_fields.csv_
=============================  ==========================

Instalação
============

.. code-block:: shell

  $ pip install sped-extractor


Utilização
==========

Uma vez a distribuição ``sped-extractor`` instalada, o package ``spedextractor`` está disponível com as 3 funções ``get_fields``, ``get_registers`` e ``get_blocks`` que permitem acessar aos **campos**, **registros** e **blocos** do módulo desejado :

>>> from spedextractor import get_fields, get_registers, get_blocks
>>> ecd_fields_2020 = get_fields("ecd")
  323 fields catched in ECD
>>> ecd_fields_2019 = get_fields("ecd", 2019)
  282 fields catched in ECD
>>> efd_pis_cofins_registers_2020 = get_registers("efd_pis_cofins")
  203 registers catched in EFD_PIS_COFINS

É só indicar o nome do módulo (``"ecd"``, ``"ecf"``, ``"efd_icms_ipi"`` ou ``"efd_pis_cofins"``).


Extração dos campos e registros
===============================

O package é composto de todos os scripts necessários à construção desses 4 tipos de arquivos CSV. Para usá-los e extrair as informações de novos pdfs do SPED, primeiro é necessário baixar o `repositório github <https://github.com/akretion/sped-extractor/>`_ do projeto ::

  $ git clone https://github.com/akretion/sped-extractor/

🗄️ A pasta *spedextractor/specs/* reúne **os pdf** baixados, **os CSV** extraídos, **os patches** possíveis para essas extrações além das **infos para baixar os pdf**, tudo agrupado pelo **ano de publicação** das versões dos pdf dos manuais da SPED, enquanto os outros arquivos da pasta *spedextractor/* são os scripts de extração dos dados :

::

  .
  specs
    ├── ecd/9
    |   ├── ecd.pdf
    │   ├── accurate_fields.csv
    │   ├── fields.csv
    │   └── registers.csv
    ├── ecf/10
    |   ├── ecf.pdf
    |   [...]
    ├── efd_icms_ipi/19
    |   ├── efd_icms_ipi.pdf
    |   [...]
    ├── efd_pis_cofins/6
    |   └── efd_pis_cofins.pdf
    |   [...]


Você pode lançar o script principal do package (posicionando-se na raiz do projeto *sped-extractor/*)::

  PATH/TO/sped-extractor$ python -m spedextractor

Esse script vai realizar automaticamente as 3 etapas para a construção dos arquivos CSV :

1. 📥 Baixar os pdf graça aos URLs informados (módulo ``download.py``) se for preciso.
2. ⛏️ Extrair todas as tabelas desses pdfs com `camelot`_ e colocar os CSV brutos extraidos na subpasta *MODULE/LAYOUT/raw_camelot_csv/* (módulo ``extract_tables.py``)
3. 🏗️ Construir os arquivos CSV interpretando essas tabelas brutas (módulo ``build_csv.py``)

  ⚠️ É bom verificar se o package ``sped-extractor`` não for instalado no seu ambiente de trabalho com ``pip uninstall sped-extractor`` antes de lançar o script de extração afim de evitar modificar o seu package instalado na sua pasta *lib/python3.7/site-packages/* em vez de modificar esse package baixado de github.

Obviamente os scripts ``download.py`` e ``extract_tables.py`` são utilizáveis individualmente se precisar apenas baixar ou extrair as tabelas de todos os módulos SPED: ::

  $ python -m sped-download
  $ python -m sped-extract-tables


Configuração
============

Patches
~~~~~~~

Apesar de `camelot`_ ser o melhor package python para extrair tabelas de pdf, ele não é 100% perfeito. No entanto, **é possível substituir linhas de campos extraidas incorretamente** por linhas certas registradas manualmente.

Para isso basta escrever a linha correta no arquivo *specs/MODULE/LAYOUT/camelot_patch/camelot_patch.csv* para ela ser applicada no lugar certo no CSV *accurate_fields.csv*.

  🔎  O ``spedextractor`` aplica as linhas corretivas por padrão. Para não aplicar essas correções, usar a opção ``--no-patch``.

Cabeçalhos de Módulos
~~~~~~~~~~~~~~~~~~~~~

Os arquivos CSV "fiéis" de cada módulo SPED usam um cabeçalho (comum a todos os campos do módulo) escrito em duro nas constantes ``constants.py``.

Para definir "manualmente" esses cabeçalhos, é possível usar o script ``get_table_headers.py`` que exibe no terminal todos os diferentes cabeçalhos extraídos por camelot :

::

  PATH/TO/sped-extractor$ python -m spedextractor.get_table_headers

  ECD's headers :
  ['Nº', 'Campo', 'Descrição', 'Tipo', 'Tamanho', 'Decimal']
  ['Nº', 'Campo', 'Descrição', 'Tipo', 'Tamanho', 'Decimal', 'Valores Válidos', 'Obrigatório', 'Regras de Validação do Campo']
  ['Nº', 'Campo', 'Descrição', '', 'Tipo Tamanho', 'Decimal', 'Valores Válidos', 'Obrigatório', 'Regras de Validação do Campo']
  ['Nº', 'Campo', 'Descrição', 'Tipo', 'Tamanho', 'Decimal', 'Valores Válidos', 'Obrigatório', 'Regras de Validação de Campo']

  [...]


Créditos
========

Autores
~~~~~~~

* Akretion

Contributores
~~~~~~~~~~~~~

* Raphaël Valyi <raphael.valyi@akretion.com.br>
* Clément Mombereau <clement.mombereau@akretion.com.br>


Administradores
~~~~~~~~~~~~~~~~

Esse package está administrado por `Akretion <https://akretion.com/pt-BR>`_.

.. _camelot: https://github.com/atlanhq/camelot
.. _python-sped: https://github.com/sped-br/python-sped/

.. _ECD_registers.csv: https://github.com/akretion/sped-extractor/blob/master/spedextractor/specs/ecd/9/registers.csv
.. _ECF_registers.csv: https://github.com/akretion/sped-extractor/blob/master/spedextractor/specs/ecf/9/registers.csv
.. _EFD_ICMS_IPI_registers.csv: https://github.com/akretion/sped-extractor/blob/master/spedextractor/specs/efd_icms_ipi/19/icms_ipi_registers.csv
.. _EFD_PIS_COFINS_registers.csv: https://github.com/akretion/sped-extractor/blob/master/spedextractor/specs/efd_pis_cofins/6/pis_cofins_registers.csv

.. _ECD_fields.csv: https://github.com/akretion/sped-extractor/blob/master/spedextractor/specs/2020/ecd/ecd_fields.csv
.. _ECF_fields.csv: https://github.com/akretion/sped-extractor/blob/master/spedextractor/specs/2020/ecf/ecf_fields.csv
.. _EFD_ICMS_IPI_fields.csv: https://github.com/akretion/sped-extractor/blob/master/spedextractor/specs/2020/efd_icms_ipi/efd_icms_ipi_fields.csv
.. _EFD_PIS_COFINS_fields.csv: https://github.com/akretion/sped-extractor/blob/master/spedextractor/specs/2020/efd_pis_cofins/efd_pis_cofins_fields.csv
