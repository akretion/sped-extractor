============
sped_extractor
============


Esse package extrai as tabelas dos pdf das `especificações da SPED <http://sped.rfb.gov.br/pasta/show/9>`_ usando o package python `camelot`_ e cria arquivos CSV e JSON com as informações da **integralidade dos registros e campos de cada módulo**, levemente formatados para ser utilizados por outros programas.

Os módulos da SPED tratados por esse package são :

- `ECD <http://sped.rfb.gov.br/pasta/show/1569>`_
- `ECF <http://sped.rfb.gov.br/pasta/show/1644>`_
- `EFD Contribuições (PIS, COFINS) <http://sped.rfb.gov.br/pasta/show/1989>`_
- `EFD ICMS IPI <http://sped.rfb.gov.br/pasta/show/1573>`_

📚  Para cada módulo estão gerados 4 arquivos :

- *MODULE_registers.csv* : a lista detalhada dos **registros** do módulo ``MODULE``.
- *MODULE_accurate_fields.csv* : a lista das linhas dos **campos** de cada registro *como eles aparecem no pdf* das especificações (para conferir e melhorar o resultado da extração).
- *MODULE_fields.csv* : a lista dos mesmos campos porém **com atributos "interpretados"**, utilizáveis mais facilmente por outros programas.
- *MODULE_fields.json* : a mesma lista dos campos com atributos "interpretados", em **formato JSON** em vez de CSV.


**Table of contents**

.. contents::
   :local:

Arquivos extraidos
==================

=============================  ===================================  ==========================  ===========================
Registros                      CSV fiél                             CSV utilizável              JSON "tipo python-sped"
=============================  ===================================  ==========================  ===========================
ECD_registers.csv_             ECD_accurate_fields.csv_             ECD_fields.csv_             ECD_fields.json_
ECF_registers.csv_             ECF_accurate_fields.csv_             ECF_fields.csv_             ECF_fields.json_
EFD_ICMS_IPI_registers.csv_    EFD_ICMS_IPI_accurate_fields.csv_    EFD_ICMS_IPI_fields.csv_    EFD_ICMS_IPI_fields.json_
EFD_PIS_COFINS_registers.csv_  EFD_PIS_COFINS_accurate_fields.csv_  EFD_PIS_COFINS_fields.csv_  EFD_PIS_COFINS_fields.json_
=============================  ===================================  ==========================  ===========================

Instalação
============

Os scripts precisam da última versão de `camelot`_ para funcionar. Para isso precisa primeiro `instalar as dependências de camelot <https://camelot-py.readthedocs.io/en/master/user/install-deps.html>`_ ::

  $ apt install python3-tk ghostscript

E depois instalar camelot a partir do repositório github ::

  $ git clone https://www.github.com/camelot-dev/camelot
  $ cd camelot
  $ pip install ".[cv]"

Uma vez `camelot`_ instalado, é só baixar esse repositório ::

  $ git clone https://github.com/akretion/sped_extractor/

E ir na pasta *scripts/* para lançar os scripts desejados.

Utilização
==========

Depois de ter baixado esse repositório, todos os arquivos da pasta *scripts/* podem ser usados como Interface de linha de comando no terminal.

1. 📥 ``./download.sh`` : **Baixe os arquivos pdf** originais contendo as especificações da SPED :

  🔎  A opção ``--year`` permite definir a versão dos pdf do ano desejado. Se não indicar nada os pdf mais recentes serão baixados.

::

  PATH_TO/sped_extractor/scripts$ ./download.py
  Downloading ECD pdf from 2020...
  Downloading ECF pdf from 2020...
  [...]


2. ⛏️ ``./extract_csv.py`` : Use `camelot`_ para **extrair as tabelas dos pdf** e coloque os arquivos CSV extraidos na pasta */specs/MODULE/raw_camelot_csv/* :

  🔎  A opção ``--limit=n`` é facultativa para extrair apenas as tabelas das 'n' primeiras páginas.

::

  PATH_TO/sped_extractor/scripts$ ./extract_csv.py --limit=5
  Extracting tables from SPED pdf. It can take a while (easily 20 minutes)
  > ECD - 5 pages
      extracting pages 0 to 5...
  > ECF - 5 pages
      extracting pages 0 to 5...
  [...]

3. 🏗️ ``./build_csv.py`` : Percorre os CSV da pasta */specs/MODULE/raw_camelot_csv/* e **cria 3 arquivos CSV** por módulo :

  🔎  O ``./build_csv.py`` aplica linhas corretivas escritas em duro na pasta *scripts/camelot_patch/2019/* por padrão. Para não aplicar essas correções, usar a opção ``--no-patch``.

::

  PATH_TO/sped_extractor/scripts$ ./build_csv.py

  Building CSV files for ECD...
  > ecd_accurate_fields.csv
  > ecd_registers.csv
  > ecd_fields.csv

  Building CSV files for ECF...
  > ecf_accurate_fields.csv
  > ecf_registers.csv
  > ecf_fields.csv
  [...]


-------

Além desses scripts básicos, existe também o ``./build_json.py`` para **criar um arquivo JSON** por módulo com a lista dos campos com atributos "interpretados" :

  ⚠️  Como esse script usa os arquivos CSV dos campos "fiéis" criados por ``./build_csv.py`` para criar os JSON, é nécessário ter gerado esses arquivos primeiro.

::

  PATH_TO/sped_extractor/scripts$ ./build_json.py
  Building JSON files for each modules...
  > ecd_fields.json
  > ecf_fields.json
  [...]

Configuração
============

Patches
~~~~~~~

Apesar de `camelot`_ ser o melhor package python para extrair tabelas de pdf, ele não é 100% perfeito. No entanto, **é possível substituir linhas de campos extraidas incorretamente** por linhas certas registradas manualmente.

Para isso basta escrever a linha correta no arquivo *scripts/camelot_patch/2019/MODULE_camelot_patch.csv* para ela ser applicada no lugar certo no CSV *MODULE_accurate_fields.csv*.

  🔎  O ``./build_csv.py`` aplica as linhas corretivas por padrão. Para não aplicar essas correções, usar a opção ``--no-patch``.

Cabeçalhos de Módulos
~~~~~~~

Os arquivos CSV "fiéis" de cada módulo usam um cabeçalho (comum a todos os campos do módulo) escrito em duro no início de *build_csv.py*.

Para definir "manualmente" esses cabeçalhos, é possível usar o script ``./get_mod_headers.py`` que exibe no terminal todos os diferentes cabeçalhos extraídos por camelot :

::

  PATH_TO/sped_extractor/scripts$ ./get_mod_headers.py

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

Comparar sped_extractor com python-sped
~~~~~~~

python-sped_ é uma biblioteca python com a lista dos campos de cada módulo da SPED, porém escrita "manualmente" e desatualizada (ECD e ECF seguindo os pdf das especificações de 2017, EFD/ICMS-IPI e EFD/PIS-COFINS seguindo os pdf das especificações de 2015).

Apesar disso, pode ser interessante comparar essas listas de campos com as listas extraidas pelo **sped_extractor**. Para isso é só lançar o script ``./compare_ptyhon-sped.py``.

Um exemple de comparação com python-sped_ pode ser encontrada `aqui <https://gist.github.com/clementmbr/3a730276bd19f639780521777628d763>`_.


Roadmap
========

- Criar pacote python instalável com pip.
- Criar o arquivo JSON para os registros de cada módulo.
- Work on ``./build_json.py`` in order to render JSON with a real nested structure : *Block > Register > Field* (with nested Registers following their own level, following *python-sped* structure)

Créditos
=======

Autores
~~~~~~~

* Akretion

Contributores
~~~~~~~~~~~~

* Raphaël Valyi <raphael.valyi@akretion.com.br>
* Clément Mombereau <clement.mombereau@akretion.com.br>


Administradores
~~~~~~~~~~~

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

.. _ECD_fields.json: specs/2020/ecd/ecd_fields.json
.. _ECF_fields.json: specs/2020/ecf/ecf_fields.json
.. _EFD_ICMS_IPI_fields.json: specs/2020/efd_icms_ipi/efd_icms_ipi_fields.json
.. _EFD_PIS_COFINS_fields.json: specs/2020/efd_pis_cofins/efd_pis_cofins_fields.json
