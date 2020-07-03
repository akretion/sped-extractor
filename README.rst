==============
sped-extractor
==============


Esse package extrai as tabelas dos pdf das `especificações da SPED <http://sped.rfb.gov.br/pasta/show/9>`_ usando o package python `camelot`_ e cria arquivos CSV com as informações **dos registros e campos de cada módulo**, levemente formatados para ser utilizados por outros programas.

Os módulos da SPED tratados por esse package são :

- `ECD <http://sped.rfb.gov.br/pasta/show/1569>`_
- `ECF <http://sped.rfb.gov.br/pasta/show/1644>`_
- `EFD Contribuições (PIS, COFINS) <http://sped.rfb.gov.br/pasta/show/1989>`_
- `EFD ICMS IPI <http://sped.rfb.gov.br/pasta/show/1573>`_

📚  Para cada módulo estão gerados 4 arquivos :

- *MODULE_registers.csv* : a lista detalhada dos **registros** do módulo ``MODULE``.
- *MODULE_accurate_fields.csv* : a lista das linhas dos **campos** de cada registro *como eles aparecem no pdf* das especificações (para conferir e melhorar o resultado da extração).
- *MODULE_fields.csv* : a lista dos mesmos campos porém **com atributos "interpretados"**, utilizáveis mais facilmente por outros programas.
- *MODULE_python-sped.json* : A lista dos blocos, registros e campos de cada módulo, formatada em JSON, seguindo o leiaute do package `python-sped`_ para ser utilizado por ele.


**Table of contents**

.. contents::
   :local:

Arquivos extraidos
==================

=============================  ===================================  ==========================  ===========================
Registros                      CSV fiél                             CSV utilizável              JSON "tipo python-sped"
=============================  ===================================  ==========================  ===========================
ECD_registers.csv_             ECD_accurate_fields.csv_             ECD_fields.csv_             ECD_python-sped.json_
ECF_registers.csv_             ECF_accurate_fields.csv_             ECF_fields.csv_             ECF_python-sped.json_
EFD_ICMS_IPI_registers.csv_    EFD_ICMS_IPI_accurate_fields.csv_    EFD_ICMS_IPI_fields.csv_    EFD_ICMS_IPI_python-sped.json_
EFD_PIS_COFINS_registers.csv_  EFD_PIS_COFINS_accurate_fields.csv_  EFD_PIS_COFINS_fields.csv_  EFD_PIS_COFINS_python-sped.json_
=============================  ===================================  ==========================  ===========================

Instalação
============

O package ``spedextractor`` da última versão de `camelot`_ para funcionar. Para isso precisa primeiro `instalar as dependências de camelot <https://camelot-py.readthedocs.io/en/master/user/install-deps.html>`_ ::

  $ apt install python3-tk ghostscript

E depois instalar camelot a partir do repositório github ::

  $ git clone https://www.github.com/camelot-dev/camelot
  $ cd camelot
  $ pip install ".[cv]"

Uma vez `camelot`_ instalado, é só baixar esse repositório ::

  $ git clone https://github.com/akretion/sped-extractor/

A pasta *spedextractor/* reúne os scripts para baixar e extrair os registros e campos de cada módulo SPED enquanto a pasta *specs/* reúne **os pdf** baixados, **os CSV** e JSON extraídos, **os patches** possíveis para essas extrações além das **infos para baixar os pdf**, agrupados pelo **ano de publicação** das versões dos pdf dos manuais da SPED :

::

  .
  ├── spedextractor
  |   [...]
  └── specs
      ├── 2019
      |   [...]
      └── 2020
          ├── camelot_patch
          │   ├── ecd_camelot_patch.csv
          |   [...]
          ├── download_info.csv
          ├── ecd
          │   ├── ecd_accurate_fields.csv
          │   ├── ecd_fields.csv
          │   ├── ecd_python-sped.json
          │   └── ecd_registers.csv
          ├── ecf
          |   [...]
          ├── efd_icms_ipi
          |   [...]
          ├── efd_pis_cofins
          |   [...]
          └── pdf
              ├── ecd.pdf
              ├── ecf.pdf
              ├── efd_icms_ipi.pdf
              └── efd_pis_cofins.pdf

Utilização
==========

Depois de ter baixado esse repositório, todos os arquivos da pasta *spedextractor/* podem ser usados como Interface de linha de comando no terminal.

1. 📥 ``./download.sh`` : **Baixe os arquivos pdf** originais contendo as especificações da SPED :

  A opção ``--year`` permite definir a versão dos pdf do ano desejado. Se não indicar nada os pdf os mais recentes serão baixados.

::

  PATH_TO/sped-extractor/spedextractor$ $ ./download.py --year=2019
  Downloading pdf ECD 2019...
  Downloading pdf ECF 2019...
  Downloading pdf EFD_ICMS_IPI 2019...
  Downloading pdf EFD_PIS_COFINS 2019...

Os links usados para baixar esses pdf se encontram no arquivo *download_info.csv* na pasta do ano de publicação das versões dos pdf a baixar.

  ⚠️  É importante diferenciar o ano de *publicação* dos manuais do ano de *aplicação* desses manuais. Assim, os pdf baixados na pasta **2020/** correspondem às tabelas para serem usadas principalmente no ano-calendário de **2019** (informação anotada na colona ``date_init`` do arquivo *download_info.csv*).


2. ⛏️ ``./extract_csv.py`` : Use `camelot`_ para **extrair as tabelas dos pdf** e coloque os arquivos CSV extraidos na pasta */specs/YEAR/MODULE/raw_camelot_csv/* :

  A opção ``--limit=n`` é facultativa para extrair apenas as tabelas das 'n' primeiras páginas.

::

  PATH_TO/sped-extractor/spedextractor$ ./extract_csv.py --limit=5
  Extracting tables from SPED pdf. It can take a while (easily 20 minutes)
  > ECD - 5 pages
      extracting pages 0 to 5...
  > ECF - 5 pages
      extracting pages 0 to 5...
  [...]

3. 🏗️ ``./build_csv.py`` : Percorre os CSV da pasta */specs/MODULE/raw_camelot_csv/* e **cria 3 arquivos CSV** por módulo :

  O ``./build_csv.py`` aplica linhas corretivas escritas em duro na pasta *spedextractor/YEAR/camelot_patch/* por padrão. Para não aplicar essas correções, usar a opção ``--no-patch``.

::

  PATH_TO/sped-extractor/spedextractor$ ./build_csv.py --no-patch

  Building CSV files for ECD 2020...
  > ecd_accurate_fields.csv
  > ecd_registers.csv
      70 registers catched in ECD
  > ecd_fields.csv
      323 fields catched in ECD

  Building CSV files for ECF 2020...
  > ecf_accurate_fields.csv
  > ecf_registers.csv
      179 registers catched in ECF
  > ecf_fields.csv
      903 fields catched in ECF

  [...]


-------

Além desses scripts básicos, existe também o ``./build_python-sped_json.py`` para **criar um arquivo JSON "tipo python-sped"** por módulo com a lista dos campos com atributos "interpretados" :

  ⚠️  Da mesma maneira que para usar ``./build_csv.py``, é necessário extrair primeiro as tabelas dos pdf com ``./extract_csv.py`` antes de usar ``./build_python-sped_json.py``

::

  PATH_TO/sped-extractor/spedextractor$ ./build_python-sped_json.py
  Building JSON files for each modules...
  > ecd_python-sped.json
  > ecf_python-sped.json
  [...]

Configuração
============

Patches
~~~~~~~

Apesar de `camelot`_ ser o melhor package python para extrair tabelas de pdf, ele não é 100% perfeito. No entanto, **é possível substituir linhas de campos extraidas incorretamente** por linhas certas registradas manualmente.

Para isso basta escrever a linha correta no arquivo *spedextractor/YEAR/camelot_patch/MODULE_camelot_patch.csv* para ela ser applicada no lugar certo no CSV *MODULE_accurate_fields.csv*.

  🔎  O ``./build_csv.py`` aplica as linhas corretivas por padrão. Para não aplicar essas correções, usar a opção ``--no-patch``.

Cabeçalhos de Módulos
~~~~~~~~~~~~~~~~~~~~~

Os arquivos CSV "fiéis" de cada módulo usam um cabeçalho (comum a todos os campos do módulo) escrito em duro no início de *build_csv.py*.

Para definir "manualmente" esses cabeçalhos, é possível usar o script ``./get_mod_headers.py`` que exibe no terminal todos os diferentes cabeçalhos extraídos por camelot :

::

  PATH_TO/sped-extractor/spedextractor$ ./get_mod_headers.py

  ECD's headers :
  ['Nº', 'Campo', 'Descrição', 'Tipo', 'Tamanho', 'Decimal']
  ['Nº', 'Campo', 'Descrição', 'Tipo', 'Tamanho', 'Decimal', 'Valores Válidos', 'Obrigatório', 'Regras de Validação do Campo']
  ['Nº', 'Campo', 'Descrição', '', 'Tipo Tamanho', 'Decimal', 'Valores Válidos', 'Obrigatório', 'Regras de Validação do Campo']
  ['Nº', 'Campo', 'Descrição', 'Tipo', 'Tamanho', 'Decimal', 'Valores Válidos', 'Obrigatório', 'Regras de Validação de Campo']

  ECF's headers :
  ['Nº', 'Campo', 'Descrição', 'Tipo', '', 'Tamanho Decimal', 'Valores Válidos', 'Obrigatório']
  ['Nº', 'Campo', 'Descrição', 'Tipo', 'Tamanho', 'Decimal', 'Valores Válidos', 'Obrigatório']
  ['Nº', 'Campo', 'Descrição', 'Tipo', 'Tamanho Decimal', '', 'Valores Válidos', 'Obrigatório']
  ['Nº', 'Campo', 'Descrição', 'Tipo', '', 'Tamanho Decimal', '', 'Valores Válidos Obrigatório']

  [...]

Comparar sped-extractor com python-sped
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

python-sped_ é uma biblioteca python com a lista dos campos de cada módulo da SPED, porém escrita "manualmente" e desatualizada (ECD e ECF seguindo os pdf das especificações de 2017, EFD/ICMS-IPI e EFD/PIS-COFINS seguindo os pdf das especificações de 2015).

Apesar disso, pode ser interessante comparar essas listas de campos com as listas extraidas pelo **sped-extractor**. Para isso é só lançar o script ``./compare_ptyhon-sped.py``.

Um exemple de comparação com python-sped_ pode ser encontrada `aqui <https://gist.github.com/clementmbr/d422c02c52e1bbae7d2972475b363ea2>`_.

  🔎  Para detalhar as listas dos campos faltando em cada modelo, usar a opção ``--detail``.

Roadmap
========

- Criar pacote python instalável com pip.
- Melhorar o arquivo JSON "tipo python-sped" (valor dos itens "regras" e "campos_chave" dos registros)

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

.. _ECD_registers.csv: specs/2020/ecd/ecd_registers.csv
.. _ECF_registers.csv: specs/2020/ecf/ecf_registers.csv
.. _EFD_ICMS_IPI_registers.csv: specs/2020/efd_icms_ipi/efd_icms_ipi_registers.csv
.. _EFD_PIS_COFINS_registers.csv: specs/2020/efd_pis_cofins/efd_pis_cofins_registers.csv

.. _ECD_accurate_fields.csv: specs/2020/ecd/ecd_accurate_fields.csv
.. _ECF_accurate_fields.csv: specs/2020/ecf/ecf_accurate_fields.csv
.. _EFD_ICMS_IPI_accurate_fields.csv: specs/2020/efd_icms_ipi/efd_icms_ipi_accurate_fields.csv
.. _EFD_PIS_COFINS_accurate_fields.csv: specs/2020/efd_pis_cofins/efd_pis_cofins_accurate_fields.csv

.. _ECD_fields.csv: specs/2020/ecd/ecd_fields.csv
.. _ECF_fields.csv: specs/2020/ecf/ecf_fields.csv
.. _EFD_ICMS_IPI_fields.csv: specs/2020/efd_icms_ipi/efd_icms_ipi_fields.csv
.. _EFD_PIS_COFINS_fields.csv: specs/2020/efd_pis_cofins/efd_pis_cofins_fields.csv

.. _ECD_python-sped.json: specs/2020/ecd/ecd_python-sped.json
.. _ECF_python-sped.json: specs/2020/ecf/ecf_python-sped.json
.. _EFD_ICMS_IPI_python-sped.json: specs/2020/efd_icms_ipi/efd_icms_ipi_python-sped.json
.. _EFD_PIS_COFINS_python-sped.json: specs/2020/efd_pis_cofins/efd_pis_cofins_python-sped.json
