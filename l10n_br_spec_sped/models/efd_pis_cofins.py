from odoo import fields, models

from . import spec_models


class Registro0000(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.0000"
    _description = u"""Abertura do Arquivo Digital e Identificação da Pessoa Jurídica"""
    _inherit = "l10n.br.sped.mixin"
    cod_ver = fields.Integer(
        "Código da versão do leiaute conforme a tabela 3", required=True
    )
    tipo_escrit = fields.Integer("Tipo de escrituração", required=True)
    ind_sit_esp = fields.Integer("Indicador de situação especial")
    num_rec_anterior = fields.Char(
        "NUM_REC_ANTERIOR",
        help="""Número do Recibo da Escrituração anterior a ser retificada, utilizado quando TIPO_ESCRIT for igual a 1
Ver pagina 59""",
    )
    dt_ini = fields.Integer(
        "Data inicial das informações contidas no arquivo", required=True
    )
    dt_fin = fields.Integer(
        "Data final das informações contidas no arquivo", required=True
    )
    nome = fields.Char(
        "Nome empresarial da pessoa jurídica",
        required=True,
        help="""Nome empresarial da pessoa jurídica
Ver pagina 59""",
    )
    cnpj = fields.Integer("CNPJ", required=True)
    uf = fields.Char(
        "Sigla da Unidade da Federação da pessoa jurídica",
        required=True,
        help="""Sigla da Unidade da Federação da pessoa jurídica.
Ver pagina 59""",
    )
    cod_mun = fields.Integer("COD_MUN", required=True)
    suframa = fields.Char(
        "Inscrição da pessoa jurídica na Suframa",
        help="""Inscrição da pessoa jurídica na Suframa
Ver pagina 59""",
    )
    ind_nat_pj = fields.Integer("Indicador da natureza da pessoa jurídica")
    ind_ativ = fields.Integer(
        "Indicador de tipo de atividade preponderante", required=True
    )


class Registro0035(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.0035"
    _description = u"""Identificação da Sociedade em Conta de Participação - SCP"""
    _inherit = "l10n.br.sped.mixin"
    cod_scp = fields.Integer("Identificação da SCP")
    desc_scp = fields.Char(
        "Descrição da SCP",
        help="""Descrição da SCP
Ver pagina 63""",
    )
    inf_comp = fields.Char(
        "Informação Complementar",
        help="""Informação Complementar
Ver pagina 63""",
    )


class Registro0100(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.0100"
    _description = u"""Dados do Contabilista"""
    _inherit = "l10n.br.sped.mixin"
    nome = fields.Char(
        "Nome do contabilista.",
        required=True,
        help="""Nome do contabilista.
Ver pagina 63""",
    )
    cpf = fields.Integer("Número de inscrição do contabilista no CPF", required=True)
    crc = fields.Char(
        "CRC",
        required=True,
        help="""Número de inscrição do contabilista no  Conselho Regional de Contabilidade.
Ver pagina 63""",
    )
    cnpj = fields.Integer("CNPJ")
    cep = fields.Integer("Código de Endereçamento Postal.")
    end = fields.Char(
        "Logradouro e endereço do imóvel.",
        help="""Logradouro e endereço do imóvel.
Ver pagina 64""",
    )
    num = fields.Char(
        "Número do imóvel.",
        help="""Número do imóvel.
Ver pagina 64""",
    )
    compl = fields.Char(
        "Dados complementares do endereço.",
        help="""Dados complementares do endereço.
Ver pagina 64""",
    )
    bairro = fields.Char(
        "Bairro em que o imóvel está situado.",
        help="""Bairro em que o imóvel está situado.
Ver pagina 64""",
    )
    fone = fields.Char(
        "Número do telefone.",
        help="""Número do telefone.
Ver pagina 64""",
    )
    fax = fields.Char(
        "Número do fax.",
        help="""Número do fax.
Ver pagina 64""",
    )
    email = fields.Char(
        "Endereço do correio eletrônico.",
        help="""Endereço do correio eletrônico.
Ver pagina 64""",
    )
    cod_mun = fields.Integer("Código do município, conforme tabela IBGE")


class Registro0110(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.0110"
    _description = (
        u"""Regimes de Apuração da Contribuição Social e de Apropriação de Crédito"""
    )
    _inherit = "l10n.br.sped.mixin"
    cod_inc_trib = fields.Integer(
        "Código indicador da incidência tributária no período", required=True
    )
    ind_apro_cred = fields.Integer("IND_APRO_CRED")
    cod_tipo_cont = fields.Integer("COD_TIPO_CONT")
    ind_reg_cum = fields.Integer("IND_REG_CUM")
    reg_0111_id = fields.Many2one(
        "l10n.br.sped.efd_pis_cofins.0111",
        string="Tabela de Receita Bruta Mensal para Fins de Rateio de Créditos Comuns",
        help="Bloco 0",
    )  # m2o


class Registro0111(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.0111"
    _description = (
        u"""Tabela de Receita Bruta Mensal para Fins de Rateio de Créditos Comuns"""
    )
    _inherit = "l10n.br.sped.mixin"
    rec_bru_ncum_trib_mi = fields.Integer(
        "Receita Bruta Não-Cumulativa - Tributada no Mercado Interno", required=True
    )
    rec_bru_ = fields.Integer("Receita Bruta Não-Cumulativa – Não")
    rec_bru_ncum_exp = fields.Integer(
        "Receita Bruta Não-Cumulativa – Exportação", required=True
    )
    rec_bru_cum = fields.Integer("Receita Bruta Cumulativa", required=True)
    rec_bru_total = fields.Integer("Receita Bruta Total", required=True)


class Registro0120(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.0120"
    _description = u"""Identificação de EFD-Contribuições sem dados a Escriturar"""
    _inherit = "l10n.br.sped.mixin"
    mes_refer = fields.Char(
        "MES_REFER",
        required=True,
        help="""Mês de referência do ano-calendário daescrituração  sem dados, dispensada da entrega. Campo a ser preenchido no formato “mmaaaa”
Ver pagina 70""",
    )
    inf_comp = fields.Char(
        "Informação complementar do registro",
        required=True,
        help="""Informação complementar do registro. No caso de escrituração  sem  dados,  deve  ser  informado  o  real  motivo dessa situação, conforme indicadores abaixo: 01 - Pessoa jurídica imune ou isenta do IRPJ 02 - Órgãos públicos, autarquias e fundações públicas   03 - Pessoa jurídica inativa   04 -  Pessoa jurídica em  geral,  que  não realizou  operações geradoras de receitas (tributáveis ou não) ou de créditos   05 - Sociedade em Conta de Participação  - SCP, que não realizou operações geradoras de receitas (tributáveis ou não) ou de créditos   06 - Sociedade Cooperativa, que não realizou operações geradoras de receitas (tributáveis ou não) ou de créditos   07 - Escrituração decorrente de incorporação, fusão ou cisão, sem operações geradoras de receitas (tributáveis ou não) ou de créditos   99 - Demais hipóteses de dispensa de escrituração, relacionadas no art. 5º, da IN RFB nº 1.252, de 2012
Ver pagina 70""",
    )


class Registro0140(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.0140"
    _description = u"""Tabela de Cadastro de Estabelecimento"""
    _inherit = "l10n.br.sped.mixin"
    cod_est = fields.Char(
        "Código de identificação do estabelecimento",
        help="""Código de identificação do estabelecimento
Ver pagina 71""",
    )
    nome = fields.Char(
        "Nome empresarial do estabelecimento",
        required=True,
        help="""Nome empresarial do estabelecimento
Ver pagina 71""",
    )
    cnpj = fields.Integer(
        "Número de inscrição do estabelecimento no CNPJ", required=True
    )
    uf = fields.Char(
        "Sigla da unidade da federação do estabelecimento",
        required=True,
        help="""Sigla da unidade da federação do estabelecimento.
Ver pagina 71""",
    )
    ie = fields.Char(
        "IE",
        help="""Inscrição  Estadual  do  estabelecimento,  se  contribuinte  de ICMS.
Ver pagina 72""",
    )
    cod_mun = fields.Integer("COD_MUN", required=True)
    im = fields.Char(
        "Inscrição Municipal do estabelecimento, se contribuinte do ISS",
        help="""Inscrição Municipal do estabelecimento, se contribuinte do ISS.
Ver pagina 72""",
    )
    suframa = fields.Char(
        "Inscrição do estabelecimento na Suframa",
        help="""Inscrição do estabelecimento na Suframa
Ver pagina 72""",
    )
    reg_0145_id = fields.Many2one(
        "l10n.br.sped.efd_pis_cofins.0145",
        string="Regime de Apuração da Contribuição Previdenciária sobre a Receita Bruta",
        help="Bloco 0",
    )  # m2o
    reg_0150_ids = fields.One2many(
        "l10n.br.sped.efd_pis_cofins.0150",
        "parent_0140_id",
        string="Tabela de Cadastro do Participante",
        help="Bloco 0",
    )
    reg_0190_ids = fields.One2many(
        "l10n.br.sped.efd_pis_cofins.0190",
        "parent_0140_id",
        string="Identificação das Unidades de Medida",
        help="Bloco 0",
    )
    reg_0200_ids = fields.One2many(
        "l10n.br.sped.efd_pis_cofins.0200",
        "parent_0140_id",
        string="Tabela de Identificação do Item (Produtos e Serviços)",
        help="Bloco 0",
    )
    reg_0400_ids = fields.One2many(
        "l10n.br.sped.efd_pis_cofins.0400",
        "parent_0140_id",
        string="Tabela de Natureza da Operação/ Prestação",
        help="Bloco 0",
    )
    reg_0450_ids = fields.One2many(
        "l10n.br.sped.efd_pis_cofins.0450",
        "parent_0140_id",
        string="Tabela de Informação Complementar do Documento Fiscal",
        help="Bloco 0",
    )


class Registro0145(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.0145"
    _description = (
        u"""Regime de Apuração da Contribuição Previdenciária sobre a Receita Bruta"""
    )
    _inherit = "l10n.br.sped.mixin"
    cod_inc_trib = fields.Integer(
        "Código indicador da incidência tributária no período", required=True
    )
    vl_rec_tot = fields.Integer(
        "Valor da Receita Bruta Total da Pessoa Jurídica no Período", required=True
    )
    vl_rec_ativ = fields.Integer("VL_REC_ATIV", required=True)
    vl_rec_demais_ativ = fields.Integer("VL_REC_DEMAIS_ATIV")
    info_compl = fields.Char(
        "Informação complementar",
        help="""Informação complementar
Ver pagina 73""",
    )


class Registro0150(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.0150"
    _description = u"""Tabela de Cadastro do Participante"""
    _inherit = "l10n.br.sped.mixin"
    cod_part = fields.Char(
        "Código de identificação do participante no arquivo",
        required=True,
        help="""Código de identificação do participante no arquivo.
Ver pagina 74""",
    )
    nome = fields.Char(
        "Nome pessoal ou empresarial do participante",
        required=True,
        help="""Nome pessoal ou empresarial do participante.
Ver pagina 74""",
    )
    parent_0140_id = fields.Many2one(
        "l10n.br.sped.efd_pis_cofins.0140",
        string="Tabela de Cadastro de Estabelecimento",
    )


class Registro0190(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.0190"
    _description = u"""Identificação das Unidades de Medida"""
    _inherit = "l10n.br.sped.mixin"
    unid = fields.Char(
        "Código da unidade de medida",
        help="""Código da unidade de medida
Ver pagina 76""",
    )
    descr = fields.Char(
        "Descrição da unidade de medida",
        help="""Descrição da unidade de medida
Ver pagina 76""",
    )
    parent_0140_id = fields.Many2one(
        "l10n.br.sped.efd_pis_cofins.0140",
        string="Tabela de Cadastro de Estabelecimento",
    )


class Registro0200(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.0200"
    _description = u"""Tabela de Identificação do Item (Produtos e Serviços)"""
    _inherit = "l10n.br.sped.mixin"
    cod_item = fields.Char(
        "Código do item",
        required=True,
        help="""Código do item
Ver pagina 76""",
    )
    descr_item = fields.Char(
        "Descrição do item",
        required=True,
        help="""Descrição do item
Ver pagina 76""",
    )
    cod_barra = fields.Char(
        "COD_BARRA",
        help="""Representação alfanumérico do código de barra do produto, se houver.
Ver pagina 76""",
    )
    cod_ant_item = fields.Char(
        "COD_ANT_ITEM",
        help="""Código anterior do item com relação à última informação apresentada.
Ver pagina 76""",
    )
    unid_inv = fields.Char(
        "Unidade de medida utilizada na quantificação de estoques",
        help="""Unidade de medida utilizada na quantificação de estoques.
Ver pagina 76""",
    )
    tipo_item = fields.Integer(
        "Tipo do item – Atividades Industriais, Comerciais e Serviços", required=True
    )
    cod_ncm = fields.Char(
        "Código da Nomenclatura Comum do Mercosul",
        help="""Código da Nomenclatura Comum do Mercosul
Ver pagina 77""",
    )
    ex_ipi = fields.Char(
        "Código EX, conforme a TIPI",
        help="""Código EX, conforme a TIPI
Ver pagina 77""",
    )
    cod_gen = fields.Integer("Código do gênero do item, conforme a Tabela 4")
    cod_lst = fields.Integer("COD_LST")
    aliq_icms = fields.Monetary(
        "Alíquota de ICMS aplicável ao item nas operações internas", digits=2
    )
    parent_0140_id = fields.Many2one(
        "l10n.br.sped.efd_pis_cofins.0140",
        string="Tabela de Cadastro de Estabelecimento",
    )
    reg_0206_id = fields.Many2one(
        "l10n.br.sped.efd_pis_cofins.0206",
        string="Código de Produto conforme Tabela ANP (Combustíveis)",
        help="Bloco 0",
    )  # m2o
    reg_0208_id = fields.Many2one(
        "l10n.br.sped.efd_pis_cofins.0208",
        string="Código de Grupos por Marca Comercial – REFRI (Bebidas Frias)",
        help="Bloco 0",
    )  # m2o
    reg_0205_ids = fields.One2many(
        "l10n.br.sped.efd_pis_cofins.0205",
        "parent_0200_id",
        string="Alteração do Item",
        help="Bloco 0",
    )


class Registro0205(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.0205"
    _description = u"""Alteração do Item"""
    _inherit = "l10n.br.sped.mixin"
    descr_ant_item = fields.Char(
        "Descrição anterior do item",
        help="""Descrição anterior do item
Ver pagina 79""",
    )
    dt_ini = fields.Integer(
        "Data inicial de utilização da descrição do item", required=True
    )
    dt_fim = fields.Integer(
        "Data final de utilização da descrição do item", required=True
    )
    parent_0200_id = fields.Many2one(
        "l10n.br.sped.efd_pis_cofins.0200",
        string="Tabela de Identificação do Item (Produtos e Serviços)",
    )


class Registro0206(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.0206"
    _description = u"""Código de Produto conforme Tabela ANP (Combustíveis)"""
    _inherit = "l10n.br.sped.mixin"
    cod_comb = fields.Char(
        "Código  do  combustível,  conforme  tabela  publicada  pela ANP",
        required=True,
        help="""Código  do  combustível,  conforme  tabela  publicada  pela ANP
Ver pagina 79""",
    )


class Registro0208(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.0208"
    _description = u"""Código de Grupos por Marca Comercial – REFRI (Bebidas Frias)"""
    _inherit = "l10n.br.sped.mixin"
    cod_tab = fields.Char(
        "COD_TAB",
        required=True,
        help="""Código indicador  da  Tabela  de Incidência,  conforme Anexo III do Decreto nº 6.707/08: 01 – Tabela I 02 – Tabela II 03 – Tabela III 04 – Tabela IV 05 – Tabela V 06 – Tabela VI 07 – Tabela VII 08– Tabela VIII 09 – Tabela IX 10 – Tabela X 11 – Tabela XI 12 – Tabela XII
Ver pagina 80""",
    )
    cod_gru = fields.Char(
        "Código  do  grupo,  conforme  Anexo  III  do  Decreto  nº 6",
        required=True,
        help="""Código  do  grupo,  conforme  Anexo  III  do  Decreto  nº 6.707/08.
Ver pagina 80""",
    )
    marca_com = fields.Char(
        "Marca Comercial",
        required=True,
        help="""Marca Comercial
Ver pagina 80""",
    )


class Registro0400(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.0400"
    _description = u"""Tabela de Natureza da Operação/ Prestação"""
    _inherit = "l10n.br.sped.mixin"
    cod_nat = fields.Char(
        "Código da natureza da operação/prestação",
        required=True,
        help="""Código da natureza da operação/prestação
Ver pagina 81""",
    )
    parent_0140_id = fields.Many2one(
        "l10n.br.sped.efd_pis_cofins.0140",
        string="Tabela de Cadastro de Estabelecimento",
    )


class Registro0450(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.0450"
    _description = u"""Tabela de Informação Complementar do Documento Fiscal"""
    _inherit = "l10n.br.sped.mixin"
    cod_inf = fields.Char(
        "Código da informação complementar do documento fiscal",
        required=True,
        help="""Código da informação complementar do documento fiscal.
Ver pagina 81""",
    )
    txt = fields.Char(
        "TXT",
        required=True,
        help="""Texto livre da informação complementar existente no documento  fiscal,  inclusive  espécie  de  normas  legais,  poder normativo,  número,  capitulação,  data  e  demais  referências pertinentes com indicação referentes ao tributo.
Ver pagina 81""",
    )
    parent_0140_id = fields.Many2one(
        "l10n.br.sped.efd_pis_cofins.0140",
        string="Tabela de Cadastro de Estabelecimento",
    )


class Registro0500(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.0500"
    _description = u"""Plano de Contas Contábeis – Contas Informadas"""
    _inherit = "l10n.br.sped.mixin"
    dt_alt = fields.Integer("Data da inclusão/alteração", required=True)
    cod_nat_cc = fields.Char(
        "Código da natureza da conta/grupo de contas",
        required=True,
        help="""Código da natureza da conta/grupo de contas: 01 - Contas de ativo 02 - Contas de passivo; 03 - Patrimônio líquido; 04 - Contas de resultado; 05 - Contas de compensação; 09 - Outras.
Ver pagina 83""",
    )
    ind_cta = fields.Char(
        "Indicador do tipo de conta",
        required=True,
        help="""Indicador do tipo de conta: S - Sintética (grupo de contas); A - Analítica (conta).
Ver pagina 83""",
    )
    nivel = fields.Integer("Nível da conta analítica/grupo de contas", required=True)
    cod_cta = fields.Char(
        "Código da conta analítica/grupo de contas",
        required=True,
        help="""Código da conta analítica/grupo de contas.
Ver pagina 83""",
    )
    nome_cta = fields.Char(
        "Nome da conta analítica/grupo de contas",
        required=True,
        help="""Nome da conta analítica/grupo de contas.
Ver pagina 83""",
    )
    cod_cta_ref = fields.Char(
        "COD_CTA_REF",
        help="""Código da conta correlacionada no Plano de Contas Referenciado, publicado pela RFB.
Ver pagina 83""",
    )
    cnpj_est = fields.Integer("CNPJ_EST")


class Registro0600(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.0600"
    _description = u"""Centro de Custos"""
    _inherit = "l10n.br.sped.mixin"
    dt_alt = fields.Integer("Data da inclusão/alteração.")
    cod_ccus = fields.Char(
        "C",
        help="""C
Ver pagina 84""",
    )
    ccus = fields.Char(
        "Nome do centro de custos.",
        help="""Nome do centro de custos.
Ver pagina 84""",
    )


class Registro1010(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.1010"
    _description = u"""Processo Referenciado – Ação Judicial"""
    _inherit = "l10n.br.sped.mixin"
    num_proc = fields.Char(
        "Identificação do Número do Processo Judicial",
        help="""Identificação do Número do Processo Judicial
Ver pagina 335""",
    )
    id_sec_jud = fields.Char(
        "Identificação da Seção Judiciária",
        required=True,
        help="""Identificação da Seção Judiciária
Ver pagina 335""",
    )
    id_vara = fields.Char(
        "Identificação da Vara",
        required=True,
        help="""Identificação da Vara
Ver pagina 335""",
    )
    ind_nat_acao = fields.Char(
        "IND_NAT_ACAO",
        required=True,
        help="""Indicador  da  Natureza  da  Ação  Judicial,  impetrada  na Justiça Federal: 01  –  Decisão judicial  transitada  em  julgado,  a  favor da pessoa jurídica. 02 – Decisão judicial não transitada em julgado, a favor da pessoa jurídica. 03 – Decisão judicial oriunda de liminar em mandado de segurança. 04  –  Decisão  judicial  oriunda  de  liminar  em  medida cautelar. 05 – Decisão judicial oriunda de antecipação de tutela. 06 - Decisão judicial vinculada a depósito
Ver pagina 335""",
    )
    desc_dec_jud = fields.Char(
        "C",
        help="""C
Ver pagina 336""",
    )
    dt_sent_jud = fields.Date("N")


class Registro1020(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.1020"
    _description = u"""Processo Referenciado – Processo Administrativo"""
    _inherit = "l10n.br.sped.mixin"
    num_proc = fields.Char(
        "C",
        help="""C
Ver pagina 336""",
    )
    ind_nat_acao = fields.Char(
        "IND_NAT_ACAO",
        required=True,
        help="""Indicador  da  Natureza  da  Ação,  decorrente  de  Processo Administrativo na Secretaria da Receita Federal do Brasil: 01 – Processo Administrativo de Consulta 02 – Despacho Decisório 03 – Ato Declaratório Executivo 04 – Ato Declaratório Interpretativo 05 – Decisão Administrativa de DRJ ou do CARF 06 – Auto de Infração 99 – Outros
Ver pagina 336""",
    )


class Registro1100(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.1100"
    _description = u"""Controle de Créditos Fiscais – PIS/PASEP"""
    _inherit = "l10n.br.sped.mixin"
    per_apu_cred = fields.Integer(
        "Período de Apuração do Crédito (MM/AAAA)", required=True
    )
    orig_cred = fields.Integer("Indicador da origem do crédito", required=True)
    cnpj_suc = fields.Integer(
        "CNPJ da pessoa jurídica cedente do crédito (se ORIG_CRED = 02)"
    )
    cod_cred = fields.Integer(
        "Código do Tipo do Crédito, conforme Tabela 4", required=True
    )
    vl_cred_apu = fields.Integer("VL_CRED_APU", required=True)
    vl_cred_ext_apu = fields.Integer("VL_CRED_EXT_APU")
    vl_tot_cred_apu = fields.Integer(
        "Valor Total do Crédito Apurado (06 + 07)", required=True
    )
    vl_cred_desc_pa_ant = fields.Integer("VL_CRED_DESC_PA_ANT", required=True)
    vl_cred_per_pa_ant = fields.Integer("VL_CRED_PER_PA_ANT")
    vl_cred_dcomp_pa_ant = fields.Integer("VL_CRED_DCOMP_PA_ANT")
    sd_cred_disp_efd = fields.Integer("SD_CRED_DISP_EFD", required=True)
    vl_cred_desc_efd = fields.Integer(
        "Valor do Crédito descontado neste período de escrituração"
    )
    vl_cred_per_efd = fields.Integer("VL_CRED_PER_EFD")
    vl_cred_dcomp_efd = fields.Integer("VL_CRED_DCOMP_EFD")
    vl_cred_trans = fields.Integer("VL_CRED_TRANS")
    vl_cred_out = fields.Integer("Valor do crédito utilizado por outras formas")
    sld_cred_fim = fields.Integer("SLD_CRED_FIM")
    reg_1101_ids = fields.One2many(
        "l10n.br.sped.efd_pis_cofins.1101",
        "parent_1100_id",
        string="Apuração de Crédito Extemporâneo - Documentos e Operações de Períodos Anteriores – PIS/PASEP (Para períodos de apuração até Julho de 2013)",
        help="Bloco 1",
    )


class Registro1101(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.1101"
    _description = u"""Apuração de Crédito Extemporâneo - Documentos e Operações de Períodos Anteriores – PIS/PASEP (Para períodos de apuração até Julho de 2013)"""
    _inherit = "l10n.br.sped.mixin"
    cod_part = fields.Char(
        "Código do participante (Campo 02 do Registro 0150)",
        help="""Código do participante (Campo 02 do Registro 0150)
Ver pagina 341""",
    )
    cod_item = fields.Char(
        "Código do item (campo 02 do Registro 0200)",
        help="""Código do item (campo 02 do Registro 0200)
Ver pagina 341""",
    )
    cod_mod = fields.Char(
        "Código do modelo do documento fiscal, conforme a Tabela 4",
        help="""Código do modelo do documento fiscal, conforme a Tabela 4.1.1.
Ver pagina 341""",
    )
    ser = fields.Char(
        "Série do documento fiscal",
        help="""Série do documento fiscal
Ver pagina 341""",
    )
    sub_ser = fields.Char(
        "Subsérie do documento fiscal",
        help="""Subsérie do documento fiscal
Ver pagina 341""",
    )
    num_doc = fields.Integer("Número do documento fiscal")
    dt_oper = fields.Integer("Data da Operação (ddmmaaaa)", required=True)
    chv_nfe = fields.Integer("Chave da Nota Fiscal Eletrônica")
    vl_oper = fields.Integer("Valor da Operação", required=True)
    cfop = fields.Integer("Código fiscal de operação e prestação")
    nat_bc_cred = fields.Char(
        "NAT_BC_CRED",
        required=True,
        help="""Código da Base de Cálculo do Crédito, conforme a Tabela indicada no item 4.3.7.
Ver pagina 341""",
    )
    ind_orig_cred = fields.Char(
        "Indicador da origem do crédito",
        required=True,
        help="""Indicador da origem do crédito: 0 – Operação no Mercado Interno 1 – Operação de Importação
Ver pagina 341""",
    )
    cst_pis = fields.Integer("CST_PIS", required=True)
    vl_bc_pis = fields.Integer("VL_BC_PIS", required=True)
    aliq_pis = fields.Integer(
        "Alíquota do PIS/PASEP (em percentual ou em reais)", required=True
    )
    vl_pis = fields.Integer("Valor do Crédito de PIS/PASEP.", required=True)
    cod_cta = fields.Char(
        "Código da conta analítica contábil debitada/creditada",
        help="""Código da conta analítica contábil debitada/creditada.
Ver pagina 341""",
    )
    cod_ccus = fields.Char(
        "Código do Centro de Custos.",
        help="""Código do Centro de Custos.
Ver pagina 341""",
    )
    desc_compl = fields.Char(
        "Descrição complementar do Documento/Operação",
        help="""Descrição complementar do Documento/Operação.
Ver pagina 341""",
    )
    parent_1100_id = fields.Many2one(
        "l10n.br.sped.efd_pis_cofins.1100",
        string="Controle de Créditos Fiscais – PIS/PASEP",
    )
    reg_1102_id = fields.Many2one(
        "l10n.br.sped.efd_pis_cofins.1102",
        string="Detalhamento do Crédito Extemporâneo, Vinculado a mais de um Tipo de Receita – PIS/PASEP (Para períodos de apuração até",
        help="Bloco 1",
    )  # m2o


class Registro1102(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.1102"
    _description = u"""Detalhamento do Crédito Extemporâneo, Vinculado a mais de um Tipo de Receita – PIS/PASEP (Para períodos de apuração até"""
    _inherit = "l10n.br.sped.mixin"
    vl_cred_pis_trib_mi = fields.Integer("VL_CRED_PIS_TRIB_MI")
    vl_cred_pis_nt_mi = fields.Integer("VL_CRED_PIS_NT_MI")
    vl_cred_pis_exp = fields.Integer("VL_CRED_PIS_EXP")


class RegistroM100(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.m100"
    _description = u"""Crédito de PIS/PASEP Relativo ao Período"""
    _inherit = "l10n.br.sped.mixin"
    cod_cred = fields.Char(
        "COD_CRED",
        required=True,
        help="""Código  de  Tipo  de  Crédito  apurado  no  período, conforme a Tabela 4.3.6.
Ver pagina 271""",
    )
    ind_cred_ori = fields.Integer("Indicador de Crédito Oriundo de", required=True)
    vl_bc_pis = fields.Integer("Valor da Base de Cálculo do Crédito")
    aliq_pis = fields.Monetary("Alíquota do PIS/PASEP (em percentual)", digits=4)
    reg_m105_ids = fields.One2many(
        "l10n.br.sped.efd_pis_cofins.m105",
        "parent_m100_id",
        string="Detalhamento da Base de Cálculo do Crédito Apurado no Período – PIS/PASEP",
        help="Bloco M",
    )
    reg_m110_ids = fields.One2many(
        "l10n.br.sped.efd_pis_cofins.m110",
        "parent_m100_id",
        string="Ajustes do Crédito de PIS/PASEP Apurado",
        help="Bloco M",
    )


class RegistroM105(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.m105"
    _description = (
        u"""Detalhamento da Base de Cálculo do Crédito Apurado no Período – PIS/PASEP"""
    )
    _inherit = "l10n.br.sped.mixin"
    nat_bc_cred = fields.Char(
        "NAT_BC_CRED",
        required=True,
        help="""Código  da  Base  de  Cálculo  do  Crédito  apurado  no período, conforme a Tabela 4.3.7.
Ver pagina 275""",
    )
    cst_pis = fields.Integer("CST_PIS", required=True)
    vl_bc_pis_tot = fields.Integer("VL_BC_PIS_TOT")
    parent_m100_id = fields.Many2one(
        "l10n.br.sped.efd_pis_cofins.m100",
        string="Crédito de PIS/PASEP Relativo ao Período",
    )


class RegistroM110(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.m110"
    _description = u"""Ajustes do Crédito de PIS/PASEP Apurado"""
    _inherit = "l10n.br.sped.mixin"
    ind_aj = fields.Char(
        "Indicador do tipo de ajuste",
        required=True,
        help="""Indicador do tipo de ajuste: 0- Ajuste de redução; 1- Ajuste de acréscimo.
Ver pagina 279""",
    )
    vl_aj = fields.Integer("Valor do ajuste", required=True)
    cod_aj = fields.Char(
        "Código  do  ajuste,  conforme  a  Tabela indicada  no item 4",
        required=True,
        help="""Código  do  ajuste,  conforme  a  Tabela indicada  no item 4.3.8.
Ver pagina 279""",
    )
    num_doc = fields.Char(
        "NUM_DOC",
        help="""Número  do  processo,  documento  ou  ato  concessório  ao qual o ajuste está vinculado, se houver.
Ver pagina 279""",
    )
    descr_aj = fields.Char(
        "Descrição resumida do ajuste.",
        help="""Descrição resumida do ajuste.
Ver pagina 279""",
    )
    dt_ref = fields.Integer("Data de referência do ajuste (ddmmaaaa)")
    parent_m100_id = fields.Many2one(
        "l10n.br.sped.efd_pis_cofins.m100",
        string="Crédito de PIS/PASEP Relativo ao Período",
    )
    reg_m115_ids = fields.One2many(
        "l10n.br.sped.efd_pis_cofins.m115",
        "parent_m110_id",
        string="Detalhamento dos Ajustes do Crédito de Pis/Pasep Apurado (Disponibilizado na versão 2.0.12 do PVA, para período de apuração a partir de 01/10/2015)",
        help="Bloco M",
    )


class RegistroM115(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.m115"
    _description = u"""Detalhamento dos Ajustes do Crédito de Pis/Pasep Apurado (Disponibilizado na versão 2.0.12 do PVA, para período de apuração a partir de 01/10/2015)"""
    _inherit = "l10n.br.sped.mixin"
    det_valor_aj = fields.Integer("DET_VALOR_AJ", required=True)
    cst_pis = fields.Integer("CST_PIS")
    det_bc_cred = fields.Integer(
        "Detalhamento da base de cálculo geradora de ajuste de crédito"
    )
    det_aliq = fields.Monetary(
        "Detalhamento da alíquota a que se refere o ajuste de crédito", digits=4
    )
    dt_oper_aj = fields.Integer("DT_OPER_AJ", required=True)
    desc_aj = fields.Char(
        "DESC_AJ",
        help="""Descrição da(s) operação(ões) a que se refere o valor informado no Campo 02 (DET_VALOR_AJ)
Ver pagina 280""",
    )
    cod_cta = fields.Char(
        "Código da conta contábil debitada/creditada",
        help="""Código da conta contábil debitada/creditada
Ver pagina 280""",
    )
    info_compl = fields.Char(
        "Informação complementar",
        help="""Informação complementar
Ver pagina 280""",
    )
    parent_m110_id = fields.Many2one(
        "l10n.br.sped.efd_pis_cofins.m110",
        string="Ajustes do Crédito de PIS/PASEP Apurado",
    )


class RegistroM200(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.m200"
    _description = u"""Consolidação da Contribuição para o PIS/PASEP do Período"""
    _inherit = "l10n.br.sped.mixin"
    vl_tot_cont_nc_per = fields.Integer("VL_TOT_CONT_NC_PER", required=True)
    vl_tot_cred_desc = fields.Integer("VL_TOT_CRED_DESC", required=True)
    vl_tot_cred_desc_ant = fields.Integer("VL_TOT_CRED_DESC_ANT", required=True)
    vl_tot_cont_nc_dev = fields.Integer(
        "Valor Total da Contribuição Não Cumulativa Devida (02 – 03 - 04)",
        required=True,
    )
    vl_ret_nc = fields.Integer(
        "Valor Retido na Fonte Deduzido no Período", required=True
    )
    vl_out_ded_nc = fields.Integer("Outras Deduções no Período", required=True)
    vl_cont_nc_rec = fields.Integer("VL_CONT_NC_REC", required=True)
    vl_tot_cont_cum_per = fields.Integer("VL_TOT_CONT_CUM_PER", required=True)
    vl_ret_cum = fields.Integer(
        "Valor Retido na Fonte Deduzido no Período", required=True
    )
    vl_out_ded_cum = fields.Integer("Outras Deduções no Período", required=True)
    vl_cont_cum_rec = fields.Integer(
        "Valor da Contribuição Cumulativa a Recolher/Pagar (09 - 10 – 11)",
        required=True,
    )
    vl_tot_cont_rec = fields.Integer("VL_TOT_CONT_REC", required=True)
    reg_m205_ids = fields.One2many(
        "l10n.br.sped.efd_pis_cofins.m205",
        "parent_m200_id",
        string="Contribuição para o PIS/Pasep a Recolher – Detalhamento por Código de Receita (Visão Débito DCTF)",
        help="Bloco M",
    )
    reg_m210_ids = fields.One2many(
        "l10n.br.sped.efd_pis_cofins.m210",
        "parent_m200_id",
        string="Detalhamento da Contribuição para o PIS/PASEP do Período",
        help="Bloco M",
    )


class RegistroM205(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.m205"
    _description = u"""Contribuição para o PIS/Pasep a Recolher – Detalhamento por Código de Receita (Visão Débito DCTF)"""
    _inherit = "l10n.br.sped.mixin"
    num_campo = fields.Char(
        "NUM_CAMPO",
        required=True,
        help="""Informar  o  número  do  campo  do  registro  “M200” (Campo 08 (contribuição não cumulativa) ou Campo 12 (contribuição cumulativa)), objeto de detalhamento neste registro.
Ver pagina 284""",
    )
    cod_rec = fields.Char(
        "COD_REC",
        required=True,
        help="""Informar o código da receita referente à contribuição a recolher, detalhada neste registro.
Ver pagina 284""",
    )
    vl_debito = fields.Integer("VL_DEBITO", required=True)
    parent_m200_id = fields.Many2one(
        "l10n.br.sped.efd_pis_cofins.m200",
        string="Consolidação da Contribuição para o PIS/PASEP do Período",
    )


class RegistroM210(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.m210"
    _description = u"""Detalhamento da Contribuição para o PIS/PASEP do Período"""
    _inherit = "l10n.br.sped.mixin"
    cod_cont = fields.Char(
        "COD_CONT",
        required=True,
        help="""Código da contribuição social apurada no período, conforme a Tabela 4.3.5.
Ver pagina 285""",
    )
    vl_rec_brt = fields.Integer("Valor da Receita Bruta", required=True)
    vl_bc_cont = fields.Integer(
        "Valor da Base de Cálculo da Contribuição", required=True
    )
    aliq_pis = fields.Monetary("Alíquota do PIS/PASEP (em percentual)", digits=4)
    quant_bc_pis = fields.Integer("Quantidade – Base de cálculo PIS")
    parent_m200_id = fields.Many2one(
        "l10n.br.sped.efd_pis_cofins.m200",
        string="Consolidação da Contribuição para o PIS/PASEP do Período",
    )
    reg_m211_id = fields.Many2one(
        "l10n.br.sped.efd_pis_cofins.m211",
        string="Sociedades Cooperativas – Composição da Base de Cálculo – PIS/PASEP",
        help="Bloco M",
    )  # m2o
    reg_m220_ids = fields.One2many(
        "l10n.br.sped.efd_pis_cofins.m220",
        "parent_m210_id",
        string="Ajustes da Contribuição para o PIS/PASEP Apurada",
        help="Bloco M",
    )
    reg_m230_ids = fields.One2many(
        "l10n.br.sped.efd_pis_cofins.m230",
        "parent_m210_id",
        string="Informações Adicionais de Diferimento",
        help="Bloco M",
    )


class RegistroM211(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.m211"
    _description = (
        u"""Sociedades Cooperativas – Composição da Base de Cálculo – PIS/PASEP"""
    )
    _inherit = "l10n.br.sped.mixin"
    ind_tip_coop = fields.Integer(
        "Indicador do Tipo de Sociedade Cooperativa", required=True
    )
    vl_bc_cont_ant_exc_coop = fields.Integer("VL_BC_CONT_ANT_EXC_COOP", required=True)
    vl_exc_coop_ger = fields.Integer("VL_EXC_COOP_GER")
    vl_exc_esp_coop = fields.Integer("VL_EXC_ESP_COOP")
    vl_bc_cont = fields.Integer("VL_BC_CONT", required=True)


class RegistroM220(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.m220"
    _description = u"""Ajustes da Contribuição para o PIS/PASEP Apurada"""
    _inherit = "l10n.br.sped.mixin"
    ind_aj = fields.Char(
        "Indicador do tipo de ajuste",
        required=True,
        help="""Indicador do tipo de ajuste: 0- Ajuste de redução; 1- Ajuste de acréscimo.
Ver pagina 290""",
    )
    vl_aj = fields.Integer("Valor do ajuste", required=True)
    cod_aj = fields.Char(
        "Código  do  ajuste,  conforme  a  Tabela indicada  no item 4",
        required=True,
        help="""Código  do  ajuste,  conforme  a  Tabela indicada  no item 4.3.8.
Ver pagina 290""",
    )
    num_doc = fields.Char(
        "NUM_DOC",
        help="""Número  do  processo,  documento  ou  ato  concessório  ao qual o ajuste está vinculado, se houver.
Ver pagina 290""",
    )
    descr_aj = fields.Char(
        "Descrição resumida do ajuste.",
        help="""Descrição resumida do ajuste.
Ver pagina 290""",
    )
    dt_ref = fields.Integer("Data de referência do ajuste (ddmmaaaa)")
    parent_m210_id = fields.Many2one(
        "l10n.br.sped.efd_pis_cofins.m210",
        string="Detalhamento da Contribuição para o PIS/PASEP do Período",
    )
    reg_m225_ids = fields.One2many(
        "l10n.br.sped.efd_pis_cofins.m225",
        "parent_m220_id",
        string="Detalhamento dos Ajustes da Contribuição para o PIS/Pasep Apurada (Disponibilizado na versão 2.0.12 do PVA, para período de apuração a partir de 01/10/2015)",
        help="Bloco M",
    )


class RegistroM225(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.m225"
    _description = u"""Detalhamento dos Ajustes da Contribuição para o PIS/Pasep Apurada (Disponibilizado na versão 2.0.12 do PVA, para período de apuração a partir de 01/10/2015)"""
    _inherit = "l10n.br.sped.mixin"
    det_valor_aj = fields.Integer("DET_VALOR_AJ", required=True)
    cst_pis = fields.Integer("CST_PIS")
    det_bc_cred = fields.Integer("DET_BC_CRED")
    det_aliq = fields.Monetary("DET_ALIQ", digits=4)
    dt_oper_aj = fields.Integer("DT_OPER_AJ", required=True)
    desc_aj = fields.Char(
        "DESC_AJ",
        help="""Descrição da(s) operação(ões) a que se refere o valor informado no Campo 02 (DET_VALOR_AJ)
Ver pagina 291""",
    )
    cod_cta = fields.Char(
        "Código da conta contábil debitada/creditada",
        help="""Código da conta contábil debitada/creditada
Ver pagina 291""",
    )
    info_compl = fields.Char(
        "Informação complementar",
        help="""Informação complementar
Ver pagina 291""",
    )
    parent_m220_id = fields.Many2one(
        "l10n.br.sped.efd_pis_cofins.m220",
        string="Ajustes da Contribuição para o PIS/PASEP Apurada",
    )


class RegistroM230(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.m230"
    _description = u"""Informações Adicionais de Diferimento"""
    _inherit = "l10n.br.sped.mixin"
    cnpj = fields.Integer("CNPJ", required=True)
    vl_vend = fields.Integer("Valor Total das vendas no período", required=True)
    parent_m210_id = fields.Many2one(
        "l10n.br.sped.efd_pis_cofins.m210",
        string="Detalhamento da Contribuição para o PIS/PASEP do Período",
    )


class RegistroM300(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.m300"
    _description = u"""Contribuição de PIS/PASEP Diferida em Períodos Anteriores - Valores a Pagar no Período"""
    _inherit = "l10n.br.sped.mixin"
    cod_cont = fields.Char(
        "COD_CONT",
        required=True,
        help="""Código da contribuição social diferida em períodos anteriores, conforme a Tabela 4.3.5.
Ver pagina 293""",
    )
    vl_cont_apur_difer = fields.Integer(
        "Valor da Contribuição Apurada, diferida em períodos anteriores", required=True
    )
    nat_cred_desc = fields.Char(
        "NAT_CRED_DESC",
        help="""Natureza do Crédito Diferido, vinculado à receita tributada no mercado interno, a descontar: 01 – Crédito a Alíquota Básica; 02 – Crédito a Alíquota Diferenciada; 03 – Crédito a Alíquota por Unidade de Produto; 04 – Crédito Presumido da Agroindústria.
Ver pagina 293""",
    )
    vl_cred_desc_difer = fields.Integer(
        "Valor do Crédito a Descontar vinculado à contribuição diferida"
    )
    vl_cont_difer_ant = fields.Integer("VL_CONT_DIFER_ANT", required=True)
    per_apur = fields.Integer("PER_APUR", required=True)
    dt_receb = fields.Integer("Data de recebimento da receita, objeto de diferimento")


class RegistroM350(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.m350"
    _description = u"""PIS/PASEP - Folha de Salários"""
    _inherit = "l10n.br.sped.mixin"
    vl_tot_fol = fields.Integer("Valor Total da Folha de Salários", required=True)
    vl_exc_bc = fields.Integer(
        "Valor Total das Exclusões à Base de Cálculo", required=True
    )
    vl_tot_bc = fields.Integer("Valor Total da Base de Cálculo", required=True)
    aliq_pis_fol = fields.Monetary(
        "Alíquota do PIS/PASEP – Folha de Salários", required=True, digits=2
    )
    vl_tot_cont_fol = fields.Integer(
        "Valor Total da Contribuição Social sobre a Folha de Salários", required=True
    )


class RegistroM400(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.m400"
    _description = u"""Receitas Isentas, Não Alcançadas pela Incidência da Contribuição, Sujeitas à Alíquota Zero ou de Vendas com Suspensão – PIS/PASEP"""
    _inherit = "l10n.br.sped.mixin"
    cst_pis = fields.Char(
        "CST_PIS",
        required=True,
        help="""Código  de  Situação  Tributária  –  CST  das  demais receitas auferidas  no  período, sem incidência  da contribuição,  ou  sem  contribuição  apurada  a  pagar, conforme a Tabela 4.3.3.
Ver pagina 295""",
    )
    vl_tot_rec = fields.Integer(
        "Valor total da receita bruta no período", required=True
    )
    cod_cta = fields.Char(
        "Código da conta analítica contábil debitada/creditada",
        help="""Código da conta analítica contábil debitada/creditada.
Ver pagina 295""",
    )
    desc_compl = fields.Char(
        "Descrição Complementar da Natureza da Receita",
        help="""Descrição Complementar da Natureza da Receita.
Ver pagina 295""",
    )
    reg_m410_ids = fields.One2many(
        "l10n.br.sped.efd_pis_cofins.m410",
        "parent_m400_id",
        string="Detalhamento das Receitas Isentas, Não Alcançadas pela Incidência da Contribuição, Sujeitas à Alíquota Zero ou de Vendas com Suspensão – PIS/PASEP",
        help="Bloco M",
    )


class RegistroM410(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.m410"
    _description = u"""Detalhamento das Receitas Isentas, Não Alcançadas pela Incidência da Contribuição, Sujeitas à Alíquota Zero ou de Vendas com Suspensão – PIS/PASEP"""
    _inherit = "l10n.br.sped.mixin"
    nat_rec = fields.Char(
        "NAT_REC",
        required=True,
        help="""Natureza da Receita, conforme relação constante nas Tabelas de Detalhamento da Natureza da Receita por Situação Tributária abaixo: -  Tabela  4.3.10:  Produtos  Sujeitos à Incidência Monofásica  da  Contribuição  Social  –  Alíquotas Diferenciadas (CST 04 - Revenda); -  Tabela  4.3.11:  Produtos  Sujeitos à Incidência Monofásica  da  Contribuição  Social  – Alíquotas  por Unidade de Medida de Produto (CST 04 - Revenda); -  Tabela  4.3.12:  Produtos  Sujeitos  à  Substituição Tributária da  Contribuição Social (CST 05 - Revenda);
Ver pagina 296""",
    )
    vl_rec = fields.Integer("VL_REC", required=True)
    cod_cta = fields.Char(
        "Código da conta analítica contábil debitada/creditada",
        help="""Código da conta analítica contábil debitada/creditada.
Ver pagina 297""",
    )
    desc_compl = fields.Char(
        "Descrição Complementar da Natureza da Receita",
        help="""Descrição Complementar da Natureza da Receita.
Ver pagina 297""",
    )
    parent_m400_id = fields.Many2one(
        "l10n.br.sped.efd_pis_cofins.m400",
        string="Receitas Isentas, Não Alcançadas pela Incidência da Contribuição, Sujeitas à Alíquota Zero ou de Vendas com Suspensão – PIS/PASEP",
    )


class RegistroM500(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.m500"
    _description = u"""Crédito de COFINS Relativo ao Período"""
    _inherit = "l10n.br.sped.mixin"
    cod_cred = fields.Char(
        "COD_CRED",
        required=True,
        help="""Código de  Tipo de  Crédito apurado no período, conforme a Tabela 4.3.6.
Ver pagina 298""",
    )
    ind_cred_ori = fields.Integer("Indicador de Crédito Oriundo de", required=True)
    vl_bc_cofins = fields.Integer("Valor da Base de Cálculo do Crédito")
    aliq_cofins = fields.Monetary("Alíquota da COFINS (em percentual)", digits=4)
    quant_bc_cofins = fields.Integer("Quantidade – Base de cálculo COFINS")
    aliq_cofins_quant = fields.Integer("Alíquota da COFINS (em reais)")
    vl_cred = fields.Integer("Valor total do crédito apurado no período", required=True)
    vl_ajus_acres = fields.Integer(
        "Valor total dos ajustes de acréscimo", required=True
    )
    vl_ajus_reduc = fields.Integer("Valor total dos ajustes de redução", required=True)
    vl_cred_difer = fields.Integer(
        "Valor total do crédito diferido no período", required=True
    )
    vl_cred_disp = fields.Integer("VL_CRED_DISP", required=True)
    ind_desc_cred = fields.Char(
        "Indicador  de  utilização  do  crédito  disponível no período",
        required=True,
        help="""Indicador  de  utilização  do  crédito  disponível no período: 0  –  Utilização  do  valor total  para  desconto  da contribuição  apurada  no  período,  no  Registro M600; 1  –  Utilização  de  valor  parcial  para  desconto da contribuição apurada no período, no Registro M600.
Ver pagina 299""",
    )
    vl_cred_desc = fields.Integer("VL_CRED_DESC")
    sld_cred = fields.Integer(
        "Saldo de créditos a utilizar em períodos futuros (12 – 14)", required=True
    )
    reg_m505_ids = fields.One2many(
        "l10n.br.sped.efd_pis_cofins.m505",
        "parent_m500_id",
        string="Detalhamento da Base de Cálculo do Crédito Apurado no Período – COFINS",
        help="Bloco M",
    )
    reg_m510_ids = fields.One2many(
        "l10n.br.sped.efd_pis_cofins.m510",
        "parent_m500_id",
        string="Ajustes do Crédito de COFINS Apurado",
        help="Bloco M",
    )


class RegistroM505(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.m505"
    _description = (
        u"""Detalhamento da Base de Cálculo do Crédito Apurado no Período – COFINS"""
    )
    _inherit = "l10n.br.sped.mixin"
    nat_bc_cred = fields.Char(
        "NAT_BC_CRED",
        required=True,
        help="""Código  da  Base  de  Cálculo  do  Crédito  apurado  no período, conforme a Tabela 4.3.7.
Ver pagina 302""",
    )
    cst_cofins = fields.Integer("CST_COFINS", required=True)
    vl_bc_cofins_tot = fields.Integer("VL_BC_COFINS_TOT")
    vl_bc_cofins_cum = fields.Integer("VL_BC_COFINS_CUM")
    vl_bc_cofins_nc = fields.Integer("VL_BC_COFINS_NC")
    vl_bc_cofins = fields.Integer("VL_BC_COFINS")
    quant_bc_cofins_tot = fields.Integer("QUANT_BC_COFINS_TOT")
    quant_bc_cofins = fields.Integer("QUANT_BC_COFINS")
    desc_cred = fields.Char(
        "Descrição do crédito",
        help="""Descrição do crédito
Ver pagina 303""",
    )
    parent_m500_id = fields.Many2one(
        "l10n.br.sped.efd_pis_cofins.m500",
        string="Crédito de COFINS Relativo ao Período",
    )


class RegistroM510(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.m510"
    _description = u"""Ajustes do Crédito de COFINS Apurado"""
    _inherit = "l10n.br.sped.mixin"
    ind_aj = fields.Char(
        "Indicador do tipo de ajuste",
        required=True,
        help="""Indicador do tipo de ajuste: 0- Ajuste de redução; 1- Ajuste de acréscimo.
Ver pagina 306""",
    )
    vl_aj = fields.Integer("Valor do ajuste", required=True)
    cod_aj = fields.Char(
        "Código  do  ajuste,  conforme  a  Tabela indicada  no item 4",
        required=True,
        help="""Código  do  ajuste,  conforme  a  Tabela indicada  no item 4.3.8.
Ver pagina 306""",
    )
    num_doc = fields.Char(
        "NUM_DOC",
        help="""Número  do  processo,  documento  ou  ato  concessório  ao qual o ajuste está vinculado, se houver.
Ver pagina 306""",
    )
    descr_aj = fields.Char(
        "Descrição resumida do ajuste.",
        help="""Descrição resumida do ajuste.
Ver pagina 306""",
    )
    dt_ref = fields.Integer("Data de referência do ajuste (ddmmaaaa)")
    parent_m500_id = fields.Many2one(
        "l10n.br.sped.efd_pis_cofins.m500",
        string="Crédito de COFINS Relativo ao Período",
    )
    reg_m515_ids = fields.One2many(
        "l10n.br.sped.efd_pis_cofins.m515",
        "parent_m510_id",
        string="Detalhamento dos Ajustes do Crédito de Cofins Apurado (Disponibilizado na versão 2.0.12 do PVA, para período de apuração a partir de 01/10/2015)",
        help="Bloco M",
    )


class RegistroM515(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.m515"
    _description = u"""Detalhamento dos Ajustes do Crédito de Cofins Apurado (Disponibilizado na versão 2.0.12 do PVA, para período de apuração a partir de 01/10/2015)"""
    _inherit = "l10n.br.sped.mixin"
    det_valor_aj = fields.Integer("DET_VALOR_AJ", required=True)
    cst_cofins = fields.Integer("CST_COFINS")
    det_bc_cred = fields.Integer(
        "Detalhamento da base de cálculo geradora de ajuste de crédito"
    )
    det_aliq = fields.Monetary(
        "Detalhamento da alíquota a que se refere o ajuste de crédito", digits=4
    )
    dt_oper_aj = fields.Integer("DT_OPER_AJ", required=True)
    desc_aj = fields.Char(
        "DESC_AJ",
        help="""Descrição da(s) operação(ões) a que se refere o valor informado no Campo 02 (DET_VALOR_AJ)
Ver pagina 307""",
    )
    cod_cta = fields.Char(
        "Código da conta contábil debitada/creditada",
        help="""Código da conta contábil debitada/creditada
Ver pagina 307""",
    )
    info_compl = fields.Char(
        "Informação complementar",
        help="""Informação complementar
Ver pagina 307""",
    )
    parent_m510_id = fields.Many2one(
        "l10n.br.sped.efd_pis_cofins.m510",
        string="Ajustes do Crédito de COFINS Apurado",
    )


class RegistroM600(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.m600"
    _description = (
        u"""Consolidação da Contribuição para a Seguridade Social - COFINS do Período"""
    )
    _inherit = "l10n.br.sped.mixin"
    vl_tot_cont_nc_per = fields.Integer("VL_TOT_CONT_NC_PER", required=True)
    vl_tot_cred_desc = fields.Integer("VL_TOT_CRED_DESC", required=True)
    vl_tot_cred_desc_ant = fields.Integer("VL_TOT_CRED_DESC_ANT", required=True)
    vl_tot_cont_nc_dev = fields.Integer(
        "Valor Total da Contribuição Não Cumulativa Devida (02 - 03 - 04)",
        required=True,
    )
    vl_ret_nc = fields.Integer(
        "Valor Retido na Fonte Deduzido no Período", required=True
    )
    vl_out_ded_nc = fields.Integer("Outras Deduções no Período", required=True)
    vl_cont_nc_rec = fields.Integer("VL_CONT_NC_REC", required=True)
    vl_tot_cont_cum_per = fields.Integer("VL_TOT_CONT_CUM_PER", required=True)
    vl_ret_cum = fields.Integer(
        "Valor Retido na Fonte Deduzido no Período", required=True
    )
    vl_out_ded_cum = fields.Integer("Outras Deduções no Período", required=True)
    vl_cont_cum_rec = fields.Integer(
        "Valor da Contribuição Cumulativa a Recolher/Pagar (09 - 10 - 11)",
        required=True,
    )
    vl_tot_cont_rec = fields.Integer("VL_TOT_CONT_REC", required=True)
    reg_m605_ids = fields.One2many(
        "l10n.br.sped.efd_pis_cofins.m605",
        "parent_m600_id",
        string="Contribuição para a Seguridade Social - COFINS a Recolher – Detalhamento por Código de Receita (Visão Débito DCTF)",
        help="Bloco M",
    )
    reg_m610_ids = fields.One2many(
        "l10n.br.sped.efd_pis_cofins.m610",
        "parent_m600_id",
        string="Detalhamento da Contribuição para a Seguridade Social - COFINS do Período",
        help="Bloco M",
    )


class RegistroM605(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.m605"
    _description = u"""Contribuição para a Seguridade Social - COFINS a Recolher – Detalhamento por Código de Receita (Visão Débito DCTF)"""
    _inherit = "l10n.br.sped.mixin"
    num_campo = fields.Char(
        "NUM_CAMPO",
        required=True,
        help="""Informar  o  número  do  campo  do  registro  “M600” (Campo 08 (contribuição não cumulativa) ou Campo 12 (contribuição cumulativa)), objeto de detalhamento neste registro.
Ver pagina 311""",
    )
    cod_rec = fields.Char(
        "COD_REC",
        required=True,
        help="""Informar o código da receita referente à contribuição a recolher, detalhada neste registro.
Ver pagina 311""",
    )
    vl_debito = fields.Integer("VL_DEBITO", required=True)
    parent_m600_id = fields.Many2one(
        "l10n.br.sped.efd_pis_cofins.m600",
        string="Consolidação da Contribuição para a Seguridade Social - COFINS do Período",
    )


class RegistroM610(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.m610"
    _description = (
        u"""Detalhamento da Contribuição para a Seguridade Social - COFINS do Período"""
    )
    _inherit = "l10n.br.sped.mixin"
    cod_cont = fields.Char(
        "COD_CONT",
        required=True,
        help="""Código  da  contribuição  social  apurada  no  período, conforme a Tabela 4.3.5.
Ver pagina 313""",
    )
    vl_rec_brt = fields.Integer("Valor da Receita Bruta", required=True)
    vl_bc_cont = fields.Integer(
        "Valor da Base de Cálculo da Contribuição", required=True
    )
    aliq_cofins = fields.Monetary("Alíquota do COFINS (em percentual)", digits=4)
    quant_bc_cofins = fields.Integer("Quantidade – Base de cálculo COFINS")
    aliq_cofins_quant = fields.Integer("Alíquota do COFINS (em reais)")
    vl_cont_apur = fields.Integer(
        "Valor total da contribuição social apurada", required=True
    )
    vl_ajus_acres = fields.Integer(
        "Valor total dos ajustes de acréscimo", required=True
    )
    vl_ajus_reduc = fields.Integer("Valor total dos ajustes de redução", required=True)
    vl_cont_difer = fields.Integer("Valor da contribuição a diferir no período")
    vl_cont_difer_ant = fields.Integer(
        "Valor da contribuição diferida em períodos anteriores"
    )
    vl_cont_per = fields.Integer("VL_CONT_PER", required=True)
    parent_m600_id = fields.Many2one(
        "l10n.br.sped.efd_pis_cofins.m600",
        string="Consolidação da Contribuição para a Seguridade Social - COFINS do Período",
    )
    reg_m611_id = fields.Many2one(
        "l10n.br.sped.efd_pis_cofins.m611",
        string="Sociedades Cooperativas – Composição da Base de Cálculo – COFINS",
        help="Bloco M",
    )  # m2o
    reg_m620_ids = fields.One2many(
        "l10n.br.sped.efd_pis_cofins.m620",
        "parent_m610_id",
        string="Ajustes da COFINS Apurada",
        help="Bloco M",
    )
    reg_m630_ids = fields.One2many(
        "l10n.br.sped.efd_pis_cofins.m630",
        "parent_m610_id",
        string="Informações Adicionais de Diferimento",
        help="Bloco M",
    )


class RegistroM611(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.m611"
    _description = (
        u"""Sociedades Cooperativas – Composição da Base de Cálculo – COFINS"""
    )
    _inherit = "l10n.br.sped.mixin"
    ind_tip_coop = fields.Integer(
        "Indicador do Tipo de Sociedade Cooperativa", required=True
    )
    vl_bc_cont_ant_exc_coop = fields.Integer("VL_BC_CONT_ANT_EXC_COOP", required=True)
    vl_exc_coop_ger = fields.Integer("VL_EXC_COOP_GER")
    vl_exc_esp_coop = fields.Integer("VL_EXC_ESP_COOP")
    vl_bc_cont = fields.Integer("VL_BC_CONT", required=True)


class RegistroM620(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.m620"
    _description = u"""Ajustes da COFINS Apurada"""
    _inherit = "l10n.br.sped.mixin"
    ind_aj = fields.Char(
        "Indicador do tipo de ajuste",
        required=True,
        help="""Indicador do tipo de ajuste: 0- Ajuste de redução; 1- Ajuste de acréscimo.
Ver pagina 318""",
    )
    vl_aj = fields.Integer("Valor do ajuste", required=True)
    cod_aj = fields.Char(
        "Código  do  ajuste,  conforme  a  Tabela indicada  no item 4",
        required=True,
        help="""Código  do  ajuste,  conforme  a  Tabela indicada  no item 4.3.8.
Ver pagina 318""",
    )
    num_doc = fields.Char(
        "NUM_DOC",
        help="""Número  do  processo,  documento  ou  ato  concessório  ao qual o ajuste está vinculado, se houver.
Ver pagina 318""",
    )
    descr_aj = fields.Char(
        "Descrição resumida do ajuste.",
        help="""Descrição resumida do ajuste.
Ver pagina 318""",
    )
    dt_ref = fields.Integer("Data de referência do ajuste (ddmmaaaa)")
    parent_m610_id = fields.Many2one(
        "l10n.br.sped.efd_pis_cofins.m610",
        string="Detalhamento da Contribuição para a Seguridade Social - COFINS do Período",
    )
    reg_m625_ids = fields.One2many(
        "l10n.br.sped.efd_pis_cofins.m625",
        "parent_m620_id",
        string="Detalhamento dos Ajustes da Cofins Apurada (Disponibilizado na versão 2.0.12 do PVA, para período de apuração a partir de 01/10/2015)",
        help="Bloco M",
    )


class RegistroM625(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.m625"
    _description = u"""Detalhamento dos Ajustes da Cofins Apurada (Disponibilizado na versão 2.0.12 do PVA, para período de apuração a partir de 01/10/2015)"""
    _inherit = "l10n.br.sped.mixin"
    det_valor_aj = fields.Integer("DET_VALOR_AJ", required=True)
    cst_cofins = fields.Integer("CST_COFINS")
    det_bc_cred = fields.Integer("DET_BC_CRED")
    det_aliq = fields.Monetary("DET_ALIQ", digits=4)
    dt_oper_aj = fields.Integer("DT_OPER_AJ", required=True)
    desc_aj = fields.Char(
        "DESC_AJ",
        help="""Descrição da(s) operação(ões) a que se refere o valor informado no Campo 02 (DET_VALOR_AJ)
Ver pagina 319""",
    )
    cod_cta = fields.Char(
        "Código da conta contábil debitada/creditada",
        help="""Código da conta contábil debitada/creditada
Ver pagina 319""",
    )
    info_compl = fields.Char(
        "Informação complementar",
        help="""Informação complementar
Ver pagina 319""",
    )
    parent_m620_id = fields.Many2one(
        "l10n.br.sped.efd_pis_cofins.m620", string="Ajustes da COFINS Apurada"
    )


class RegistroM630(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.m630"
    _description = u"""Informações Adicionais de Diferimento"""
    _inherit = "l10n.br.sped.mixin"
    cnpj = fields.Integer("CNPJ", required=True)
    vl_vend = fields.Integer("Valor Total das vendas no período", required=True)
    parent_m610_id = fields.Many2one(
        "l10n.br.sped.efd_pis_cofins.m610",
        string="Detalhamento da Contribuição para a Seguridade Social - COFINS do Período",
    )


class RegistroM700(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.m700"
    _description = (
        u"""COFINS Diferida em Períodos Anteriores – Valores a Pagar no Período"""
    )
    _inherit = "l10n.br.sped.mixin"
    cod_cont = fields.Char(
        "COD_CONT",
        required=True,
        help="""Código da contribuição social diferida em períodos anteriores, conforme a Tabela 4.3.5.
Ver pagina 321""",
    )
    vl_cont_apur_difer = fields.Integer(
        "Valor da Contribuição Apurada, diferida em períodos anteriores", required=True
    )
    nat_cred_desc = fields.Char(
        "NAT_CRED_DESC",
        help="""Natureza do Crédito Diferido, vinculado à receita tributada no mercado interno, a descontar: 01 – Crédito a Alíquota Básica; 02 – Crédito a Alíquota Diferenciada; 03 – Crédito a Alíquota por Unidade de Produto; 04 – Crédito Presumido da Agroindústria.
Ver pagina 321""",
    )
    vl_cred_desc_difer = fields.Integer(
        "Valor do Crédito a Descontar vinculado à contribuição diferida"
    )
    vl_cont_difer_ant = fields.Integer("VL_CONT_DIFER_ANT", required=True)
    per_apur = fields.Integer("PER_APUR", required=True)
    dt_receb = fields.Integer("Data de recebimento da receita, objeto de diferimento")


class RegistroM800(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.m800"
    _description = u"""Receitas Isentas, Não Alcançadas pela Incidência da Contribuição, Sujeitas à Alíquota Zero ou de Vendas com Suspensão – COFINS"""
    _inherit = "l10n.br.sped.mixin"
    cst_cofins = fields.Char(
        "CST_COFINS",
        required=True,
        help="""Código  de  Situação  Tributária  –  CST  das  demais receitas auferidas  no  período, sem incidência  da contribuição,  ou  sem  contribuição  apurada  a  pagar, conforme a Tabela 4.3.4.
Ver pagina 322""",
    )
    vl_tot_rec = fields.Integer(
        "Valor total da receita bruta no período", required=True
    )
    cod_cta = fields.Char(
        "Código da conta analítica contábil debitada/creditada",
        help="""Código da conta analítica contábil debitada/creditada.
Ver pagina 322""",
    )
    desc_compl = fields.Char(
        "Descrição Complementar da Natureza da Receita",
        help="""Descrição Complementar da Natureza da Receita.
Ver pagina 322""",
    )
    reg_m810_ids = fields.One2many(
        "l10n.br.sped.efd_pis_cofins.m810",
        "parent_m800_id",
        string="Detalhamento das Receitas Isentas, Não Alcançadas pela Incidência da Contribuição, Sujeitas à Alíquota Zero ou de Vendas com Suspensão – COFINS",
        help="Bloco M",
    )


class RegistroM810(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.m810"
    _description = u"""Detalhamento das Receitas Isentas, Não Alcançadas pela Incidência da Contribuição, Sujeitas à Alíquota Zero ou de Vendas com Suspensão – COFINS"""
    _inherit = "l10n.br.sped.mixin"
    nat_rec = fields.Char(
        "NAT_REC",
        required=True,
        help="""Natureza da Receita, conforme relação constante nas Tabelas de Detalhamento da Natureza da Receita por Situação Tributária abaixo: -  Tabela  4.3.10:  Produtos  Sujeitos à Incidência Monofásica  da  Contribuição  Social  –  Alíquotas Diferenciadas (CST 04 - Revenda); -  Tabela  4.3.11:  Produtos  Sujeitos à Incidência Monofásica  da  Contribuição  Social  – Alíquotas  por Unidade de Medida de Produto (CST 04 - Revenda); -  Tabela  4.3.12:  Produtos  Sujeitos  à  Substituição Tributária da  Contribuição Social (CST 05 - Revenda); - Tabela 4.3.13: Produtos Sujeitos à Alíquota Zero da Contribuição Social (CST 06);
Ver pagina 323""",
    )
    vl_rec = fields.Integer("VL_REC", required=True)
    cod_cta = fields.Char(
        "Código da conta analítica contábil debitada/creditada",
        help="""Código da conta analítica contábil debitada/creditada.
Ver pagina 324""",
    )
    desc_compl = fields.Char(
        "Descrição Complementar da Natureza da Receita",
        help="""Descrição Complementar da Natureza da Receita.
Ver pagina 324""",
    )
    parent_m800_id = fields.Many2one(
        "l10n.br.sped.efd_pis_cofins.m800",
        string="Receitas Isentas, Não Alcançadas pela Incidência da Contribuição, Sujeitas à Alíquota Zero ou de Vendas com Suspensão – COFINS",
    )


class RegistroP010(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.p010"
    _description = u"""Identificação do Estabelecimento"""
    _inherit = "l10n.br.sped.mixin"
    cnpj = fields.Integer(
        "Número de inscrição do estabelecimento no CNPJ", required=True
    )
    reg_p100_ids = fields.One2many(
        "l10n.br.sped.efd_pis_cofins.p100",
        "parent_p010_id",
        string="Contribuição Previdenciária sobre a Receita Bruta",
        help="Bloco P",
    )


class RegistroP100(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.p100"
    _description = u"""Contribuição Previdenciária sobre a Receita Bruta"""
    _inherit = "l10n.br.sped.mixin"
    dt_ini = fields.Char(
        "Data inicial a que a apuração se refere",
        required=True,
        help="""Data inicial a que a apuração se refere
Ver pagina 329""",
    )
    dt_fin = fields.Char(
        "Data final a que a apuração se refere",
        required=True,
        help="""Data final a que a apuração se refere
Ver pagina 329""",
    )
    vl_rec_tot_est = fields.Integer(
        "Valor da Receita Bruta Total do Estabelecimento no Período", required=True
    )
    cod_ativ_econ = fields.Char(
        "COD_ATIV_ECON",
        required=True,
        help="""Código indicador correspondente à atividade sujeita a incidência da Contribuição Previdenciária sobre a Receita Bruta, conforme Tabela 5.1.1.
Ver pagina 329""",
    )
    vl_rec_ativ_estab = fields.Integer("VL_REC_ATIV_ESTAB", required=True)
    vl_exc = fields.Integer(
        "Valor das Exclusões da Receita Bruta informada no Campo 06"
    )
    vl_bc_cont = fields.Integer("VL_BC_CONT", required=True)
    aliq_cont = fields.Monetary(
        "Alíquota da Contribuição Previdenciária sobre a Receita B ruta",
        required=True,
        digits=4,
    )
    vl_cont_apu = fields.Integer("VL_CONT_APU", required=True)
    cod_cta = fields.Char(
        "COD_CTA",
        help="""Código da conta analítica contábil referente à Contribuição Previdenciária sobre a Receita Bruta
Ver pagina 329""",
    )
    info_compl = fields.Char(
        "Informação complementar do registro",
        help="""Informação complementar do registro
Ver pagina 329""",
    )
    parent_p010_id = fields.Many2one(
        "l10n.br.sped.efd_pis_cofins.p010", string="Identificação do Estabelecimento"
    )
    reg_p110_ids = fields.One2many(
        "l10n.br.sped.efd_pis_cofins.p110",
        "parent_p100_id",
        string="Complemento da Escrituração – Detalhamento da Apuração da Contribuição",
        help="Bloco P",
    )
    reg_p199_ids = fields.One2many(
        "l10n.br.sped.efd_pis_cofins.p199",
        "parent_p100_id",
        string="Processo Referenciado",
        help="Bloco P",
    )


class RegistroP110(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.p110"
    _description = (
        u"""Complemento da Escrituração – Detalhamento da Apuração da Contribuição"""
    )
    _inherit = "l10n.br.sped.mixin"
    num_campo = fields.Char(
        "NUM_CAMPO",
        required=True,
        help="""Informar  o  número  do  campo  do registro “P100”, objeto de detalhamento neste registro.
Ver pagina 331""",
    )
    cod_det = fields.Char(
        "Código  do tipo  de  detalhamento,  conforme Tabela 5",
        help="""Código  do tipo  de  detalhamento,  conforme Tabela 5.1.2
Ver pagina 331""",
    )
    parent_p100_id = fields.Many2one(
        "l10n.br.sped.efd_pis_cofins.p100",
        string="Contribuição Previdenciária sobre a Receita Bruta",
    )


class RegistroP199(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.p199"
    _description = u"""Processo Referenciado"""
    _inherit = "l10n.br.sped.mixin"
    num_proc = fields.Char(
        "Identificação do processo ou ato concessório",
        required=True,
        help="""Identificação do processo ou ato concessório
Ver pagina 331""",
    )
    ind_proc = fields.Char(
        "Indicador da origem do processo",
        required=True,
        help="""Indicador da origem do processo: 1 - Justiça Federal; 3 – Secretaria da Receita Federal do Brasil 9 – Outros.
Ver pagina 332""",
    )
    parent_p100_id = fields.Many2one(
        "l10n.br.sped.efd_pis_cofins.p100",
        string="Contribuição Previdenciária sobre a Receita Bruta",
    )


class RegistroP200(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.p200"
    _description = (
        u"""Consolidação da Contribuição Previdenciária sobre a Receita Bruta"""
    )
    _inherit = "l10n.br.sped.mixin"
    per_ref = fields.Integer(
        "Período de referencia da escrituração (MMAAAA)", required=True
    )
    vl_tot_cont_apu = fields.Integer("VL_TOT_CONT_APU", required=True)
    vl_tot_aj_reduc = fields.Integer("VL_TOT_AJ_REDUC")
    vl_tot_aj_acres = fields.Integer("VL_TOT_AJ_ACRES")
    vl_tot_cont_dev = fields.Integer("VL_TOT_CONT_DEV", required=True)
    cod_rec = fields.Char(
        "COD_REC",
        required=True,
        help="""Código de Receita referente à Contribuição Previdenciária, conforme informado em DCTF
Ver pagina 332""",
    )
    reg_p210_ids = fields.One2many(
        "l10n.br.sped.efd_pis_cofins.p210",
        "parent_p200_id",
        string="Ajuste da Contribuição Previdenciária Apurada sobre a Receita Bruta",
        help="Bloco P",
    )


class RegistroP210(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.p210"
    _description = (
        u"""Ajuste da Contribuição Previdenciária Apurada sobre a Receita Bruta"""
    )
    _inherit = "l10n.br.sped.mixin"
    ind_aj = fields.Char(
        "Indicador do tipo de ajuste",
        required=True,
        help="""Indicador do tipo de ajuste: 0- Ajuste de redução; 1- Ajuste de acréscimo.
Ver pagina 333""",
    )
    vl_aj = fields.Integer("Valor do ajuste", required=True)
    cod_aj = fields.Char(
        "Código  do  ajuste,  conforme  a  Tabela indicada  no item 4",
        required=True,
        help="""Código  do  ajuste,  conforme  a  Tabela indicada  no item 4.3.8., versão 1.01
Ver pagina 333""",
    )
    parent_p200_id = fields.Many2one(
        "l10n.br.sped.efd_pis_cofins.p200",
        string="Consolidação da Contribuição Previdenciária sobre a Receita Bruta",
    )


class Registro9900(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.9900"
    _description = u"""Registros do Arquivo"""
    _inherit = "l10n.br.sped.mixin"


class Registro9999(models.Model):
    _name = "l10n.br.sped.efd_pis_cofins.9999"
    _description = u"""Encerramento do Arquivo Digital"""
    _inherit = "l10n.br.sped.mixin"
    qtd_lin = fields.Integer("Quantidade total de linhas do arquivo digital")
