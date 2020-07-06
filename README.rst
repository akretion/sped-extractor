==============
sped-extractor
==============


Esse package extrai as tabelas dos pdf das `especificações do SPED <http://sped.rfb.gov.br/pasta/show/9>`_ usando o package python `camelot`_ e cria arquivos CSV com as informações **dos registros e campos de cada módulo**, levemente formatados para ser utilizados por outros programas.

Os módulos da SPED tratados por esse package são :

- `ECD <http://sped.rfb.gov.br/pasta/show/1569>`_
- `ECF <http://sped.rfb.gov.br/pasta/show/1644>`_
- `EFD Contribuições (PIS, COFINS) <http://sped.rfb.gov.br/pasta/show/1989>`_
- `EFD ICMS IPI <http://sped.rfb.gov.br/pasta/show/1573>`_

📚  Para cada módulo estão gerados 4 arquivos :

- *MODULE_registers.csv* : a lista detalhada dos **registros** do módulo ``MODULE``.
- *MODULE_accurate_fields.csv* : a lista das linhas dos **campos** de cada registro *como eles aparecem no pdf* das especificações (para conferir e melhorar o resultado da extração).
- *MODULE_fields.csv* : a lista dos mesmos campos porém **com atributos "interpretados"**, utilizáveis mais facilmente por outros programas.
- *MODULE_pythonsped.json* : A lista dos blocos, registros e campos de cada módulo, formatada em JSON, seguindo o leiaute do package `python-sped`_ para ser utilizado por ele.

📇 Uma vez ``sped-extractor`` for instalado, os campos, registros e blocos de cada módulo são facilmente accessiveis como **dicionários python**  :

>>> from spedextractor import get_fields, get_registers, get_blocks
>>> get_fields("ecd")
  [{'register': '0000', 'index': 2, 'code': 'LECD', 'desc': 'Texto fixo contendo “LECD”.', 'length': '004', 'type': 'char', 'required': True, [...]}, [...] ]



**Índice**

.. contents::
   :local:

Arquivos extraidos
==================

=============================  ===================================  ==========================  ===========================
Registros                      CSV fiél                             CSV utilizável              JSON "tipo python-sped"
=============================  ===================================  ==========================  ===========================
ECD_registers.csv_             ECD_accurate_fields.csv_             ECD_fields.csv_             ECD_pythonsped.json_
ECF_registers.csv_             ECF_accurate_fields.csv_             ECF_fields.csv_             ECF_pythonsped.json_
EFD_ICMS_IPI_registers.csv_    EFD_ICMS_IPI_accurate_fields.csv_    EFD_ICMS_IPI_fields.csv_    EFD_ICMS_IPI_pythonsped.json_
EFD_PIS_COFINS_registers.csv_  EFD_PIS_COFINS_accurate_fields.csv_  EFD_PIS_COFINS_fields.csv_  EFD_PIS_COFINS_pythonsped.json_
=============================  ===================================  ==========================  ===========================

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

É só indicar o nome do módulo (``"ecd"``, ``"ecf"``, ``"efd_icms_ipi"`` ou ``"efd_pis_cofins"``) e o ano da versão do pdf do módulo. Se não indicar nada, o ano mais recente presente na pasta *specs/* é usado.


Extração dos campos e registros
===============================

O package é composto de todos os scripts necessários à construção desses 4 tipos de arquivos CSV e JSON. Para usá-los e extrair as informações de novos pdfs do SPED, primeiro é necessário baixar o `repositório github <https://github.com/akretion/sped-extractor/>`_ do projeto ::

  $ git clone https://github.com/akretion/sped-extractor/

🗄️ A pasta *spedextractor/specs/* reúne **os pdf** baixados, **os CSV** e JSON extraídos, **os patches** possíveis para essas extrações além das **infos para baixar os pdf**, tudo agrupado pelo **ano de publicação** das versões dos pdf dos manuais da SPED, enquanto os outros arquivos da pasta *spedextractor/* são os scripts de extração dos dados :

::

  .
  ├── spedextractor
  ├── specs
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
          │   ├── ecd_pythonsped.json
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

Para extrair as informações de uma nova versão de pdf, você precisa apenas **criar uma nova pasta** cujo nome seja o ano de publicação dessa nova versão (por exemplo ``2021/``) e contendo um arquivo ``download_info.csv`` com os URLs dos pdf para serem baixados e usados, seguindo o modelo dos arquivos atuais :

.. csv-table:: download_info.csv

  module,version,date_init,url
  ecd,8,2019-01-01,http://sped.rfb.gov.br/arquivo/download/4210
  ecf,6,2019-01-01,http://sped.rfb.gov.br/arquivo/download/4272
  efd_icms_ipi,3.0.3,2019-01-01,http://sped.rfb.gov.br/arquivo/download/4202
  efd_pis_cofins,1.33,2019-01-01,http://sped.rfb.gov.br/arquivo/download/4263

.. epigraph::

  ⚠️ É importante diferenciar o *ano de publicação* de um manual (número da pasta contendo os pdf e os arquivos extraidos) da *data de início* de validade do manual (o ``date_init`` indicado no arquivo ``download_info.csv``).

  Por exemplo, o package `python-sped`_ chama de *ecd_2017.json* o leiaute do manual para ser usado a partir do 01/01/2017 enquanto nós achamos que faz mais sentido colocar esse mesmo manual na pasta ``specs/2018/`` porque ele foi divulgado em 2018.

Uma vez que essa pasta e esse arquivo forem criados, você pode lançar o script principal do package (posicionando-se na raiz do projeto *sped-extractor/*)::

  PATH/TO/sped-extractor$ python -m spedextractor

Se a pasta com o arquivo ``download_info.csv`` for realmente vazia, ele vai realizar automaticamente as 3 etapas para a construção dos arquivos CSV :

1. 📥 Baixar os pdf graça aos URLs informados (módulo ``download.py``)
2. ⛏️ Extrair todas as tabelas desses pdfs com `camelot`_ e colocar os CSV brutos extraidos na subpasta *MODULE/raw_camelot_csv/* (módulo ``extract_tables.py``)
3. 🏗️ Construir os arquivos CSV interpretando essas tabelas brutas (módulo ``build_csv.py``)

  ⚠️ É bom verificar se o package ``sped-extractor`` não for instalado no seu ambiente de trabalho com ``pip uninstall sped-extractor`` antes de lançar o script de extração afim de evitar modificar o seu package instalado na sua pasta *lib/python3.7/site-packages/* em vez de modificar esse package baixado de github.

Se o número da nova pasta for anterior ao ano mais recente da pasta *specs/*, é necessário indicar ao script em que pasta ele tem que trabalhar com a opção ``--year``, por exemplo ::

  $ python -m spedextractor --year=2018

Obviamente os scripts ``download.py`` e ``extract_tables.py`` são utilizáveis individualmente se precisar apenas baixar ou extrair as tabelas de todos os módulos SPED: ::

  $ python -m spedextractor.download
  $ python -m spedextractor.extract_tables

-------

Além desses scripts principais construindo os arquivos CSV, existe também o ``build_pythonsped_json.py`` para **criar um arquivo JSON "tipo python-sped"** por módulo com todos os campos aninhados nos seus registros respectivos ::

  $ python -m spedextractor.build_pythonsped_json

...adicionando a opção ``--year`` se precisar.

Configuração
============

Patches
~~~~~~~

Apesar de `camelot`_ ser o melhor package python para extrair tabelas de pdf, ele não é 100% perfeito. No entanto, **é possível substituir linhas de campos extraidas incorretamente** por linhas certas registradas manualmente.

Para isso basta escrever a linha correta no arquivo *specs/YEAR/camelot_patch/MODULE_camelot_patch.csv* para ela ser applicada no lugar certo no CSV *MODULE_accurate_fields.csv*.

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

Comparar sped-extractor com python-sped
=======================================

python-sped_ é uma biblioteca python com a lista dos campos de cada módulo da SPED, porém escrita "manualmente" e desatualizada (ECD e ECF seguindo os pdf das especificações de 2017, EFD/ICMS-IPI e EFD/PIS-COFINS seguindo os pdf das especificações de 2015).

Apesar disso, pode ser interessante comparar essas listas de campos com as listas extraidas pelo **sped-extractor**. Para isso é só lançar o script ``compare_pythonsped.py`` ::

  $ python -m spedextractor.compare_pythonsped

Um exemplo de comparação com python-sped_ pode ser encontrado `aqui <https://gist.github.com/clementmbr/d422c02c52e1bbae7d2972475b363ea2>`_.

  🔎  Para detalhar as listas dos campos faltando em cada modelo, adicionar a opção ``--detail``.

Roadmap
========

- Adicionar colonas de mapping com ERP externos nos arquivos CSV.
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

.. _ECD_registers.csv: https://github.com/akretion/sped-extractor/blob/master/spedextractor/specs/2020/ecd/ecd_registers.csv
.. _ECF_registers.csv: https://github.com/akretion/sped-extractor/blob/master/spedextractor/specs/2020/ecf/ecf_registers.csv
.. _EFD_ICMS_IPI_registers.csv: https://github.com/akretion/sped-extractor/blob/master/spedextractor/specs/2020/efd_icms_ipi/efd_icms_ipi_registers.csv
.. _EFD_PIS_COFINS_registers.csv: https://github.com/akretion/sped-extractor/blob/master/spedextractor/specs/2020/efd_pis_cofins/efd_pis_cofins_registers.csv

.. _ECD_accurate_fields.csv: https://github.com/akretion/sped-extractor/blob/master/spedextractor/specs/2020/ecd/ecd_accurate_fields.csv
.. _ECF_accurate_fields.csv: https://github.com/akretion/sped-extractor/blob/master/spedextractor/specs/2020/ecf/ecf_accurate_fields.csv
.. _EFD_ICMS_IPI_accurate_fields.csv: https://github.com/akretion/sped-extractor/blob/master/spedextractor/specs/2020/efd_icms_ipi/efd_icms_ipi_accurate_fields.csv
.. _EFD_PIS_COFINS_accurate_fields.csv: https://github.com/akretion/sped-extractor/blob/master/spedextractor/specs/2020/efd_pis_cofins/efd_pis_cofins_accurate_fields.csv

.. _ECD_fields.csv: https://github.com/akretion/sped-extractor/blob/master/spedextractor/specs/2020/ecd/ecd_fields.csv
.. _ECF_fields.csv: https://github.com/akretion/sped-extractor/blob/master/spedextractor/specs/2020/ecf/ecf_fields.csv
.. _EFD_ICMS_IPI_fields.csv: https://github.com/akretion/sped-extractor/blob/master/spedextractor/specs/2020/efd_icms_ipi/efd_icms_ipi_fields.csv
.. _EFD_PIS_COFINS_fields.csv: https://github.com/akretion/sped-extractor/blob/master/spedextractor/specs/2020/efd_pis_cofins/efd_pis_cofins_fields.csv

.. _ECD_pythonsped.json: https://github.com/akretion/sped-extractor/blob/master/spedextractor/specs/2020/ecd/ecd_pythonsped.json
.. _ECF_pythonsped.json: https://github.com/akretion/sped-extractor/blob/master/spedextractor/specs/2020/ecf/ecf_pythonsped.json
.. _EFD_ICMS_IPI_pythonsped.json: https://github.com/akretion/sped-extractor/blob/master/spedextractor/specs/2020/efd_icms_ipi/efd_icms_ipi_pythonsped.json
.. _EFD_PIS_COFINS_pythonsped.json: https://github.com/akretion/sped-extractor/blob/master/spedextractor/specs/2020/specs/2020/efd_pis_cofins/efd_pis_cofins_pythonsped.json
