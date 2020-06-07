from odoo import fields, models

from . import spec_models


class Registro0000(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.0000"
    _description = u"""Abertura do Arquivo Digital e Identificação da entidade"""
    _inherit = "l10n.br.sped.mixin"
    cod_ver = fields.Integer("COD_VER", required=True)
    cod_fin = fields.Integer("Código da finalidade do arquivo", required=True)
    dt_ini = fields.Integer(
        "Data inicial das informações contidas no arquivo", required=True
    )
    dt_fin = fields.Integer(
        "Data final das informações contidas no arquivo", required=True
    )
    nome = fields.Char(
        "Nome empresarial da entidade.",
        required=True,
        help="""Nome empresarial da entidade.
Ver pagina 25""",
    )
    cnpj = fields.Integer("Número de inscrição da entidade no CNPJ*")
    cpf = fields.Integer("Número de inscrição da entidade no CPF.*")
    uf = fields.Char(
        "Sigla da unidade da federação da entidade",
        required=True,
        help="""Sigla da unidade da federação da entidade.
Ver pagina 25""",
    )
    ie = fields.Char(
        "Inscrição Estadual da entidade.",
        required=True,
        help="""Inscrição Estadual da entidade.
Ver pagina 25""",
    )
    cod_mun = fields.Integer("COD_MUN", required=True)
    im = fields.Char(
        "Inscrição Municipal da entidade.*",
        help="""Inscrição Municipal da entidade.
Ver pagina 25""",
    )
    suframa = fields.Char(
        "Inscrição da entidade na SUFRAMA*",
        help="""Inscrição da entidade na SUFRAMA
Ver pagina 25""",
    )
    ind_perfil = fields.Char(
        "IND_PERFIL",
        required=True,
        help="""Perfil de apresentação do arquivo fiscal;A – Perfil A;B – Perfil B.;C – Perfil C.
Ver pagina 25""",
    )
    ind_ativ = fields.Integer("Indicador de tipo de atividade", required=True)


class Registro0005(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.0005"
    _description = u"""Dados Complementares da entidade"""
    _inherit = "l10n.br.sped.mixin"
    fantasia = fields.Char(
        "Nome de fantasia associado ao nome empresarial",
        required=True,
        help="""Nome de fantasia associado ao nome empresarial.
Ver pagina 27""",
    )
    cep = fields.Integer("Código de Endereçamento Postal.", required=True)
    end = fields.Char(
        "Logradouro e endereço do imóvel.",
        required=True,
        help="""Logradouro e endereço do imóvel.
Ver pagina 27""",
    )
    num = fields.Char(
        "Número do imóvel.*",
        help="""Número do imóvel.
Ver pagina 27""",
    )
    compl = fields.Char(
        "Dados complementares do endereço.*",
        help="""Dados complementares do endereço.
Ver pagina 27""",
    )
    bairro = fields.Char(
        "Bairro em que o imóvel está situado.",
        required=True,
        help="""Bairro em que o imóvel está situado.
Ver pagina 27""",
    )
    fone = fields.Char(
        "Número do telefone (DDD+FONE).*",
        help="""Número do telefone (DDD+FONE).
Ver pagina 27""",
    )
    fax = fields.Char(
        "Número do fax.*",
        help="""Número do fax.
Ver pagina 27""",
    )
    email = fields.Char(
        "Endereço do correio eletrônico.*",
        help="""Endereço do correio eletrônico.
Ver pagina 27""",
    )


class Registro0015(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.0015"
    _description = (
        u"""Dados do Contribuinte Substituto ou Responsável pelo ICMS Destino"""
    )
    _inherit = "l10n.br.sped.mixin"
    uf_st = fields.Char(
        "UF_ST",
        required=True,
        help="""Sigla da unidade da federação do contribuinte substituídoou   unidade   de   federação   do   consumidor   final   nãocontribuinte - ICMS Destino EC 87/15.
Ver pagina 27""",
    )
    ie_st = fields.Char(
        "IE_ST",
        required=True,
        help="""Inscrição Estadual do contribuinte substituto na unidadeda federação do contribuinte substituído ou unidade defederação do consumidor final não contribuinte - ICMSDestino EC 87/15.
Ver pagina 27""",
    )


class Registro0100(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.0100"
    _description = u"""Dados do Contabilista"""
    _inherit = "l10n.br.sped.mixin"
    nome = fields.Char(
        "Nome do contabilista.",
        required=True,
        help="""Nome do contabilista.
Ver pagina 28""",
    )
    cpf = fields.Integer("Número de inscrição do contabilista no CPF", required=True)
    crc = fields.Char(
        "CRC",
        required=True,
        help="""Número   de   inscrição   do   contabilista   no   ConselhoRegional de Contabilidade.
Ver pagina 28""",
    )
    cnpj = fields.Integer("CNPJ*")
    cep = fields.Integer("Código de Endereçamento Postal.*")
    end = fields.Char(
        "Logradouro e endereço do imóvel.*",
        help="""Logradouro e endereço do imóvel.
Ver pagina 28""",
    )
    num = fields.Char(
        "Número do imóvel.*",
        help="""Número do imóvel.
Ver pagina 28""",
    )
    compl = fields.Char(
        "Dados complementares do endereço.*",
        help="""Dados complementares do endereço.
Ver pagina 28""",
    )
    bairro = fields.Char(
        "Bairro em que o imóvel está situado.*",
        help="""Bairro em que o imóvel está situado.
Ver pagina 28""",
    )
    fone = fields.Char(
        "Número do telefone (DDD+FONE).*",
        help="""Número do telefone (DDD+FONE).
Ver pagina 28""",
    )
    fax = fields.Char(
        "Número do fax.*",
        help="""Número do fax.
Ver pagina 28""",
    )
    email = fields.Char(
        "Endereço do correio eletrônico.",
        required=True,
        help="""Endereço do correio eletrônico.
Ver pagina 28""",
    )
    cod_mun = fields.Integer("Código do município, conforme tabela IBGE", required=True)


class Registro0150(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.0150"
    _description = u"""Tabela de Cadastro do Participante"""
    _inherit = "l10n.br.sped.mixin"
    cod_part = fields.Char(
        "Código de identificação do participante no arquivo",
        required=True,
        help="""Código de identificação do participante no arquivo.
Ver pagina 29""",
    )
    nome = fields.Char(
        "Nome pessoal ou empresarial do participante",
        required=True,
        help="""Nome pessoal ou empresarial do participante.
Ver pagina 29""",
    )
    cod_pais = fields.Integer("COD_PAIS", required=True)
    cnpj = fields.Integer("CNPJ do participante.*")
    cpf = fields.Integer("CPF do participante.*")
    ie = fields.Char(
        "Inscrição Estadual do participante.*",
        help="""Inscrição Estadual do participante.
Ver pagina 29""",
    )
    cod_mun = fields.Integer("Código do município, conforme a tabela IBGE*")
    suframa = fields.Char(
        "Número de inscrição do participante na SUFRAMA*",
        help="""Número de inscrição do participante na SUFRAMA.
Ver pagina 29""",
    )
    end = fields.Char(
        "Logradouro e endereço do imóvel",
        required=True,
        help="""Logradouro e endereço do imóvel
Ver pagina 29""",
    )
    num = fields.Char(
        "Número do imóvel*",
        help="""Número do imóvel
Ver pagina 29""",
    )
    compl = fields.Char(
        "Dados complementares do endereço*",
        help="""Dados complementares do endereço
Ver pagina 29""",
    )
    bairro = fields.Char(
        "Bairro em que o imóvel está situado*",
        help="""Bairro em que o imóvel está situado
Ver pagina 29""",
    )
    reg_0175_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.0175",
        "parent_0150_id",
        string="Alteração da Tabela de Cadastro de Participante",
        help="Bloco 0",
    )


class Registro0175(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.0175"
    _description = u"""Alteração da Tabela de Cadastro de Participante"""
    _inherit = "l10n.br.sped.mixin"
    dt_alt = fields.Integer("Data de alteração do cadastro", required=True)
    nr_campo = fields.Char(
        "Número do campo alterado (campos 03 a 13, exceto 07)",
        required=True,
        help="""Número do campo alterado (campos 03 a 13, exceto 07)
Ver pagina 30""",
    )
    cont_ant = fields.Char(
        "Conteúdo anterior do campo",
        required=True,
        help="""Conteúdo anterior do campo
Ver pagina 30""",
    )
    parent_0150_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.0150", string="Tabela de Cadastro do Participante"
    )


class Registro0190(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.0190"
    _description = u"""Identificação das unidades de medida"""
    _inherit = "l10n.br.sped.mixin"
    unid = fields.Char(
        "Código da unidade de medida",
        required=True,
        help="""Código da unidade de medida
Ver pagina 31""",
    )
    descr = fields.Char(
        "Descrição da unidade de medida",
        required=True,
        help="""Descrição da unidade de medida
Ver pagina 31""",
    )


class Registro0200(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.0200"
    _description = u"""Tabela de Identificação do Item (Produtos e Serviços)"""
    _inherit = "l10n.br.sped.mixin"
    cod_item = fields.Char(
        "Código do item",
        required=True,
        help="""Código do item
Ver pagina 31""",
    )
    descr_item = fields.Char(
        "Descrição do item",
        required=True,
        help="""Descrição do item
Ver pagina 31""",
    )
    cod_barra = fields.Char(
        "COD_BARRA*",
        help="""Representação   alfanumérico   do   código   de   barra   doproduto, se houver
Ver pagina 31""",
    )
    reg_0206_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.0206",
        string="Código de produto conforme Tabela ANP",
        help="Bloco 0",
    )  # m2o
    reg_0205_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.0205",
        "parent_0200_id",
        string="Alteração do Item",
        help="Bloco 0",
    )
    reg_0210_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.0210",
        "parent_0200_id",
        string="Consumo Específico Padronizado",
        help="Bloco 0",
    )
    reg_0220_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.0220",
        "parent_0200_id",
        string="Fatores de Conversão de Unidades",
        help="Bloco 0",
    )


class Registro0205(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.0205"
    _description = u"""Alteração do Item"""
    _inherit = "l10n.br.sped.mixin"
    parent_0200_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.0200",
        string="Tabela de Identificação do Item (Produtos e Serviços)",
    )


class Registro0206(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.0206"
    _description = u"""Código de produto conforme Tabela ANP"""
    _inherit = "l10n.br.sped.mixin"
    cod_comb = fields.Char(
        "Código do produto, conforme tabela publicada pela ANP",
        required=True,
        help="""Código do produto, conforme tabela publicada pela ANP
Ver pagina 34""",
    )


class Registro0210(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.0210"
    _description = u"""Consumo Específico Padronizado"""
    _inherit = "l10n.br.sped.mixin"
    cod_item_comp = fields.Char(
        "Código do item componente/insumo (campo02 do Registro 0200)",
        required=True,
        help="""Código do item componente/insumo (campo02 do Registro 0200)
Ver pagina 35""",
    )
    qtd_comp = fields.Integer("QTD_COMP", required=True)
    perda = fields.Integer("PERDA", required=True)
    parent_0200_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.0200",
        string="Tabela de Identificação do Item (Produtos e Serviços)",
    )


class Registro0220(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.0220"
    _description = u"""Fatores de Conversão de Unidades"""
    _inherit = "l10n.br.sped.mixin"
    unid_conv = fields.Char(
        "UNID_CONV",
        required=True,
        help="""Unidade   comercial   a   ser   convertida   na   unidade   deestoque, referida no registro 0200.
Ver pagina 36""",
    )
    fat_conv = fields.Integer("Fator   de   conversão", required=True)
    parent_0200_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.0200",
        string="Tabela de Identificação do Item (Produtos e Serviços)",
    )


class Registro0300(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.0300"
    _description = u"""Cadastro de bens ou componentes do Ativo Imobilizado"""
    _inherit = "l10n.br.sped.mixin"
    cod_ind_bem = fields.Char(
        "COD_IND_BEM",
        required=True,
        help="""Código   individualizado   do   bem   ou   componenteadotado no controle patrimonial do estabelecimentoinformante
Ver pagina 36""",
    )
    ident_merc = fields.Char(
        "Identificação do tipo de mercadoria",
        required=True,
        help="""Identificação do tipo de mercadoria:1 = bem;2 = componente.
Ver pagina 36""",
    )
    descr_item = fields.Char(
        "DESCR_ITEM",
        required=True,
        help="""Descrição do bem ou componente (modelo, marca eoutras características necessárias a suaindividualização)
Ver pagina 36""",
    )
    cod_prnc = fields.Char(
        "COD_PRNC*",
        help="""Código de cadastro do bem principal nos casos emque   o   bem   ou   componente   (   campo   02)   estejavinculado a um bem principal.
Ver pagina 36""",
    )
    cod_cta = fields.Char(
        "COD_CTA",
        required=True,
        help="""Código da conta analítica de contabilização do bemou componente (campo 06 do Registro 0500)
Ver pagina 36""",
    )
    nr_parc = fields.Integer("NR_PARC*")
    reg_0305_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.0305",
        string="Informação sobre a Utilização do Bem",
        help="Bloco 0",
    )  # m2o


class Registro0305(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.0305"
    _description = u"""Informação sobre a Utilização do Bem"""
    _inherit = "l10n.br.sped.mixin"
    cod_ccus = fields.Char(
        "COD_CCUS",
        required=True,
        help="""Código do centro de custo onde o bem está sendo ou seráutilizado (campo 03 do Registro 0600)
Ver pagina 37""",
    )
    func = fields.Char(
        "FUNC",
        required=True,
        help="""Descrição   sucinta   da função   do   bem   na   atividade   doestabelecimento
Ver pagina 37""",
    )
    vida_util = fields.Integer("Vida útil estimada do bem, em número de meses*")


class Registro0400(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.0400"
    _description = u"""Tabela de Natureza da Operação/ Prestação"""
    _inherit = "l10n.br.sped.mixin"
    cod_nat = fields.Char(
        "Código da natureza da operação/prestação",
        required=True,
        help="""Código da natureza da operação/prestação
Ver pagina 38""",
    )
    descr_nat = fields.Char(
        "Descrição da natureza da operação/prestação",
        required=True,
        help="""Descrição da natureza da operação/prestação
Ver pagina 38""",
    )


class Registro0450(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.0450"
    _description = u"""Tabela de Informação Complementar do documento fiscal"""
    _inherit = "l10n.br.sped.mixin"
    cod_inf = fields.Char(
        "Código   da   informação   complementar   do   documentofiscal",
        required=True,
        help="""Código   da   informação   complementar   do   documentofiscal.
Ver pagina 38""",
    )
    txt = fields.Char(
        "TXT",
        required=True,
        help="""Texto livre  da  informação   complementar  existente  nodocumento   fiscal,   inclusive   espécie   de  normas   legais,poder   normativo,   número,   capitulação,   data   e   demaisreferências   pertinentes   com   indicação   referentes   aotributo.
Ver pagina 38""",
    )


class Registro0460(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.0460"
    _description = u"""Tabela de Observações do Lançamento Fiscal"""
    _inherit = "l10n.br.sped.mixin"
    cod_obs = fields.Char(
        "Código da Observação do lançamento fiscal",
        required=True,
        help="""Código da Observação do lançamento fiscal.
Ver pagina 39""",
    )
    txt = fields.Char(
        "Descrição da observação vinculada ao lançamento  fiscal",
        required=True,
        help="""Descrição da observação vinculada ao lançamento  fiscal
Ver pagina 39""",
    )


class Registro0500(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.0500"
    _description = u"""Plano de contas contábeis"""
    _inherit = "l10n.br.sped.mixin"
    dt_alt = fields.Integer("Data da inclusão/alteração", required=True)
    cod_nat_cc = fields.Char(
        "Código da natureza da conta/grupo de contas",
        required=True,
        help="""Código da natureza da conta/grupo de contas: 01 - Contas de ativo; 02 - Contas de passivo; 03 - Patrimônio líquido; 04 - Contas de resultado; 05 - Contas de compensação; 09 - Outras.
Ver pagina 39""",
    )
    ind_cta = fields.Char(
        "Indicador do tipo de conta",
        required=True,
        help="""Indicador do tipo de conta: S - Sintética (grupo de contas); A - Analítica (conta).
Ver pagina 39""",
    )
    nivel = fields.Integer("Nível da conta analítica/grupo de contas", required=True)
    cod_cta = fields.Char(
        "Código da conta analítica/grupo de contas",
        required=True,
        help="""Código da conta analítica/grupo de contas.
Ver pagina 39""",
    )
    nome_cta = fields.Char(
        "Nome da conta analítica/grupo de contas",
        required=True,
        help="""Nome da conta analítica/grupo de contas.
Ver pagina 39""",
    )


class Registro0600(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.0600"
    _description = u"""Centro de custos"""
    _inherit = "l10n.br.sped.mixin"
    dt_alt = fields.Integer("Data da inclusão/alteração.", required=True)
    cod_ccus = fields.Char(
        "Código do centro de custos.",
        required=True,
        help="""Código do centro de custos.
Ver pagina 40""",
    )
    ccus = fields.Char(
        "Nome do centro de custos.",
        required=True,
        help="""Nome do centro de custos.
Ver pagina 40""",
    )


class Registro1010(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.1010"
    _description = u"""Obrigatoriedade de registros do Bloco 1"""
    _inherit = "l10n.br.sped.mixin"
    ind_exp = fields.Char(
        "Reg",
        required=True,
        help="""Reg.   1100   -   Ocorreu   averbação   (conclusão)   de   exportação   noperíodo:S –  SimN -  Não
Ver pagina 194""",
    )
    ind_ccrf = fields.Char(
        "IND_CCRF",
        required=True,
        help="""Reg 1200 – Existem informações acerca de créditos de ICMS aserem controlados, definidos pela Sefaz:S –  SimN -  Não
Ver pagina 194""",
    )
    ind_comb = fields.Char(
        "Reg",
        required=True,
        help="""Reg.  1300   –   É   comercio   varejista   de   combustíveis   commovimentação e/ou estoque no período:S –  SimN -  Não
Ver pagina 194""",
    )
    ind_usina = fields.Char(
        "Reg",
        required=True,
        help="""Reg. 1390 – Usinas de açúcar e/álcool – O estabelecimento éprodutor de açúcar e/ou álcool carburante com movimentação e/ouestoque no período:S – SimN -  Não
Ver pagina 194""",
    )
    ind_va = fields.Char(
        "IND_VA",
        required=True,
        help="""Reg   1400   –   Sendo   o   registro   obrigatório   em   sua   Unidade   deFederação, existem informações a serem prestadas neste registro:
Ver pagina 194""",
    )
    ind_ee = fields.Char(
        "IND_EE",
        required=True,
        help="""Reg   1500   -   A   empresa   é   distribuidora   de   energia   e   ocorreufornecimento de energia elétrica para consumidores de outra UF:S – Sim;N -  Não
Ver pagina 195""",
    )
    ind_cart = fields.Char(
        "Reg 1600 - Realizou vendas com Cartão de Crédito ou de débito",
        required=True,
        help="""Reg 1600 - Realizou vendas com Cartão de Crédito ou de débito:S –  Sim;N -  Não
Ver pagina 195""",
    )
    ind_form = fields.Char(
        "Reg",
        required=True,
        help="""Reg.   1700  –  Foram   emitidos  documentos   fiscais  em  papel   noperíodo    em   unidade   da   federação   que   exija   o   controle   deutilização de documentos fiscais:S – SimN - Não
Ver pagina 195""",
    )
    ind_aer = fields.Char(
        "IND_AER",
        required=True,
        help="""Reg 1800 – A empresa prestou serviços de transporte aéreo decargas e de passageiros:S –  SimN -  Não
Ver pagina 195""",
    )


class Registro1100(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.1100"
    _description = u"""Registro de Informações sobre Exportação"""
    _inherit = "l10n.br.sped.mixin"
    ind_doc = fields.Integer("Informe o tipo de documento", required=True)
    nro_de = fields.Char(
        "Número da declaração",
        required=True,
        help="""Número da declaração
Ver pagina 195""",
    )
    dt_de = fields.Integer("Data da declaração (DDMMAAAA)", required=True)
    nat_exp = fields.Integer(
        "Preencher com: 0 - Exportação Direta1 - Exportação Indireta", required=True
    )
    nro_re = fields.Integer("Nº do registro de Exportação*")
    dt_re = fields.Integer("Data do Registro de Exportação (DDMMAAAA)*")
    chc_emb = fields.Char(
        "Nº do conhecimento de embarque*",
        help="""Nº do conhecimento de embarque
Ver pagina 195""",
    )
    dt_chc = fields.Integer("Data do conhecimento de embarque (DDMMAAAA)*")
    dt_avb = fields.Integer(
        "Data da averbação da Declaração de exportação (ddmmaaaa)", required=True
    )
    tp_chc = fields.Integer(
        "Informação do tipo de conhecimento de embarque", required=True
    )
    pais = fields.Integer("PAIS", required=True)
    reg_1105_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.1105",
        "parent_1100_id",
        string="Documentos Fiscais de Exportação",
        help="Bloco 1",
    )


class Registro1105(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.1105"
    _description = u"""Documentos Fiscais de Exportação"""
    _inherit = "l10n.br.sped.mixin"
    parent_1100_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.1100",
        string="Registro de Informações sobre Exportação",
    )
    reg_1110_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.1110",
        "parent_1105_id",
        string="Operações de Exportação Indireta - Mercadorias de terceiros",
        help="Bloco 1",
    )


class Registro1110(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.1110"
    _description = u"""Operações de Exportação Indireta - Mercadorias de terceiros"""
    _inherit = "l10n.br.sped.mixin"
    cod_part = fields.Char(
        "COD_PART",
        required=True,
        help="""Código do participante-Fornecedor da Mercadoria destinada à exportação (campo 02 do Registro 0150)
Ver pagina 197""",
    )
    cod_mod = fields.Char(
        "Código do documento fiscal, conforme a Tabela 4",
        required=True,
        help="""Código do documento fiscal, conforme a Tabela 4.1.1
Ver pagina 197""",
    )
    ser = fields.Char(
        "SER*",
        help="""Série do documento fiscal recebido com fins específicos de exportação.
Ver pagina 197""",
    )
    num_doc = fields.Integer("NUM_DOC", required=True)
    dt_doc = fields.Integer("DT_DOC", required=True)
    chv_nfe = fields.Integer("Chave da Nota Fiscal Eletrônica*")
    nr_memo = fields.Integer("Número do Memorando de Exportação*")
    qtd = fields.Integer("Quantidade do item efetivamente exportado", required=True)
    unid = fields.Char(
        "Unidade do item  (Campo 02 do registro 0190)",
        required=True,
        help="""Unidade do item  (Campo 02 do registro 0190)
Ver pagina 197""",
    )
    parent_1105_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.1105", string="Documentos Fiscais de Exportação"
    )


class Registro1200(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.1200"
    _description = u"""Controle de Créditos Fiscais - ICMS"""
    _inherit = "l10n.br.sped.mixin"
    cod_aj_apur = fields.Char(
        "COD_AJ_APUR",
        required=True,
        help="""Código de ajuste, conforme informado na Tabela indicada no item 5.1.1.
Ver pagina 198""",
    )
    sld_cred = fields.Integer(
        "Saldo de créditos fiscais de períodos anteriores", required=True
    )
    cred_apr = fields.Integer("Total de crédito apropriado no mês", required=True)
    cred_receb = fields.Integer(
        "Total de créditos recebidos por transferência", required=True
    )
    cred_util = fields.Integer("Total de créditos utilizados no período", required=True)
    sld_cred_fim = fields.Integer("SLD_CRED_FIM", required=True)
    reg_1210_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.1210",
        "parent_1200_id",
        string="Utilização de Créditos Fiscais - ICMS",
        help="Bloco 1",
    )


class Registro1210(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.1210"
    _description = u"""Utilização de Créditos Fiscais - ICMS"""
    _inherit = "l10n.br.sped.mixin"
    tipo_util = fields.Char(
        "TIPO_UTIL",
        required=True,
        help="""Tipo de utilização do crédito, conforme tabela indicada no item 5.5.
Ver pagina 199""",
    )
    nr_doc = fields.Char(
        "Número do documento utilizado na baixa de créditos*",
        help="""Número do documento utilizado na baixa de créditos
Ver pagina 199""",
    )
    vl_cred_util = fields.Integer("Total de crédito utilizado", required=True)
    parent_1200_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.1200", string="Controle de Créditos Fiscais - ICMS"
    )


class Registro1300(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.1300"
    _description = u"""Movimentação diária de combustíveis"""
    _inherit = "l10n.br.sped.mixin"
    cod_item = fields.Char(
        "Código do Produto, constante do registro 0200",
        required=True,
        help="""Código do Produto, constante do registro 0200
Ver pagina 199""",
    )
    dt_fech = fields.Integer("Data do fechamento da movimentação", required=True)
    estq_abert = fields.Integer("Estoque no início do dia, em litros", required=True)
    vol_entr = fields.Integer("Volume Recebido no dia (em litros)", required=True)
    vol_disp = fields.Integer("Volume Disponível (04 + 05), em litros", required=True)
    vol_saidas = fields.Integer("Volume Total das Saídas, em litros", required=True)
    estq_escr = fields.Integer("Estoque Escritural (06 – 07), litros", required=True)
    val_aj_perda = fields.Integer("Valor da Perda, em litros", required=True)
    val_aj_ganho = fields.Integer("Valor do ganho, em litros", required=True)
    fech_fisico = fields.Integer("Estoque de Fechamento, em litros", required=True)
    reg_1310_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.1310",
        "parent_1300_id",
        string="Movimentação diária de combustíveis por tanque",
        help="Bloco 1",
    )


class Registro1310(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.1310"
    _description = u"""Movimentação diária de combustíveis por tanque"""
    _inherit = "l10n.br.sped.mixin"
    num_tanque = fields.Char(
        "Tanque que armazena o combustível.",
        required=True,
        help="""Tanque que armazena o combustível.
Ver pagina 200""",
    )
    estq_abert = fields.Integer("Estoque no inicio do dia, em litros", required=True)
    vol_entr = fields.Integer("Volume Recebido no dia (em litros)", required=True)
    vol_disp = fields.Integer("Volume Disponível (03 + 04), em litros", required=True)
    vol_saidas = fields.Integer("Volume Total das Saídas, em litros", required=True)
    estq_escr = fields.Integer("Estoque Escritural(05 – 06), litros", required=True)
    val_aj_perda = fields.Integer("Valor da Perda, em litros", required=True)
    val_aj_ganho = fields.Integer("Valor do ganho, em litros", required=True)
    fech_fisico = fields.Integer("Volume aferido no tanque, em litros", required=True)
    parent_1300_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.1300", string="Movimentação diária de combustíveis"
    )
    reg_1320_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.1320",
        "parent_1310_id",
        string="Volume de vendas",
        help="Bloco 1",
    )


class Registro1320(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.1320"
    _description = u"""Volume de vendas"""
    _inherit = "l10n.br.sped.mixin"
    num_bico = fields.Integer("Bico Ligado à Bomba", required=True)
    nr_interv = fields.Integer("Número da intervenção*")
    mot_interv = fields.Char(
        "Motivo da Intervenção*",
        help="""Motivo da Intervenção
Ver pagina 201""",
    )
    nom_interv = fields.Char(
        "Nome do Interventor*",
        help="""Nome do Interventor
Ver pagina 201""",
    )
    cnpj_interv = fields.Integer("CNPJ da empresa responsável pela intervenção*")
    cpf_interv = fields.Integer("CPF do técnico responsável pela intervenção*")
    val_fecha = fields.Integer(
        "Valor da leitura final do contador, no fechamento do bico", required=True
    )
    val_abert = fields.Integer(
        "Valor da leitura inicial do contador, na abertura do bico", required=True
    )
    vol_aferi = fields.Integer("Aferições da Bomba, em litros*")
    vol_vendas = fields.Integer(
        "Vendas (08 – 09 - 10 ) do bico , em litros", required=True
    )
    parent_1310_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.1310",
        string="Movimentação diária de combustíveis por tanque",
    )


class Registro1350(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.1350"
    _description = u"""Bombas"""
    _inherit = "l10n.br.sped.mixin"
    serie = fields.Char(
        "Número de Série da Bomba",
        required=True,
        help="""Número de Série da Bomba
Ver pagina 202""",
    )
    fabricante = fields.Char(
        "Nome do Fabricante da Bomba",
        required=True,
        help="""Nome do Fabricante da Bomba
Ver pagina 202""",
    )
    modelo = fields.Char(
        "Modelo da Bomba",
        required=True,
        help="""Modelo da Bomba
Ver pagina 202""",
    )
    tipo_medicao = fields.Char(
        "Identificador de medição",
        required=True,
        help="""Identificador de medição:0 - analógico;1 – digital
Ver pagina 202""",
    )
    reg_1360_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.1360",
        "parent_1350_id",
        string="Lacres das bombas",
        help="Bloco 1",
    )
    reg_1370_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.1370",
        "parent_1350_id",
        string="Bicos da bomba",
        help="Bloco 1",
    )


class Registro1360(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.1360"
    _description = u"""Lacres das bombas"""
    _inherit = "l10n.br.sped.mixin"
    num_lacre = fields.Char(
        "Número do Lacre associado na Bomba",
        required=True,
        help="""Número do Lacre associado na Bomba
Ver pagina 202""",
    )
    dt_aplicacao = fields.Integer("Data de aplicação do Lacre", required=True)
    parent_1350_id = fields.Many2one("l10n.br.sped.efd_icms_ipi.1350", string="Bombas")


class Registro1370(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.1370"
    _description = u"""Bicos da bomba"""
    _inherit = "l10n.br.sped.mixin"
    num_bico = fields.Integer("Número sequencial do bico ligado a bomba", required=True)
    cod_item = fields.Char(
        "Código do Produto, constante do registro 0200",
        required=True,
        help="""Código do Produto, constante do registro 0200
Ver pagina 203""",
    )
    num_tanque = fields.Char(
        "Tanque que armazena o combustível.",
        required=True,
        help="""Tanque que armazena o combustível.
Ver pagina 203""",
    )
    parent_1350_id = fields.Many2one("l10n.br.sped.efd_icms_ipi.1350", string="Bombas")


class Registro1390(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.1390"
    _description = u"""Controle de produção de Usina"""
    _inherit = "l10n.br.sped.mixin"
    cod_prod = fields.Integer("Código do produto", required=True)
    reg_1391_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.1391",
        "parent_1390_id",
        string="Produção diária da usina",
        help="Bloco 1",
    )


class Registro1391(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.1391"
    _description = u"""Produção diária da usina"""
    _inherit = "l10n.br.sped.mixin"
    dt_registro = fields.Char(
        "Data de produção (DDMMAAAA)",
        required=True,
        help="""Data de produção (DDMMAAAA)
Ver pagina 203""",
    )
    qtd_moid = fields.Integer("Quantidade de cana esmagada (toneladas)*")
    estq_ini = fields.Integer("Estoque inicial (litros / Kg)", required=True)
    qtd_produz = fields.Integer("Quantidade produzida (litros / Kg)*")
    ent_anid_hid = fields.Integer("ENT_ANID_HID*")
    outr_entr = fields.Integer("Outras entradas  (litros / Kg)*")
    perda = fields.Integer("Evaporação (litros) ou Quebra de peso (Kg)*")
    cons = fields.Integer("Consumo (litros)*")
    sai_ani_hid = fields.Integer("Saída para transformação (litros).*")
    saidas = fields.Integer("Saídas (litros / Kg)*")
    estq_fin = fields.Integer("Estoque final  (litros / Kg)", required=True)
    estq_ini_mel = fields.Integer("Estoque inicial de mel residual (Kg)*")
    prod_dia_mel = fields.Integer(
        "Produção de mel residual (Kg) e entradas de mel (Kg)*"
    )
    util_mel = fields.Integer("Mel residual utilizado (Kg) e saídas de mel (Kg)*")
    prod_alc_mel = fields.Integer("PROD_ALC_MEL*")
    obs = fields.Char(
        "Observações*",
        help="""Observações
Ver pagina 204""",
    )
    parent_1390_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.1390", string="Controle de produção de Usina"
    )


class Registro1400(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.1400"
    _description = u"""Informação sobre Valor Agregado"""
    _inherit = "l10n.br.sped.mixin"
    cod_item_ipm = fields.Char(
        "COD_ITEM_IPM",
        required=True,
        help="""Código do item (Tabela própria da unidade da federação(Tabela   de   Itens   UF   Índice   de   Participação   dosMunicípios) ou campo 02 do Registro 0200
Ver pagina 205""",
    )
    mun = fields.Integer("Código do Município de origem/destino", required=True)
    valor = fields.Integer("Valor mensal correspondente ao município", required=True)


class Registro1500(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.1500"
    _description = u"""Nota fiscal/Conta de energia elétrica (código 06) - Operações Interestaduais"""
    _inherit = "l10n.br.sped.mixin"
    ind_oper = fields.Char(
        "Indicador do tipo de operação: 1- Saída",
        required=True,
        help="""Indicador do tipo de operação: 1- Saída
Ver pagina 206""",
    )
    ind_emit = fields.Char(
        "Indicador do emitente do documento fiscal",
        required=True,
        help="""Indicador do emitente do documento fiscal:0- Emissão própria;
Ver pagina 206""",
    )
    cod_part = fields.Char(
        "Código do participante (campo 02 do Registro 0150)",
        required=True,
        help="""Código do participante (campo 02 do Registro 0150):- do adquirente, no caso das saídas.
Ver pagina 206""",
    )
    cod_mod = fields.Char(
        "Código do modelo do documento fiscal, conforme a Tabela 4",
        required=True,
        help="""Código do modelo do documento fiscal, conforme a Tabela 4.1.1
Ver pagina 206""",
    )
    cod_sit = fields.Integer(
        "Código da situação do documento fiscal, conforme a Tabela 4", required=True
    )
    ser = fields.Char(
        "Série do documento fiscal*",
        help="""Série do documento fiscal
Ver pagina 206""",
    )
    sub = fields.Integer("Subsérie do documento fiscal*")
    cod_cons = fields.Char(
        "Código de classe de consumo de energia elétrica",
        required=True,
        help="""Código de classe de consumo de energia elétrica:01 - Comercial02 - Consumo Próprio03 - Iluminação Pública04 - Industrial05 - Poder Público06 - Residencial07 - Rural08 -Serviço Público
Ver pagina 206""",
    )
    num_doc = fields.Integer("Número do documento fiscal", required=True)
    dt_doc = fields.Integer("Data da emissão do documento fiscal", required=True)
    dt_e_s = fields.Integer("Data da entrada ou da saída", required=True)
    vl_doc = fields.Integer("Valor total do documento fiscal", required=True)
    vl_desc = fields.Integer("Valor total do desconto*")
    vl_forn = fields.Integer("Valor total fornecido/consumido", required=True)
    vl_serv_nt = fields.Integer("Valor total dos serviços não-tributados pelo ICMS*")
    vl_terc = fields.Integer("Valor total cobrado em nome de terceiros*")
    vl_da = fields.Integer(
        "Valor total de despesas acessórias indicadas no documento fiscal*"
    )
    vl_bc_icms = fields.Integer("Valor acumulado da base de cálculo do ICMS*")
    vl_icms = fields.Integer("Valor acumulado do ICMS*")
    vl_bc_icms_st = fields.Integer("VL_BC_ICMS_ST*")
    vl_icms_st = fields.Integer(
        "Valor acumulado do ICMS retido por substituição tributária*"
    )
    cod_inf = fields.Char(
        "COD_INF*",
        help="""Código da informação complementar do documento fiscal (campo 02 do Registro 0450)
Ver pagina 206""",
    )
    vl_pis = fields.Integer("Valor do PIS*")
    vl_cofins = fields.Integer("Valor da COFINS*")
    tp_ligacao = fields.Integer(
        "Código de tipo de Ligação1 - Monofásico2 - Bifásico3 - Trifásico*"
    )
    cod_grupo_tensao = fields.Char(
        "Código de grupo de tensão*",
        help="""Código de grupo de tensão:01 - A1 - Alta Tensão (230kV ou mais)02 - A2 - Alta Tensão (88 a 138kV)
Ver pagina 206""",
    )
    reg_1510_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.1510",
        "parent_1500_id",
        string="Itens do documento Nota fiscal/Conta de energia elétrica (código 06)",
        help="Bloco 1",
    )


class Registro1510(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.1510"
    _description = (
        u"""Itens do documento Nota fiscal/Conta de energia elétrica (código 06)"""
    )
    _inherit = "l10n.br.sped.mixin"
    num_item = fields.Integer(
        "Número sequencial do item no documento fiscal", required=True
    )
    cod_item = fields.Char(
        "Código do item (campo 02 do Registro 0200)",
        required=True,
        help="""Código do item (campo 02 do Registro 0200)
Ver pagina 208""",
    )
    cod_class = fields.Integer("COD_CLASS", required=True)
    qtd = fields.Integer("Quantidade do item*")
    unid = fields.Char(
        "Unidade do item (Campo 02 do registro 0190)*",
        help="""Unidade do item (Campo 02 do registro 0190)
Ver pagina 208""",
    )
    vl_item = fields.Integer("Valor do item", required=True)
    vl_desc = fields.Integer("Valor total do desconto*")
    cst_icms = fields.Integer("CST_ICMS", required=True)
    cfop = fields.Integer("Código Fiscal de Operação e Prestação", required=True)
    vl_bc_icms = fields.Integer("Valor da base de cálculo do ICMS*")
    aliq_icms = fields.Monetary("Alíquota do ICMS*", digits=2)
    vl_icms = fields.Integer("Valor do ICMS creditado/debitado*")
    vl_bc_icms_st = fields.Integer(
        "Valor da base de cálculo referente à substituição tributária*"
    )
    aliq_st = fields.Integer("ALIQ_ST*")
    vl_icms_st = fields.Integer("Valor do ICMS referente à substituição tributária*")
    ind_rec = fields.Char(
        "Indicador do tipo de receita",
        required=True,
        help="""Indicador do tipo de receita:0- Receita própria;1- Receita de terceiros
Ver pagina 208""",
    )
    cod_part = fields.Char(
        "COD_PART*",
        help="""Código do participante receptor da receita, terceiro da operação (campo 02 do Registro 0150)
Ver pagina 208""",
    )
    vl_pis = fields.Integer("Valor do PIS*")
    vl_cofins = fields.Integer("Valor da COFINS*")
    cod_cta = fields.Char(
        "Código da conta analítica contábil debitada/creditada*",
        help="""Código da conta analítica contábil debitada/creditada
Ver pagina 208""",
    )
    parent_1500_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.1500",
        string="Nota fiscal/Conta de energia elétrica (código 06) - Operações Interestaduais",
    )


class Registro1600(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.1600"
    _description = u"""Total das operações com cartão de crédito e/ou débito"""
    _inherit = "l10n.br.sped.mixin"
    cod_part = fields.Char(
        "Código do participante (campo 02 do Registro 0150)",
        required=True,
        help="""Código do participante (campo 02 do Registro 0150): identificação da administradora do cartão de débito/crédito
Ver pagina 209""",
    )
    tot_credito = fields.Integer("TOT_CREDITO", required=True)
    tot_debito = fields.Integer("TOT_DEBITO", required=True)


class Registro1700(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.1700"
    _description = u"""Documentos fiscais utilizados"""
    _inherit = "l10n.br.sped.mixin"
    cod_disp = fields.Char(
        "Código dispositivo autorizado",
        required=True,
        help="""Código dispositivo autorizado:00 - Formulário de Segurança – impressor autônomo01 - FS-DA – Formulário de Segurança para Impressão de DANFE02 – Formulário de segurança - NF-e03 - Formulário Contínuo04 – Blocos05 - Jogos Soltos
Ver pagina 209""",
    )
    cod_mod = fields.Char(
        "Código do modelo do dispositivo autorizado, conforme a Tabela 4",
        required=True,
        help="""Código do modelo do dispositivo autorizado, conforme a Tabela 4.1.1
Ver pagina 209""",
    )
    ser = fields.Char(
        "Série do dispositivo autorizado*",
        help="""Série do dispositivo autorizado
Ver pagina 209""",
    )
    sub = fields.Char(
        "Subsérie do dispositivo autorizado*",
        help="""Subsérie do dispositivo autorizado
Ver pagina 209""",
    )
    num_doc_ini = fields.Integer(
        "Número do dispositivo autorizado (utilizado) inicial", required=True
    )
    num_doc_fin = fields.Integer(
        "Número do dispositivo autorizado (utilizado) final", required=True
    )
    num_aut = fields.Integer(
        "Número da autorização, conforme dispositivo autorizado", required=True
    )
    reg_1710_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.1710",
        "parent_1700_id",
        string="Documentos fiscais cancelados/inutilizados",
        help="Bloco 1",
    )


class Registro1710(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.1710"
    _description = u"""Documentos fiscais cancelados/inutilizados"""
    _inherit = "l10n.br.sped.mixin"
    num_doc_ini = fields.Integer(
        "Número do dispositivo autorizado (inutilizado) inicial", required=True
    )
    num_doc_fin = fields.Integer(
        "Número do dispositivo autorizado (inutilizado) final", required=True
    )
    parent_1700_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.1700", string="Documentos fiscais utilizados"
    )


class Registro1800(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.1800"
    _description = u"""DCTA - Demonstrativo de crédito do ICMS sobre transporte aéreo"""
    _inherit = "l10n.br.sped.mixin"
    vl_carga = fields.Integer("Valor das prestações cargas (Tributado)", required=True)
    vl_pass = fields.Integer(
        "Valor das prestações passageiros/cargas (Não Tributado)", required=True
    )
    vl_fat = fields.Integer("Valor total do faturamento (2+3)", required=True)
    ind_rat = fields.Monetary("Índice para rateio(2 / 4)", required=True, digits=6)
    vl_icms_ant = fields.Integer("Valor total dos créditos do ICMS", required=True)
    vl_bc_icms = fields.Integer("Valor da base de cálculo do ICMS", required=True)
    vl_icms_apur = fields.Integer(
        "Valor do ICMS apurado no cálculo (5 x 6)", required=True
    )
    vl_bc_icms_apur = fields.Integer(
        "Valor da base de cálculo do ICMS apurada (5 x 7)", required=True
    )
    vl_dif = fields.Integer("VL_DIF", required=True)


class Registro1900(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.1900"
    _description = u"""Indicador de sub-apuração do ICMS"""
    _inherit = "l10n.br.sped.mixin"
    ind_apur_icms = fields.Char(
        "Indicador de outra apuração do ICMS",
        required=True,
        help="""Indicador de outra apuração do ICMS:3 – APURAÇÃO 1;4 – APURAÇÃO 2;5 – APURAÇÃO 3;6 – APURAÇÃO 4;7 – APURAÇÃO 5;8 – APURAÇÃO 6.
Ver pagina 211""",
    )
    descr_compl_out_apur = fields.Char(
        "Descrição complementar de Outra Apuraçãodo ICMS",
        required=True,
        help="""Descrição complementar de Outra Apuraçãodo ICMS
Ver pagina 211""",
    )
    reg_1910_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.1910",
        "parent_1900_id",
        string="Período da sub-apuração do ICMS",
        help="Bloco 1",
    )


class Registro1910(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.1910"
    _description = u"""Período da sub-apuração do ICMS"""
    _inherit = "l10n.br.sped.mixin"
    dt_ini = fields.Integer("Data inicial da sub-apuração", required=True)
    dt_fin = fields.Integer("Data final da sub-apuração", required=True)
    parent_1900_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.1900", string="Indicador de sub-apuração do ICMS"
    )
    reg_1920_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.1920", string="Sub-apuração do ICMS", help="Bloco 1"
    )  # m2o


class Registro1920(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.1920"
    _description = u"""Sub-apuração do ICMS"""
    _inherit = "l10n.br.sped.mixin"
    vl_tot_transf_debitos_oa = fields.Integer("VL_TOT_TRANSF_DEBITOS_OA", required=True)
    vl_tot_aj_debitos_oa = fields.Integer(
        "Valor total de “Ajustes a débito”", required=True
    )
    vl_estornos_cred_oa = fields.Integer(
        "Valor  total  de   Ajustes   “Estornos   decréditos”", required=True
    )
    reg_1921_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.1921",
        "parent_1920_id",
        string="Ajuste/benefício/incentivo da sub-apuração do ICMS",
        help="Bloco 1",
    )
    reg_1925_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.1925",
        "parent_1920_id",
        string="Informações adicionais da sub-apuração do ICMS - Valores declaratórios",
        help="Bloco 1",
    )
    reg_1926_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.1926",
        "parent_1920_id",
        string="Obrigações do ICMS a recolher - Operações referentes à sub-apuração do ICMS",
        help="Bloco 1",
    )


class Registro1921(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.1921"
    _description = u"""Ajuste/benefício/incentivo da sub-apuração do ICMS"""
    _inherit = "l10n.br.sped.mixin"
    cod_aj_apur = fields.Char(
        "COD_AJ_APUR",
        required=True,
        help="""Código do ajuste da SUB-APURAÇÃO e dedução,conforme a Tabela indicada no item 5.1.1.
Ver pagina 215""",
    )
    descr_compl_aj = fields.Char(
        "Descrição complementar do ajuste da apuração*",
        help="""Descrição complementar do ajuste da apuração.
Ver pagina 215""",
    )
    vl_aj_apur = fields.Integer("Valor do ajuste da apuração", required=True)
    parent_1920_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.1920", string="Sub-apuração do ICMS"
    )
    reg_1922_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.1922",
        "parent_1921_id",
        string="Informações adicionais dos ajustes da sub-apuração do ICMS",
        help="Bloco 1",
    )
    reg_1923_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.1923",
        "parent_1921_id",
        string="Informações adicionais dos ajustes da sub-apuração do ICMS - Identificação dos documentos fiscais",
        help="Bloco 1",
    )


class Registro1922(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.1922"
    _description = u"""Informações adicionais dos ajustes da sub-apuração do ICMS"""
    _inherit = "l10n.br.sped.mixin"
    num_da = fields.Char(
        "Número do documento de arrecadação estadual, se houver*",
        help="""Número do documento de arrecadação estadual, se houver
Ver pagina 215""",
    )
    num_proc = fields.Char(
        "Número do processo ao qual o ajuste está vinculado, se houver*",
        help="""Número do processo ao qual o ajuste está vinculado, se houver
Ver pagina 215""",
    )
    ind_proc = fields.Char(
        "Indicador da origem do processo*",
        help="""Indicador da origem do processo:0- SEFAZ;1- Justiça Federal;2- Justiça Estadual;9- Outros
Ver pagina 215""",
    )
    proc = fields.Char(
        "Descrição resumida do processo que embasou o lançamento*",
        help="""Descrição resumida do processo que embasou o lançamento
Ver pagina 215""",
    )
    txt_compl = fields.Char(
        "Descrição complementar*",
        help="""Descrição complementar
Ver pagina 215""",
    )
    parent_1921_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.1921",
        string="Ajuste/benefício/incentivo da sub-apuração do ICMS",
    )


class Registro1923(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.1923"
    _description = u"""Informações adicionais dos ajustes da sub-apuração do ICMS - Identificação dos documentos fiscais"""
    _inherit = "l10n.br.sped.mixin"
    cod_part = fields.Char(
        "Código do participante (campo 02 do Registro 0150)",
        required=True,
        help="""Código do participante (campo 02 do Registro 0150):- do emitente do documento ou do remetente das mercadorias,no caso de entradas;- do adquirente, no caso de saídas
Ver pagina 216""",
    )
    cod_mod = fields.Char(
        "Código  do modelo do documento fiscal, conforme  a Tabela4",
        required=True,
        help="""Código  do modelo do documento fiscal, conforme  a Tabela4.1.1
Ver pagina 216""",
    )
    ser = fields.Char(
        "Série do documento fiscal*",
        help="""Série do documento fiscal
Ver pagina 216""",
    )
    sub = fields.Integer("Subsérie do documento fiscal*")
    num_doc = fields.Integer("Número do documento fiscal", required=True)
    dt_doc = fields.Integer("Data da emissão do documento fiscal", required=True)
    cod_item = fields.Char(
        "Código do item (campo 02 do Registro 0200)*",
        help="""Código do item (campo 02 do Registro 0200)
Ver pagina 216""",
    )
    vl_aj_item = fields.Integer("Valor do ajuste para a operação/item", required=True)
    parent_1921_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.1921",
        string="Ajuste/benefício/incentivo da sub-apuração do ICMS",
    )


class Registro1925(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.1925"
    _description = (
        u"""Informações adicionais da sub-apuração do ICMS - Valores declaratórios"""
    )
    _inherit = "l10n.br.sped.mixin"
    cod_inf_adic = fields.Char(
        "COD_INF_ADIC",
        required=True,
        help="""Código   da   informação   adicional   conforme   tabela   a   serdefinida pelas SEFAZ, conforme tabela definida no item 5.2.
Ver pagina 217""",
    )
    vl_inf_adic = fields.Integer(
        "Valor referente à informação adicional", required=True
    )
    parent_1920_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.1920", string="Sub-apuração do ICMS"
    )


class Registro1926(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.1926"
    _description = u"""Obrigações do ICMS a recolher - Operações referentes à sub-apuração do ICMS"""
    _inherit = "l10n.br.sped.mixin"
    cod_or = fields.Char(
        "Código da obrigação a recolher, conforme a Tabela 5",
        required=True,
        help="""Código da obrigação a recolher, conforme a Tabela 5.4
Ver pagina 217""",
    )
    vl_or = fields.Integer("Valor da obrigação a recolher", required=True)
    dt_vcto = fields.Integer("Data de vencimento da obrigação", required=True)
    cod_rec = fields.Char(
        "COD_REC",
        required=True,
        help="""Código de receita referente à obrigação, próprio da unidade dafederação, conforme legislação estadual,
Ver pagina 217""",
    )
    num_proc = fields.Char(
        "NUM_PROC*",
        help="""Número do processo ou auto de infração ao qual a obrigaçãoestá vinculada, se houver.
Ver pagina 217""",
    )
    ind_proc = fields.Char(
        "Indicador da origem do processo*",
        help="""Indicador da origem do processo:0- SEFAZ;1- Justiça Federal;2- Justiça Estadual;9- Outros
Ver pagina 217""",
    )
    proc = fields.Char(
        "Descrição resumida do processo que embasou o lançamento*",
        help="""Descrição resumida do processo que embasou o lançamento
Ver pagina 217""",
    )
    txt_compl = fields.Char(
        "Descrição complementar das obrigações a recolher*",
        help="""Descrição complementar das obrigações a recolher.
Ver pagina 217""",
    )
    mes_ref = fields.Integer(
        "Informe o mês de referência no formato “mmaaaa”", required=True
    )
    parent_1920_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.1920", string="Sub-apuração do ICMS"
    )


class RegistroC100(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c100"
    _description = u"""Documento - Nota Fiscal (código 01), Nota Fiscal Avulsa (código 1B), Nota Fiscal de Produtor (código 04), Nota Fiscal Eletrônica (código 55) e Nota Fiscal Eletrônica para Consumidor Final (código 65)"""
    _inherit = "l10n.br.sped.mixin"
    ind_oper = fields.Char(
        "Indicador do tipo de operação",
        required=True,
        help="""Indicador do tipo de operação:0 - Entrada;1 - Saída
Ver pagina 42""",
    )
    ind_emit = fields.Char(
        "Indicador do emitente do documento fiscal",
        required=True,
        help="""Indicador do emitente do documento fiscal:0- Emissão própria;1- Terceiros
Ver pagina 42""",
    )
    cod_part = fields.Char(
        "Código do participante (campo 02 do Registro 0150)",
        required=True,
        help="""Código do participante (campo 02 do Registro 0150):- do emitente do documento ou do remetente das mercadorias, no caso de entradas;- do adquirente, no caso de saídas
Ver pagina 42""",
    )
    cod_mod = fields.Char(
        "Código do modelo do documento fiscal, conformea Tabela 4",
        required=True,
        help="""Código do modelo do documento fiscal, conformea Tabela 4.1.1
Ver pagina 42""",
    )
    cod_sit = fields.Integer("COD_SIT", required=True)
    ser = fields.Char(
        "Série do documento fiscal",
        help="""Série do documento fiscal
Ver pagina 42""",
    )
    num_doc = fields.Integer("Número do documento fiscal", required=True)
    chv_nfe = fields.Integer("Chave da Nota Fiscal Eletrônica")
    dt_doc = fields.Integer("Data da emissão do documento fiscal", required=True)
    dt_e_s = fields.Integer("Data da entrada ou da saída")
    vl_doc = fields.Integer("Valor total do documento fiscal", required=True)
    ind_pgto = fields.Char(
        "Indicador do tipo de pagamento",
        required=True,
        help="""Indicador do tipo de pagamento:0- À vista;1- A prazo;9- Sem pagamento.
Ver pagina 42""",
    )
    vl_desc = fields.Integer("Valor total do desconto")
    vl_abat_nt = fields.Integer(
        "Abatimento   não   tributado   e   não   comercial   Ex"
    )
    vl_merc = fields.Integer("Valor total das mercadorias e serviços")
    ind_frt = fields.Char(
        "Indicador do tipo do frete",
        required=True,
        help="""Indicador do tipo do frete:0 - Por conta de terceiros;1 - Por conta do emitente;2 - Por conta do destinatário;9 - Sem cobrança de frete.
Ver pagina 43""",
    )
    vl_frt = fields.Integer("Valor do frete indicado no documento fiscal")
    vl_seg = fields.Integer("Valor do seguro indicado no documento fiscal")
    vl_out_da = fields.Integer("Valor de outras despesas acessórias")
    vl_bc_icms = fields.Integer("Valor da base de cálculo do ICMS")
    vl_icms = fields.Integer("Valor do ICMS")
    reg_c101_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c101",
        string="Informação complementar dos documentos fiscais quando das operações interestaduais destinadas a consumidor final não contribuinte EC 87/15 (código 55)",
        help="Bloco C",
    )  # m2o
    reg_c105_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c105",
        string="Operações com ICMS ST recolhido para UF diversa do destinatário do documento fiscal (Código 55)",
        help="Bloco C",
    )  # m2o
    reg_c130_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c130",
        string="Complemento de Documento - ISSQN, IRRF e Previdência Social",
        help="Bloco C",
    )  # m2o
    reg_c140_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c140",
        string="Complemento de Documento - Fatura (código 01)",
        help="Bloco C",
    )  # m2o
    reg_c160_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c160",
        string="Complemento de Documento - Volumes Transportados (código 01 e 04) Exceto Combustíveis",
        help="Bloco C",
    )  # m2o
    reg_c110_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.c110",
        "parent_c100_id",
        string="Complemento de Documento - Informação Complementar da Nota Fiscal (código 01, 1B, 55)",
        help="Bloco C",
    )
    reg_c120_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.c120",
        "parent_c100_id",
        string="Complemento de Documento - Operações de Importação (código 01 e 55)",
        help="Bloco C",
    )
    reg_c165_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.c165",
        "parent_c100_id",
        string="Complemento de Documento - Operações com combustíveis (código 01)",
        help="Bloco C",
    )
    reg_c170_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.c170",
        "parent_c100_id",
        string="Complemento de Documento - Itens do Documento (código 01, 1B, 04 e 55)",
        help="Bloco C",
    )
    reg_c190_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.c190",
        "parent_c100_id",
        string="Registro Analítico do Documento (código 01, 1B, 04, 55 e 65)",
        help="Bloco C",
    )
    reg_c195_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.c195",
        "parent_c100_id",
        string="Complemento do Registro Analítico - Observações do Lançamento Fiscal (código 01, 1B, 04 e 55)",
        help="Bloco C",
    )


class RegistroC101(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c101"
    _description = u"""Informação complementar dos documentos fiscais quando das operações interestaduais destinadas a consumidor final não contribuinte EC 87/15 (código 55)"""
    _inherit = "l10n.br.sped.mixin"
    vl_fcp_uf_dest = fields.Integer("VL_FCP_UF_DEST", required=True)
    vl_icms_uf_dest = fields.Integer(
        "Valor total do ICMS Interestadual para a UF dedestino", required=True
    )
    vl_icms_uf_rem = fields.Integer(
        "Valor total do ICMS Interestadual para a UF doremetente", required=True
    )


class RegistroC105(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c105"
    _description = u"""Operações com ICMS ST recolhido para UF diversa do destinatário do documento fiscal (Código 55)"""
    _inherit = "l10n.br.sped.mixin"
    oper = fields.Integer("Indicador do tipo de operação", required=True)
    uf = fields.Char(
        "Sigla da UF de destino do ICMS_ST",
        required=True,
        help="""Sigla da UF de destino do ICMS_ST
Ver pagina 47""",
    )


class RegistroC110(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c110"
    _description = u"""Complemento de Documento - Informação Complementar da Nota Fiscal (código 01, 1B, 55)"""
    _inherit = "l10n.br.sped.mixin"
    cod_inf = fields.Char(
        "COD_INF",
        required=True,
        help="""Código da informação complementar dodocumento fiscal (campo 02 do Registro 0450)
Ver pagina 48""",
    )
    txt_compl = fields.Char(
        "Descrição complementar do código de referência",
        help="""Descrição complementar do código de referência.
Ver pagina 48""",
    )
    parent_c100_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c100",
        string="Documento - Nota Fiscal (código 01), Nota Fiscal Avulsa (código 1B), Nota Fiscal de Produtor (código 04), Nota Fiscal Eletrônica (código 55) e Nota Fiscal Eletrônica para Consumidor Final (código 65)",
    )
    reg_c111_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.c111",
        "parent_c110_id",
        string="Complemento de Documento - Processo referenciado",
        help="Bloco C",
    )
    reg_c112_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.c112",
        "parent_c110_id",
        string="Complemento de Documento - Documento de Arrecadação Referenciado",
        help="Bloco C",
    )
    reg_c113_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.c113",
        "parent_c110_id",
        string="Complemento de Documento - Documento Fiscal Referenciado",
        help="Bloco C",
    )
    reg_c114_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.c114",
        "parent_c110_id",
        string="Complemento de Documento - Cupom Fiscal Referenciado",
        help="Bloco C",
    )
    reg_c115_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.c115",
        "parent_c110_id",
        string="Local de coleta e/ou entrega (CÓDIGOS 01, 1B e 04)",
        help="Bloco C",
    )
    reg_c116_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.c116",
        "parent_c110_id",
        string="Cupom Fiscal Eletrônico - CF-e referenciado",
        help="Bloco C",
    )


class RegistroC111(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c111"
    _description = u"""Complemento de Documento - Processo referenciado"""
    _inherit = "l10n.br.sped.mixin"
    num_proc = fields.Char(
        "Identificação do processo ou ato concessório",
        required=True,
        help="""Identificação do processo ou ato concessório.
Ver pagina 48""",
    )
    ind_proc = fields.Char(
        "Indicador da origem do processo",
        required=True,
        help="""Indicador da origem do processo:0 - SEFAZ;1 - Justiça Federal;2 - Justiça Estadual;3 - SECEX/SRF9 -  Outros.
Ver pagina 48""",
    )
    parent_c110_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c110",
        string="Complemento de Documento - Informação Complementar da Nota Fiscal (código 01, 1B, 55)",
    )


class RegistroC112(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c112"
    _description = (
        u"""Complemento de Documento - Documento de Arrecadação Referenciado"""
    )
    _inherit = "l10n.br.sped.mixin"
    cod_da = fields.Char(
        "Código do modelo do documento de arrecadação ",
        required=True,
        help="""Código do modelo do documento de arrecadação :0 - documento estadual de arrecadação1 – GNRE
Ver pagina 48""",
    )
    uf = fields.Char(
        "Unidade federada beneficiária do recolhimento",
        required=True,
        help="""Unidade federada beneficiária do recolhimento
Ver pagina 48""",
    )
    num_da = fields.Char(
        "Número do documento de arrecadação",
        help="""Número do documento de arrecadação
Ver pagina 48""",
    )
    cod_aut = fields.Char(
        "Código completo da autenticação bancária",
        help="""Código completo da autenticação bancária
Ver pagina 48""",
    )
    vl_da = fields.Integer(
        "Valor   do   total   do   documento   de   arrecadação", required=True
    )
    dt_vcto = fields.Integer(
        "Data de vencimento do documento de arrecadação", required=True
    )
    dt_pgto = fields.Integer("DT_PGTO", required=True)
    parent_c110_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c110",
        string="Complemento de Documento - Informação Complementar da Nota Fiscal (código 01, 1B, 55)",
    )


class RegistroC113(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c113"
    _description = u"""Complemento de Documento - Documento Fiscal Referenciado"""
    _inherit = "l10n.br.sped.mixin"
    ind_oper = fields.Char(
        "Indicador do tipo de operação",
        required=True,
        help="""Indicador do tipo de operação:0- Entrada/aquisição;1- Saída/prestação
Ver pagina 49""",
    )
    ind_emit = fields.Char(
        "Indicador do emitente do título",
        required=True,
        help="""Indicador do emitente do título:0- Emissão própria;1- Terceiros
Ver pagina 49""",
    )
    cod_part = fields.Char(
        "COD_PART",
        required=True,
        help="""Código do participante emitente (campo 02 do Registro 0150) do documento referenciado.
Ver pagina 49""",
    )
    cod_mod = fields.Char(
        "Código do documento fiscal, conforme a Tabela 4",
        required=True,
        help="""Código do documento fiscal, conforme a Tabela 4.1.1
Ver pagina 49""",
    )
    ser = fields.Char(
        "Série do documento fiscal",
        help="""Série do documento fiscal
Ver pagina 49""",
    )
    sub = fields.Integer("Subsérie do documento fiscal")
    num_doc = fields.Integer("Número do documento fiscal", required=True)
    dt_doc = fields.Integer("Data da emissão do documento fiscal.", required=True)
    parent_c110_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c110",
        string="Complemento de Documento - Informação Complementar da Nota Fiscal (código 01, 1B, 55)",
    )


class RegistroC114(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c114"
    _description = u"""Complemento de Documento - Cupom Fiscal Referenciado"""
    _inherit = "l10n.br.sped.mixin"
    cod_mod = fields.Char(
        "COD_MOD",
        required=True,
        help="""Código do modelo do documento fiscal, conformea tabela indicada no item 4.1.1
Ver pagina 50""",
    )
    ecf_fab = fields.Char(
        "Número de série de fabricação do ECF",
        required=True,
        help="""Número de série de fabricação do ECF
Ver pagina 50""",
    )
    ecf_cx = fields.Integer("Número do caixa atribuído ao ECF", required=True)
    num_doc = fields.Integer("Número do documento fiscal", required=True)
    dt_doc = fields.Integer("Data da emissão do documento fiscal", required=True)
    parent_c110_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c110",
        string="Complemento de Documento - Informação Complementar da Nota Fiscal (código 01, 1B, 55)",
    )


class RegistroC115(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c115"
    _description = u"""Local de coleta e/ou entrega (CÓDIGOS 01, 1B e 04)"""
    _inherit = "l10n.br.sped.mixin"
    ind_carga = fields.Integer("Indicador do tipo de transporte")
    cnpj_col = fields.Integer(
        "Número   do  CNPJ   do  contribuinte   do   local   decoleta"
    )
    ie_col = fields.Char(
        "Inscrição   Estadual   do   contribuinte   do   local   decoleta",
        help="""Inscrição   Estadual   do   contribuinte   do   local   decoleta
Ver pagina 51""",
    )
    cpf_col = fields.Integer("CPF_COL")
    cod_mun_col = fields.Integer("Código do Município do local de coleta")
    cnpj_entg = fields.Integer(
        "Número   do  CNPJ   do  contribuinte   do   local   deentrega"
    )
    ie_entg = fields.Char(
        "IE_ENTG",
        help="""Inscrição   Estadual   do   contribuinte   do   local   deentrega
Ver pagina 51""",
    )
    cpf_entg = fields.Integer("Cpf do contribuinte do local de entrega")
    parent_c110_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c110",
        string="Complemento de Documento - Informação Complementar da Nota Fiscal (código 01, 1B, 55)",
    )


class RegistroC116(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c116"
    _description = u"""Cupom Fiscal Eletrônico - CF-e referenciado"""
    _inherit = "l10n.br.sped.mixin"
    cod_mod = fields.Char(
        "Código do modelo do documento fiscal, conforme a Tabela 4",
        required=True,
        help="""Código do modelo do documento fiscal, conforme a Tabela 4.1.1
Ver pagina 52""",
    )
    nr_sat = fields.Integer("Número de Série do equipamento SAT", required=True)
    chv_cfe = fields.Integer("Chave do Cupom Fiscal Eletrônico", required=True)
    num_cfe = fields.Integer("Número do cupom fiscal eletrônico", required=True)
    dt_doc = fields.Integer("Data da emissão do documento fiscal", required=True)
    parent_c110_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c110",
        string="Complemento de Documento - Informação Complementar da Nota Fiscal (código 01, 1B, 55)",
    )


class RegistroC120(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c120"
    _description = (
        u"""Complemento de Documento - Operações de Importação (código 01 e 55)"""
    )
    _inherit = "l10n.br.sped.mixin"
    cod_doc_imp = fields.Char(
        "Documento de importação",
        help="""Documento de importação:0 – Declaração de Importação;1 – Declaração Simplificada de Importação.
Ver pagina 53""",
    )
    num_doc_imp = fields.Char(
        "Número do documento de Importação.",
        help="""Número do documento de Importação.
Ver pagina 53""",
    )
    pis_imp = fields.Integer("Valor pago de PIS na importação")
    cofins_imp = fields.Integer("Valor pago de COFINS na importação")
    num_acdraw = fields.Char(
        "Número   do   Ato   Concessório   do  regimeDrawback",
        help="""Número   do   Ato   Concessório   do  regimeDrawback
Ver pagina 53""",
    )
    parent_c100_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c100",
        string="Documento - Nota Fiscal (código 01), Nota Fiscal Avulsa (código 1B), Nota Fiscal de Produtor (código 04), Nota Fiscal Eletrônica (código 55) e Nota Fiscal Eletrônica para Consumidor Final (código 65)",
    )


class RegistroC130(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c130"
    _description = u"""Complemento de Documento - ISSQN, IRRF e Previdência Social"""
    _inherit = "l10n.br.sped.mixin"
    vl_serv_nt = fields.Integer("VL_SERV_NT")
    vl_bc_issqn = fields.Integer("Valor da base de cálculo do ISSQN")
    vl_issqn = fields.Integer("Valor do ISSQN")
    vl_bc_irrf = fields.Integer(
        "Valor da base de cálculo do Imposto de RendaRetido na Fonte"
    )
    vl_irrf = fields.Integer("Valor do Imposto de Renda - Retido na Fonte")
    vl_bc_prev = fields.Integer("VL_BC_PREV")
    vl_prev = fields.Integer(
        "Valor   destacado   para   retenção   da   PrevidênciaSocial"
    )


class RegistroC140(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c140"
    _description = u"""Complemento de Documento - Fatura (código 01)"""
    _inherit = "l10n.br.sped.mixin"
    ind_emit = fields.Char(
        "Indicador do emitente do título",
        required=True,
        help="""Indicador do emitente do título:0- Emissão própria;1- Terceiros
Ver pagina 54""",
    )
    ind_tit = fields.Char(
        "Indicador do tipo de título de crédito",
        required=True,
        help="""Indicador do tipo de título de crédito:00- Duplicata;01- Cheque;02- Promissória;03- Recibo;99- Outros (descrever)
Ver pagina 54""",
    )
    desc_tit = fields.Char(
        "Descrição complementar do título de crédito",
        help="""Descrição complementar do título de crédito
Ver pagina 54""",
    )
    num_tit = fields.Char(
        "Número   ou   código   identificador   do   título   decrédito",
        required=True,
        help="""Número   ou   código   identificador   do   título   decrédito
Ver pagina 54""",
    )
    qtd_parc = fields.Integer("Quantidade de parcelas a receber/pagar", required=True)
    vl_tit = fields.Integer("Valor total dos títulos de créditos", required=True)
    reg_c141_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.c141",
        "parent_c140_id",
        string="Complemento de Documento - Vencimento da Fatura (código 01)",
        help="Bloco C",
    )


class RegistroC141(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c141"
    _description = u"""Complemento de Documento - Vencimento da Fatura (código 01)"""
    _inherit = "l10n.br.sped.mixin"
    num_parc = fields.Integer("Número da parcela a receber/pagar", required=True)
    dt_vcto = fields.Integer("Data de vencimento da parcela", required=True)
    vl_parc = fields.Integer("Valor da parcela a receber/pagar", required=True)
    parent_c140_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c140",
        string="Complemento de Documento - Fatura (código 01)",
    )


class RegistroC160(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c160"
    _description = u"""Complemento de Documento - Volumes Transportados (código 01 e 04) Exceto Combustíveis"""
    _inherit = "l10n.br.sped.mixin"
    cod_part = fields.Char(
        "Código do participante (campo 02 do Registro 0150)",
        help="""Código do participante (campo 02 do Registro 0150):- transportador, se houver
Ver pagina 55""",
    )
    veic_id = fields.Char(
        "Placa de identificação do veículo automotor",
        help="""Placa de identificação do veículo automotor
Ver pagina 55""",
    )
    qtd_vol = fields.Integer("Quantidade de volumes transportados")
    peso_brt = fields.Integer("Peso bruto dos volumes transportados (em Kg)")
    peso_liq = fields.Integer("Peso líquido dos volumes transportados (em Kg)")
    uf_id = fields.Char(
        "Sigla da UF da placa do veículo",
        help="""Sigla da UF da placa do veículo
Ver pagina 55""",
    )


class RegistroC165(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c165"
    _description = (
        u"""Complemento de Documento - Operações com combustíveis (código 01)"""
    )
    _inherit = "l10n.br.sped.mixin"
    cod_part = fields.Char(
        "Código do participante (campo 02 do Registro 0150)",
        help="""Código do participante (campo 02 do Registro 0150):- transportador, se houver
Ver pagina 55""",
    )
    veic_id = fields.Char(
        "Placa de identificação do veículo",
        help="""Placa de identificação do veículo
Ver pagina 55""",
    )
    cod_aut = fields.Char(
        "COD_AUT",
        help="""Código   da   autorização   fornecido   pela   SEFAZ(combustíveis)
Ver pagina 55""",
    )
    nr_passe = fields.Char(
        "Número do Passe Fiscal",
        help="""Número do Passe Fiscal
Ver pagina 55""",
    )
    hora = fields.Integer("Hora da saída das mercadorias")
    temper = fields.Integer("TEMPER")
    qtd_vol = fields.Integer("Quantidade de volumes transportados")
    peso_brt = fields.Integer("Peso bruto dos volumes transportados (em Kg)")
    peso_liq = fields.Integer("Peso líquido dos volumes transportados (em Kg)")
    nom_mot = fields.Char(
        "Nome do motorista",
        help="""Nome do motorista
Ver pagina 55""",
    )
    cpf = fields.Integer("CPF do motorista")
    uf_id = fields.Char(
        "Sigla da UF da placa do veículo",
        help="""Sigla da UF da placa do veículo
Ver pagina 55""",
    )
    parent_c100_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c100",
        string="Documento - Nota Fiscal (código 01), Nota Fiscal Avulsa (código 1B), Nota Fiscal de Produtor (código 04), Nota Fiscal Eletrônica (código 55) e Nota Fiscal Eletrônica para Consumidor Final (código 65)",
    )


class RegistroC170(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c170"
    _description = (
        u"""Complemento de Documento - Itens do Documento (código 01, 1B, 04 e 55)"""
    )
    _inherit = "l10n.br.sped.mixin"
    num_item = fields.Integer(
        "Número sequencial do item no documento fiscal", required=True
    )
    cod_item = fields.Char(
        "Código do item (campo 02 do Registro 0200)",
        required=True,
        help="""Código do item (campo 02 do Registro 0200)
Ver pagina 56""",
    )
    descr_compl = fields.Char(
        "Descrição complementar do item como adotadono documento fiscal",
        help="""Descrição complementar do item como adotadono documento fiscal
Ver pagina 56""",
    )
    qtd = fields.Integer("Quantidade do item", required=True)
    unid = fields.Char(
        "Unidade do item (Campo 02 do registro 0190)",
        required=True,
        help="""Unidade do item (Campo 02 do registro 0190)
Ver pagina 56""",
    )
    vl_item = fields.Integer(
        "Valor total do item (mercadorias ou serviços)", required=True
    )
    vl_desc = fields.Integer("Valor do desconto comercial")
    ind_mov = fields.Char(
        "Movimentação física do ITEM/PRODUTO",
        required=True,
        help="""Movimentação física do ITEM/PRODUTO:0. SIM1. NÃO
Ver pagina 56""",
    )
    cst_icms = fields.Integer("CST_ICMS", required=True)
    cfop = fields.Integer("Código Fiscal de Operação e Prestação", required=True)
    cod_nat = fields.Char(
        "Código da natureza da operação (campo 02 doRegistro 0400)",
        help="""Código da natureza da operação (campo 02 doRegistro 0400)
Ver pagina 56""",
    )
    vl_bc_icms = fields.Integer("Valor da base de cálculo do ICMS")
    aliq_icms = fields.Monetary("Alíquota do ICMS", digits=2)
    vl_icms = fields.Integer("Valor do ICMS creditado/debitado")
    vl_bc_icms_st = fields.Integer(
        "Valor da base de cálculo referente à substituiçãotributária"
    )
    aliq_st = fields.Integer("ALIQ_ST")
    vl_icms_st = fields.Integer("Valor do ICMS referente à substituição tributária")
    ind_apur = fields.Char(
        "Indicador de período de apuração do IPI",
        help="""Indicador de período de apuração do IPI:0 - Mensal;1 - Decendial
Ver pagina 56""",
    )
    cst_ipi = fields.Char(
        "CST_IPI",
        help="""Código da Situação Tributária referente ao IPI,conforme a Tabela indicada no item 4.3.2.
Ver pagina 56""",
    )
    cod_enq = fields.Char(
        "COD_ENQ",
        help="""Código de enquadramento legal do IPI, conformetabela indicada no item 4.5.3.
Ver pagina 56""",
    )
    vl_bc_ipi = fields.Integer("Valor da base de cálculo do IPI")
    aliq_ipi = fields.Monetary("Alíquota do IPI", digits=2)
    vl_ipi = fields.Integer("Valor do IPI creditado/debitado")
    cst_pis = fields.Integer("Código da Situação Tributária referente ao PIS")
    vl_bc_pis = fields.Integer("Valor da base de cálculo do PIS")
    aliq_pis = fields.Monetary("Alíquota do PIS (em percentual)", digits=4)
    quant_bc_pis = fields.Integer("Quantidade – Base de cálculo PIS")
    aliq_pis = fields.Integer("Alíquota do PIS (em reais)")
    vl_pis = fields.Integer("Valor do PIS")
    cst_cofins = fields.Integer(
        "Código   da   Situação   Tributária   referente   aoCOFINS"
    )
    vl_bc_cofins = fields.Integer("Valor da base de cálculo da COFINS")
    aliq_cofins = fields.Monetary("Alíquota do COFINS (em percentual)", digits=4)
    quant_bc_cofins = fields.Integer("Quantidade – Base de cálculo COFINS")
    aliq_cofins = fields.Integer("Alíquota da COFINS (em reais)")
    vl_cofins = fields.Integer("Valor da COFINS")
    cod_cta = fields.Char(
        "Código da conta analítica contábildebitada/creditada",
        help="""Código da conta analítica contábildebitada/creditada
Ver pagina 57""",
    )
    parent_c100_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c100",
        string="Documento - Nota Fiscal (código 01), Nota Fiscal Avulsa (código 1B), Nota Fiscal de Produtor (código 04), Nota Fiscal Eletrônica (código 55) e Nota Fiscal Eletrônica para Consumidor Final (código 65)",
    )
    reg_c172_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c172",
        string="Complemento de Item - Operações com ISSQN (código 01)",
        help="Bloco C",
    )  # m2o
    reg_c177_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c177",
        string="Complemento de Item - Operações com Produtos Sujeitos a Selo de Controle IPI (código 01)",
        help="Bloco C",
    )  # m2o
    reg_c178_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c178",
        string="Complemento de Item - Operações com Produtos Sujeitos a Tributação de IPI por Unidade ou Quantidade de produto",
        help="Bloco C",
    )  # m2o
    reg_c179_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c179",
        string="Complemento de Item - Informações Complementares ST (código 01)",
        help="Bloco C",
    )  # m2o
    reg_c171_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.c171",
        "parent_c170_id",
        string="Complemento de Item - Armazenamento de Combustíveis (código 01,55)",
        help="Bloco C",
    )
    reg_c173_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.c173",
        "parent_c170_id",
        string="Complemento de Item - Operações com Medicamentos (código 01,55)",
        help="Bloco C",
    )
    reg_c174_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.c174",
        "parent_c170_id",
        string="Complemento de Item - Operações com Armas de Fogo (código 01)",
        help="Bloco C",
    )
    reg_c175_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.c175",
        "parent_c170_id",
        string="Complemento de Item - Operações com Veículos Novos (código 01,55)",
        help="Bloco C",
    )
    reg_c176_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.c176",
        "parent_c170_id",
        string="Complemento de Item -Ressarcimento de ICMS em operações com Substituição Tributária (código 01,55)",
        help="Bloco C",
    )


class RegistroC171(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c171"
    _description = (
        u"""Complemento de Item - Armazenamento de Combustíveis (código 01,55)"""
    )
    _inherit = "l10n.br.sped.mixin"
    num_tanque = fields.Char(
        "Tanque onde foi armazenado o combustível",
        help="""Tanque onde foi armazenado o combustível
Ver pagina 61""",
    )
    qtde = fields.Integer("Quantidade ou volume armazenado")
    parent_c170_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c170",
        string="Complemento de Documento - Itens do Documento (código 01, 1B, 04 e 55)",
    )


class RegistroC172(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c172"
    _description = u"""Complemento de Item - Operações com ISSQN (código 01)"""
    _inherit = "l10n.br.sped.mixin"
    vl_bc_issqn = fields.Integer("Valor da base de cálculo do ISSQN")
    aliq_issqn = fields.Monetary("Alíquota do ISSQN", digits=2)
    vl_issqn = fields.Integer("Valor do ISSQN")


class RegistroC173(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c173"
    _description = (
        u"""Complemento de Item - Operações com Medicamentos (código 01,55)"""
    )
    _inherit = "l10n.br.sped.mixin"
    lote_med = fields.Char(
        "Número do lote de fabricação do medicamento",
        required=True,
        help="""Número do lote de fabricação do medicamento
Ver pagina 62""",
    )
    qtd_item = fields.Integer("Quantidade de item por lote", required=True)
    dt_fab = fields.Integer("Data de fabricação do medicamento", required=True)
    dt_val = fields.Integer(
        "Data de expiração da validade do medicamento", required=True
    )
    ind_med = fields.Char(
        "IND_MED",
        required=True,
        help="""Indicador de tipo de referência da base de cálculo do ICMS (ST) do produto farmacêutico:0- Base de cálculo referente ao preço tabelado ou preço máximo sugerido;1- Base cálculo – Margem de valor agregado; 2- Base de cálculo referente à Lista Negativa;3- Base de cálculo referente à Lista Positiva;4- Base de cálculo referente à Lista Neutra
Ver pagina 62""",
    )
    tp_prod = fields.Char(
        "Tipo de produto:0- Similar;1- Genérico;2- Ético ou de marca;",
        required=True,
        help="""Tipo de produto:0- Similar;1- Genérico;2- Ético ou de marca;
Ver pagina 62""",
    )
    vl_tab_max = fields.Integer(
        "Valor   do   preço   tabelado   ou   valor   do   preçomáximo", required=True
    )
    parent_c170_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c170",
        string="Complemento de Documento - Itens do Documento (código 01, 1B, 04 e 55)",
    )


class RegistroC174(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c174"
    _description = u"""Complemento de Item - Operações com Armas de Fogo (código 01)"""
    _inherit = "l10n.br.sped.mixin"
    ind_arm = fields.Char(
        "Indicador do tipo da arma de fogo",
        help="""Indicador do tipo da arma de fogo:0- Uso permitido;1- Uso restrito
Ver pagina 63""",
    )
    num_arm = fields.Char(
        "Numeração de série de fabricação da arma",
        help="""Numeração de série de fabricação da arma
Ver pagina 63""",
    )
    parent_c170_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c170",
        string="Complemento de Documento - Itens do Documento (código 01, 1B, 04 e 55)",
    )


class RegistroC175(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c175"
    _description = (
        u"""Complemento de Item - Operações com Veículos Novos (código 01,55)"""
    )
    _inherit = "l10n.br.sped.mixin"
    ind_veic_oper = fields.Char(
        "Indicador do tipo de operação com veículo",
        required=True,
        help="""Indicador do tipo de operação com veículo:0- Venda para concessionária;1- Faturamento direto;2- Venda direta;3- Venda da concessionária;9- Outros
Ver pagina 63""",
    )
    cnpj = fields.Integer("CNPJ da Concessionária")
    uf = fields.Char(
        "Sigla da unidade da federação da Concessionária",
        help="""Sigla da unidade da federação da Concessionária
Ver pagina 63""",
    )
    chassi_veic = fields.Char(
        "Chassi do veículo",
        required=True,
        help="""Chassi do veículo
Ver pagina 63""",
    )
    parent_c170_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c170",
        string="Complemento de Documento - Itens do Documento (código 01, 1B, 04 e 55)",
    )


class RegistroC176(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c176"
    _description = u"""Complemento de Item -Ressarcimento de ICMS em operações com Substituição Tributária (código 01,55)"""
    _inherit = "l10n.br.sped.mixin"
    cod_mod_ult_e = fields.Char(
        "Código do modelo do documento fiscal relativa aúltima entrada",
        help="""Código do modelo do documento fiscal relativa aúltima entrada
Ver pagina 64""",
    )
    num_doc_ult_e = fields.Integer(
        "Número   do   documento   fiscal   relativa   a   últimaentrada"
    )
    ser_ult_e = fields.Char(
        "Série   do   documento   fiscal   relativa   a   últimaentrada",
        help="""Série   do   documento   fiscal   relativa   a   últimaentrada
Ver pagina 64""",
    )
    dt_ult_e = fields.Integer("Data relativa a última entrada da mercadoria")
    cod_part_ult_e = fields.Char(
        "COD_PART_ULT_E",
        help="""Código   do   participante (do   emitente   dodocumento relativa a última entrada)
Ver pagina 64""",
    )
    quant_ult_e = fields.Integer("Quantidade do item relativa a última entrada")
    vl_unit_ult_e = fields.Integer("VL_UNIT_ULT_E")
    vl_unit_bc_st = fields.Integer("VL_UNIT_BC_ST")
    chave_nfe_ult_e = fields.Integer("CHAVE_NFE_ULT_E")
    num_item_ult_e = fields.Integer("NUM_ITEM_ULT_E")
    vl_unit_bc_icms_ult_e = fields.Integer("VL_UNIT_BC_ICMS_ULT_E")
    aliq_icms_ult_e = fields.Integer(
        "Alíquota do ICMS aplicável à última entrada damercadoria"
    )
    vl_unit_limite_bc_icms_ult_e = fields.Integer("VL_UNIT_LIMITE_BC_ICMS_ULT_E")
    vl_unit_icms_ult_e = fields.Integer("VL_UNIT_ICMS_ULT_E")
    aliq_st_ult_e = fields.Integer(
        "Alíquota do ICMS ST relativa à última entrada damercadoria"
    )
    vl_unit_res = fields.Integer("VL_UNIT_RES")
    cod_resp_ret = fields.Integer(
        "Código que indica o responsável pela retenção doICMS-ST"
    )
    cod_mot_res = fields.Integer("Código do motivo do ressarcimento")
    chave_nfe_ret = fields.Integer("CHAVE_NFE_RET")
    cod_part_nfe_ret = fields.Char(
        "COD_PART_NFE_RET",
        help="""Código do participante do emitente da NF-e emque houve a retenção do ICMS-ST – campo 02 doregistro 0150
Ver pagina 65""",
    )
    ser_nfe_ret = fields.Char(
        "Série da NF-e em que houve a retenção do ICMS-ST",
        help="""Série da NF-e em que houve a retenção do ICMS-ST
Ver pagina 65""",
    )
    num_nfe_ret = fields.Integer("Número da NF-e em que houve a retenção doICMS-ST")
    item_nfe_ret = fields.Integer("ITEM_NFE_RET")
    cod_da = fields.Char(
        "Código do modelo do documento de arrecadação",
        help="""Código do modelo do documento de arrecadação:0 – Documento estadual de arrecadação1 – GNRE
Ver pagina 65""",
    )
    num_da = fields.Char(
        "Número do documento de arrecadação estadual,se houver",
        help="""Número do documento de arrecadação estadual,se houver
Ver pagina 65""",
    )
    parent_c170_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c170",
        string="Complemento de Documento - Itens do Documento (código 01, 1B, 04 e 55)",
    )


class RegistroC177(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c177"
    _description = u"""Complemento de Item - Operações com Produtos Sujeitos a Selo de Controle IPI (código 01)"""
    _inherit = "l10n.br.sped.mixin"
    cod_selo_ipi = fields.Char(
        "COD_SELO_IPI",
        help="""Código   do   selo   de   controle   do   IPI,   conformeTabela 4.5.2
Ver pagina 67""",
    )
    qt_selo_ipi = fields.Integer("Quantidade de selo de controle do IPI aplicada")


class RegistroC178(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c178"
    _description = u"""Complemento de Item - Operações com Produtos Sujeitos a Tributação de IPI por Unidade ou Quantidade de produto"""
    _inherit = "l10n.br.sped.mixin"
    cl_enq = fields.Char(
        "CL_ENQ",
        help="""Código   da   classe   de   enquadramento   do   IPI,conforme Tabela 4.5.1.
Ver pagina 67""",
    )
    vl_unid = fields.Integer("Valor por unidade padrão de tributação")
    quant_pad = fields.Integer(
        "Quantidade total de produtos na unidade padrão detributação"
    )


class RegistroC179(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c179"
    _description = (
        u"""Complemento de Item - Informações Complementares ST (código 01)"""
    )
    _inherit = "l10n.br.sped.mixin"
    bc_st_orig_dest = fields.Integer("BC_ST_ORIG_DEST")
    icms_st_rep = fields.Integer("ICMS_ST_REP")
    icms_st_compl = fields.Integer(
        "Valor   do ICMS-ST a  complementar  à  UF   dedestino"
    )
    bc_ret = fields.Integer("BC_RET")
    icms_ret = fields.Integer("ICMS_RET")


class RegistroC190(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c190"
    _description = u"""Registro Analítico do Documento (código 01, 1B, 04, 55 e 65)"""
    _inherit = "l10n.br.sped.mixin"
    cst_icms = fields.Integer("CST_ICMS", required=True)
    cfop = fields.Integer("CFOP", required=True)
    aliq_icms = fields.Monetary("Alíquota do ICMS", digits=2)
    vl_opr = fields.Integer("VL_OPR", required=True)
    vl_bc_icms = fields.Integer("VL_BC_ICMS", required=True)
    vl_icms = fields.Integer("VL_ICMS", required=True)
    vl_bc_icms_st = fields.Integer("VL_BC_ICMS_ST", required=True)
    vl_icms_st = fields.Integer("VL_ICMS_ST", required=True)
    vl_red_bc = fields.Integer("VL_RED_BC", required=True)
    vl_ipi = fields.Integer("VL_IPI", required=True)
    cod_obs = fields.Char(
        "Código   da   observação   do  lançamento   fiscal",
        help="""Código   da   observação   do  lançamento   fiscal
Ver pagina 68""",
    )
    parent_c100_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c100",
        string="Documento - Nota Fiscal (código 01), Nota Fiscal Avulsa (código 1B), Nota Fiscal de Produtor (código 04), Nota Fiscal Eletrônica (código 55) e Nota Fiscal Eletrônica para Consumidor Final (código 65)",
    )


class RegistroC195(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c195"
    _description = u"""Complemento do Registro Analítico - Observações do Lançamento Fiscal (código 01, 1B, 04 e 55)"""
    _inherit = "l10n.br.sped.mixin"
    cod_obs = fields.Char(
        "COD_OBS",
        required=True,
        help="""Código da observação do lançamento fiscal (campo02 do Registro 0460)
Ver pagina 70""",
    )
    txt_compl = fields.Char(
        "Descrição complementar do código de observação",
        help="""Descrição complementar do código de observação.
Ver pagina 70""",
    )
    parent_c100_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c100",
        string="Documento - Nota Fiscal (código 01), Nota Fiscal Avulsa (código 1B), Nota Fiscal de Produtor (código 04), Nota Fiscal Eletrônica (código 55) e Nota Fiscal Eletrônica para Consumidor Final (código 65)",
    )
    reg_c197_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.c197",
        "parent_c195_id",
        string="Outras Obrigações Tributárias, Ajustes e Informações provenientes de Documento Fiscal",
        help="Bloco C",
    )


class RegistroC197(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c197"
    _description = u"""Outras Obrigações Tributárias, Ajustes e Informações provenientes de Documento Fiscal"""
    _inherit = "l10n.br.sped.mixin"
    cod_aj = fields.Char(
        "COD_AJ",
        required=True,
        help="""Código do ajustes/benefício/incentivo, conformetabela indicada no item 5.3.
Ver pagina 71""",
    )
    parent_c195_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c195",
        string="Complemento do Registro Analítico - Observações do Lançamento Fiscal (código 01, 1B, 04 e 55)",
    )


class RegistroC300(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c300"
    _description = u"""Documento - Resumo Diário das Notas Fiscais de Venda a Consumidor (código 02)"""
    _inherit = "l10n.br.sped.mixin"
    cod_mod = fields.Char(
        "Código do modelo do documento fiscal, conformea Tabela 4",
        help="""Código do modelo do documento fiscal, conformea Tabela 4.1.1
Ver pagina 72""",
    )
    ser = fields.Char(
        "Série do documento fiscal",
        help="""Série do documento fiscal
Ver pagina 72""",
    )
    sub = fields.Char(
        "Subsérie do documento fiscal",
        help="""Subsérie do documento fiscal
Ver pagina 72""",
    )
    num_doc_ini = fields.Integer("Número do documento fiscal inicial")
    num_doc_fin = fields.Integer("Número do documento fiscal final")
    dt_doc = fields.Integer("Data da emissão dos documentos fiscais")
    vl_doc = fields.Integer("Valor total dos documentos")
    vl_pis = fields.Integer("Valor total do PIS")
    vl_cofins = fields.Integer("Valor total da COFINS")
    cod_cta = fields.Char(
        "Código da conta analítica contábildebitada/creditada",
        help="""Código da conta analítica contábildebitada/creditada
Ver pagina 72""",
    )
    reg_c310_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.c310",
        "parent_c300_id",
        string="Documentos Cancelados de Nota Fiscal de Venda a Consumidor (código 02)",
        help="Bloco C",
    )
    reg_c320_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.c320",
        "parent_c300_id",
        string="Registro Analítico das Notas Fiscais de Venda a Consumidor (código 02)",
        help="Bloco C",
    )


class RegistroC310(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c310"
    _description = (
        u"""Documentos Cancelados de Nota Fiscal de Venda a Consumidor (código 02)"""
    )
    _inherit = "l10n.br.sped.mixin"
    parent_c300_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c300",
        string="Documento - Resumo Diário das Notas Fiscais de Venda a Consumidor (código 02)",
    )


class RegistroC320(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c320"
    _description = (
        u"""Registro Analítico das Notas Fiscais de Venda a Consumidor (código 02)"""
    )
    _inherit = "l10n.br.sped.mixin"
    cst_icms = fields.Integer("CST_ICMS")
    cfop = fields.Integer("Código Fiscal de Operação e Prestação")
    aliq_icms = fields.Monetary("Alíquota do ICMS", digits=2)
    vl_opr = fields.Integer("VL_OPR")
    vl_bc_icms = fields.Integer("VL_BC_ICMS")
    vl_icms = fields.Integer("VL_ICMS")
    vl_red_bc = fields.Integer("VL_RED_BC")
    cod_obs = fields.Char(
        "COD_OBS",
        help="""Código   da   observação   do   lançamento   fiscal(campo 02 do Registro 0460)
Ver pagina 73""",
    )
    parent_c300_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c300",
        string="Documento - Resumo Diário das Notas Fiscais de Venda a Consumidor (código 02)",
    )
    reg_c321_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.c321",
        "parent_c320_id",
        string="Itens dos Resumos Diários dos Documentos (código 02)",
        help="Bloco C",
    )


class RegistroC321(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c321"
    _description = u"""Itens dos Resumos Diários dos Documentos (código 02)"""
    _inherit = "l10n.br.sped.mixin"
    cod_item = fields.Char(
        "Código do item (campo 02 do Registro 0200)",
        help="""Código do item (campo 02 do Registro 0200)
Ver pagina 73""",
    )
    qtd = fields.Integer("Quantidade acumulada do item")
    unid = fields.Char(
        "Unidade do item (Campo 02 do registro 0190)",
        help="""Unidade do item (Campo 02 do registro 0190)
Ver pagina 73""",
    )
    vl_item = fields.Integer("Valor acumulado do item")
    vl_desc = fields.Integer("Valor do desconto acumulado")
    vl_bc_icms = fields.Integer("Valor acumulado da base de cálculo do ICMS")
    vl_icms = fields.Integer("Valor acumulado do ICMS debitado")
    vl_pis = fields.Integer("Valor acumulado do PIS")
    vl_cofins = fields.Integer("Valor acumulado da COFINS")
    parent_c320_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c320",
        string="Registro Analítico das Notas Fiscais de Venda a Consumidor (código 02)",
    )


class RegistroC350(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c350"
    _description = u"""Nota Fiscal de venda a consumidor (código 02)"""
    _inherit = "l10n.br.sped.mixin"
    ser = fields.Char(
        "Série do documento fiscal",
        help="""Série do documento fiscal
Ver pagina 74""",
    )
    sub_ser = fields.Char(
        "Subsérie do documento fiscal",
        help="""Subsérie do documento fiscal
Ver pagina 74""",
    )
    num_doc = fields.Integer("Número do documento fiscal")
    dt_doc = fields.Integer("Data da emissão do documento fiscal")
    cnpj_cpf = fields.Integer("CNPJ ou CPF do destinatário")
    vl_merc = fields.Integer("Valor das mercadorias constantes no documento fiscal")
    vl_doc = fields.Integer("Valor total do documento fiscal")
    vl_desc = fields.Integer("Valor total do desconto")
    vl_pis = fields.Integer("Valor total do PIS")
    vl_cofins = fields.Integer("Valor total da COFINS")
    cod_cta = fields.Char(
        "Código da conta analítica contábil debitada/creditada",
        help="""Código da conta analítica contábil debitada/creditada
Ver pagina 74""",
    )
    reg_c370_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.c370",
        "parent_c350_id",
        string="Itens do documento (código 02)",
        help="Bloco C",
    )
    reg_c390_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.c390",
        "parent_c350_id",
        string="Registro Analítico das Notas Fiscais de Venda a Consumidor (código 02)",
        help="Bloco C",
    )


class RegistroC370(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c370"
    _description = u"""Itens do documento (código 02)"""
    _inherit = "l10n.br.sped.mixin"
    num_item = fields.Integer("Número sequencial do item no documento fiscal")
    cod_item = fields.Char(
        "Código do Item (campo 02 do registro 0200)",
        help="""Código do Item (campo 02 do registro 0200)
Ver pagina 75""",
    )
    qtd = fields.Integer("Quantidade do item")
    unid = fields.Char(
        "Unidade do item (campo 02 do registro 0190)",
        help="""Unidade do item (campo 02 do registro 0190)
Ver pagina 75""",
    )
    vl_item = fields.Integer("Valor total do item")
    vl_desc = fields.Integer("Valor total do desconto no item")
    parent_c350_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c350",
        string="Nota Fiscal de venda a consumidor (código 02)",
    )


class RegistroC390(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c390"
    _description = (
        u"""Registro Analítico das Notas Fiscais de Venda a Consumidor (código 02)"""
    )
    _inherit = "l10n.br.sped.mixin"
    cst_icms = fields.Integer("CST_ICMS")
    cfop = fields.Integer("Código Fiscal de Operação e Prestação")
    aliq_icms = fields.Monetary("Alíquota do ICMS", digits=2)
    vl_opr = fields.Integer("VL_OPR")
    vl_bc_icms = fields.Integer("VL_BC_ICMS")
    vl_icms = fields.Integer("VL_ICMS")
    vl_red_bc = fields.Integer("VL_RED_BC")
    cod_obs = fields.Char(
        "COD_OBS",
        help="""Código da observação do lançamento fiscal (campo 02 do Registro 0460)
Ver pagina 75""",
    )
    parent_c350_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c350",
        string="Nota Fiscal de venda a consumidor (código 02)",
    )


class RegistroC400(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c400"
    _description = u"""Equipamento ECF (código 02, 2D e 60),"""
    _inherit = "l10n.br.sped.mixin"
    cod_mod = fields.Char(
        "COD_MOD",
        help="""Código   do   modelo   do   documento  fiscal,conforme a Tabela 4.1.1
Ver pagina 76""",
    )
    ecf_mod = fields.Char(
        "Modelo do equipamento",
        help="""Modelo do equipamento
Ver pagina 76""",
    )
    ecf_fab = fields.Char(
        "Número de série de fabricação do ECF",
        help="""Número de série de fabricação do ECF
Ver pagina 76""",
    )
    ecf_cx = fields.Integer("Número do caixa atribuído ao ECF")
    reg_c405_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.c405",
        "parent_c400_id",
        string="Redução Z (código 02, 2D e 60)",
        help="Bloco C",
    )


class RegistroC405(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c405"
    _description = u"""Redução Z (código 02, 2D e 60)"""
    _inherit = "l10n.br.sped.mixin"
    dt_doc = fields.Integer("Data do movimento a que se refere a Redução Z")
    cro = fields.Integer("Posição do Contador de Reinício de Operação")
    crz = fields.Integer("Posição do Contador de Redução Z")
    num_coo_fin = fields.Integer("NUM_COO_FIN")
    gt_fin = fields.Integer("Valor do Grande Total final")
    vl_brt = fields.Integer("Valor da venda bruta")
    parent_c400_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c400", string="Equipamento ECF (código 02, 2D e 60),"
    )
    reg_c410_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c410",
        string="PIS e COFINS Totalizados no Dia (código 02 e 2D)",
        help="Bloco C",
    )  # m2o
    reg_c420_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.c420",
        "parent_c405_id",
        string="Registro dos Totalizadores Parciais da Redução Z (código 02, 2D e 60)",
        help="Bloco C",
    )
    reg_c460_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.c460",
        "parent_c405_id",
        string="Documento Fiscal Emitido por ECF (código 02, 2D e 60)",
        help="Bloco C",
    )
    reg_c490_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.c490",
        "parent_c405_id",
        string="Registro Analítico do movimento diário (código 02, 2D e 60)",
        help="Bloco C",
    )


class RegistroC410(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c410"
    _description = u"""PIS e COFINS Totalizados no Dia (código 02 e 2D)"""
    _inherit = "l10n.br.sped.mixin"
    vl_pis = fields.Integer("Valor total do PIS")
    vl_cofins = fields.Integer("Valor total da COFINS")


class RegistroC420(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c420"
    _description = (
        u"""Registro dos Totalizadores Parciais da Redução Z (código 02, 2D e 60)"""
    )
    _inherit = "l10n.br.sped.mixin"
    cod_tot_par = fields.Char(
        "Código do totalizador, conforme Tabela 4",
        help="""Código do totalizador, conforme Tabela 4.4.6
Ver pagina 77""",
    )
    parent_c405_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c405", string="Redução Z (código 02, 2D e 60)"
    )
    reg_c425_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.c425",
        "parent_c420_id",
        string="Resumo de itens do movimento diário (código 02 e 2D)",
        help="Bloco C",
    )


class RegistroC425(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c425"
    _description = u"""Resumo de itens do movimento diário (código 02 e 2D)"""
    _inherit = "l10n.br.sped.mixin"
    cod_item = fields.Char(
        "Código do item (campo 02 do Registro 0200)",
        help="""Código do item (campo 02 do Registro 0200)
Ver pagina 78""",
    )
    qtd = fields.Integer("Quantidade acumulada do item")
    unid = fields.Char(
        "Unidade do item (Campo 02 do registro 0190)",
        help="""Unidade do item (Campo 02 do registro 0190)
Ver pagina 78""",
    )
    vl_item = fields.Integer("Valor acumulado do item")
    vl_pis = fields.Integer("Valor do PIS")
    vl_cofins = fields.Integer("Valor da COFINS")
    parent_c420_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c420",
        string="Registro dos Totalizadores Parciais da Redução Z (código 02, 2D e 60)",
    )


class RegistroC460(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c460"
    _description = u"""Documento Fiscal Emitido por ECF (código 02, 2D e 60)"""
    _inherit = "l10n.br.sped.mixin"
    cod_mod = fields.Char(
        "COD_MOD",
        help="""Código   do   modelo   do   documento  fiscal,conforme a Tabela 4.1.1
Ver pagina 79""",
    )
    cod_sit = fields.Integer("COD_SIT")
    num_doc = fields.Integer("Número do documento fiscal (COO)")
    dt_doc = fields.Integer("Data da emissão do documento fiscal")
    vl_doc = fields.Integer("Valor total do documento fiscal")
    vl_pis = fields.Integer("Valor do PIS")
    vl_cofins = fields.Integer("Valor da COFINS")
    cpf_cnpj = fields.Integer("CPF ou CNPJ do adquirente")
    nom_adq = fields.Char(
        "Nome do adquirente",
        help="""Nome do adquirente
Ver pagina 79""",
    )
    parent_c405_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c405", string="Redução Z (código 02, 2D e 60)"
    )
    reg_c465_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c465",
        string="Complemento do Cupom Fiscal Eletrônico Emitido por ECF - CF-e-ECF (código 60)",
        help="Bloco C",
    )  # m2o
    reg_c470_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.c470",
        "parent_c460_id",
        string="Itens do Documento Fiscal Emitido por ECF (código 02 e 2D)",
        help="Bloco C",
    )


class RegistroC465(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c465"
    _description = u"""Complemento do Cupom Fiscal Eletrônico Emitido por ECF - CF-e-ECF (código 60)"""
    _inherit = "l10n.br.sped.mixin"
    chv_cfe = fields.Integer("Chave do Cupom Fiscal Eletrônico")
    num_ccf = fields.Integer("Número do Contador de Cupom Fiscal")


class RegistroC470(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c470"
    _description = u"""Itens do Documento Fiscal Emitido por ECF (código 02 e 2D)"""
    _inherit = "l10n.br.sped.mixin"
    cod_item = fields.Char(
        "Código do item (campo 02 do Registro 0200)",
        help="""Código do item (campo 02 do Registro 0200)
Ver pagina 80""",
    )
    qtd = fields.Integer("Quantidade do item")
    qtd_canc = fields.Integer(
        "Quantidade cancelada, no caso de cancelamentoparcial de item"
    )
    unid = fields.Char(
        "Unidade do item (Campo 02 do registro 0190)",
        help="""Unidade do item (Campo 02 do registro 0190)
Ver pagina 80""",
    )
    vl_item = fields.Integer("Valor total do item")
    cst_icms = fields.Integer("CST_ICMS")
    cfop = fields.Integer("Código Fiscal de Operação e Prestação")
    aliq_icms = fields.Monetary(
        "Alíquota do ICMS – Carga tributária efetiva empercentual", digits=2
    )
    vl_pis = fields.Integer("Valor do PIS")
    vl_cofins = fields.Integer("Valor da COFINS")
    parent_c460_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c460",
        string="Documento Fiscal Emitido por ECF (código 02, 2D e 60)",
    )


class RegistroC490(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c490"
    _description = u"""Registro Analítico do movimento diário (código 02, 2D e 60)"""
    _inherit = "l10n.br.sped.mixin"
    cst_icms = fields.Integer("CST_ICMS")
    cfop = fields.Integer("Código Fiscal de Operação e Prestação")
    aliq_icms = fields.Monetary("Alíquota do ICMS", digits=2)
    vl_opr = fields.Integer("VL_OPR")
    vl_bc_icms = fields.Integer("VL_BC_ICMS")
    vl_icms = fields.Integer("VL_ICMS")
    cod_obs = fields.Char(
        "COD_OBS",
        help="""Código   da   observação   do   lançamento   fiscal(campo 02 do Registro 0460)
Ver pagina 81""",
    )
    parent_c405_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c405", string="Redução Z (código 02, 2D e 60)"
    )


class RegistroC495(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c495"
    _description = (
        u"""Resumo Mensal de Itens do ECF por Estabelecimento (código 02 e 2D e 2E)"""
    )
    _inherit = "l10n.br.sped.mixin"
    aliq_icms = fields.Monetary("Alíquota do ICMS", digits=2)
    cod_item = fields.Char(
        "Código do item (campo 02 do Registro 0200)",
        help="""Código do item (campo 02 do Registro 0200)
Ver pagina 82""",
    )
    qtd = fields.Integer("Quantidade acumulada do item")
    qtd_canc = fields.Integer("QTD_CANC")
    unid = fields.Char(
        "Unidade do item  (Campo 02 do registro 0190)",
        help="""Unidade do item  (Campo 02 do registro 0190)
Ver pagina 82""",
    )
    vl_item = fields.Integer("Valor acumulado do item")
    vl_desc = fields.Integer("Valor acumulado dos descontos")
    vl_canc = fields.Integer("Valor acumulado dos cancelamentos")
    vl_acmo = fields.Integer("Valor acumulado dos acréscimos")
    vl_bc_icms = fields.Integer("Valor acumulado da base de cálculo do ICMS")
    vl_icms = fields.Integer("Valor acumulado do ICMS")
    vl_isen = fields.Integer("Valor das saídas isentas do ICMS")
    vl_nt = fields.Integer("VL_NT")
    vl_icms_st = fields.Integer("VL_ICMS_ST")


class RegistroC500(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c500"
    _description = u"""Nota Fiscal/Conta de Energia Elétrica (código 06), Nota Fiscal/Conta de fornecimento d'água canalizada (código 29) e Nota Fiscal/Consumo Fornecimento de Gás (Código 28)"""
    _inherit = "l10n.br.sped.mixin"
    ind_oper = fields.Char(
        "Indicador do tipo de operação",
        required=True,
        help="""Indicador do tipo de operação:0- Entrada;1- Saída
Ver pagina 83""",
    )
    ind_emit = fields.Char(
        "Indicador do emitente do documento fiscal",
        required=True,
        help="""Indicador do emitente do documento fiscal:0- Emissão própria;1- Terceiros
Ver pagina 83""",
    )
    cod_part = fields.Char(
        "Código do participante (campo 02 do Registro 0150)",
        required=True,
        help="""Código do participante (campo 02 do Registro 0150):- do adquirente, no caso das saídas;- do fornecedor no caso de entradas
Ver pagina 83""",
    )
    cod_mod = fields.Char(
        "COD_MOD",
        required=True,
        help="""Código   do   modelo   do   documento  fiscal,conforme a Tabela 4.1.1
Ver pagina 83""",
    )
    cod_sit = fields.Integer("COD_SIT", required=True)
    ser = fields.Char(
        "Série do documento fiscal",
        help="""Série do documento fiscal
Ver pagina 83""",
    )
    sub = fields.Integer("Subsérie do documento fiscal")
    cod_cons = fields.Char(
        "- Código de classe de consumo de energia elétrica ou gás",
        required=True,
        help="""- Código de classe de consumo de energia elétrica ou gás:01 - Comercial02 - Consumo Próprio
Ver pagina 83""",
    )
    num_doc = fields.Integer("Número do documento fiscal", required=True)
    dt_doc = fields.Integer("Data da emissão do documento fiscal", required=True)
    dt_e_s = fields.Integer("Data da entrada ou da saída", required=True)
    vl_doc = fields.Integer("Valor total do documento fiscal", required=True)
    vl_desc = fields.Integer("Valor total do desconto")
    vl_forn = fields.Integer("Valor total fornecido/consumido", required=True)
    vl_serv_nt = fields.Integer(
        "Valor   total   dos   serviços   não-tributados   peloICMS"
    )
    vl_terc = fields.Integer("Valor total cobrado em nome de terceiros")
    vl_da = fields.Integer(
        "Valor total de despesas acessórias indicadas nodocumento fiscal"
    )
    vl_bc_icms = fields.Integer("Valor acumulado da base de cálculo do ICMS")
    vl_icms = fields.Integer("Valor acumulado do ICMS")
    vl_bc_icms_st = fields.Integer("VL_BC_ICMS_ST")
    vl_icms_st = fields.Integer(
        "Valor acumulado   do  ICMS  retido   porsubstituição tributária"
    )
    cod_inf = fields.Char(
        "COD_INF",
        help="""Código   da informação  complementar  dodocumento fiscal (campo 02 do Registro 0450)
Ver pagina 84""",
    )
    vl_pis = fields.Integer("Valor do PIS")
    vl_cofins = fields.Integer("Valor da COFINS")
    tp_ligacao = fields.Integer(
        "Código de tipo de Ligação1 - Monofásico2 - Bifásico3 - Trifásico"
    )
    reg_c510_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.c510",
        "parent_c500_id",
        string="Itens do Documento - Nota Fiscal/Conta de Energia Elétrica (código 06), Nota Fiscal/Conta de fornecimento d'água canalizada (código 29) e Nota Fiscal/Conta Fornecimento de Gás (Código 28)",
        help="Bloco C",
    )
    reg_c590_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.c590",
        "parent_c500_id",
        string="Registro Analítico do Documento - Nota Fiscal/Conta de Energia Elétrica (código 06), Nota Fiscal/Conta de fornecimento d'água canalizada (código 29) e Nota Fiscal/Conta Fornecimento de Gás (Código 28)",
        help="Bloco C",
    )


class RegistroC510(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c510"
    _description = u"""Itens do Documento - Nota Fiscal/Conta de Energia Elétrica (código 06), Nota Fiscal/Conta de fornecimento d'água canalizada (código 29) e Nota Fiscal/Conta Fornecimento de Gás (Código 28)"""
    _inherit = "l10n.br.sped.mixin"
    num_item = fields.Integer("Número sequencial do item no documento fiscal")
    cod_item = fields.Char(
        "Código do item (campo 02 do Registro 0200)",
        help="""Código do item (campo 02 do Registro 0200)
Ver pagina 85""",
    )
    cod_class = fields.Integer("COD_CLASS")
    qtd = fields.Integer("Quantidade do item")
    unid = fields.Char(
        "Unidade do item (Campo 02 do registro 0190)",
        help="""Unidade do item (Campo 02 do registro 0190)
Ver pagina 85""",
    )
    vl_item = fields.Integer("Valor do item")
    vl_desc = fields.Integer("Valor total do desconto")
    cst_icms = fields.Integer("CST_ICMS")
    cfop = fields.Integer("Código Fiscal de Operação e Prestação")
    vl_bc_icms = fields.Integer("Valor da base de cálculo do ICMS")
    aliq_icms = fields.Monetary("Alíquota do ICMS", digits=2)
    vl_icms = fields.Integer("Valor do ICMS creditado/debitado")
    parent_c500_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c500",
        string="Nota Fiscal/Conta de Energia Elétrica (código 06), Nota Fiscal/Conta de fornecimento d'água canalizada (código 29) e Nota Fiscal/Consumo Fornecimento de Gás (Código 28)",
    )


class RegistroC590(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c590"
    _description = u"""Registro Analítico do Documento - Nota Fiscal/Conta de Energia Elétrica (código 06), Nota Fiscal/Conta de fornecimento d'água canalizada (código 29) e Nota Fiscal/Conta Fornecimento de Gás (Código 28)"""
    _inherit = "l10n.br.sped.mixin"
    cst_icms = fields.Integer("CST_ICMS", required=True)
    cfop = fields.Integer("CFOP", required=True)
    aliq_icms = fields.Monetary("Alíquota do ICMS", digits=2)
    vl_opr = fields.Integer("VL_OPR", required=True)
    vl_bc_icms = fields.Integer("VL_BC_ICMS", required=True)
    vl_icms = fields.Integer("VL_ICMS", required=True)
    vl_bc_icms_st = fields.Integer("VL_BC_ICMS_ST", required=True)
    vl_icms_st = fields.Integer("VL_ICMS_ST", required=True)
    vl_red_bc = fields.Integer("VL_RED_BC", required=True)
    cod_obs = fields.Char(
        "COD_OBS",
        help="""Código   da   observação   do  lançamento   fiscal(campo 02 do Registro 0460)
Ver pagina 87""",
    )
    parent_c500_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c500",
        string="Nota Fiscal/Conta de Energia Elétrica (código 06), Nota Fiscal/Conta de fornecimento d'água canalizada (código 29) e Nota Fiscal/Consumo Fornecimento de Gás (Código 28)",
    )


class RegistroC600(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c600"
    _description = u"""Consolidação Diária de Notas Fiscais/Contas de Energia Elétrica (Código 06), Nota Fiscal/Conta de Fornecimento d´água (código 29) e Nota Fiscal/Conta de Fornecimento de Gás (Código 28) - (Empresas não obrigadas ao Convênio ICMS 115/03)"""
    _inherit = "l10n.br.sped.mixin"
    cod_mod = fields.Char(
        "COD_MOD",
        help="""Código   do   modelo   do   documento  fiscal,conforme a Tabela 4.1.1
Ver pagina 89""",
    )
    cod_mun = fields.Integer(
        "Código do município dos pontos de consumo,conforme a tabela IBGE"
    )
    ser = fields.Char(
        "Série do documento fiscal",
        help="""Série do documento fiscal
Ver pagina 89""",
    )
    sub = fields.Integer("Subsérie do documento fiscal")
    cod_cons = fields.Char(
        "- Código de classe de consumo de energia elétrica ou gás",
        help="""- Código de classe de consumo de energia elétrica ou gás:01 - Comercial02 - Consumo Próprio03 - Iluminação Pública04 - Industrial05 - Poder Público06 - Residencial07 - Rural08 -Serviço Público.- Código de classe de consumo de FornecimentoD´água – Tabela 4.4.2.
Ver pagina 89""",
    )
    qtd_cons = fields.Integer(
        "Quantidade   de   documentos   consolidados   nesteregistro"
    )
    qtd_canc = fields.Integer("Quantidade de documentos cancelados")
    dt_doc = fields.Integer("Data dos documentos consolidados")
    vl_doc = fields.Integer("Valor total dos documentos")
    vl_desc = fields.Integer("Valor acumulado dos descontos")
    cons = fields.Integer("Consumo total acumulado, em kWh (Código 06)")
    vl_forn = fields.Integer("Valor acumulado do fornecimento")
    vl_serv_nt = fields.Integer(
        "Valor   acumulado   dos   serviços   não-tributadospelo ICMS"
    )
    vl_terc = fields.Integer("Valores cobrados em nome de terceiros")
    vl_da = fields.Integer("Valor acumulado das despesas acessórias")
    vl_bc_icms = fields.Integer("Valor acumulado da base de cálculo do ICMS")
    vl_icms = fields.Integer("Valor acumulado do ICMS")
    reg_c601_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.c601",
        "parent_c600_id",
        string="Documentos cancelados - Consolidação diária de notas fiscais/conta de energia elétrica (Código 06), nota fiscal/conta de fornecimento de água (código 29) e nota fiscal/conta de fornecimento de gás (código 28)",
        help="Bloco C",
    )
    reg_c610_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.c610",
        "parent_c600_id",
        string="Itens do Documento Consolidado - Notas Fiscais/Contas de Energia Elétrica (Código 06), Nota Fiscal/Conta de Fornecimento d´água (código 29) e Nota Fiscal/Conta de Fornecimento de Gás (Código 28) - (Empresas não obrigadas ao Convênio ICMS 115/03)",
        help="Bloco C",
    )
    reg_c690_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.c690",
        "parent_c600_id",
        string="Registro Analítico dos Documentos - Notas Fiscais/Contas de Energia Elétrica (Código 06), Nota Fiscal/Conta de Fornecimento d´água (código 29) e Nota Fiscal/Conta de Fornecimento de Gás (Código 28)",
        help="Bloco C",
    )


class RegistroC601(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c601"
    _description = u"""Documentos cancelados - Consolidação diária de notas fiscais/conta de energia elétrica (Código 06), nota fiscal/conta de fornecimento de água (código 29) e nota fiscal/conta de fornecimento de gás (código 28)"""
    _inherit = "l10n.br.sped.mixin"
    parent_c600_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c600",
        string="Consolidação Diária de Notas Fiscais/Contas de Energia Elétrica (Código 06), Nota Fiscal/Conta de Fornecimento d´água (código 29) e Nota Fiscal/Conta de Fornecimento de Gás (Código 28) - (Empresas não obrigadas ao Convênio ICMS 115/03)",
    )


class RegistroC610(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c610"
    _description = u"""Itens do Documento Consolidado - Notas Fiscais/Contas de Energia Elétrica (Código 06), Nota Fiscal/Conta de Fornecimento d´água (código 29) e Nota Fiscal/Conta de Fornecimento de Gás (Código 28) - (Empresas não obrigadas ao Convênio ICMS 115/03)"""
    _inherit = "l10n.br.sped.mixin"
    cod_class = fields.Integer("COD_CLASS")
    cod_item = fields.Char(
        "Código do item (campo 02 do Registro 0200)",
        help="""Código do item (campo 02 do Registro 0200)
Ver pagina 91""",
    )
    qtd = fields.Integer("Quantidade acumulada do item")
    unid = fields.Char(
        "Unidade do item  (Campo 02 do registro 0190)",
        help="""Unidade do item  (Campo 02 do registro 0190)
Ver pagina 91""",
    )
    vl_item = fields.Integer("Valor acumulado do item")
    vl_desc = fields.Integer("Valor acumulado dos descontos")
    cst_icms = fields.Integer("CST_ICMS")
    cfop = fields.Integer("CFOP")
    aliq_icms = fields.Monetary("Alíquota do ICMS", digits=2)
    vl_bc_icms = fields.Integer("Valor acumulado da base de cálculo do ICMS")
    vl_icms = fields.Integer("Valor acumulado do ICMS debitado")
    parent_c600_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c600",
        string="Consolidação Diária de Notas Fiscais/Contas de Energia Elétrica (Código 06), Nota Fiscal/Conta de Fornecimento d´água (código 29) e Nota Fiscal/Conta de Fornecimento de Gás (Código 28) - (Empresas não obrigadas ao Convênio ICMS 115/03)",
    )


class RegistroC690(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c690"
    _description = u"""Registro Analítico dos Documentos - Notas Fiscais/Contas de Energia Elétrica (Código 06), Nota Fiscal/Conta de Fornecimento d´água (código 29) e Nota Fiscal/Conta de Fornecimento de Gás (Código 28)"""
    _inherit = "l10n.br.sped.mixin"
    cst_icms = fields.Integer("CST_ICMS")
    cfop = fields.Integer("CFOP")
    aliq_icms = fields.Monetary("Alíquota do ICMS", digits=2)
    vl_opr = fields.Integer("VL_OPR")
    vl_bc_icms = fields.Integer("VL_BC_ICMS")
    vl_icms = fields.Integer("VL_ICMS")
    vl_red_bc = fields.Integer("VL_RED_BC")
    parent_c600_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c600",
        string="Consolidação Diária de Notas Fiscais/Contas de Energia Elétrica (Código 06), Nota Fiscal/Conta de Fornecimento d´água (código 29) e Nota Fiscal/Conta de Fornecimento de Gás (Código 28) - (Empresas não obrigadas ao Convênio ICMS 115/03)",
    )


class RegistroC700(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c700"
    _description = u"""Consolidação dos Documentos Nota Fiscal/Conta Energia Elétrica (código 06) emitidasem via única - (Empresas obrigadas à entrega do arquivo previsto no Convênio ICMS 115/03) e Nota Fiscal/Conta de Fornecimento de Gás Canalizado (Código 28)"""
    _inherit = "l10n.br.sped.mixin"
    cod_mod = fields.Char(
        "Código do modelo do documento fiscal, conforme a Tabela 4",
        help="""Código do modelo do documento fiscal, conforme a Tabela 4.1.1
Ver pagina 93""",
    )
    ser = fields.Char(
        "Série do documento fiscal",
        help="""Série do documento fiscal
Ver pagina 93""",
    )
    nro_ord_ini = fields.Integer("Número de ordem inicial")
    nro_ord_fin = fields.Integer("Número de ordem final")
    dt_doc_ini = fields.Integer("DT_DOC_INI")
    dt_doc_fin = fields.Integer("DT_DOC_FIN")
    nom_mest = fields.Char(
        "Nome do arquivo Mestre de Documento Fiscal",
        help="""Nome do arquivo Mestre de Documento Fiscal
Ver pagina 93""",
    )
    chv_cod_dig = fields.Char(
        "CHV_COD_DIG",
        help="""Chave de codificação digital do arquivo Mestrede Documento Fiscal
Ver pagina 93""",
    )
    reg_c790_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.c790",
        "parent_c700_id",
        string="Registro Analítico dos Documentos - Nota Fiscal/Conta Energia Elétrica (código 06) emitidas em via única",
        help="Bloco C",
    )


class RegistroC790(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c790"
    _description = u"""Registro Analítico dos Documentos - Nota Fiscal/Conta Energia Elétrica (código 06) emitidas em via única"""
    _inherit = "l10n.br.sped.mixin"
    cst_icms = fields.Integer("CST_ICMS")
    cfop = fields.Integer("CFOP")
    aliq_icms = fields.Monetary("Alíquota do ICMS", digits=2)
    vl_opr = fields.Integer("VL_OPR")
    vl_bc_icms = fields.Integer("VL_BC_ICMS")
    vl_icms = fields.Integer("VL_ICMS")
    parent_c700_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c700",
        string="Consolidação dos Documentos Nota Fiscal/Conta Energia Elétrica (código 06) emitidasem via única - (Empresas obrigadas à entrega do arquivo previsto no Convênio ICMS 115/03) e Nota Fiscal/Conta de Fornecimento de Gás Canalizado (Código 28)",
    )
    reg_c791_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.c791",
        "parent_c790_id",
        string="Registro de Informações de ICMS ST por UF",
        help="Bloco C",
    )


class RegistroC791(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c791"
    _description = u"""Registro de Informações de ICMS ST por UF"""
    _inherit = "l10n.br.sped.mixin"
    parent_c790_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c790",
        string="Registro Analítico dos Documentos - Nota Fiscal/Conta Energia Elétrica (código 06) emitidas em via única",
    )


class RegistroC800(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c800"
    _description = u"""Registro Cupom Fiscal Eletrônico - CF-e (Código 59)"""
    _inherit = "l10n.br.sped.mixin"
    cod_mod = fields.Char(
        "Código do modelo do documento fiscal, conforme aTabela 4",
        help="""Código do modelo do documento fiscal, conforme aTabela 4.1.1
Ver pagina 95""",
    )
    cod_sit = fields.Integer(
        "Código da situação do documento fiscal, conforme aTabela 4"
    )
    num_cfe = fields.Integer("Número do Cupom Fiscal Eletrônico")
    dt_doc = fields.Integer("Data da emissão do Cupom Fiscal Eletrônico")
    vl_cfe = fields.Integer("Valor total do Cupom Fiscal Eletrônico")
    vl_pis = fields.Integer("Valor total do PIS")
    vl_cofins = fields.Integer("Valor total da COFINS")
    cnpj_cpf = fields.Integer("CNPJ ou CPF do destinatário")
    nr_sat = fields.Integer("Número de Série do equipamento SAT")
    chv_cfe = fields.Integer("Chave do Cupom Fiscal Eletrônico")
    vl_desc = fields.Integer("Valor total de descontos")
    vl_merc = fields.Integer("Valor total das mercadorias e serviços")
    vl_out_da = fields.Integer(
        "Valor total de  outras despesas acessórias e acréscimos"
    )
    vl_icms = fields.Integer("Valor do ICMS")
    vl_pis_st = fields.Integer("Valor total do PIS retido por subst")
    vl_cofins_st = fields.Integer("Valor total da COFINS retido por subst")
    reg_c850_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.c850",
        "parent_c800_id",
        string="Registro Analítico do CF-e (Código 59)",
        help="Bloco C",
    )


class RegistroC850(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c850"
    _description = u"""Registro Analítico do CF-e (Código 59)"""
    _inherit = "l10n.br.sped.mixin"
    cst_icms = fields.Integer("CST_ICMS")
    cfop = fields.Integer(
        "Código Fiscal de Operação e Prestação do agrupamento deitens"
    )
    aliq_icms = fields.Monetary("Alíquota do ICMS", digits=2)
    vl_opr = fields.Integer("VL_OPR")
    vl_bc_icms = fields.Integer("VL_BC_ICMS")
    vl_icms = fields.Integer("VL_ICMS")
    cod_obs = fields.Char(
        "COD_OBS",
        help="""Código da observação do lançamento fiscal  (campo 02 doregistro 0460)
Ver pagina 97""",
    )
    parent_c800_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c800",
        string="Registro Cupom Fiscal Eletrônico - CF-e (Código 59)",
    )


class RegistroC860(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c860"
    _description = u"""Identificação do equipamento SAT-CF-e (Código 59)"""
    _inherit = "l10n.br.sped.mixin"
    cod_mod = fields.Char(
        "Código  do modelo do documento fiscal, conforme  a Tabela4",
        required=True,
        help="""Código  do modelo do documento fiscal, conforme  a Tabela4.1.1
Ver pagina 98""",
    )
    nr_sat = fields.Integer("Número de Série do equipamento SAT", required=True)
    dt_doc = fields.Integer("Data de emissão dos documentos fiscais", required=True)
    doc_ini = fields.Integer("Número do documento inicial", required=True)
    doc_fim = fields.Integer("Número do documento final", required=True)
    reg_c890_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.c890",
        "parent_c860_id",
        string="Resumo diário de CF-e (Código 59) por equipamento SAT-CF-e",
        help="Bloco C",
    )


class RegistroC890(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.c890"
    _description = u"""Resumo diário de CF-e (Código 59) por equipamento SAT-CF-e"""
    _inherit = "l10n.br.sped.mixin"
    cst_icms = fields.Integer("CST_ICMS")
    cfop = fields.Integer(
        "Código Fiscal de Operação e Prestação do agrupamento de itens"
    )
    aliq_icms = fields.Monetary("Alíquota do ICMS", digits=2)
    vl_opr = fields.Integer("VL_OPR")
    vl_bc_icms = fields.Integer("VL_BC_ICMS")
    vl_icms = fields.Integer("VL_ICMS")
    cod_obs = fields.Char(
        "COD_OBS",
        help="""Código   da   observação   do   lançamento   fiscal   (campo   02   doregistro 0460)
Ver pagina 99""",
    )
    parent_c860_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.c860",
        string="Identificação do equipamento SAT-CF-e (Código 59)",
    )


class RegistroD100(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.d100"
    _description = u"""Nota Fiscal de Serviço de Transporte (código 07), Conhecimentos de Transporte Rodoviário De Cargas (código 08), Conhecimentos de Transporte de Cargas Avulso (código 8b), Aquaviário de Cargas (código 09), Aéreo (código 10), Ferroviário de Cargas (código 11), Multimodal de Cargas (código 26), Nota Fiscal de Transporte Ferroviário de Carga (código 27), Conhecimento de Transporte Eletrônico – CT-e (código 57), Conhecimento de Transporte Eletrônico para Outros Serviços - CT-e OS (código 67) e Bilhete de Passagem Eletrônico (código 63)"""
    _inherit = "l10n.br.sped.mixin"
    ind_oper = fields.Char(
        "Indicador do tipo de operação",
        required=True,
        help="""Indicador do tipo de operação:0- Aquisição;1- Prestação
Ver pagina 101""",
    )
    ind_emit = fields.Char(
        "Indicador do emitente do documento fiscal",
        required=True,
        help="""Indicador do emitente do documento fiscal:0- Emissão própria;1- Terceiros
Ver pagina 101""",
    )
    cod_part = fields.Char(
        "Código do participante (campo 02 do Registro 0150)",
        required=True,
        help="""Código do participante (campo 02 do Registro 0150):- do prestador de serviço, no caso de aquisição de serviço;- do tomador do serviço, no caso de prestação de serviços.
Ver pagina 102""",
    )
    cod_mod = fields.Char(
        "Código do modelo do documento fiscal, conforme a Tabela 4",
        required=True,
        help="""Código do modelo do documento fiscal, conforme a Tabela 4.1.1
Ver pagina 102""",
    )
    cod_sit = fields.Integer(
        "Código da situação do documento fiscal, conforme a Tabela 4", required=True
    )
    ser = fields.Char(
        "Série do documento fiscal",
        help="""Série do documento fiscal
Ver pagina 102""",
    )
    sub = fields.Char(
        "Subsérie do documento fiscal",
        help="""Subsérie do documento fiscal
Ver pagina 102""",
    )
    num_doc = fields.Integer("Número do documento fiscal", required=True)
    chv_cte = fields.Integer("CHV_CTE")
    dt_doc = fields.Integer("Data da emissão do documento fiscal", required=True)
    dt_a_p = fields.Integer("Data da aquisição ou da prestação do serviço")
    reg_d101_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.d101",
        string="Informação complementar dos documentos fiscais quando das prestações interestaduaisdestinadas a consumidor final não contribuinte EC 87/15 (código 57 e 67)",
        help="Bloco D",
    )  # m2o
    reg_d140_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.d140",
        string="Complemento do Conhecimento Aquaviário de Cargas (código 09)",
        help="Bloco D",
    )  # m2o
    reg_d150_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.d150",
        string="Complemento do Conhecimento Aéreo de Cargas (código 10)",
        help="Bloco D",
    )  # m2o
    reg_d170_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.d170",
        string="Complemento do Conhecimento Multimodal de Cargas (código 26)",
        help="Bloco D",
    )  # m2o
    reg_d110_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.d110",
        "parent_d100_id",
        string="Itens do documento - Nota Fiscal de Serviços de Transporte (código 07)",
        help="Bloco D",
    )
    reg_d130_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.d130",
        "parent_d100_id",
        string="Complemento do Conhecimento Rodoviário de Cargas (código 08) e Conhecimento de Transporte de Cargas Avulso (Código 8B)",
        help="Bloco D",
    )
    reg_d160_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.d160",
        "parent_d100_id",
        string="Carga Transportada  (CÓDIGO 08, 8B, 09, 10, 11, 26 E 27)",
        help="Bloco D",
    )
    reg_d180_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.d180",
        "parent_d100_id",
        string="Modais (código 26)",
        help="Bloco D",
    )
    reg_d190_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.d190",
        "parent_d100_id",
        string="Registro Analítico dos Documentos (CÓDIGO 07, 08, 8B, 09, 10, 11, 26, 27, 57 e 67)",
        help="Bloco D",
    )
    reg_d195_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.d195",
        "parent_d100_id",
        string="Observações do lançamento (CÓDIGO 07, 08, 8B, 09, 10, 11, 26, 27, 57 e 67)",
        help="Bloco D",
    )


class RegistroD101(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.d101"
    _description = u"""Informação complementar dos documentos fiscais quando das prestações interestaduaisdestinadas a consumidor final não contribuinte EC 87/15 (código 57 e 67)"""
    _inherit = "l10n.br.sped.mixin"
    vl_fcp_uf_dest = fields.Integer("VL_FCP_UF_DEST", required=True)
    vl_icms_uf_dest = fields.Integer(
        "Valor total do ICMS Interestadual para a UF de destino", required=True
    )
    vl_icms_uf_rem = fields.Integer(
        "Valor total do ICMS Interestadual para a UF do remetente", required=True
    )


class RegistroD110(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.d110"
    _description = (
        u"""Itens do documento - Nota Fiscal de Serviços de Transporte (código 07)"""
    )
    _inherit = "l10n.br.sped.mixin"
    num_item = fields.Integer("Número sequencial do item no documento fiscal")
    cod_item = fields.Char(
        "Código do item (campo 02 do Registro 0200)",
        help="""Código do item (campo 02 do Registro 0200)
Ver pagina 105""",
    )
    vl_serv = fields.Integer("Valor do serviço")
    vl_out = fields.Integer("Outros valores")
    parent_d100_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.d100",
        string="Nota Fiscal de Serviço de Transporte (código 07), Conhecimentos de Transporte Rodoviário De Cargas (código 08), Conhecimentos de Transporte de Cargas Avulso (código 8b), Aquaviário de Cargas (código 09), Aéreo (código 10), Ferroviário de Cargas (código 11), Multimodal de Cargas (código 26), Nota Fiscal de Transporte Ferroviário de Carga (código 27), Conhecimento de Transporte Eletrônico – CT-e (código 57), Conhecimento de Transporte Eletrônico para Outros Serviços - CT-e OS (código 67) e Bilhete de Passagem Eletrônico (código 63)",
    )
    reg_d120_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.d120",
        "parent_d110_id",
        string="Complemento da Nota Fiscal de Serviços de Transporte (código 07)",
        help="Bloco D",
    )


class RegistroD120(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.d120"
    _description = (
        u"""Complemento da Nota Fiscal de Serviços de Transporte (código 07)"""
    )
    _inherit = "l10n.br.sped.mixin"
    cod_mun_orig = fields.Integer("COD_MUN_ORIG")
    cod_mun_dest = fields.Integer("COD_MUN_DEST")
    veic_id = fields.Char(
        "Placa de identificação do veículo",
        help="""Placa de identificação do veículo
Ver pagina 105""",
    )
    uf_id = fields.Char(
        "Sigla da UF da placa do veículo",
        help="""Sigla da UF da placa do veículo
Ver pagina 105""",
    )
    parent_d110_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.d110",
        string="Itens do documento - Nota Fiscal de Serviços de Transporte (código 07)",
    )


class RegistroD130(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.d130"
    _description = u"""Complemento do Conhecimento Rodoviário de Cargas (código 08) e Conhecimento de Transporte de Cargas Avulso (Código 8B)"""
    _inherit = "l10n.br.sped.mixin"
    parent_d100_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.d100",
        string="Nota Fiscal de Serviço de Transporte (código 07), Conhecimentos de Transporte Rodoviário De Cargas (código 08), Conhecimentos de Transporte de Cargas Avulso (código 8b), Aquaviário de Cargas (código 09), Aéreo (código 10), Ferroviário de Cargas (código 11), Multimodal de Cargas (código 26), Nota Fiscal de Transporte Ferroviário de Carga (código 27), Conhecimento de Transporte Eletrônico – CT-e (código 57), Conhecimento de Transporte Eletrônico para Outros Serviços - CT-e OS (código 67) e Bilhete de Passagem Eletrônico (código 63)",
    )


class RegistroD140(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.d140"
    _description = u"""Complemento do Conhecimento Aquaviário de Cargas (código 09)"""
    _inherit = "l10n.br.sped.mixin"
    cod_part_consg = fields.Char(
        "Código do participante (campo 02 do Registro 0150)",
        help="""Código do participante (campo 02 do Registro 0150):- consignatário, se houver
Ver pagina 107""",
    )
    cod_mun_orig = fields.Integer("COD_MUN_ORIG")
    cod_mun_dest = fields.Integer("COD_MUN_DEST")
    ind_veic = fields.Char(
        "Indicador do tipo do veículo transportador",
        help="""Indicador do tipo do veículo transportador:0- Embarcação;1- Empurrador/rebocador
Ver pagina 107""",
    )
    veic_id = fields.Char(
        "Identificação da embarcação (IRIM ou Registro CPP)",
        help="""Identificação da embarcação (IRIM ou Registro CPP)
Ver pagina 107""",
    )
    ind_nav = fields.Char(
        "Indicador do tipo da navegação",
        help="""Indicador do tipo da navegação:0- Interior;1- Cabotagem
Ver pagina 107""",
    )
    viagem = fields.Integer("Número da viagem")
    vl_frt_liq = fields.Integer("Valor líquido do frete")
    vl_desp_port = fields.Integer("Valor das despesas portuárias")


class RegistroD150(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.d150"
    _description = u"""Complemento do Conhecimento Aéreo de Cargas (código 10)"""
    _inherit = "l10n.br.sped.mixin"
    cod_mun_orig = fields.Integer("COD_MUN_ORIG")
    cod_mun_dest = fields.Integer("COD_MUN_DEST")
    veic_id = fields.Char(
        "Identificação da aeronave (DAC)",
        help="""Identificação da aeronave (DAC)
Ver pagina 108""",
    )
    viagem = fields.Integer("Número do vôo.")
    ind_tfa = fields.Char(
        "Indicador do tipo de tarifa aplicada",
        help="""Indicador do tipo de tarifa aplicada:0- Exp.;1- Enc.;2- C.I.;9- Outra
Ver pagina 108""",
    )
    vl_peso_tx = fields.Integer("Peso taxado")
    vl_tx_terr = fields.Integer("Valor da taxa terrestre")
    vl_tx_red = fields.Integer("Valor da taxa de redespacho")
    vl_out = fields.Integer("Outros valores")
    vl_tx_adv = fields.Integer("Valor da taxa 'ad valorem'")


class RegistroD160(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.d160"
    _description = u"""Carga Transportada  (CÓDIGO 08, 8B, 09, 10, 11, 26 E 27)"""
    _inherit = "l10n.br.sped.mixin"
    despacho = fields.Char(
        "Identificação do número do despacho",
        help="""Identificação do número do despacho
Ver pagina 108""",
    )
    cnpj_cpf_rem = fields.Integer("CNPJ_CPF_REM")
    ie_rem = fields.Char(
        "IE_REM",
        help="""Inscrição Estadual do remetente das mercadorias que constam na nota fiscal.
Ver pagina 108""",
    )
    cod_mun_ori = fields.Integer("COD_MUN_ORI")
    cnpj_cpf_dest = fields.Integer("CNPJ_CPF_DEST")
    ie_dest = fields.Char(
        "IE_DEST",
        help="""Inscrição Estadual do destinatáriodas mercadorias que constam na nota fiscal.
Ver pagina 109""",
    )
    cod_mun_dest = fields.Integer("COD_MUN_DEST")
    parent_d100_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.d100",
        string="Nota Fiscal de Serviço de Transporte (código 07), Conhecimentos de Transporte Rodoviário De Cargas (código 08), Conhecimentos de Transporte de Cargas Avulso (código 8b), Aquaviário de Cargas (código 09), Aéreo (código 10), Ferroviário de Cargas (código 11), Multimodal de Cargas (código 26), Nota Fiscal de Transporte Ferroviário de Carga (código 27), Conhecimento de Transporte Eletrônico – CT-e (código 57), Conhecimento de Transporte Eletrônico para Outros Serviços - CT-e OS (código 67) e Bilhete de Passagem Eletrônico (código 63)",
    )
    reg_d161_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.d161",
        string="Local de Coleta e Entrega (códigos 08, 8B, 09, 10, 11 e 26)",
        help="Bloco D",
    )  # m2o
    reg_d162_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.d162",
        "parent_d160_id",
        string="Identificação dos documentos fiscais (código 08,8B, 09,10,11,26 e 27)",
        help="Bloco D",
    )


class RegistroD161(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.d161"
    _description = u"""Local de Coleta e Entrega (códigos 08, 8B, 09, 10, 11 e 26)"""
    _inherit = "l10n.br.sped.mixin"
    ind_carga = fields.Integer("Indicador do tipo de transporte da carga coletada")
    cnpj_cpf_col = fields.Char(
        "Número do CNPJ ou CPF do local da coleta",
        help="""Número do CNPJ ou CPF do local da coleta
Ver pagina 109""",
    )
    ie_col = fields.Char(
        "Inscrição Estadual do contribuinte do local decoleta",
        help="""Inscrição Estadual do contribuinte do local decoleta
Ver pagina 109""",
    )
    cod_mun_col = fields.Integer("COD_MUN_COL")
    cnpj_cpf_entg = fields.Char(
        "Número do CNPJ ou CPF do local da entrega",
        help="""Número do CNPJ ou CPF do local da entrega
Ver pagina 109""",
    )
    ie_entg = fields.Char(
        "Inscrição Estadual do contribuinte do local deentrega",
        help="""Inscrição Estadual do contribuinte do local deentrega
Ver pagina 109""",
    )
    cod_mun_entg = fields.Integer("COD_MUN_ENTG")


class RegistroD162(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.d162"
    _description = (
        u"""Identificação dos documentos fiscais (código 08,8B, 09,10,11,26 e 27)"""
    )
    _inherit = "l10n.br.sped.mixin"
    cod_mod = fields.Char(
        "Código do modelo do documento fiscal, conforme a Tabela 4",
        help="""Código do modelo do documento fiscal, conforme a Tabela 4.1.1
Ver pagina 110""",
    )
    ser = fields.Char(
        "Série do documento fiscal",
        help="""Série do documento fiscal
Ver pagina 110""",
    )
    num_doc = fields.Integer("Número do documento fiscal")
    dt_doc = fields.Integer("Data da emissão do documento fiscal")
    vl_doc = fields.Integer("Valor total do documento fiscal")
    vl_merc = fields.Integer("Valor das mercadorias constantes no documento fiscal")
    qtd_vol = fields.Integer("Quantidade de volumes transportados")
    peso_brt = fields.Integer("Peso bruto dos volumes transportados (em Kg)")
    peso_liq = fields.Integer("Peso líquido dos volumes transportados (em Kg)")
    parent_d160_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.d160",
        string="Carga Transportada  (CÓDIGO 08, 8B, 09, 10, 11, 26 E 27)",
    )


class RegistroD170(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.d170"
    _description = u"""Complemento do Conhecimento Multimodal de Cargas (código 26)"""
    _inherit = "l10n.br.sped.mixin"


class RegistroD180(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.d180"
    _description = u"""Modais (código 26)"""
    _inherit = "l10n.br.sped.mixin"
    num_seq = fields.Integer("Número de ordem sequencial do modal")
    ind_emit = fields.Char(
        "Indicador do emitente do documento fiscal",
        help="""Indicador do emitente do documento fiscal:0- Emissão própria;1- Terceiros
Ver pagina 112""",
    )
    cnpj_cpf_emit = fields.Integer("CNPJ ou CPF do participante emitente do modal")
    uf_emit = fields.Char(
        "Sigla da unidade da federação do participante emitente do modal",
        help="""Sigla da unidade da federação do participante emitente do modal
Ver pagina 112""",
    )
    ie_emit = fields.Char(
        "Inscrição Estadual do participante emitente do modal",
        help="""Inscrição Estadual do participante emitente do modal
Ver pagina 112""",
    )
    cod_mun_orig = fields.Integer("COD_MUN_ORIG")
    cnpj_cpf_tom = fields.Integer("CNPJ/CPF do participante tomador do serviço")
    uf_tom = fields.Char(
        "Sigla da unidade da federação do participante tomador do serviço",
        help="""Sigla da unidade da federação do participante tomador do serviço
Ver pagina 112""",
    )
    ie_tom = fields.Char(
        "Inscrição Estadual do participante tomador do serviço",
        help="""Inscrição Estadual do participante tomador do serviço
Ver pagina 112""",
    )
    cod_mun_dest = fields.Integer("COD_MUN_DEST")
    cod_mod = fields.Char(
        "Código do modelo do documento fiscal, conformea Tabela 4",
        help="""Código do modelo do documento fiscal, conformea Tabela 4.1.1
Ver pagina 112""",
    )
    ser = fields.Char(
        "Série do documento fiscal",
        help="""Série do documento fiscal
Ver pagina 112""",
    )
    sub = fields.Integer("Subsérie do documento fiscal")
    num_doc = fields.Integer("Número do documento fiscal")
    dt_doc = fields.Integer("Data da emissão do documento fiscal")
    vl_doc = fields.Integer("Valor total do documento fiscal")
    parent_d100_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.d100",
        string="Nota Fiscal de Serviço de Transporte (código 07), Conhecimentos de Transporte Rodoviário De Cargas (código 08), Conhecimentos de Transporte de Cargas Avulso (código 8b), Aquaviário de Cargas (código 09), Aéreo (código 10), Ferroviário de Cargas (código 11), Multimodal de Cargas (código 26), Nota Fiscal de Transporte Ferroviário de Carga (código 27), Conhecimento de Transporte Eletrônico – CT-e (código 57), Conhecimento de Transporte Eletrônico para Outros Serviços - CT-e OS (código 67) e Bilhete de Passagem Eletrônico (código 63)",
    )


class RegistroD190(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.d190"
    _description = u"""Registro Analítico dos Documentos (CÓDIGO 07, 08, 8B, 09, 10, 11, 26, 27, 57 e 67)"""
    _inherit = "l10n.br.sped.mixin"
    cst_icms = fields.Integer("CST_ICMS", required=True)
    cfop = fields.Integer("CFOP", required=True)
    aliq_icms = fields.Monetary("Alíquota do ICMS", digits=2)
    vl_opr = fields.Integer("VL_OPR", required=True)
    vl_bc_icms = fields.Integer("VL_BC_ICMS", required=True)
    vl_icms = fields.Integer("VL_ICMS", required=True)
    vl_red_bc = fields.Integer("VL_RED_BC", required=True)
    cod_obs = fields.Char(
        "COD_OBS",
        help="""Código da observação do lançamento fiscal (campo 02 do Registro 0460)
Ver pagina 113""",
    )
    parent_d100_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.d100",
        string="Nota Fiscal de Serviço de Transporte (código 07), Conhecimentos de Transporte Rodoviário De Cargas (código 08), Conhecimentos de Transporte de Cargas Avulso (código 8b), Aquaviário de Cargas (código 09), Aéreo (código 10), Ferroviário de Cargas (código 11), Multimodal de Cargas (código 26), Nota Fiscal de Transporte Ferroviário de Carga (código 27), Conhecimento de Transporte Eletrônico – CT-e (código 57), Conhecimento de Transporte Eletrônico para Outros Serviços - CT-e OS (código 67) e Bilhete de Passagem Eletrônico (código 63)",
    )


class RegistroD195(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.d195"
    _description = u"""Observações do lançamento (CÓDIGO 07, 08, 8B, 09, 10, 11, 26, 27, 57 e 67)"""
    _inherit = "l10n.br.sped.mixin"
    cod_obs = fields.Char(
        "COD_OBS",
        required=True,
        help="""Código da observação do lançamento fiscal (campo 02 do Registro 0460)
Ver pagina 114""",
    )
    txt_compl = fields.Char(
        "Descrição complementar do código de observação",
        help="""Descrição complementar do código de observação.
Ver pagina 114""",
    )
    parent_d100_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.d100",
        string="Nota Fiscal de Serviço de Transporte (código 07), Conhecimentos de Transporte Rodoviário De Cargas (código 08), Conhecimentos de Transporte de Cargas Avulso (código 8b), Aquaviário de Cargas (código 09), Aéreo (código 10), Ferroviário de Cargas (código 11), Multimodal de Cargas (código 26), Nota Fiscal de Transporte Ferroviário de Carga (código 27), Conhecimento de Transporte Eletrônico – CT-e (código 57), Conhecimento de Transporte Eletrônico para Outros Serviços - CT-e OS (código 67) e Bilhete de Passagem Eletrônico (código 63)",
    )
    reg_d197_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.d197",
        "parent_d195_id",
        string="Outras obrigações tributárias, ajustes e informações de valores provenientes do documento fiscal.",
        help="Bloco D",
    )


class RegistroD197(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.d197"
    _description = u"""Outras obrigações tributárias, ajustes e informações de valores provenientes do documento fiscal."""
    _inherit = "l10n.br.sped.mixin"
    cod_aj = fields.Char(
        "COD_AJ",
        required=True,
        help="""Código do ajustes/benefício/incentivo, conforme tabelaindicada no item 5.3.
Ver pagina 115""",
    )
    descr_compl_aj = fields.Char(
        "Descrição complementar do ajuste do documento fiscal",
        help="""Descrição complementar do ajuste do documento fiscal
Ver pagina 115""",
    )
    cod_item = fields.Char(
        "Código do item (campo 02 do Registro 0200)",
        help="""Código do item (campo 02 do Registro 0200)
Ver pagina 115""",
    )
    vl_bc_icms = fields.Integer("Base de cálculo do ICMS ou do ICMS ST")
    aliq_icms = fields.Monetary("Alíquota do ICMS", digits=2)
    vl_icms = fields.Integer("Valor do ICMS ou do ICMS ST")
    vl_outros = fields.Integer("Outros valores")
    parent_d195_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.d195",
        string="Observações do lançamento (CÓDIGO 07, 08, 8B, 09, 10, 11, 26, 27, 57 e 67)",
    )


class RegistroD300(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.d300"
    _description = u"""Registro Analítico dos bilhetes consolidados de Passagem Rodoviário (código 13), de Passagem Aquaviário (código 14), de Passagem e Nota de Bagagem (código 15) e de Passagem Ferroviário (código 16)"""
    _inherit = "l10n.br.sped.mixin"
    cod_mod = fields.Char(
        "Código do modelo do documento fiscal, conforme a Tabela 4",
        help="""Código do modelo do documento fiscal, conforme a Tabela 4.1.1
Ver pagina 116""",
    )
    ser = fields.Char(
        "Série do documento fiscal",
        help="""Série do documento fiscal
Ver pagina 116""",
    )
    sub = fields.Integer("Subsérie do documento fiscal")
    num_doc_ini = fields.Integer("NUM_DOC_INI")
    num_doc_fin = fields.Integer("NUM_DOC_FIN")
    cst_icms = fields.Integer("CST_ICMS")
    cfop = fields.Integer("CFOP")
    aliq_icms = fields.Monetary("Alíquota do ICMS", digits=2)
    dt_doc = fields.Integer("Data da emissão dos documentos fiscais")
    vl_opr = fields.Integer("VL_OPR")
    vl_desc = fields.Integer("Valor total dos descontos")
    vl_serv = fields.Integer("Valor total da prestação de serviço")
    vl_seg = fields.Integer("Valor de seguro")
    vl_out_desp = fields.Integer("Valor de outras despesas")
    vl_bc_icms = fields.Integer("Valor total da base de cálculo do ICMS")
    vl_icms = fields.Integer("Valor total do ICMS")
    vl_red_bc = fields.Integer("VL_RED_BC")
    cod_obs = fields.Char(
        "COD_OBS",
        help="""Código da observação do lançamento fiscal (campo 02 do Registro 0460)
Ver pagina 116""",
    )
    cod_cta = fields.Char(
        "Código da conta analítica contábil debitada/creditada",
        help="""Código da conta analítica contábil debitada/creditada
Ver pagina 116""",
    )
    reg_d301_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.d301",
        "parent_d300_id",
        string="Documentos cancelados dos Bilhetes de Passagem Rodoviário (código 13), de Passagem Aquaviário (código 14), de Passagem e Nota de Bagagem (código 15) e de Passagem Ferroviário (código 16)",
        help="Bloco D",
    )
    reg_d310_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.d310",
        "parent_d300_id",
        string="Complemento dos Bilhetes (código 13, código 14, código 15 e código 16)",
        help="Bloco D",
    )


class RegistroD301(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.d301"
    _description = u"""Documentos cancelados dos Bilhetes de Passagem Rodoviário (código 13), de Passagem Aquaviário (código 14), de Passagem e Nota de Bagagem (código 15) e de Passagem Ferroviário (código 16)"""
    _inherit = "l10n.br.sped.mixin"
    parent_d300_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.d300",
        string="Registro Analítico dos bilhetes consolidados de Passagem Rodoviário (código 13), de Passagem Aquaviário (código 14), de Passagem e Nota de Bagagem (código 15) e de Passagem Ferroviário (código 16)",
    )


class RegistroD310(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.d310"
    _description = (
        u"""Complemento dos Bilhetes (código 13, código 14, código 15 e código 16)"""
    )
    _inherit = "l10n.br.sped.mixin"
    parent_d300_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.d300",
        string="Registro Analítico dos bilhetes consolidados de Passagem Rodoviário (código 13), de Passagem Aquaviário (código 14), de Passagem e Nota de Bagagem (código 15) e de Passagem Ferroviário (código 16)",
    )


class RegistroD350(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.d350"
    _description = u"""Equipamento ECF (Códigos 2E, 13, 14, 15 e 16)"""
    _inherit = "l10n.br.sped.mixin"
    cod_mod = fields.Char(
        "Código do modelo do documento fiscal, conformea Tabela 4",
        help="""Código do modelo do documento fiscal, conformea Tabela 4.1.1
Ver pagina 118""",
    )
    ecf_mod = fields.Char(
        "Modelo do equipamento",
        help="""Modelo do equipamento
Ver pagina 118""",
    )
    ecf_fab = fields.Char(
        "Número de série de fabricação do ECF",
        help="""Número de série de fabricação do ECF
Ver pagina 118""",
    )
    ecf_cx = fields.Integer("Número do caixa atribuído ao ECF")
    reg_d355_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.d355",
        "parent_d350_id",
        string="Redução Z (Códigos 2E, 13, 14, 15 e 16)",
        help="Bloco D",
    )


class RegistroD355(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.d355"
    _description = u"""Redução Z (Códigos 2E, 13, 14, 15 e 16)"""
    _inherit = "l10n.br.sped.mixin"
    dt_doc = fields.Integer("Data do movimento a que se refere a Redução Z")
    cro = fields.Integer("Posição do Contador de Reinício de Operação")
    crz = fields.Integer("Posição do Contador de Redução Z")
    num_coo_fin = fields.Integer("NUM_COO_FIN")
    gt_fin = fields.Integer("Valor do Grande Total final")
    vl_brt = fields.Integer("Valor da venda bruta")
    parent_d350_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.d350",
        string="Equipamento ECF (Códigos 2E, 13, 14, 15 e 16)",
    )
    reg_d360_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.d360",
        string="PIS E COFINS totalizados no dia (Códigos 2E, 13, 14, 15 e 16)",
        help="Bloco D",
    )  # m2o
    reg_d365_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.d365",
        "parent_d355_id",
        string="Registro dos Totalizadores Parciais da Redução Z (Códigos 2E, 13, 14, 15 e 16)",
        help="Bloco D",
    )
    reg_d390_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.d390",
        "parent_d355_id",
        string="Registro analítico do movimento diário (Códigos 13, 14, 15, 16 E 2E)",
        help="Bloco D",
    )


class RegistroD360(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.d360"
    _description = u"""PIS E COFINS totalizados no dia (Códigos 2E, 13, 14, 15 e 16)"""
    _inherit = "l10n.br.sped.mixin"
    vl_pis = fields.Integer("Valor total do PIS")
    vl_cofins = fields.Integer("Valor total da COFINS")


class RegistroD365(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.d365"
    _description = u"""Registro dos Totalizadores Parciais da Redução Z (Códigos 2E, 13, 14, 15 e 16)"""
    _inherit = "l10n.br.sped.mixin"
    cod_tot_par = fields.Char(
        "Código do totalizador, conforme Tabela 4",
        help="""Código do totalizador, conforme Tabela 4.4.6
Ver pagina 120""",
    )
    vlr_acum_tot = fields.Integer(
        "Valor acumulado no totalizador, relativo à respectiva Redução Z"
    )
    nr_tot = fields.Integer("NR_TOT")
    descr_nr_tot = fields.Char(
        "DESCR_NR_TOT",
        help="""Descrição da situação tributária relativa ao totalizador parcial, quando houver mais de um com a mesma carga tributária efetiva.
Ver pagina 120""",
    )
    parent_d355_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.d355",
        string="Redução Z (Códigos 2E, 13, 14, 15 e 16)",
    )
    reg_d370_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.d370",
        "parent_d365_id",
        string="Complemento dos documentos informados (Códigos 13, 14, 15, 16 E 2E)",
        help="Bloco D",
    )


class RegistroD370(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.d370"
    _description = (
        u"""Complemento dos documentos informados (Códigos 13, 14, 15, 16 E 2E)"""
    )
    _inherit = "l10n.br.sped.mixin"
    parent_d365_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.d365",
        string="Registro dos Totalizadores Parciais da Redução Z (Códigos 2E, 13, 14, 15 e 16)",
    )


class RegistroD390(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.d390"
    _description = (
        u"""Registro analítico do movimento diário (Códigos 13, 14, 15, 16 E 2E)"""
    )
    _inherit = "l10n.br.sped.mixin"
    cst_icms = fields.Integer("CST_ICMS")
    cfop = fields.Integer("Código Fiscal de Operação e Prestação")
    aliq_icms = fields.Monetary("Alíquota do ICMS", digits=2)
    vl_opr = fields.Integer("VL_OPR")
    vl_bc_issqn = fields.Integer("Valor da base de cálculo do ISSQN")
    aliq_issqn = fields.Monetary("Alíquota do ISSQN", digits=2)
    vl_issqn = fields.Integer("Valor do ISSQN")
    vl_bc_icms = fields.Integer(
        "Base de cálculo do ICMS acumulada relativa àalíquota informada"
    )
    vl_icms = fields.Integer(
        "Valor  do  ICMS   acumulado  relativo  à  alíquotainformada"
    )
    cod_obs = fields.Char(
        "COD_OBS",
        help="""Código   da   observação   do   lançamento   fiscal(campo 02 do Registro 0460)
Ver pagina 121""",
    )
    parent_d355_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.d355",
        string="Redução Z (Códigos 2E, 13, 14, 15 e 16)",
    )


class RegistroD400(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.d400"
    _description = u"""Resumo do Movimento Diário (código 18)"""
    _inherit = "l10n.br.sped.mixin"
    cod_part = fields.Char(
        "Código do participante (campo 02 do Registro 0150)",
        help="""Código do participante (campo 02 do Registro 0150):- agência, filial ou posto
Ver pagina 122""",
    )
    cod_mod = fields.Char(
        "Código do modelo do documento fiscal, conforme a Tabela 4",
        help="""Código do modelo do documento fiscal, conforme a Tabela 4.1.1
Ver pagina 122""",
    )
    cod_sit = fields.Integer(
        "Código da situação do documento fiscal, conformea Tabela 4"
    )
    ser = fields.Char(
        "Série do documento fiscal",
        help="""Série do documento fiscal
Ver pagina 122""",
    )
    sub = fields.Integer("Subsérie do documento fiscal")
    num_doc = fields.Integer("Número do documento fiscal resumo.")
    dt_doc = fields.Integer("Data da emissão do documento fiscal")
    vl_doc = fields.Integer("Valor total do documento fiscal")
    vl_desc = fields.Integer("Valor acumulado dos descontos")
    vl_serv = fields.Integer("Valor acumulado da prestação de serviço")
    vl_bc_icms = fields.Integer("Valor total da base de cálculo do ICMS")
    vl_icms = fields.Integer("Valor total do ICMS")
    vl_pis = fields.Integer("Valor do PIS")
    vl_cofins = fields.Integer("Valor da COFINS")
    cod_cta = fields.Char(
        "Código da conta analítica contábil debitada/creditada",
        help="""Código da conta analítica contábil debitada/creditada
Ver pagina 122""",
    )
    reg_d410_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.d410",
        "parent_d400_id",
        string="Documentos Informados (Códigos 13, 14, 15 e 16)",
        help="Bloco D",
    )
    reg_d420_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.d420",
        "parent_d400_id",
        string="Complemento dos Documentos Informados (Códigos 13, 14, 15 e 16)",
        help="Bloco D",
    )


class RegistroD410(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.d410"
    _description = u"""Documentos Informados (Códigos 13, 14, 15 e 16)"""
    _inherit = "l10n.br.sped.mixin"
    cod_mod = fields.Char(
        "Código do modelo do documento fiscal , conformea Tabela 4",
        help="""Código do modelo do documento fiscal , conformea Tabela 4.1.1
Ver pagina 123""",
    )
    ser = fields.Char(
        "Série do documento fiscal",
        help="""Série do documento fiscal
Ver pagina 123""",
    )
    sub = fields.Integer("Subsérie do documento fiscal")
    num_doc_ini = fields.Integer("NUM_DOC_INI")
    num_doc_fin = fields.Integer(
        "Número do documento fiscal final(mesmo modelo,série e subsérie)"
    )
    dt_doc = fields.Integer("Data da emissão dos documentos fiscais")
    cst_icms = fields.Integer("CST_ICMS")
    cfop = fields.Integer("Código Fiscal de Operação e Prestação")
    aliq_icms = fields.Monetary("Alíquota do ICMS", digits=2)
    vl_opr = fields.Integer("VL_OPR")
    vl_desc = fields.Integer("Valor acumulado dos descontos")
    vl_serv = fields.Integer("Valor acumulado da prestação de serviço")
    vl_bc_icms = fields.Integer("Valor acumulado da base de cálculo do ICMS")
    vl_icms = fields.Integer("Valor acumulado do ICMS")
    parent_d400_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.d400",
        string="Resumo do Movimento Diário (código 18)",
    )
    reg_d411_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.d411",
        "parent_d410_id",
        string="Documentos Cancelados dos Documentos Informados (Códigos 13, 14, 15 e 16)",
        help="Bloco D",
    )


class RegistroD411(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.d411"
    _description = (
        u"""Documentos Cancelados dos Documentos Informados (Códigos 13, 14, 15 e 16)"""
    )
    _inherit = "l10n.br.sped.mixin"
    parent_d410_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.d410",
        string="Documentos Informados (Códigos 13, 14, 15 e 16)",
    )


class RegistroD420(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.d420"
    _description = (
        u"""Complemento dos Documentos Informados (Códigos 13, 14, 15 e 16)"""
    )
    _inherit = "l10n.br.sped.mixin"
    parent_d400_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.d400",
        string="Resumo do Movimento Diário (código 18)",
    )


class RegistroD500(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.d500"
    _description = u"""Nota Fiscal de Serviço de Comunicação (código 21) e Serviço de Telecomunicação (código 22)"""
    _inherit = "l10n.br.sped.mixin"
    ind_oper = fields.Char(
        "Indicador do tipo de operação",
        required=True,
        help="""Indicador do tipo de operação:0- Aquisição;1- Prestação
Ver pagina 125""",
    )
    ind_emit = fields.Char(
        "Indicador do emitente do documento fiscal",
        required=True,
        help="""Indicador do emitente do documento fiscal:0- Emissão própria;1- Terceiros
Ver pagina 125""",
    )
    cod_part = fields.Char(
        "Código do participante (campo 02 do Registro 0150)",
        required=True,
        help="""Código do participante (campo 02 do Registro 0150):- do prestador do serviço, no caso de aquisição;- do tomador do serviço, no caso de prestação.
Ver pagina 126""",
    )
    cod_mod = fields.Char(
        "Código do modelo do documento fiscal, conforme a Tabela 4",
        required=True,
        help="""Código do modelo do documento fiscal, conforme a Tabela 4.1.1
Ver pagina 126""",
    )
    cod_sit = fields.Integer(
        "Código da situação do documento fiscal, conforme a Tabela 4", required=True
    )
    ser = fields.Char(
        "Série do documento fiscal",
        help="""Série do documento fiscal
Ver pagina 126""",
    )
    sub = fields.Char(
        "Subsérie do documento fiscal",
        help="""Subsérie do documento fiscal
Ver pagina 126""",
    )
    num_doc = fields.Integer("Número do documento fiscal", required=True)
    dt_doc = fields.Integer("Data da emissão do documento fiscal", required=True)
    dt_a_p = fields.Integer(
        "Data da entrada (aquisição) ou da saída (prestação do serviço)"
    )
    vl_doc = fields.Integer("Valor total do documento fiscal", required=True)
    vl_desc = fields.Integer("Valor total do desconto")
    vl_serv = fields.Integer("Valor da prestação de serviços", required=True)
    vl_serv_nt = fields.Integer(
        "Valor total dos serviços não-tributados pelo ICMS", required=True
    )
    vl_terc = fields.Integer("Valores cobrados em nome de terceiros", required=True)
    vl_da = fields.Integer(
        "Valor de outras despesas indicadas no documento fiscal", required=True
    )
    vl_bc_icms = fields.Integer("Valor da base de cálculo do ICMS", required=True)
    vl_icms = fields.Integer("Valor do ICMS", required=True)
    cod_inf = fields.Char(
        "Código da informação complementar (campo 02 do Registro 0450)",
        help="""Código da informação complementar (campo 02 do Registro 0450)
Ver pagina 126""",
    )
    vl_pis = fields.Integer("Valor do PIS")
    vl_cofins = fields.Integer("Valor da COFINS")
    cod_cta = fields.Char(
        "Código da conta analítica contábil debitada/creditada",
        help="""Código da conta analítica contábil debitada/creditada
Ver pagina 126""",
    )
    tp_assinante = fields.Integer("Código do Tipo de Assinante", required=True)
    reg_d510_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.d510",
        "parent_d500_id",
        string="Itens do Documento - Nota Fiscal de Serviço de Comunicação (código 21) e Serviço deTelecomunicação (código 22)",
        help="Bloco D",
    )
    reg_d530_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.d530",
        "parent_d500_id",
        string="Terminal Faturado",
        help="Bloco D",
    )
    reg_d590_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.d590",
        "parent_d500_id",
        string="Registro Analítico do Documento (códigos 21 e 22)",
        help="Bloco D",
    )


class RegistroD510(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.d510"
    _description = u"""Itens do Documento - Nota Fiscal de Serviço de Comunicação (código 21) e Serviço deTelecomunicação (código 22)"""
    _inherit = "l10n.br.sped.mixin"
    num_item = fields.Integer("Número sequencial do item no documento fiscal")
    cod_item = fields.Char(
        "Código do item (campo 02 do Registro 0200)",
        help="""Código do item (campo 02 do Registro 0200)
Ver pagina 127""",
    )
    cod_class = fields.Integer("COD_CLASS")
    qtd = fields.Integer("Quantidade do item")
    unid = fields.Char(
        "Unidade do item  (Campo 02 do registro 0190)",
        help="""Unidade do item  (Campo 02 do registro 0190)
Ver pagina 127""",
    )
    vl_item = fields.Integer("Valor do item")
    vl_desc = fields.Integer("Valor total do desconto")
    cst_icms = fields.Integer("CST_ICMS")
    cfop = fields.Integer("Código Fiscal de Operação e Prestação")
    vl_bc_icms = fields.Integer("Valor da base de cálculo do ICMS")
    aliq_icms = fields.Monetary("Alíquota do ICMS", digits=2)
    vl_icms = fields.Integer("Valor do ICMS creditado/debitado")
    vl_bc_icms_uf = fields.Integer("Valor da base de cálculo do ICMS de outras UFs")
    vl_icms_uf = fields.Integer("Valor do ICMS de outras UFs")
    ind_rec = fields.Char(
        "Indicador do tipo de receita",
        help="""Indicador do tipo de receita:0- Receita própria - serviços prestados;1- Receita própria - cobrança de débitos;2- Receita própria - venda de mercadorias;3- Receita própria - venda de serviço pré-pago;4- Outras receitas próprias;5- Receitas de terceiros (co-faturamento);9- Outras receitas de terceiros
Ver pagina 127""",
    )
    cod_part = fields.Char(
        "COD_PART",
        help="""Código do participante (campo 02 do Registro 0150) receptor da receita, terceiro da operação, se houver.
Ver pagina 127""",
    )
    vl_pis = fields.Integer("Valor do PIS")
    vl_cofins = fields.Integer("Valor da COFINS")
    cod_cta = fields.Char(
        "Código da conta analítica contábil debitada/creditada",
        help="""Código da conta analítica contábil debitada/creditada
Ver pagina 127""",
    )
    parent_d500_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.d500",
        string="Nota Fiscal de Serviço de Comunicação (código 21) e Serviço de Telecomunicação (código 22)",
    )


class RegistroD530(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.d530"
    _description = u"""Terminal Faturado"""
    _inherit = "l10n.br.sped.mixin"
    ind_serv = fields.Char(
        "Indicador do tipo de serviço prestado",
        help="""Indicador do tipo de serviço prestado:0- Telefonia;1- Comunicação de dados;2- TV por assinatura;3- Provimento de acesso à Internet;4- Multimídia;9- Outros
Ver pagina 129""",
    )
    dt_ini_serv = fields.Integer("Data em que se iniciou a prestação do serviço")
    dt_fin_serv = fields.Integer("Data em que se encerrou a prestação do serviço")
    per_fiscal = fields.Integer("Período fiscal da prestação do serviço (MMAAAA)")
    cod_area = fields.Char(
        "Código de área do terminal faturado",
        help="""Código de área do terminal faturado
Ver pagina 129""",
    )
    terminal = fields.Integer("Identificação do terminal faturado")
    parent_d500_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.d500",
        string="Nota Fiscal de Serviço de Comunicação (código 21) e Serviço de Telecomunicação (código 22)",
    )


class RegistroD590(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.d590"
    _description = u"""Registro Analítico do Documento (códigos 21 e 22)"""
    _inherit = "l10n.br.sped.mixin"
    cst_icms = fields.Integer("CST_ICMS", required=True)
    cfop = fields.Integer("CFOP", required=True)
    aliq_icms = fields.Monetary("Alíquota do ICMS", digits=2)
    vl_opr = fields.Integer("VL_OPR", required=True)
    vl_bc_icms = fields.Integer("VL_BC_ICMS", required=True)
    vl_icms = fields.Integer("VL_ICMS", required=True)
    vl_bc_icms_uf = fields.Integer("VL_BC_ICMS_UF", required=True)
    vl_icms_uf = fields.Integer("VL_ICMS_UF", required=True)
    vl_red_bc = fields.Integer("VL_RED_BC", required=True)
    cod_obs = fields.Char(
        "Código  da observação  (campo 02 do Registro 0460)",
        help="""Código  da observação  (campo 02 do Registro 0460)
Ver pagina 130""",
    )
    parent_d500_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.d500",
        string="Nota Fiscal de Serviço de Comunicação (código 21) e Serviço de Telecomunicação (código 22)",
    )


class RegistroD600(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.d600"
    _description = u"""Consolidação da Prestação de Serviços - Notas de Serviço de Comunicação (código 21) e de Serviço de Telecomunicação (código 22)"""
    _inherit = "l10n.br.sped.mixin"
    cod_mod = fields.Char(
        "Código do modelo do documento fiscal, conforme a Tabela 4",
        help="""Código do modelo do documento fiscal, conforme a Tabela 4.1.1
Ver pagina 130""",
    )
    cod_mun = fields.Integer("COD_MUN")
    ser = fields.Char(
        "Série do documento fiscal",
        help="""Série do documento fiscal
Ver pagina 131""",
    )
    sub = fields.Integer("Subsérie do documento fiscal")
    cod_cons = fields.Integer("COD_CONS")
    qtd_cons = fields.Integer("Quantidade de documentos consolidados neste registro")
    dt_doc = fields.Integer("Data dos documentos consolidados")
    vl_doc = fields.Integer("Valor total acumulado dos documentos fiscais")
    vl_desc = fields.Integer("Valor acumulado dos descontos")
    vl_serv = fields.Integer(
        "Valor acumulado das prestações de serviços tributados pelo ICMS"
    )
    vl_serv_nt = fields.Integer("Valor acumulado dos serviços não-tributados pelo ICMS")
    vl_terc = fields.Integer("Valores cobrados em nome de terceiros")
    vl_da = fields.Integer("Valor acumulado das despesas acessórias")
    vl_bc_icms = fields.Integer("Valor acumulado da base de cálculo do ICMS")
    vl_icms = fields.Integer("Valor acumulado do ICMS")
    vl_pis = fields.Integer("Valor do PIS")
    vl_cofins = fields.Integer("Valor da COFINS")
    reg_d610_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.d610",
        "parent_d600_id",
        string="Itens do Documento Consolidado (códigos 21 e 22)",
        help="Bloco D",
    )
    reg_d690_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.d690",
        "parent_d600_id",
        string="Registro Analítico dos Documentos (códigos 21 e 22)",
        help="Bloco D",
    )


class RegistroD610(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.d610"
    _description = u"""Itens do Documento Consolidado (códigos 21 e 22)"""
    _inherit = "l10n.br.sped.mixin"
    cod_class = fields.Integer("COD_CLASS")
    cod_item = fields.Char(
        "Código do item (campo 02 do Registro 0200)",
        help="""Código do item (campo 02 do Registro 0200)
Ver pagina 132""",
    )
    qtd = fields.Integer("Quantidade acumulada do item")
    unid = fields.Char(
        "Unidade do item  (Campo 02 do registro 0190)",
        help="""Unidade do item  (Campo 02 do registro 0190)
Ver pagina 132""",
    )
    vl_item = fields.Integer("Valor acumulado do item")
    vl_desc = fields.Integer("Valor acumulado dos descontos")
    cst_icms = fields.Integer("CST_ICMS")
    cfop = fields.Integer("CFOP")
    aliq_icms = fields.Monetary("Alíquota do ICMS", digits=2)
    vl_bc_icms = fields.Integer("Valor acumulado da base de cálculo do ICMS")
    vl_icms = fields.Integer("Valor acumulado do ICMS debitado")
    vl_bc_icms_uf = fields.Integer("Valor da base de cálculo do ICMS de outras UFs")
    vl_icms_uf = fields.Integer("Valor do ICMS de outras UFs")
    vl_red_bc = fields.Integer("VL_RED_BC")
    vl_pis = fields.Integer("Valor acumulado do PIS")
    vl_cofins = fields.Integer("Valor acumulado da COFINS")
    cod_cta = fields.Char(
        "Código da conta analítica contábil debitada/creditada",
        help="""Código da conta analítica contábil debitada/creditada
Ver pagina 132""",
    )
    parent_d600_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.d600",
        string="Consolidação da Prestação de Serviços - Notas de Serviço de Comunicação (código 21) e de Serviço de Telecomunicação (código 22)",
    )


class RegistroD690(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.d690"
    _description = u"""Registro Analítico dos Documentos (códigos 21 e 22)"""
    _inherit = "l10n.br.sped.mixin"
    cst_icms = fields.Integer("CST_ICMS")
    cfop = fields.Integer("CFOP")
    aliq_icms = fields.Monetary("Alíquota do ICMS", digits=2)
    vl_opr = fields.Integer("VL_OPR")
    vl_bc_icms = fields.Integer("VL_BC_ICMS")
    vl_icms = fields.Integer("VL_ICMS")
    vl_bc_icms_uf = fields.Integer("VL_BC_ICMS_UF")
    vl_icms_uf = fields.Integer("VL_ICMS_UF")
    vl_red_bc = fields.Integer("VL_RED_BC")
    cod_obs = fields.Char(
        "COD_OBS",
        help="""Código da observação do lançamento fiscal (campo02 do Registro 0460)
Ver pagina 133""",
    )
    parent_d600_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.d600",
        string="Consolidação da Prestação de Serviços - Notas de Serviço de Comunicação (código 21) e de Serviço de Telecomunicação (código 22)",
    )


class RegistroD695(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.d695"
    _description = u"""Consolidação da Prestação de Serviços - Notas de Serviço de Comunicação (código 21) e de Serviço de Telecomunicação (código 22)"""
    _inherit = "l10n.br.sped.mixin"
    cod_mod = fields.Char(
        "Código do modelo do documento fiscal, conforme a Tabela 4",
        help="""Código do modelo do documento fiscal, conforme a Tabela 4.1.1.
Ver pagina 134""",
    )
    ser = fields.Char(
        "Série do documento fiscal",
        help="""Série do documento fiscal
Ver pagina 134""",
    )
    nro_ord_ini = fields.Integer("Número de ordem inicial")
    nro_ord_fin = fields.Integer("Número de ordem final")
    dt_doc_ini = fields.Integer("DT_DOC_INI")
    dt_doc_fin = fields.Integer("DT_DOC_FIN")
    nom_mest = fields.Char(
        "Nome do arquivo Mestre de Documento Fiscal",
        help="""Nome do arquivo Mestre de Documento Fiscal
Ver pagina 135""",
    )
    chv_cod_dig = fields.Char(
        "CHV_COD_DIG",
        help="""Chave de codificação digital do arquivo Mestre de Documento Fiscal
Ver pagina 135""",
    )
    reg_d696_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.d696",
        "parent_d695_id",
        string="Registro Analítico dos Documentos (códigos 21 e 22)",
        help="Bloco D",
    )


class RegistroD696(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.d696"
    _description = u"""Registro Analítico dos Documentos (códigos 21 e 22)"""
    _inherit = "l10n.br.sped.mixin"
    cst_icms = fields.Integer("CST_ICMS")
    cfop = fields.Integer("CFOP")
    aliq_icms = fields.Monetary("Alíquota do ICMS", digits=2)
    vl_opr = fields.Integer("VL_OPR")
    vl_bc_icms = fields.Integer("VL_BC_ICMS")
    vl_icms = fields.Integer("VL_ICMS")
    vl_bc_icms_uf = fields.Integer("VL_BC_ICMS_UF")
    vl_icms_uf = fields.Integer("VL_ICMS_UF")
    vl_red_bc = fields.Integer("VL_RED_BC")
    cod_obs = fields.Char(
        "COD_OBS",
        help="""Código da observação do lançamento fiscal (campo02 do Registro 0460)
Ver pagina 136""",
    )
    parent_d695_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.d695",
        string="Consolidação da Prestação de Serviços - Notas de Serviço de Comunicação (código 21) e de Serviço de Telecomunicação (código 22)",
    )
    reg_d697_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.d697",
        "parent_d696_id",
        string="Registro de informações de outras UFs, relativamente aos serviços “não-medidos” de televisão por assinatura via satélite",
        help="Bloco D",
    )


class RegistroD697(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.d697"
    _description = u"""Registro de informações de outras UFs, relativamente aos serviços “não-medidos” de televisão por assinatura via satélite"""
    _inherit = "l10n.br.sped.mixin"
    parent_d696_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.d696",
        string="Registro Analítico dos Documentos (códigos 21 e 22)",
    )


class RegistroE100(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.e100"
    _description = u"""Período de Apuração do ICMS"""
    _inherit = "l10n.br.sped.mixin"
    dt_ini = fields.Integer("Data inicial a que a apuração se refere", required=True)
    dt_fin = fields.Integer("Data final a que a apuração se refere", required=True)
    reg_e110_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.e110",
        string="Apuração do ICMS - Operações Próprias",
        help="Bloco E",
    )  # m2o


class RegistroE110(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.e110"
    _description = u"""Apuração do ICMS - Operações Próprias"""
    _inherit = "l10n.br.sped.mixin"
    vl_tot_debitos = fields.Integer("VL_TOT_DEBITOS", required=True)
    vl_aj_debitos = fields.Integer(
        "Valor total dos ajustes a débito decorrentes dodocumento fiscal", required=True
    )
    vl_tot_aj_debitos = fields.Integer(
        "Valor total de 'Ajustes a débito'", required=True
    )
    vl_estornos_cred = fields.Integer(
        "Valor total de Ajustes “Estornos de créditos”", required=True
    )
    vl_tot_creditos = fields.Integer("VL_TOT_CREDITOS", required=True)
    vl_aj_creditos = fields.Integer(
        "Valor total dos ajustes a crédito decorrentes dodocumento fiscal",
        required=True,
    )
    vl_tot_aj_creditos = fields.Integer(
        "Valor total de 'Ajustes a crédito'", required=True
    )
    vl_estornos_deb = fields.Integer(
        "Valor total de Ajustes “Estornos de Débitos”", required=True
    )
    vl_sld_credor_ant = fields.Integer(
        "Valor  total  de   'Saldo   credor   do   períodoanterior'", required=True
    )
    vl_sld_apurado = fields.Integer("Valor do saldo devedor apurado", required=True)
    vl_tot_ded = fields.Integer("Valor total de 'Deduções'", required=True)
    vl_icms_recolher = fields.Integer(
        "Valor total de 'ICMS a recolher (11-12)", required=True
    )
    vl_sld_credor_transportar = fields.Integer(
        "VL_SLD_CREDOR_TRANSPORTAR", required=True
    )
    deb_esp = fields.Integer(
        "Valores  recolhidos   ou   a  recolher,  extra-apuração", required=True
    )
    reg_e111_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.e111",
        "parent_e110_id",
        string="Ajuste/Benefício/Incentivo da Apuração do ICMS",
        help="Bloco E",
    )
    reg_e115_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.e115",
        "parent_e110_id",
        string="Informações Adicionais da Apuração do ICMS - Valores Declaratórios",
        help="Bloco E",
    )
    reg_e116_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.e116",
        "parent_e110_id",
        string="Obrigações do ICMS Recolhido ou a Recolher - Obrigações Próprias",
        help="Bloco E",
    )


class RegistroE111(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.e111"
    _description = u"""Ajuste/Benefício/Incentivo da Apuração do ICMS"""
    _inherit = "l10n.br.sped.mixin"
    cod_aj_apur = fields.Char(
        "COD_AJ_APUR",
        required=True,
        help="""Código do ajuste da apuração e dedução, conforme aTabela indicada no item 5.1.1.
Ver pagina 141""",
    )
    descr_compl_aj = fields.Char(
        "Descrição complementar do ajuste da apuração*",
        help="""Descrição complementar do ajuste da apuração.
Ver pagina 141""",
    )
    vl_aj_apur = fields.Integer("Valor do ajuste da apuração", required=True)
    parent_e110_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.e110", string="Apuração do ICMS - Operações Próprias"
    )
    reg_e112_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.e112",
        "parent_e111_id",
        string="Informações Adicionais dos Ajustes da Apuração do ICMS",
        help="Bloco E",
    )
    reg_e113_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.e113",
        "parent_e111_id",
        string="Informações   Adicionais   dos   Ajustes   da   Apuração   do   ICMS   -   Identificação   dosdocumentos fiscais",
        help="Bloco E",
    )


class RegistroE112(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.e112"
    _description = u"""Informações Adicionais dos Ajustes da Apuração do ICMS"""
    _inherit = "l10n.br.sped.mixin"
    num_da = fields.Char(
        "NUM_DA*",
        help="""Número   do   documento   de   arrecadação   estadual,   sehouver
Ver pagina 142""",
    )
    num_proc = fields.Char(
        "Número do processo ao qual o ajuste está vinculado, sehouver*",
        help="""Número do processo ao qual o ajuste está vinculado, sehouver
Ver pagina 142""",
    )
    ind_proc = fields.Char(
        "Indicador da origem do processo*",
        help="""Indicador da origem do processo:0- Sefaz;1- Justiça Federal;2- Justiça Estadual;9- Outros
Ver pagina 142""",
    )
    proc = fields.Char(
        "PROC*",
        help="""Descrição   resumida   do   processo   que   embasou   olançamento
Ver pagina 142""",
    )
    txt_compl = fields.Char(
        "Descrição complementar*",
        help="""Descrição complementar
Ver pagina 142""",
    )
    parent_e111_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.e111",
        string="Ajuste/Benefício/Incentivo da Apuração do ICMS",
    )


class RegistroE113(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.e113"
    _description = u"""Informações   Adicionais   dos   Ajustes   da   Apuração   do   ICMS   -   Identificação   dosdocumentos fiscais"""
    _inherit = "l10n.br.sped.mixin"
    cod_part = fields.Char(
        "Código do participante (campo 02 do Registro 0150)",
        required=True,
        help="""Código do participante (campo 02 do Registro 0150):
Ver pagina 142""",
    )
    cod_mod = fields.Char(
        "Código do modelo do documento fiscal, conforme a Tabela 4",
        required=True,
        help="""Código do modelo do documento fiscal, conforme a Tabela 4.1.1
Ver pagina 143""",
    )
    ser = fields.Char(
        "Série do documento fiscal*",
        help="""Série do documento fiscal
Ver pagina 143""",
    )
    sub = fields.Integer("Subsérie do documento fiscal*")
    num_doc = fields.Integer("Número do documento fiscal", required=True)
    dt_doc = fields.Integer("Data da emissão do documento fiscal", required=True)
    cod_item = fields.Char(
        "Código do item (campo 02 do Registro 0200)*",
        help="""Código do item (campo 02 do Registro 0200)
Ver pagina 143""",
    )
    vl_aj_item = fields.Integer("Valor do ajuste para a operação/item", required=True)
    parent_e111_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.e111",
        string="Ajuste/Benefício/Incentivo da Apuração do ICMS",
    )


class RegistroE115(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.e115"
    _description = (
        u"""Informações Adicionais da Apuração do ICMS - Valores Declaratórios"""
    )
    _inherit = "l10n.br.sped.mixin"
    cod_inf_adic = fields.Char(
        "COD_INF_ADIC",
        required=True,
        help="""Código da informação adicional conforme tabela a ser definida pelas SEFAZ, conforme tabela definida no item 5.2.
Ver pagina 143""",
    )
    vl_inf_adic = fields.Integer(
        "Valor referente à informação adicional", required=True
    )
    descr_compl_aj = fields.Char(
        "Descrição complementar do ajuste*",
        help="""Descrição complementar do ajuste
Ver pagina 143""",
    )
    parent_e110_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.e110", string="Apuração do ICMS - Operações Próprias"
    )


class RegistroE116(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.e116"
    _description = (
        u"""Obrigações do ICMS Recolhido ou a Recolher - Obrigações Próprias"""
    )
    _inherit = "l10n.br.sped.mixin"
    cod_or = fields.Char(
        "Código da obrigação a recolher, conforme a Tabela 5",
        required=True,
        help="""Código da obrigação a recolher, conforme a Tabela 5.4
Ver pagina 144""",
    )
    vl_or = fields.Integer("Valor da obrigação a recolher", required=True)
    dt_vcto = fields.Integer("Data de vencimento da obrigação", required=True)
    cod_rec = fields.Char(
        "COD_REC",
        required=True,
        help="""Código   de   receita   referente   à   obrigação,   próprio   daunidade da federação, conforme legislação estadual.
Ver pagina 144""",
    )
    num_proc = fields.Char(
        "NUM_PROC*",
        help="""Número   do   processo   ou   auto   de   infração   ao   qual   aobrigação está vinculada, se houver.
Ver pagina 144""",
    )
    ind_proc = fields.Char(
        "Indicador da origem do processo*",
        help="""Indicador da origem do processo:0- SEFAZ;1- Justiça Federal;2- Justiça Estadual;9- Outros
Ver pagina 144""",
    )
    proc = fields.Char(
        "PROC*",
        help="""Descrição   resumida   do   processo   que   embasou   olançamento
Ver pagina 144""",
    )
    txt_compl = fields.Char(
        "Descrição complementar das obrigações a recolher*",
        help="""Descrição complementar das obrigações a recolher.
Ver pagina 144""",
    )
    mes_ref = fields.Integer(
        "Informe o mês de referência no formato “mmaaaa”", required=True
    )
    parent_e110_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.e110", string="Apuração do ICMS - Operações Próprias"
    )


class RegistroE200(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.e200"
    _description = u"""Período de Apuração do ICMS - Substituição Tributária"""
    _inherit = "l10n.br.sped.mixin"
    uf = fields.Char(
        "UF",
        required=True,
        help="""Sigla da unidade da federação a que se refere a apuração do ICMS ST
Ver pagina 145""",
    )
    dt_ini = fields.Integer("Data inicial a que a apuração se refere", required=True)
    dt_fin = fields.Integer("Data final a que a apuração se refere", required=True)
    reg_e210_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.e210",
        string="Apuração do ICMS - Substituição Tributária",
        help="Bloco E",
    )  # m2o


class RegistroE210(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.e210"
    _description = u"""Apuração do ICMS - Substituição Tributária"""
    _inherit = "l10n.br.sped.mixin"
    ind_mov_st = fields.Char(
        "Indicador de movimento",
        required=True,
        help="""Indicador de movimento:0 – Sem operações com ST1 – Com operações de ST
Ver pagina 145""",
    )
    vl_sld_cred_ant_st = fields.Integer("VL_SLD_CRED_ANT_ST", required=True)
    vl_devol_st = fields.Integer(
        "Valor total do ICMS ST de devolução de", required=True
    )
    vl_ressarc_st = fields.Integer(
        "Valor total do ICMS ST de ressarcimentos", required=True
    )
    vl_out_cred_st = fields.Integer("VL_OUT_CRED_ST", required=True)
    vl_aj_creditos_st = fields.Integer("VL_AJ_CREDITOS_ST", required=True)
    vl_retencao_st = fields.Integer(
        "Valor Total do ICMS retido por Substituição Tributária", required=True
    )
    vl_out_deb_st = fields.Integer("VL_OUT_DEB_ST", required=True)
    vl_aj_debitos_st = fields.Integer("VL_AJ_DEBITOS_ST", required=True)
    vl_sld_dev_ant_st = fields.Integer(
        "Valor total de Saldo devedor antes das deduções", required=True
    )
    vl_deducoes_st = fields.Integer(
        "Valor total dos ajustes 'Deduções ST'", required=True
    )
    vl_icms_recol_st = fields.Integer("Imposto a recolher ST (11-12)", required=True)
    vl_sld_cred_st_transportar = fields.Integer(
        "VL_SLD_CRED_ST_TRANSPORTAR", required=True
    )
    deb_esp_st = fields.Integer(
        "Valores  recolhidos   ou   a  recolher,  extra-apuração", required=True
    )
    reg_e220_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.e220",
        "parent_e210_id",
        string="Ajuste/Benefício/Incentivo da Apuração do ICMS - Substituição Tributária",
        help="Bloco E",
    )
    reg_e250_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.e250",
        "parent_e210_id",
        string="Obrigações do ICMS a Recolher - Substituição Tributária",
        help="Bloco E",
    )


class RegistroE220(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.e220"
    _description = (
        u"""Ajuste/Benefício/Incentivo da Apuração do ICMS - Substituição Tributária"""
    )
    _inherit = "l10n.br.sped.mixin"
    cod_aj_apur = fields.Char(
        "COD_AJ_APUR",
        required=True,
        help="""Código do ajuste da apuração e dedução, conforme a Tabela indicada no item 5.1.1
Ver pagina 148""",
    )
    descr_compl_aj = fields.Char(
        "Descrição complementar do ajuste da apuração*",
        help="""Descrição complementar do ajuste da apuração
Ver pagina 148""",
    )
    vl_aj_apur = fields.Integer("Valor do ajuste da apuração", required=True)
    parent_e210_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.e210",
        string="Apuração do ICMS - Substituição Tributária",
    )
    reg_e230_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.e230",
        "parent_e220_id",
        string="Informações Adicionais dos Ajustes da Apuração do ICMS Substituição Tributária",
        help="Bloco E",
    )
    reg_e240_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.e240",
        "parent_e220_id",
        string="Informações Adicionais dos Ajustes da Apuração do ICMS Substituição Tributária -Identificação dos documentos fiscais",
        help="Bloco E",
    )


class RegistroE230(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.e230"
    _description = u"""Informações Adicionais dos Ajustes da Apuração do ICMS Substituição Tributária"""
    _inherit = "l10n.br.sped.mixin"
    num_da = fields.Char(
        "Número do documento de arrecadação estadual, se houver*",
        help="""Número do documento de arrecadação estadual, se houver
Ver pagina 148""",
    )
    num_proc = fields.Char(
        "Número do processo ao qual o ajuste está vinculado, se houver*",
        help="""Número do processo ao qual o ajuste está vinculado, se houver
Ver pagina 149""",
    )
    ind_proc = fields.Integer("Indicador da origem do processo*")
    proc = fields.Char(
        "Descrição resumida do processo que embasou o lançamento*",
        help="""Descrição resumida do processo que embasou o lançamento
Ver pagina 149""",
    )
    txt_compl = fields.Char(
        "Descrição complementar*",
        help="""Descrição complementar
Ver pagina 149""",
    )
    parent_e220_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.e220",
        string="Ajuste/Benefício/Incentivo da Apuração do ICMS - Substituição Tributária",
    )


class RegistroE240(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.e240"
    _description = u"""Informações Adicionais dos Ajustes da Apuração do ICMS Substituição Tributária -Identificação dos documentos fiscais"""
    _inherit = "l10n.br.sped.mixin"
    cod_part = fields.Char(
        "Código do participante (campo 02 do Registro 0150)",
        required=True,
        help="""Código do participante (campo 02 do Registro 0150):- do emitente do documento ou do remetente das mercadorias, no caso de entradas;- do adquirente, no caso de saídas
Ver pagina 149""",
    )
    cod_mod = fields.Char(
        "Código do modelo do documento fiscal, conforme a Tabela 4",
        required=True,
        help="""Código do modelo do documento fiscal, conforme a Tabela 4.1.1
Ver pagina 149""",
    )
    ser = fields.Char(
        "Série do documento fiscal*",
        help="""Série do documento fiscal
Ver pagina 149""",
    )
    sub = fields.Integer("Subsérie do documento fiscal*")
    num_doc = fields.Integer("Número do documento fiscal", required=True)
    dt_doc = fields.Integer("Data da emissão do documento fiscal", required=True)
    cod_item = fields.Char(
        "Código do item (campo 02 do Registro 0200)*",
        help="""Código do item (campo 02 do Registro 0200)
Ver pagina 149""",
    )
    vl_aj_item = fields.Integer("Valor do ajuste para a operação/item", required=True)
    parent_e220_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.e220",
        string="Ajuste/Benefício/Incentivo da Apuração do ICMS - Substituição Tributária",
    )


class RegistroE250(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.e250"
    _description = u"""Obrigações do ICMS a Recolher - Substituição Tributária"""
    _inherit = "l10n.br.sped.mixin"
    cod_or = fields.Char(
        "Código da obrigação a recolher, conforme a Tabela 5",
        required=True,
        help="""Código da obrigação a recolher, conforme a Tabela 5.4
Ver pagina 150""",
    )
    vl_or = fields.Integer("Valor da obrigação ICMS ST a recolher", required=True)
    dt_vcto = fields.Integer("Data de vencimento da obrigação", required=True)
    cod_rec = fields.Char(
        "COD_REC",
        required=True,
        help="""Código   de   receita   referente   à   obrigação,   próprio   daunidade da federação do contribuinte substituído.
Ver pagina 150""",
    )
    num_proc = fields.Char(
        "NUM_PROC*",
        help="""Número   do   processo   ou   auto   de   infração   ao   qual   aobrigação está vinculada, se houver
Ver pagina 150""",
    )
    ind_proc = fields.Char(
        "Indicador da origem do processo*",
        help="""Indicador da origem do processo:0- SEFAZ;1- Justiça Federal;2- Justiça Estadual;9- Outros
Ver pagina 150""",
    )
    proc = fields.Char(
        "PROC*",
        help="""Descrição   resumida   do   processo   que   embasou   olançamento
Ver pagina 150""",
    )
    txt_compl = fields.Char(
        "Descrição complementar das obrigações a recolher*",
        help="""Descrição complementar das obrigações a recolher
Ver pagina 150""",
    )
    mes_ref = fields.Integer(
        "Informe o mês de referência no formato “mmaaaa”", required=True
    )
    parent_e210_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.e210",
        string="Apuração do ICMS - Substituição Tributária",
    )


class RegistroE300(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.e300"
    _description = u"""Período de Apuração do ICMS Diferencial de Alíquota – UF Origem/Destino EC 87/15"""
    _inherit = "l10n.br.sped.mixin"
    uf = fields.Char(
        "UF",
        required=True,
        help="""Sigla da unidade da federação a que se refere à apuração do FCP e do ICMS Diferencial de Alíquota da UF de Origem/Destino
Ver pagina 151""",
    )
    dt_ini = fields.Integer("Data inicial a que a apuração se refere", required=True)
    dt_fin = fields.Integer("Data final a que a apuração se refere", required=True)
    reg_e310_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.e310",
        string="Apuração do ICMS Diferencial de Alíquota – UF Origem/Destino EC 87/15",
        help="Bloco E",
    )  # m2o


class RegistroE310(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.e310"
    _description = (
        u"""Apuração do ICMS Diferencial de Alíquota – UF Origem/Destino EC 87/15"""
    )
    _inherit = "l10n.br.sped.mixin"
    ind_mov_fcp_difal = fields.Char(
        "Indicador de movimento",
        required=True,
        help="""Indicador de movimento:0 – Sem operações 1 – Com operações
Ver pagina 20""",
    )
    vl_sld_cred_ant_difal = fields.Integer("VL_SLD_CRED_ANT_DIFAL", required=True)
    vl_tot_debitos_difal = fields.Integer("VL_TOT_DEBITOS_DIFAL", required=True)
    vl_out_deb_difal = fields.Integer("VL_OUT_DEB_DIFAL", required=True)
    vl_tot_creditos_difal = fields.Integer("VL_TOT_CREDITOS_DIFAL", required=True)
    vl_out_cred_difal = fields.Integer("VL_OUT_CRED_DIFAL", required=True)
    vl_sld_dev_ant_difal = fields.Integer("VL_SLD_DEV_ANT_DIFAL", required=True)
    vl_deducoes_difal = fields.Integer("VL_DEDUCOES_DIFAL", required=True)
    vl_recol_difal = fields.Integer("VL_RECOL_DIFAL", required=True)
    vl_sld_cred_transportar_difal = fields.Integer(
        "VL_SLD_CRED_TRANSPORTAR_DIFAL", required=True
    )
    deb_esp_difal = fields.Integer("DEB_ESP_DIFAL", required=True)
    vl_sld_cred_ant_fcp = fields.Integer(
        "Valor do 'Saldo credor de período anterior – FCP'", required=True
    )
    vl_tot_deb_fcp = fields.Integer(
        "Valor total dos débitos FCP por 'Saídas e prestações”", required=True
    )
    vl_out_deb_fcp = fields.Integer("VL_OUT_DEB_FCP", required=True)
    vl_tot_cred_fcp = fields.Integer(
        "Valor total dos créditos FCP por Entradas", required=True
    )
    vl_out_cred_fcp = fields.Integer("VL_OUT_CRED_FCP", required=True)
    vl_sld_dev_ant_fcp = fields.Integer(
        "Valor total de Saldo devedor FCP antes das deduções", required=True
    )
    vl_deducoes_fcp = fields.Integer("Valor total das deduções 'FCP'", required=True)
    vl_recol_fcp = fields.Integer(
        "Valor recolhido ou a recolher referente ao FCP (18–", required=True
    )
    vl_sld_cred_transportar_fcp = fields.Integer(
        "VL_SLD_CRED_TRANSPORTAR_FCP", required=True
    )
    deb_esp_fcp = fields.Integer(
        "Valores recolhidos ou a recolher, extra-apuração - FCP", required=True
    )
    reg_e311_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.e311",
        "parent_e310_id",
        string="Ajuste/Benefício/Incentivo   da   Apuração   do   ICMS   Diferencial   de   Alíquota   –   UFOrigem/Destino EC 87/15",
        help="Bloco E",
    )
    reg_e316_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.e316",
        "parent_e310_id",
        string="Obrigações   do   ICMS   recolhido   ou   a   recolher   –   Diferencial   de   Alíquota   –   UFOrigem/Destino EC 87/15",
        help="Bloco E",
    )


class RegistroE311(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.e311"
    _description = u"""Ajuste/Benefício/Incentivo   da   Apuração   do   ICMS   Diferencial   de   Alíquota   –   UFOrigem/Destino EC 87/15"""
    _inherit = "l10n.br.sped.mixin"
    cod_aj_apur = fields.Char(
        "COD_AJ_APUR",
        required=True,
        help="""Código do ajuste da apuração e dedução, conforme a Tabela indicada no item 5.1.1
Ver pagina 158""",
    )
    descr_compl_aj = fields.Char(
        "Descrição complementar do ajuste da apuração*",
        help="""Descrição complementar do ajuste da apuração
Ver pagina 158""",
    )
    vl_aj_apur = fields.Integer("Valor do ajuste da apuração", required=True)
    parent_e310_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.e310",
        string="Apuração do ICMS Diferencial de Alíquota – UF Origem/Destino EC 87/15",
    )
    reg_e312_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.e312",
        "parent_e311_id",
        string="Informações Adicionais dos Ajustes da Apuração do ICMS Diferencial de Alíquota – UFOrigem/Destino EC 87/15",
        help="Bloco E",
    )
    reg_e313_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.e313",
        "parent_e311_id",
        string="Informações   Adicionais   da   Apuração   do   ICMS   Diferencial   de   Alíquota   –   UFOrigem/Destino EC 87/15 Identificação dos Documentos Fiscais",
        help="Bloco E",
    )


class RegistroE312(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.e312"
    _description = u"""Informações Adicionais dos Ajustes da Apuração do ICMS Diferencial de Alíquota – UFOrigem/Destino EC 87/15"""
    _inherit = "l10n.br.sped.mixin"
    num_da = fields.Char(
        "Número do documento de arrecadação estadual, se houver*",
        help="""Número do documento de arrecadação estadual, se houver
Ver pagina 159""",
    )
    num_proc = fields.Char(
        "Número do processo ao qual o ajuste está vinculado, se houver*",
        help="""Número do processo ao qual o ajuste está vinculado, se houver
Ver pagina 159""",
    )
    ind_proc = fields.Integer("Indicador da origem do processo*")
    proc = fields.Char(
        "Descrição resumida do processo que embasou o lançamento*",
        help="""Descrição resumida do processo que embasou o lançamento
Ver pagina 159""",
    )
    txt_compl = fields.Char(
        "Descrição complementar*",
        help="""Descrição complementar
Ver pagina 159""",
    )
    parent_e311_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.e311",
        string="Ajuste/Benefício/Incentivo   da   Apuração   do   ICMS   Diferencial   de   Alíquota   –   UFOrigem/Destino EC 87/15",
    )


class RegistroE313(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.e313"
    _description = u"""Informações   Adicionais   da   Apuração   do   ICMS   Diferencial   de   Alíquota   –   UFOrigem/Destino EC 87/15 Identificação dos Documentos Fiscais"""
    _inherit = "l10n.br.sped.mixin"
    cod_part = fields.Char(
        "Código do participante (campo 02 do Registro 0150)",
        required=True,
        help="""Código do participante (campo 02 do Registro 0150)
Ver pagina 160""",
    )
    cod_mod = fields.Char(
        "Código do modelo do documento fiscal, conforme a Tabela 4",
        required=True,
        help="""Código do modelo do documento fiscal, conforme a Tabela 4.1.1
Ver pagina 160""",
    )
    ser = fields.Char(
        "Série do documento fiscal*",
        help="""Série do documento fiscal
Ver pagina 160""",
    )
    sub = fields.Integer("Subsérie do documento fiscal*")
    num_doc = fields.Integer("Número do documento fiscal", required=True)
    parent_e311_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.e311",
        string="Ajuste/Benefício/Incentivo   da   Apuração   do   ICMS   Diferencial   de   Alíquota   –   UFOrigem/Destino EC 87/15",
    )


class RegistroE316(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.e316"
    _description = u"""Obrigações   do   ICMS   recolhido   ou   a   recolher   –   Diferencial   de   Alíquota   –   UFOrigem/Destino EC 87/15"""
    _inherit = "l10n.br.sped.mixin"
    cod_or = fields.Char(
        "Código da obrigação recolhida ou a recolher, conforme aTabela 5",
        required=True,
        help="""Código da obrigação recolhida ou a recolher, conforme aTabela 5.4
Ver pagina 161""",
    )
    vl_or = fields.Integer("Valor da obrigação recolhida ou a recolher", required=True)
    dt_vcto = fields.Integer("Data de vencimento da obrigação", required=True)
    cod_rec = fields.Char(
        "COD_REC",
        required=True,
        help="""Código   de   receita   referente   à   obrigação,   próprio   daunidade   da   federação   da   origem/destino,  conformelegislação estadual.
Ver pagina 161""",
    )
    num_proc = fields.Char(
        "NUM_PROC*",
        help="""Número   do   processo   ou   auto   de   infração   ao   qual   aobrigação está vinculada, se houver
Ver pagina 161""",
    )
    ind_proc = fields.Char(
        "Indicador da origem do processo*",
        help="""Indicador da origem do processo:0- SEFAZ;1- Justiça Federal;2- Justiça Estadual;9- Outros
Ver pagina 161""",
    )
    proc = fields.Char(
        "PROC*",
        help="""Descrição   resumida   do   processo   que   embasou   olançamento
Ver pagina 161""",
    )
    txt_compl = fields.Char(
        "Descrição complementar das obrigações recolhidas ou arecolher*",
        help="""Descrição complementar das obrigações recolhidas ou arecolher
Ver pagina 161""",
    )
    mes_ref = fields.Integer(
        "Informe o mês de referência no formato “mmaaaa”", required=True
    )
    parent_e310_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.e310",
        string="Apuração do ICMS Diferencial de Alíquota – UF Origem/Destino EC 87/15",
    )


class RegistroE500(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.e500"
    _description = u"""Período de Apuração do IPI"""
    _inherit = "l10n.br.sped.mixin"
    ind_apur = fields.Char(
        "Indicador de período de apuração do IPI",
        required=True,
        help="""Indicador de período de apuração do IPI:0 - Mensal;1 - Decendial
Ver pagina 162""",
    )
    dt_ini = fields.Integer("Data inicial a que a apuração se refere", required=True)
    dt_fin = fields.Integer("Data final a que a apuração se refere", required=True)
    reg_e520_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.e520", string="Apuração do IPI", help="Bloco E"
    )  # m2o
    reg_e510_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.e510",
        "parent_e500_id",
        string="Consolidação dos Valores de IPI",
        help="Bloco E",
    )


class RegistroE510(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.e510"
    _description = u"""Consolidação dos Valores de IPI"""
    _inherit = "l10n.br.sped.mixin"
    cfop = fields.Integer(
        "Código Fiscal de Operação e Prestação do agrupamento de itens", required=True
    )
    cst_ipi = fields.Char(
        "CST_IPI",
        required=True,
        help="""Código da Situação Tributária referente ao IPI, conforme a Tabela indicada no item 4.3.2.
Ver pagina 162""",
    )
    vl_cont_ipi = fields.Integer("VL_CONT_IPI", required=True)
    vl_bc_ipi = fields.Integer("VL_BC_IPI", required=True)
    vl_ipi = fields.Integer("VL_IPI", required=True)
    parent_e500_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.e500", string="Período de Apuração do IPI"
    )


class RegistroE520(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.e520"
    _description = u"""Apuração do IPI"""
    _inherit = "l10n.br.sped.mixin"
    vl_sd_ant_ipi = fields.Integer(
        "Saldo credor do IPI transferido do período anterior", required=True
    )
    vl_deb_ipi = fields.Integer(
        "Valor total dos débitos por 'Saídas com débito do imposto'", required=True
    )
    vl_cred_ipi = fields.Integer("VL_CRED_IPI", required=True)
    vl_od_ipi = fields.Integer(
        "Valor de 'Outros débitos' do IPI (inclusive estornos de crédito)",
        required=True,
    )
    vl_oc_ipi = fields.Integer("VL_OC_IPI", required=True)
    vl_sc_ipi = fields.Integer("VL_SC_IPI", required=True)
    vl_sd_ipi = fields.Integer(
        "Valor do saldo devedor do IPI a recolher", required=True
    )
    reg_e530_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.e530",
        "parent_e520_id",
        string="Ajustes da Apuração do IPI",
        help="Bloco E",
    )


class RegistroE530(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.e530"
    _description = u"""Ajustes da Apuração do IPI"""
    _inherit = "l10n.br.sped.mixin"
    ind_aj = fields.Char(
        "Indicador do tipo de ajuste",
        required=True,
        help="""Indicador do tipo de ajuste:0- Ajuste a débito;1- Ajuste a crédito
Ver pagina 164""",
    )
    vl_aj = fields.Integer("Valor do ajuste", required=True)
    cod_aj = fields.Char(
        "COD_AJ",
        required=True,
        help="""Código do ajuste da apuração, conforme a Tabela indicada no item 4.5.4.
Ver pagina 164""",
    )
    ind_doc = fields.Char(
        "Indicador da origem do documento vinculado ao ajuste",
        required=True,
        help="""Indicador da origem do documento vinculado ao ajuste:0 - Processo Judicial;1 - Processo Administrativo;2 - PER/DCOMP;3 – Documento Fiscal9 – Outros.
Ver pagina 164""",
    )
    num_doc = fields.Char(
        "NUM_DOC*",
        help="""Número do documento / processo / declaração ao qual o ajuste está vinculado, se houver
Ver pagina 164""",
    )
    descr_aj = fields.Char(
        "DESCR_AJ",
        required=True,
        help="""Descrição detalhada do ajuste, com citação dos documentos fiscais.
Ver pagina 164""",
    )
    parent_e520_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.e520", string="Apuração do IPI"
    )
    reg_e531_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.e531",
        "parent_e530_id",
        string="Informações Adicionais dos Ajustes da Apuração do IPI – Identificação dos Documentos Fiscais (01 e 55)",
        help="Bloco E",
    )


class RegistroE531(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.e531"
    _description = u"""Informações Adicionais dos Ajustes da Apuração do IPI – Identificação dos Documentos Fiscais (01 e 55)"""
    _inherit = "l10n.br.sped.mixin"
    cod_part = fields.Char(
        "Código do participante (campo 02 do Registro 0150)*",
        help="""Código do participante (campo 02 do Registro 0150):- do emitente do documento ou do remetente das mercadorias, no caso de entradas;- do adquirente, no caso de saídas
Ver pagina 21""",
    )
    cod_mod = fields.Char(
        "Código do modelo do documento fiscal, conforme a Tabela 4",
        required=True,
        help="""Código do modelo do documento fiscal, conforme a Tabela 4.1.1
Ver pagina 21""",
    )
    ser = fields.Char(
        "Série do documento fiscal*",
        help="""Série do documento fiscal
Ver pagina 21""",
    )
    sub = fields.Integer("Subsérie do documento fiscal*")
    num_doc = fields.Integer("Número do documento fiscal", required=True)
    dt_doc = fields.Integer("Data da emissão do documento fiscal", required=True)
    cod_item = fields.Char(
        "Código do item (campo 02 do Registro 0200)*",
        help="""Código do item (campo 02 do Registro 0200)
Ver pagina 21""",
    )
    vl_aj_item = fields.Integer("Valor do ajuste para a operação/item", required=True)
    chv_nfe = fields.Integer("Chave da Nota Fiscal Eletrônica (modelo 55)*")
    parent_e530_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.e530", string="Ajustes da Apuração do IPI"
    )


class RegistroG110(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.g110"
    _description = u"""ICMS - Ativo Permanente - CIAP"""
    _inherit = "l10n.br.sped.mixin"
    dt_ini = fields.Integer("Data inicial a que a apuração se refere", required=True)
    dt_fin = fields.Integer("Data final a que a apuração se refere", required=True)
    saldo_in_icms = fields.Integer("SALDO_IN_ICMS", required=True)
    som_parc = fields.Integer("SOM_PARC", required=True)
    vl_trib_exp = fields.Integer("VL_TRIB_EXP", required=True)
    vl_total = fields.Integer("Valor total de saídas", required=True)
    ind_per_sai = fields.Integer("IND_PER_SAI", required=True)
    icms_aprop = fields.Integer("ICMS_APROP", required=True)
    som_icms_oc = fields.Integer("SOM_ICMS_OC", required=True)
    reg_g125_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.g125",
        "parent_g110_id",
        string="Movimentação de Bem do Ativo Imobilizado",
        help="Bloco G",
    )


class RegistroG125(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.g125"
    _description = u"""Movimentação de Bem do Ativo Imobilizado"""
    _inherit = "l10n.br.sped.mixin"
    cod_ind_bem = fields.Char(
        "COD_IND_BEM",
        required=True,
        help="""Código individualizado do bem ou componente adotadono controle patrimonial do estabelecimento informante
Ver pagina 169""",
    )
    dt_mov = fields.Integer("Data da movimentação ou do saldo inicial", required=True)
    tipo_mov = fields.Char(
        "Tipo de movimentação do bem ou componente",
        required=True,
        help="""Tipo de movimentação do bem ou componente: SI = Saldo inicial de bens imobilizados; IM = Imobilização de bem individual; IA = Imobilização em Andamento - Componente; CI = Conclusão de Imobilização em Andamento – BemResultante; MC = Imobilização oriunda do Ativo Circulante; BA = Baixa do bem - Fim do período de apropriação; AT = Alienação ou Transferência; PE = Perecimento, Extravio ou Deterioração; OT = Outras Saídas do Imobilizado
Ver pagina 169""",
    )
    vl_imob_icms_op = fields.Integer(
        "Valor do ICMS da Operação Própria na entrada do bemou componente*"
    )
    vl_imob_icms_st = fields.Integer("Valor do ICMS da Oper*")
    vl_imob_icms_frt = fields.Integer("VL_IMOB_ICMS_FRT*")
    vl_imob_icms_dif = fields.Integer(
        "Valor do ICMS - Diferencial  de Alíquota, conformeDoc*"
    )
    num_parc = fields.Integer("Número da parcela do ICMS*")
    vl_parc_pass = fields.Integer("VL_PARC_PASS*")
    parent_g110_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.g110", string="ICMS - Ativo Permanente - CIAP"
    )
    reg_g126_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.g126",
        "parent_g125_id",
        string="Outros créditos CIAP",
        help="Bloco G",
    )
    reg_g130_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.g130",
        "parent_g125_id",
        string="Identificação do documento fiscal",
        help="Bloco G",
    )


class RegistroG126(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.g126"
    _description = u"""Outros créditos CIAP"""
    _inherit = "l10n.br.sped.mixin"
    dt_ini = fields.Integer("Data inicial do período de apuração", required=True)
    dt_fim = fields.Integer("Data final do período de apuração", required=True)
    num_parc = fields.Integer("Número da parcela do ICMS", required=True)
    vl_parc_pass = fields.Integer("VL_PARC_PASS", required=True)
    vl_trib_oc = fields.Integer("VL_TRIB_OC", required=True)
    vl_total = fields.Integer(
        "Valor total de saídas no período indicado neste registro", required=True
    )
    ind_per_sai = fields.Integer("IND_PER_SAI", required=True)
    vl_parc_aprop = fields.Integer("VL_PARC_APROP", required=True)
    parent_g125_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.g125",
        string="Movimentação de Bem do Ativo Imobilizado",
    )


class RegistroG130(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.g130"
    _description = u"""Identificação do documento fiscal"""
    _inherit = "l10n.br.sped.mixin"
    ind_emit = fields.Char(
        "Indicador do emitente do documento fiscal",
        required=True,
        help="""Indicador do emitente do documento fiscal:0- Emissão própria;1- Terceiros
Ver pagina 172""",
    )
    parent_g125_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.g125",
        string="Movimentação de Bem do Ativo Imobilizado",
    )
    reg_g140_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.g140",
        "parent_g130_id",
        string="Identificação do item do documento fiscal",
        help="Bloco G",
    )


class RegistroG140(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.g140"
    _description = u"""Identificação do item do documento fiscal"""
    _inherit = "l10n.br.sped.mixin"
    num_item = fields.Integer(
        "Número sequencial do item no documento fiscal", required=True
    )
    cod_item = fields.Char(
        "COD_ITEM",
        required=True,
        help="""Código correspondente do bem no documento fiscal (campo 02 do registro 0200)
Ver pagina 173""",
    )
    parent_g130_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.g130", string="Identificação do documento fiscal"
    )


class RegistroH005(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.h005"
    _description = u"""Totais do Inventário"""
    _inherit = "l10n.br.sped.mixin"
    dt_inv = fields.Integer("Data do inventário", required=True)
    vl_inv = fields.Integer("Valor total do estoque", required=True)
    mot_inv = fields.Char(
        "Informe o motivo do Inventário",
        required=True,
        help="""Informe o motivo do Inventário:01 – No final no período;02 – Na mudança de forma de tributação da mercadoria (ICMS);03 – Na solicitação da baixa cadastral, paralisação temporária e outras situações;04 – Na alteração de regime de pagamento – condição do contribuinte;05 – Por determinação dos fiscos.
Ver pagina 174""",
    )
    reg_h010_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.h010",
        "parent_h005_id",
        string="Inventário",
        help="Bloco H",
    )


class RegistroH010(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.h010"
    _description = u"""Inventário"""
    _inherit = "l10n.br.sped.mixin"
    cod_item = fields.Char(
        "Código do item (campo 02 do Registro 0200)",
        required=True,
        help="""Código do item (campo 02 do Registro 0200)
Ver pagina 175""",
    )
    parent_h005_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.h005", string="Totais do Inventário"
    )
    reg_h020_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.h020",
        "parent_h010_id",
        string="Informação complementar do Inventário",
        help="Bloco H",
    )


class RegistroH020(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.h020"
    _description = u"""Informação complementar do Inventário"""
    _inherit = "l10n.br.sped.mixin"
    cst_icms = fields.Integer("CST_ICMS", required=True)
    bc_icms = fields.Integer("Informe a base de cálculo do ICMS", required=True)
    vl_icms = fields.Integer(
        "Informe o valor do ICMS a ser debitado ou creditado", required=True
    )
    parent_h010_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.h010", string="Inventário"
    )


class RegistroK100(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.k100"
    _description = u"""Período de Apuração do ICMS/IPI"""
    _inherit = "l10n.br.sped.mixin"
    dt_ini = fields.Integer("Data inicial a que a apuração se refere", required=True)
    dt_fin = fields.Integer("Data final a que a apuração se refere", required=True)
    reg_k200_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.k200",
        "parent_k100_id",
        string="Estoque Escriturado",
        help="Bloco K",
    )
    reg_k210_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.k210",
        "parent_k100_id",
        string="Desmontagem de mercadorias – Item de Origem",
        help="Bloco K",
    )
    reg_k220_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.k220",
        "parent_k100_id",
        string="Outras Movimentações Internas entre Mercadorias",
        help="Bloco K",
    )
    reg_k230_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.k230",
        "parent_k100_id",
        string="Itens Produzidos",
        help="Bloco K",
    )
    reg_k250_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.k250",
        "parent_k100_id",
        string="Industrialização Efetuada por Terceiros – Itens Produzidos",
        help="Bloco K",
    )
    reg_k260_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.k260",
        "parent_k100_id",
        string="Reprocessamento/Reparo de Produto/Insumo",
        help="Bloco K",
    )
    reg_k270_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.k270",
        "parent_k100_id",
        string="Correção de Apontamento dos Registros K210, K220, K230, K250 e K260",
        help="Bloco K",
    )
    reg_k280_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.k280",
        "parent_k100_id",
        string="Correção de Apontamento – Estoque Escriturado",
        help="Bloco K",
    )


class RegistroK200(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.k200"
    _description = u"""Estoque Escriturado"""
    _inherit = "l10n.br.sped.mixin"
    dt_est = fields.Integer("Data do estoque final", required=True)
    cod_item = fields.Char(
        "Código do item (campo 02 do Registro 0200)",
        required=True,
        help="""Código do item (campo 02 do Registro 0200)
Ver pagina 178""",
    )
    qtd = fields.Integer("Quantidade em estoque", required=True)
    ind_est = fields.Char(
        "Indicador do tipo de estoque",
        required=True,
        help="""Indicador do tipo de estoque:  0 = Estoque de propriedade do informante eem seu poder;  1 = Estoque de propriedade do informante eem posse de terceiros; 2 = Estoque de propriedade de terceiros e emposse do informante
Ver pagina 178""",
    )
    cod_part = fields.Char(
        "Código do participante (campo 02 do Registro 0150)*",
        help="""Código do participante (campo 02 do Registro 0150):-  proprietário/possuidor  que   não   seja   oinformante do arquivo
Ver pagina 178""",
    )
    parent_k100_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.k100", string="Período de Apuração do ICMS/IPI"
    )


class RegistroK210(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.k210"
    _description = u"""Desmontagem de mercadorias – Item de Origem"""
    _inherit = "l10n.br.sped.mixin"
    dt_ini_os = fields.Integer("Data de início da ordem de serviço*")
    dt_fin_os = fields.Integer("Data de conclusão da ordem de serviço*")
    cod_doc_os = fields.Char(
        "Código de identificação  da ordem deserviço*",
        help="""Código de identificação  da ordem deserviço
Ver pagina 179""",
    )
    cod_item_ori = fields.Char(
        "Código do item de origem (campo 02do Registro 0200)",
        required=True,
        help="""Código do item de origem (campo 02do Registro 0200)
Ver pagina 179""",
    )
    qtd_ori = fields.Integer("Quantidade de origem – saída do estoque", required=True)
    parent_k100_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.k100", string="Período de Apuração do ICMS/IPI"
    )
    reg_k215_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.k215",
        "parent_k210_id",
        string="Desmontagem de mercadorias – Item de Destino",
        help="Bloco K",
    )


class RegistroK215(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.k215"
    _description = u"""Desmontagem de mercadorias – Item de Destino"""
    _inherit = "l10n.br.sped.mixin"
    cod_item_des = fields.Char(
        "Código do item de destino (campo 02do Registro 0200)",
        required=True,
        help="""Código do item de destino (campo 02do Registro 0200)
Ver pagina 180""",
    )
    qtd_des = fields.Integer(
        "Quantidade de destino – entrada em estoque", required=True
    )
    parent_k210_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.k210",
        string="Desmontagem de mercadorias – Item de Origem",
    )


class RegistroK220(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.k220"
    _description = u"""Outras Movimentações Internas entre Mercadorias"""
    _inherit = "l10n.br.sped.mixin"
    parent_k100_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.k100", string="Período de Apuração do ICMS/IPI"
    )


class RegistroK230(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.k230"
    _description = u"""Itens Produzidos"""
    _inherit = "l10n.br.sped.mixin"
    dt_ini_op = fields.Integer("Data de início da ordem de produção*")
    dt_fin_op = fields.Integer("Data de conclusão da ordem de produção*")
    cod_doc_op = fields.Char(
        "Código de identificação da ordem de produção*",
        help="""Código de identificação da ordem de produção
Ver pagina 182""",
    )
    cod_item = fields.Char(
        "Código   do   item   produzido   (campo   02   doRegistro 0200)",
        required=True,
        help="""Código   do   item   produzido   (campo   02   doRegistro 0200)
Ver pagina 182""",
    )
    qtd_enc = fields.Integer("Quantidade de produção acabada", required=True)
    parent_k100_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.k100", string="Período de Apuração do ICMS/IPI"
    )
    reg_k235_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.k235",
        "parent_k230_id",
        string="Insumos Consumidos",
        help="Bloco K",
    )


class RegistroK235(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.k235"
    _description = u"""Insumos Consumidos"""
    _inherit = "l10n.br.sped.mixin"
    dt_saida = fields.Integer(
        "Data   de  saída   do  estoque  para  alocação  aoproduto", required=True
    )
    cod_item = fields.Char(
        "Código do item componente/insumo (campo02 do Registro 0200)",
        required=True,
        help="""Código do item componente/insumo (campo02 do Registro 0200)
Ver pagina 183""",
    )
    qtd = fields.Integer("Quantidade consumida do item", required=True)
    cod_ins_subst = fields.Char(
        "COD_INS_SUBST*",
        help="""Código do insumo que foi substituído, casoocorra a substituição (campo 02 do Registro0210)
Ver pagina 183""",
    )
    parent_k230_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.k230", string="Itens Produzidos"
    )


class RegistroK250(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.k250"
    _description = u"""Industrialização Efetuada por Terceiros – Itens Produzidos"""
    _inherit = "l10n.br.sped.mixin"
    dt_prod = fields.Integer(
        "Data   do   reconhecimento   da   produção   ocorrida   no", required=True
    )
    cod_item = fields.Char(
        "Código do item produzido (campo 02 do Registro0200)",
        required=True,
        help="""Código do item produzido (campo 02 do Registro0200)
Ver pagina 184""",
    )
    qtd = fields.Integer("Quantidade produzida", required=True)
    parent_k100_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.k100", string="Período de Apuração do ICMS/IPI"
    )
    reg_k255_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.k255",
        "parent_k250_id",
        string="Industrialização em Terceiros – Insumos Consumidos",
        help="Bloco K",
    )


class RegistroK255(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.k255"
    _description = u"""Industrialização em Terceiros – Insumos Consumidos"""
    _inherit = "l10n.br.sped.mixin"
    dt_cons = fields.Integer("DT_CONS", required=True)
    cod_item = fields.Char(
        "Código   do   insumo   (campo   02   do   Registro0200)",
        required=True,
        help="""Código   do   insumo   (campo   02   do   Registro0200)
Ver pagina 184""",
    )
    qtd = fields.Integer("Quantidade de consumo do insumo.", required=True)
    cod_ins_subst = fields.Char(
        "COD_INS_SUBST*",
        help="""Código do insumo que foi substituído, casoocorra a substituição (campo 02 do Registro0210)
Ver pagina 184""",
    )
    parent_k250_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.k250",
        string="Industrialização Efetuada por Terceiros – Itens Produzidos",
    )


class RegistroK260(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.k260"
    _description = u"""Reprocessamento/Reparo de Produto/Insumo"""
    _inherit = "l10n.br.sped.mixin"
    cod_op_os = fields.Char(
        "COD_OP_OS*",
        help="""Código   de   identificação   da   ordem   deprodução,  no   reprocessamento,  ou   daordem de serviço, no reparo
Ver pagina 185""",
    )
    cod_item = fields.Char(
        "COD_ITEM",
        required=True,
        help="""Código do produto/insumo a serreprocessado/reparado ou járeprocessado/reparado  (campo   02   doRegistro 0200)
Ver pagina 185""",
    )
    dt_saida = fields.Integer("Data de saída do estoque", required=True)
    qtd_saida = fields.Integer("Quantidade de saída do estoque", required=True)
    dt_ret = fields.Integer("Data de retorno ao estoque (entrada)*")
    qtd_ret = fields.Integer("Quantidade de retorno ao estoque (entrada)*")
    parent_k100_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.k100", string="Período de Apuração do ICMS/IPI"
    )
    reg_k265_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.k265",
        "parent_k260_id",
        string="Reprocessamento/Reparo – Mercadorias Consumidas e/ou Retornadas",
        help="Bloco K",
    )


class RegistroK265(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.k265"
    _description = (
        u"""Reprocessamento/Reparo – Mercadorias Consumidas e/ou Retornadas"""
    )
    _inherit = "l10n.br.sped.mixin"
    cod_item = fields.Char(
        "Código   da   mercadoria   (campo   02   doRegistro 0200)",
        required=True,
        help="""Código   da   mercadoria   (campo   02   doRegistro 0200)
Ver pagina 186""",
    )
    qtd_cons = fields.Integer("Quantidade   consumida   –   saída   doestoque*")
    qtd_ret = fields.Integer("Quantidade   retornada   –   entrada   emestoque*")
    parent_k260_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.k260",
        string="Reprocessamento/Reparo de Produto/Insumo",
    )


class RegistroK270(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.k270"
    _description = (
        u"""Correção de Apontamento dos Registros K210, K220, K230, K250 e K260"""
    )
    _inherit = "l10n.br.sped.mixin"
    dt_ini_ap = fields.Integer("DT_INI_AP*")
    dt_fin_ap = fields.Integer("DT_FIN_AP*")
    cod_op_os = fields.Char(
        "COD_OP_OS*",
        help="""Código   de   identificação   da   ordem   deprodução ou da ordem de serviço que estásendo corrigida
Ver pagina 187""",
    )
    cod_item = fields.Char(
        "COD_ITEM",
        required=True,
        help="""Código   da   mercadoria   que   está   sendocorrigido (campo 02 do Registro 0200)
Ver pagina 187""",
    )
    qtd_cor_pos = fields.Integer("QTD_COR_POS*")
    qtd_cor_neg = fields.Integer("QTD_COR_NEG*")
    origem = fields.Char(
        "ORIGEM",
        required=True,
        help="""1 - correção de apontamento de produçãoe/ou   consumo  relativo   aos   RegistrosK230/K235;2 - correção de apontamento de produçãoe/ou   consumo  relativo   aos   RegistrosK250/K255;3 - correção de apontamento de desmontagem e/ou consumo relativo aos Registros K210/K215;4 - correção de apontamento de reprocessamento/reparo e/ou consumo relativo aos Registros K260/K265;5 - correção de apontamento de movimentação interna relativo ao RegistroK220.6 – correção de apontamento de produção relativo ao Registro K291;7 – correção de apontamento de consumo relativo ao Registro K292;8 – correção de apontamento de produção relativo ao Registro K301;9 – correção de apontamento de consumo relativo ao Registro K302.
Ver pagina 187""",
    )
    parent_k100_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.k100", string="Período de Apuração do ICMS/IPI"
    )
    reg_k275_ids = fields.One2many(
        "l10n.br.sped.efd_icms_ipi.k275",
        "parent_k270_id",
        string="Correção de Apontamento e Retorno de Insumos dos Registros K215, K220, K235,K255 e K265",
        help="Bloco K",
    )


class RegistroK275(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.k275"
    _description = u"""Correção de Apontamento e Retorno de Insumos dos Registros K215, K220, K235,K255 e K265"""
    _inherit = "l10n.br.sped.mixin"
    cod_item = fields.Char(
        "Código   da   mercadoria   (campo   02   doRegistro 0200)",
        required=True,
        help="""Código   da   mercadoria   (campo   02   doRegistro 0200)
Ver pagina 188""",
    )
    qtd_cor_pos = fields.Integer("QTD_COR_POS*")
    qtd_cor_neg = fields.Integer("QTD_COR_NEG*")
    cod_ins_subst = fields.Char(
        "COD_INS_SUBST*",
        help="""Código do insumo que foi substituído,caso ocorra a substituição, relativo aosRegistros K235/K255.
Ver pagina 188""",
    )
    parent_k270_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.k270",
        string="Correção de Apontamento dos Registros K210, K220, K230, K250 e K260",
    )


class RegistroK280(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.k280"
    _description = u"""Correção de Apontamento – Estoque Escriturado"""
    _inherit = "l10n.br.sped.mixin"
    dt_est = fields.Integer("DT_EST", required=True)
    cod_item = fields.Char(
        "Código do item (campo 02 do Registro 0200)",
        required=True,
        help="""Código do item (campo 02 do Registro 0200)
Ver pagina 189""",
    )
    qtd_cor_pos = fields.Integer("QTD_COR_POS*")
    qtd_cor_neg = fields.Integer("QTD_COR_NEG*")
    ind_est = fields.Char(
        "Indicador do tipo de estoque",
        required=True,
        help="""Indicador do tipo de estoque: 0 = Estoque de propriedade do informante e em seu poder; 1 = Estoque de propriedade do informante e em posse de terceiros; 2 = Estoque de propriedade de terceiros e em posse do informante
Ver pagina 189""",
    )
    cod_part = fields.Char(
        "Código do participante (campo 02 do Registro0150)*",
        help="""Código do participante (campo 02 do Registro0150):-  proprietário/possuidor  que   não   seja   oinformante do arquivo
Ver pagina 189""",
    )
    parent_k100_id = fields.Many2one(
        "l10n.br.sped.efd_icms_ipi.k100", string="Período de Apuração do ICMS/IPI"
    )


class Registro9900(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.9900"
    _description = u"""Registros do Arquivo"""
    _inherit = "l10n.br.sped.mixin"
    reg_blc = fields.Char(
        "Registro que será totalizado no próximo campo",
        required=True,
        help="""Registro que será totalizado no próximo campo.
Ver pagina 219""",
    )
    qtd_reg_blc = fields.Integer(
        "Total de registros do tipo informado no campo anterior", required=True
    )


class Registro9999(models.Model):
    _name = "l10n.br.sped.efd_icms_ipi.9999"
    _description = u"""Encerramento do Arquivo Digital"""
    _inherit = "l10n.br.sped.mixin"
    qtd_lin = fields.Integer(
        "Quantidade total de linhas do arquivo digital", required=True
    )
