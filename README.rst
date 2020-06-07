===========
l10n_br_spec_sped
===========


Esse modulo cria os registros do SPED (ECD, ECF, EFD ICMS IPI, EFD PIS COFIN) no Odoo.


**Table of contents**

.. contents::
   :local:

Installation
============

Funciona muito melhor com o modulo web_responsive.


Usage
=====

Preencher os registros de acordo com as necessidades. As funcionalidades de export dos arquivos importacao dos registros Odoo serao implementadas futuramente.
Vc pode contatar a Akretion se quiser adequar o modulo as suas necessidades.

Known issues / Roadmap
======================

- Mapear campos boolean
- Mapear campos select
- Implementar a serializacao/deserializacao com a lib python-sped
- Implementar modulos adicionais para importar documentos electronicos com XPATH (e csv de XPATH na medida do possivel)
- implementar modulos adicionais para importar usando python ou SQL para os registros que nao tem formato XML

Changelog
=========

11.0.0.1.0 (2018-12-7)
~~~~~~~~~~~~~~~~~~~~~~~

**Features**

- Gera modelos de ECD, ECF, EFD ICMS IPI, EFD PIS COFINS



Credits
=======

Authors
~~~~~~~

* Akretion

Contributors
~~~~~~~~~~~~

* Raphaël Valyi <raphael.valyi@akretion.com.br>


Maintainers
~~~~~~~~~~~

This module is maintained by Akretion.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

.. |maintainer-sbidoul| image:: https://github.com/rvalyi.png?size=40px
    :target: https://github.com/rvalyi
    :alt: rvalyi

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
