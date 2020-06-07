from odoo import fields, models

from . import spec_models


class Registro0000(models.Model):
    _name = "l10n.br.sped.ecd.0000"
    _description = u"""ABERTURA DO ARQUIVO DIGITAL E IDENTIFICAÇÃO DO EMPRESÁRIO OU DA SOCIEDADE EMPRESÁRIA"""
    _inherit = "l10n.br.sped.mixin"
    lecd = fields.Char(
        "Texto fixo contendo “LECD”.",
        required=True,
        help="""Texto fixo contendo “LECD”.
Ver pagina 44""",
    )
    dt_ini = fields.Integer(
        "Data inicial das informações contidas no arquivo", required=True
    )
    dt_fin = fields.Integer(
        "Data final das informações contidas no arquivo", required=True
    )
    nome = fields.Char(
        "Nome empresarial da pessoa jurídica.",
        required=True,
        help="""Nome empresarial da pessoa jurídica.
Ver pagina 44""",
    )
    cnpj = fields.Integer(
        "Número de inscrição da pessoa jurídica no CNPJ", required=True
    )
    uf = fields.Char(
        "Sigla da unidade da federação da pessoa jurídica",
        required=True,
        help="""Sigla da unidade da federação da pessoa jurídica.
Ver pagina 44""",
    )
    ie = fields.Char(
        "Inscrição Estadual da pessoa jurídica.",
        help="""Inscrição Estadual da pessoa jurídica.
Ver pagina 44""",
    )
    cod_mun = fields.Integer("COD_MUN")
    im = fields.Char(
        "Inscrição Municipal da pessoa jurídica.",
        help="""Inscrição Municipal da pessoa jurídica.
Ver pagina 44""",
    )
    ind_sit_esp = fields.Integer("IND_SIT_ESP")
    ind_sit_ini_per = fields.Integer("IND_SIT_INI_PER", required=True)
    ind_nire = fields.Integer("Indicador de existência de NIRE", required=True)
    ind_fin_esc = fields.Integer(
        "Indicador de finalidade da escrituração", required=True
    )
    cod_hash_sub = fields.Char(
        "Hash da escrituração substituída.",
        help="""Hash da escrituração substituída.
Ver pagina 45""",
    )
    ind_grande_porte = fields.Integer(
        "Indicador de entidade sujeita a auditoria independente", required=True
    )
    tip_ecd = fields.Integer("Indicador do tipo de ECD", required=True)
    cod_scp = fields.Integer("CNPJ da SCP (Art")
    ident_mf = fields.Char(
        "Identificação de moeda funcional",
        required=True,
        help="""Identificação de moeda funcional: Indica que a escrituração abrange valores  com  base  na moeda  funcional  (art. 287 da Instrução Normativa RFB nº 1.700, de 14 de março de 2017).  Observações:  Nessa situação,  deverá  ser utilizado  o  registro I020 para informação de campos adicionais, conforme  instruções do 1.25 do capítulo 1 deste Manual.
Ver pagina 46""",
    )
    ind_esc_cons = fields.Char(
        "Escriturações Contábeis Consolidadas",
        required=True,
        help="""Escriturações Contábeis Consolidadas: (Deve ser preenchido pela empresa  controladora obrigada  a informar demonstrações contábeis consolidadas, nos termos da Lei nº 6.404/76 e do Pronunciamento Técnico  CPC  36  – Demonstrações Consolidadas) S – Sim N – Não
Ver pagina 46""",
    )


class Registro0007(models.Model):
    _name = "l10n.br.sped.ecd.0007"
    _description = u"""OUTRAS INSCRIÇÕES CADASTRAIS DA PESSOA JURÍDICA"""
    _inherit = "l10n.br.sped.mixin"
    cod_ent_ref = fields.Char(
        "COD_ENT_REF",
        required=True,
        help="""Código da instituição responsável pela administração do cadastro (conforme tabela publicada pelo Sped).
Ver pagina 55""",
    )
    cod_inscr = fields.Char(
        "COD_INSCR",
        help="""Código cadastral da pessoa jurídica na instituição identificada no campo 02.
Ver pagina 55""",
    )


class Registro0020(models.Model):
    _name = "l10n.br.sped.ecd.0020"
    _description = u"""ESCRITURAÇÃO CONTÁBIL DESCENTRALIZADA"""
    _inherit = "l10n.br.sped.mixin"
    ind_dec = fields.Integer("Indicador de descentralização", required=True)
    cnpj = fields.Integer("CNPJ", required=True)
    uf = fields.Char(
        "Sigla da unidade da federação da matriz ou da filial",
        required=True,
        help="""Sigla da unidade da federação da matriz ou da filial.
Ver pagina 57""",
    )
    ie = fields.Char(
        "Inscrição estadual da matriz ou da filial",
        help="""Inscrição estadual da matriz ou da filial.
Ver pagina 57""",
    )
    cod_mun = fields.Integer("Código do município do domicílio da matriz ou da filial")
    im = fields.Char(
        "Número de Inscrição Municipal da matriz ou da filial",
        help="""Número de Inscrição Municipal da matriz ou da filial.
Ver pagina 57""",
    )
    nire = fields.Integer("NIRE")


class Registro0035(models.Model):
    _name = "l10n.br.sped.ecd.0035"
    _description = u"""IDENTIFICAÇÃO DAS SCP"""
    _inherit = "l10n.br.sped.mixin"
    cod_scp = fields.Char(
        "CNPJ da SCP  (Art",
        required=True,
        help="""CNPJ da SCP  (Art. 4º, XVII, da Instrução Normativa RFB nº 1.634, de 6 de maio de 2016).
Ver pagina 59""",
    )
    nome_scp = fields.Char(
        "Nome da SCP",
        help="""Nome da SCP
Ver pagina 59""",
    )


class Registro0150(models.Model):
    _name = "l10n.br.sped.ecd.0150"
    _description = u"""TABELA DE CADASTRO DO PARTICIPANTE"""
    _inherit = "l10n.br.sped.mixin"
    cod_part = fields.Char(
        "COD_PART",
        required=True,
        help="""Código de identificação do participante no arquivo criado pela própria pessoa jurídica.
Ver pagina 60""",
    )
    nome = fields.Char(
        "Nome pessoal ou empresarial do participante",
        required=True,
        help="""Nome pessoal ou empresarial do participante.
Ver pagina 60""",
    )
    cod_pais = fields.Integer("COD_PAIS", required=True)
    cnpj = fields.Integer("CNPJ do participante.")
    cpf = fields.Integer("CPF do participante.")
    nit = fields.Integer("Número de Identificação do Trabalhador, Pis, Pasep, SUS")
    uf = fields.Char(
        "Sigla da unidade da federação do participante",
        help="""Sigla da unidade da federação do participante.
Ver pagina 60""",
    )
    ie = fields.Char(
        "Inscrição Estadual do participante.",
        help="""Inscrição Estadual do participante.
Ver pagina 60""",
    )
    ie_st = fields.Char(
        "IE_ST",
        help="""Inscrição Estadual do participante na unidade da federação do destinatário, na condição de contribuinte substituto.
Ver pagina 60""",
    )
    cod_mun = fields.Integer("Código do município, conforme a tabela do IBGE")
    im = fields.Char(
        "Inscrição Municipal do participante.",
        help="""Inscrição Municipal do participante.
Ver pagina 60""",
    )
    suframa = fields.Char(
        "Número de inscrição do participante na Suframa",
        help="""Número de inscrição do participante na Suframa.
Ver pagina 61""",
    )
    reg_0180_ids = fields.One2many(
        "l10n.br.sped.ecd.0180",
        "parent_0150_id",
        string="IDENTIFICAÇÃO DO RELACIONAMENTO COM O PARTICIPANTE",
        help="Bloco 0",
    )


class Registro0180(models.Model):
    _name = "l10n.br.sped.ecd.0180"
    _description = u"""IDENTIFICAÇÃO DO RELACIONAMENTO COM O PARTICIPANTE"""
    _inherit = "l10n.br.sped.mixin"
    cod_rel = fields.Integer(
        "Código do relacionamento conforme tabela publicada pelo Sped", required=True
    )
    dt_ini_rel = fields.Integer("Data do início do relacionamento.", required=True)
    dt_fin_rel = fields.Integer("Data do término do relacionamento.")
    parent_0150_id = fields.Many2one(
        "l10n.br.sped.ecd.0150", string="TABELA DE CADASTRO DO PARTICIPANTE"
    )


class RegistroI010(models.Model):
    _name = "l10n.br.sped.ecd.i010"
    _description = u"""IDENTIFICAÇÃO DA ESCRITURAÇÃO CONTÁBIL"""
    _inherit = "l10n.br.sped.mixin"
    ind_esc = fields.Char(
        "Indicador da forma de escrituração contábil",
        required=True,
        help="""Indicador da forma de escrituração contábil:  - Livro Diário (Completo sem escrituração auxiliar).  - Livro Diário com Escrituração Resumida (com escrituração auxiliar).  - Livro Diário Auxiliar ao Diário com Escrituração Resumida.  - Livro Balancetes Diários e Balanços.  – Razão Auxiliar (Livro Contábil Auxiliar conforme leiaute definido nos registros I500 a I555).   G  R  A  B  Z
Ver pagina 67""",
    )
    cod_ver_lc = fields.Char(
        "Código da Versão do Leiaute Contábil",
        required=True,
        help="""Código da Versão do Leiaute Contábil. (Preencher com 6.00)
Ver pagina 67""",
    )
    reg_i150_id = fields.Many2one(
        "l10n.br.sped.ecd.i150",
        string="SALDOS PERIÓDICOS – IDENTIFICAÇÃO DO PERÍODO",
        help="Bloco I",
    )  # m2o
    reg_i350_id = fields.Many2one(
        "l10n.br.sped.ecd.i350",
        string="SALDOS  DAS  CONTAS  DE  RESULTADO  ANTES  DO  ENCERRAMENTO  – IDENTIFICAÇÃO DA DATA",
        help="Bloco I",
    )  # m2o
    reg_i012_ids = fields.One2many(
        "l10n.br.sped.ecd.i012",
        "parent_i010_id",
        string="LIVROS AUXILIARES AO DIÁRIO",
        help="Bloco I",
    )
    reg_i020_ids = fields.One2many(
        "l10n.br.sped.ecd.i020",
        "parent_i010_id",
        string="CAMPOS ADICIONAIS",
        help="Bloco I",
    )
    reg_i030_ids = fields.One2many(
        "l10n.br.sped.ecd.i030",
        "parent_i010_id",
        string="TERMO DE ABERTURA",
        help="Bloco I",
    )
    reg_i050_ids = fields.One2many(
        "l10n.br.sped.ecd.i050",
        "parent_i010_id",
        string="PLANO DE CONTAS",
        help="Bloco I",
    )
    reg_i075_ids = fields.One2many(
        "l10n.br.sped.ecd.i075",
        "parent_i010_id",
        string="TABELA DE HISTÓRICO PADRONIZADO",
        help="Bloco I",
    )
    reg_i100_ids = fields.One2many(
        "l10n.br.sped.ecd.i100",
        "parent_i010_id",
        string="CENTRO DE CUSTOS",
        help="Bloco I",
    )
    reg_i200_ids = fields.One2many(
        "l10n.br.sped.ecd.i200",
        "parent_i010_id",
        string="LANÇAMENTO CONTÁBIL",
        help="Bloco I",
    )
    reg_i300_ids = fields.One2many(
        "l10n.br.sped.ecd.i300",
        "parent_i010_id",
        string="BALANCETES DIÁRIOS – IDENTIFICAÇÃO DA DATA",
        help="Bloco I",
    )
    reg_i500_ids = fields.One2many(
        "l10n.br.sped.ecd.i500",
        "parent_i010_id",
        string="PARÂMETROS  DE  IMPRESSÃO/VISUALIZAÇÃO  DO  LIVRO  RAZÃO  AUXILIAR COM LEIAUTE PARAMETRIZÁVEL",
        help="Bloco I",
    )
    reg_i510_ids = fields.One2many(
        "l10n.br.sped.ecd.i510",
        "parent_i010_id",
        string="DEFINIÇÃO  DOS  CAMPOS  DO  LIVRO  RAZÃO  AUXILIAR  COM  LEIAUTE PARAMETRIZÁVEL",
        help="Bloco I",
    )
    reg_i550_ids = fields.One2many(
        "l10n.br.sped.ecd.i550",
        "parent_i010_id",
        string="DETALHES DO LIVRO RAZÃO AUXILIAR COM LEIAUTE PARAMETRIZÁVEL",
        help="Bloco I",
    )


class RegistroI012(models.Model):
    _name = "l10n.br.sped.ecd.i012"
    _description = u"""LIVROS AUXILIARES AO DIÁRIO"""
    _inherit = "l10n.br.sped.mixin"
    num_ord = fields.Integer("Número de ordem do instrumento associado", required=True)
    nat_livr = fields.Char(
        "NAT_LIVR",
        required=True,
        help="""Natureza do livro associado; finalidade a que se destina o instrumento.
Ver pagina 69""",
    )
    tipo = fields.Integer("Tipo de escrituração do livro associado", required=True)
    cod_hash_aux = fields.Char(
        "COD_HASH_AUX",
        help="""Código Hash do arquivo correspondente ao livro auxiliar utilizado na assinatura digital.
Ver pagina 69""",
    )
    parent_i010_id = fields.Many2one(
        "l10n.br.sped.ecd.i010", string="IDENTIFICAÇÃO DA ESCRITURAÇÃO CONTÁBIL"
    )
    reg_i015_ids = fields.One2many(
        "l10n.br.sped.ecd.i015",
        "parent_i012_id",
        string="IDENTIFICAÇÃO  DAS  CONTAS  DA  ESCRITURAÇÃO  RESUMIDA  A  QUE  SE REFERE A ESCRITURAÇÃO AUXILIAR",
        help="Bloco I",
    )


class RegistroI015(models.Model):
    _name = "l10n.br.sped.ecd.i015"
    _description = u"""IDENTIFICAÇÃO  DAS  CONTAS  DA  ESCRITURAÇÃO  RESUMIDA  A  QUE  SE REFERE A ESCRITURAÇÃO AUXILIAR"""
    _inherit = "l10n.br.sped.mixin"
    cod_cta_res = fields.Char(
        "COD_CTA_RES",
        required=True,
        help="""Código da(s) conta(s) analítica(s) do Livro Diário com Escrituração Resumida (R) que recebe os lançamentos globais (deve corresponder a uma conta sintética no livro auxiliar).
Ver pagina 72""",
    )
    parent_i012_id = fields.Many2one(
        "l10n.br.sped.ecd.i012", string="LIVROS AUXILIARES AO DIÁRIO"
    )


class RegistroI020(models.Model):
    _name = "l10n.br.sped.ecd.i020"
    _description = u"""CAMPOS ADICIONAIS"""
    _inherit = "l10n.br.sped.mixin"
    reg_cod = fields.Char(
        "Código do registro que recepciona o campo adicional",
        required=True,
        help="""Código do registro que recepciona o campo adicional.
Ver pagina 74""",
    )
    num_ad = fields.Integer("Número sequencial do campo adicional.", required=True)
    campo = fields.Char(
        "Nome do campo adicional.",
        required=True,
        help="""Nome do campo adicional.
Ver pagina 74""",
    )
    descricao = fields.Char(
        "Descrição do campo adicional.",
        help="""Descrição do campo adicional.
Ver pagina 74""",
    )
    tipo = fields.Char(
        "Indicação do tipo de dado (N",
        required=True,
        help="""Indicação do tipo de dado (N: numérico; C: caractere).
Ver pagina 74""",
    )
    ind_dc_ini_mf = fields.Char(
        "Indicador da situação do saldo inicial em moeda funcional",
        help="""Indicador da situação do saldo inicial em moeda funcional: D - Devedor; C - Credor.
Ver pagina 75""",
    )
    parent_i010_id = fields.Many2one(
        "l10n.br.sped.ecd.i010", string="IDENTIFICAÇÃO DA ESCRITURAÇÃO CONTÁBIL"
    )


class RegistroI030(models.Model):
    _name = "l10n.br.sped.ecd.i030"
    _description = u"""TERMO DE ABERTURA"""
    _inherit = "l10n.br.sped.mixin"
    dnrc_abert = fields.Char(
        "Texto fixo contendo “TERMO DE ABERTURA”",
        required=True,
        help="""Texto fixo contendo “TERMO DE ABERTURA”.
Ver pagina 77""",
    )
    num_ord = fields.Integer(
        "Número de ordem do instrumento de escrituração", required=True
    )
    nat_livr = fields.Char(
        "Natureza do livro; finalidade a que se destina o instrumento",
        required=True,
        help="""Natureza do livro; finalidade a que se destina o instrumento.
Ver pagina 77""",
    )
    qtd_lin = fields.Integer(
        "Quantidade total de linhas do arquivo digital", required=True
    )
    nome = fields.Char(
        "Nome empresarial.",
        required=True,
        help="""Nome empresarial.
Ver pagina 77""",
    )
    nire = fields.Integer("NIRE")
    cnpj = fields.Integer("Número de inscrição no CNPJ.", required=True)
    dt_arq = fields.Integer("Data do arquivamento dos atos constitutivos")
    dt_arq_conv = fields.Integer("DT_ARQ_CONV")
    desc_mun = fields.Char(
        "Município.",
        help="""Município.
Ver pagina 77""",
    )
    dt_ex_social = fields.Integer(
        "Data de encerramento do exercício social", required=True
    )
    parent_i010_id = fields.Many2one(
        "l10n.br.sped.ecd.i010", string="IDENTIFICAÇÃO DA ESCRITURAÇÃO CONTÁBIL"
    )


class RegistroI050(models.Model):
    _name = "l10n.br.sped.ecd.i050"
    _description = u"""PLANO DE CONTAS"""
    _inherit = "l10n.br.sped.mixin"
    dt_alt = fields.Integer("Data da inclusão/alteração.", required=True)
    cod_nat = fields.Char(
        "COD_NAT",
        required=True,
        help="""Código da natureza da conta/grupo de contas, conforme tabela publicada pelo Sped.
Ver pagina 81""",
    )
    ind_cta = fields.Char(
        "Indicador do tipo de conta",
        required=True,
        help="""Indicador do tipo de conta: S - Sintética (grupo de contas) A - Analítica (conta)
Ver pagina 81""",
    )
    nivel = fields.Integer("Nível da conta analítica/grupo de contas", required=True)
    cod_cta = fields.Char(
        "Código da conta analítica/grupo de contas",
        required=True,
        help="""Código da conta analítica/grupo de contas.
Ver pagina 81""",
    )
    cod_cta_sup = fields.Char(
        "COD_CTA_SUP",
        help="""Código da conta sintética /grupo de contas de nível imediatamente superior.
Ver pagina 82""",
    )
    cta = fields.Char(
        "Nome da conta analítica/grupo de contas",
        required=True,
        help="""Nome da conta analítica/grupo de contas.
Ver pagina 82""",
    )
    parent_i010_id = fields.Many2one(
        "l10n.br.sped.ecd.i010", string="IDENTIFICAÇÃO DA ESCRITURAÇÃO CONTÁBIL"
    )
    reg_i051_ids = fields.One2many(
        "l10n.br.sped.ecd.i051",
        "parent_i050_id",
        string="PLANO DE CONTAS REFERENCIAL",
        help="Bloco I",
    )
    reg_i052_ids = fields.One2many(
        "l10n.br.sped.ecd.i052",
        "parent_i050_id",
        string="INDICAÇÃO DOS CÓDIGOS DE AGLUTINAÇÃO",
        help="Bloco I",
    )
    reg_i053_ids = fields.One2many(
        "l10n.br.sped.ecd.i053",
        "parent_i050_id",
        string="SUBCONTAS CORRELATAS",
        help="Bloco I",
    )


class RegistroI051(models.Model):
    _name = "l10n.br.sped.ecd.i051"
    _description = u"""PLANO DE CONTAS REFERENCIAL"""
    _inherit = "l10n.br.sped.mixin"
    cod_plan_ref = fields.Char(
        "COD_PLAN_REF",
        required=True,
        help="""Código da instituição responsável pela manutenção do plano de contas referencial, conforme tabela publicada pelo Sped.
Ver pagina 85""",
    )
    cod_ccus = fields.Char(
        "Código do centro de custo.",
        help="""Código do centro de custo.
Ver pagina 85""",
    )
    cod_cta_ref = fields.Char(
        "COD_CTA_REF",
        required=True,
        help="""Código da conta de acordo com o plano de contas referencial, conforme tabela publicada pelos órgãos indicados no campo 02- COD_PLAN_REF.
Ver pagina 85""",
    )
    parent_i050_id = fields.Many2one("l10n.br.sped.ecd.i050", string="PLANO DE CONTAS")


class RegistroI052(models.Model):
    _name = "l10n.br.sped.ecd.i052"
    _description = u"""INDICAÇÃO DOS CÓDIGOS DE AGLUTINAÇÃO"""
    _inherit = "l10n.br.sped.mixin"
    cod_ccus = fields.Char(
        "Código do centro de custo.",
        help="""Código do centro de custo.
Ver pagina 88""",
    )
    cod_agl = fields.Char(
        "COD_AGL",
        required=True,
        help="""Código de aglutinação utilizado nas demonstrações contábeis do bloco J (Somente para as contas analíticas).
Ver pagina 88""",
    )
    parent_i050_id = fields.Many2one("l10n.br.sped.ecd.i050", string="PLANO DE CONTAS")


class RegistroI053(models.Model):
    _name = "l10n.br.sped.ecd.i053"
    _description = u"""SUBCONTAS CORRELATAS"""
    _inherit = "l10n.br.sped.mixin"
    cod_idt = fields.Char(
        "Código de identificação do grupo de conta-subconta(s)",
        required=True,
        help="""Código de identificação do grupo de conta-subconta(s)
Ver pagina 90""",
    )
    cod_cnt_corr = fields.Char(
        "COD_CNT_CORR",
        required=True,
        help="""Código da subconta correlata (deve estar no plano de contas e só pode estar relacionada a um único grupo)
Ver pagina 90""",
    )
    nat_sub_cnt = fields.Char(
        "NAT_SUB_CNT",
        help="""Natureza da subconta correlata (conforme tabela de natureza da subconta publicada no Sped )
Ver pagina 90""",
    )
    parent_i050_id = fields.Many2one("l10n.br.sped.ecd.i050", string="PLANO DE CONTAS")


class RegistroI075(models.Model):
    _name = "l10n.br.sped.ecd.i075"
    _description = u"""TABELA DE HISTÓRICO PADRONIZADO"""
    _inherit = "l10n.br.sped.mixin"
    cod_hist = fields.Char(
        "Código do histórico padronizado.",
        required=True,
        help="""Código do histórico padronizado.
Ver pagina 93""",
    )
    descr_hist = fields.Char(
        "Descrição do histórico padronizado.",
        required=True,
        help="""Descrição do histórico padronizado.
Ver pagina 93""",
    )
    parent_i010_id = fields.Many2one(
        "l10n.br.sped.ecd.i010", string="IDENTIFICAÇÃO DA ESCRITURAÇÃO CONTÁBIL"
    )


class RegistroI100(models.Model):
    _name = "l10n.br.sped.ecd.i100"
    _description = u"""CENTRO DE CUSTOS"""
    _inherit = "l10n.br.sped.mixin"
    dt_alt = fields.Integer("Data da inclusão/alteração.", required=True)
    cod_ccus = fields.Char(
        "Código do centro de custos.",
        required=True,
        help="""Código do centro de custos.
Ver pagina 94""",
    )
    ccus = fields.Char(
        "Nome do centro de custos.",
        required=True,
        help="""Nome do centro de custos.
Ver pagina 94""",
    )
    parent_i010_id = fields.Many2one(
        "l10n.br.sped.ecd.i010", string="IDENTIFICAÇÃO DA ESCRITURAÇÃO CONTÁBIL"
    )


class RegistroI150(models.Model):
    _name = "l10n.br.sped.ecd.i150"
    _description = u"""SALDOS PERIÓDICOS – IDENTIFICAÇÃO DO PERÍODO"""
    _inherit = "l10n.br.sped.mixin"
    dt_ini = fields.Integer("Data de início do período.", required=True)
    dt_fin = fields.Integer("Data de fim do período.", required=True)
    reg_i151_ids = fields.One2many(
        "l10n.br.sped.ecd.i151",
        "parent_i150_id",
        string="FICHAS  DE ASSINATURA  DIGITAL  DOS  ARQUIVOS  QUE  CONTÉM  AS LANÇAMENTO UTILIZADAS NO PERÍODO",
        help="Bloco I",
    )
    reg_i155_ids = fields.One2many(
        "l10n.br.sped.ecd.i155",
        "parent_i150_id",
        string="DETALHES DOS SALDOS PERIÓDICOS",
        help="Bloco I",
    )


class RegistroI151(models.Model):
    _name = "l10n.br.sped.ecd.i151"
    _description = u"""FICHAS  DE ASSINATURA  DIGITAL  DOS  ARQUIVOS  QUE  CONTÉM  AS LANÇAMENTO UTILIZADAS NO PERÍODO"""
    _inherit = "l10n.br.sped.mixin"
    assin_dig = fields.Char(
        "Hash  das  fichas  de lançamento.",
        required=True,
        help="""Hash  das  fichas  de lançamento.
Ver pagina 97""",
    )
    parent_i150_id = fields.Many2one(
        "l10n.br.sped.ecd.i150", string="SALDOS PERIÓDICOS – IDENTIFICAÇÃO DO PERÍODO"
    )


class RegistroI155(models.Model):
    _name = "l10n.br.sped.ecd.i155"
    _description = u"""DETALHES DOS SALDOS PERIÓDICOS"""
    _inherit = "l10n.br.sped.mixin"
    cod_cta = fields.Char(
        "Código da conta analítica.",
        required=True,
        help="""Código da conta analítica.
Ver pagina 98""",
    )
    cod_ccus = fields.Char(
        "Código do centro de custos.",
        help="""Código do centro de custos.
Ver pagina 98""",
    )
    vl_sld_ini = fields.Monetary(
        "Valor do saldo inicial do período.", required=True, digits=2
    )
    ind_dc_ini = fields.Char(
        "Indicador da situação do saldo inicial",
        help="""Indicador da situação do saldo inicial: D - Devedor; C - Credor.
Ver pagina 98""",
    )
    vl_deb = fields.Monetary(
        "Valor total dos débitos do período.", required=True, digits=2
    )
    vl_cred = fields.Monetary(
        "Valor total dos créditos do período.", required=True, digits=2
    )
    vl_sld_fin = fields.Monetary(
        "Valor do saldo final do período.", required=True, digits=2
    )
    ind_dc_fin = fields.Char(
        "Indicador da situação do saldo final",
        help="""Indicador da situação do saldo final: D - Devedor; C - Credor.
Ver pagina 99""",
    )
    vl_sld_ini_mf = fields.Monetary("VL_SLD_INI_MF", digits=2)
    ind_dc_ini_mf = fields.Char(
        "Indicador da situação do saldo inicial em moeda funcional",
        help="""Indicador da situação do saldo inicial em moeda funcional: D - Devedor; C - Credor.
Ver pagina 99""",
    )
    vl_deb_mf = fields.Monetary("VL_DEB_MF", digits=2)
    vl_cred_mf = fields.Monetary("VL_CRED_MF", digits=2)
    vl_sld_fin_mf = fields.Monetary("VL_SLD_FIN_MF", digits=2)
    ind_dc_fin_mf = fields.Char(
        "Indicador da situação do saldo final em moeda funcional",
        help="""Indicador da situação do saldo final em moeda funcional: D - Devedor; C - Credor.
Ver pagina 100""",
    )
    parent_i150_id = fields.Many2one(
        "l10n.br.sped.ecd.i150", string="SALDOS PERIÓDICOS – IDENTIFICAÇÃO DO PERÍODO"
    )
    reg_i157_ids = fields.One2many(
        "l10n.br.sped.ecd.i157",
        "parent_i155_id",
        string="TRANSFERÊNCIA DE SALDOS DO PLANO DE CONTAS ANTERIOR",
        help="Bloco I",
    )


class RegistroI157(models.Model):
    _name = "l10n.br.sped.ecd.i157"
    _description = u"""TRANSFERÊNCIA DE SALDOS DO PLANO DE CONTAS ANTERIOR"""
    _inherit = "l10n.br.sped.mixin"
    cod_cta = fields.Char(
        "Código da conta analítica do plano de contas anterior",
        required=True,
        help="""Código da conta analítica do plano de contas anterior.
Ver pagina 104""",
    )
    cod_ccus = fields.Char(
        "Código do centro de custos do plano de contas anterior",
        help="""Código do centro de custos do plano de contas anterior.
Ver pagina 104""",
    )
    vl_sld_ini = fields.Monetary(
        "Valor do saldo inicial do período.", required=True, digits=2
    )
    ind_dc_ini = fields.Char(
        "Indicador da situação do saldo inicial",
        help="""Indicador da situação do saldo inicial: D - Devedor; C - Credor.
Ver pagina 104""",
    )
    vl_sld_ini_mf = fields.Monetary("VL_SLD_INI_MF", digits=2)
    ind_dc_ini_mf = fields.Char(
        "Indicador da situação do saldo inicial em moeda funcional",
        help="""Indicador da situação do saldo inicial em moeda funcional: D - Devedor; C - Credor.
Ver pagina 105""",
    )
    parent_i155_id = fields.Many2one(
        "l10n.br.sped.ecd.i155", string="DETALHES DOS SALDOS PERIÓDICOS"
    )


class RegistroI200(models.Model):
    _name = "l10n.br.sped.ecd.i200"
    _description = u"""LANÇAMENTO CONTÁBIL"""
    _inherit = "l10n.br.sped.mixin"
    num_lcto = fields.Char(
        "Número ou Código de identificação único do lançamento contábil",
        required=True,
        help="""Número ou Código de identificação único do lançamento contábil.
Ver pagina 106""",
    )
    dt_lcto = fields.Integer("Data do lançamento.", required=True)
    vl_lcto = fields.Monetary("Valor do lançamento.", required=True, digits=2)
    ind_lcto = fields.Char(
        "Indicador do tipo de lançamento",
        required=True,
        help="""Indicador do tipo de lançamento: N - Lançamento normal (todos os lançamentos, exceto os de encerramento das contas de resultado); E - Lançamento de encerramento de contas de resultado.
Ver pagina 106""",
    )
    vl_lcto_mf = fields.Monetary(
        "Valor do lançamento em moeda funcional, convertido para reais", digits=2
    )
    parent_i010_id = fields.Many2one(
        "l10n.br.sped.ecd.i010", string="IDENTIFICAÇÃO DA ESCRITURAÇÃO CONTÁBIL"
    )
    reg_i250_ids = fields.One2many(
        "l10n.br.sped.ecd.i250",
        "parent_i200_id",
        string="PARTIDAS DO LANÇAMENTO CONTÁBIL",
        help="Bloco I",
    )


class RegistroI250(models.Model):
    _name = "l10n.br.sped.ecd.i250"
    _description = u"""PARTIDAS DO LANÇAMENTO CONTÁBIL"""
    _inherit = "l10n.br.sped.mixin"
    cod_cta = fields.Char(
        "Código da conta analítica debitada/creditada",
        required=True,
        help="""Código da conta analítica debitada/creditada.
Ver pagina 109""",
    )
    cod_ccus = fields.Char(
        "Código do centro de custos.",
        help="""Código do centro de custos.
Ver pagina 109""",
    )
    vl_dc = fields.Monetary("Valor da partida.", required=True, digits=2)
    ind_dc = fields.Char(
        "Indicador da natureza da partida",
        required=True,
        help="""Indicador da natureza da partida: D - Débito; C - Crédito.
Ver pagina 109""",
    )
    num_arq = fields.Char(
        "NUM_ARQ",
        help="""Número, Código ou caminho de localização dos documentos arquivados.
Ver pagina 109""",
    )
    cod_hist_pad = fields.Char(
        "Código do histórico padronizado, conforme tabela I075",
        help="""Código do histórico padronizado, conforme tabela I075.
Ver pagina 110""",
    )
    hist = fields.Char(
        "Histórico completo da partida ou histórico complementar",
        help="""Histórico completo da partida ou histórico complementar.
Ver pagina 110""",
    )
    cod_part = fields.Char(
        "COD_PART",
        help="""Código de identificação do participante na partida conforme tabela 0150 (preencher somente quando identificado o tipo de participação no registro 0180).
Ver pagina 110""",
    )
    vl_dc_mf = fields.Monetary(
        "Valor da partida em moeda funcional, convertido para reais", digits=2
    )
    ind_dc_mf = fields.Char(
        "Indicador da natureza da partida em moeda funcional",
        help="""Indicador da natureza da partida em moeda funcional: D - Débito; C - Crédito.
Ver pagina 110""",
    )
    parent_i200_id = fields.Many2one(
        "l10n.br.sped.ecd.i200", string="LANÇAMENTO CONTÁBIL"
    )


class RegistroI300(models.Model):
    _name = "l10n.br.sped.ecd.i300"
    _description = u"""BALANCETES DIÁRIOS – IDENTIFICAÇÃO DA DATA"""
    _inherit = "l10n.br.sped.mixin"
    dt_bcte = fields.Integer("Data do balancete.", required=True)
    parent_i010_id = fields.Many2one(
        "l10n.br.sped.ecd.i010", string="IDENTIFICAÇÃO DA ESCRITURAÇÃO CONTÁBIL"
    )
    reg_i310_ids = fields.One2many(
        "l10n.br.sped.ecd.i310",
        "parent_i300_id",
        string="DETALHES DO BALANCETE DIÁRIO",
        help="Bloco I",
    )


class RegistroI310(models.Model):
    _name = "l10n.br.sped.ecd.i310"
    _description = u"""DETALHES DO BALANCETE DIÁRIO"""
    _inherit = "l10n.br.sped.mixin"
    cod_cta = fields.Char(
        "Código da conta analítica debitada/creditada",
        required=True,
        help="""Código da conta analítica debitada/creditada.
Ver pagina 114""",
    )
    cod_ccus = fields.Char(
        "Código do centro de custos.",
        help="""Código do centro de custos.
Ver pagina 114""",
    )
    val_debd = fields.Monetary("Total dos débitos do dia.", required=True, digits=2)
    val_credd = fields.Monetary("Total dos créditos do dia.", required=True, digits=2)
    val_deb_mf = fields.Monetary("VAL_DEB_MF", digits=2)
    val_cred_mf = fields.Monetary("VAL_CRED_MF", digits=2)
    parent_i300_id = fields.Many2one(
        "l10n.br.sped.ecd.i300", string="BALANCETES DIÁRIOS – IDENTIFICAÇÃO DA DATA"
    )


class RegistroI350(models.Model):
    _name = "l10n.br.sped.ecd.i350"
    _description = u"""SALDOS  DAS  CONTAS  DE  RESULTADO  ANTES  DO  ENCERRAMENTO  – IDENTIFICAÇÃO DA DATA"""
    _inherit = "l10n.br.sped.mixin"
    dt_res = fields.Integer("Data da apuração do resultado.", required=True)
    reg_i355_ids = fields.One2many(
        "l10n.br.sped.ecd.i355",
        "parent_i350_id",
        string="DOS SALDOS DAS CONTAS DE RESULTADO ANTES DO DETALHES ENCERRAMENTO",
        help="Bloco I",
    )


class RegistroI355(models.Model):
    _name = "l10n.br.sped.ecd.i355"
    _description = (
        u"""DOS SALDOS DAS CONTAS DE RESULTADO ANTES DO DETALHES ENCERRAMENTO"""
    )
    _inherit = "l10n.br.sped.mixin"
    cod_cta = fields.Char(
        "Código da conta analítica de resultado.",
        required=True,
        help="""Código da conta analítica de resultado.
Ver pagina 117""",
    )
    cod_ccus = fields.Char(
        "Código do centro de custos.",
        help="""Código do centro de custos.
Ver pagina 117""",
    )
    vl_cta = fields.Monetary(
        "Valor do saldo final antes do lançamento de encerramento",
        required=True,
        digits=2,
    )
    ind_dc = fields.Char(
        "Indicador da situação do saldo final",
        required=True,
        help="""Indicador da situação do saldo final: D - Devedor; C - Credor.
Ver pagina 117""",
    )
    vl_cta_mf = fields.Monetary("VL_CTA_MF", digits=2)
    ind_dc_mf = fields.Char(
        "Indicador da situação do saldo final em moeda funcional",
        help="""Indicador da situação do saldo final em moeda funcional: D - Devedor; C - Credor.
Ver pagina 118""",
    )
    parent_i350_id = fields.Many2one(
        "l10n.br.sped.ecd.i350",
        string="SALDOS  DAS  CONTAS  DE  RESULTADO  ANTES  DO  ENCERRAMENTO  – IDENTIFICAÇÃO DA DATA",
    )


class RegistroI500(models.Model):
    _name = "l10n.br.sped.ecd.i500"
    _description = u"""PARÂMETROS  DE  IMPRESSÃO/VISUALIZAÇÃO  DO  LIVRO  RAZÃO  AUXILIAR COM LEIAUTE PARAMETRIZÁVEL"""
    _inherit = "l10n.br.sped.mixin"
    tam_fonte = fields.Integer("Tamanho da fonte.", required=True)
    parent_i010_id = fields.Many2one(
        "l10n.br.sped.ecd.i010", string="IDENTIFICAÇÃO DA ESCRITURAÇÃO CONTÁBIL"
    )


class RegistroI510(models.Model):
    _name = "l10n.br.sped.ecd.i510"
    _description = u"""DEFINIÇÃO  DOS  CAMPOS  DO  LIVRO  RAZÃO  AUXILIAR  COM  LEIAUTE PARAMETRIZÁVEL"""
    _inherit = "l10n.br.sped.mixin"
    nm_campo = fields.Char(
        "Nome do campo, sem espaços em branco ou caractere especial",
        required=True,
        help="""Nome do campo, sem espaços em branco ou caractere especial.
Ver pagina 121""",
    )
    desc_campo = fields.Char(
        "Descrição do campo (utilizada na visualização do Livro Auxiliar)",
        required=True,
        help="""Descrição do campo (utilizada na visualização do Livro Auxiliar)
Ver pagina 121""",
    )
    tipo_campo = fields.Char(
        "Tipo do campo: “N” – Numérico; “C” – Caractere",
        required=True,
        help="""Tipo do campo: “N” – Numérico; “C” – Caractere.
Ver pagina 121""",
    )
    tam_campo = fields.Integer("Tamanho do campo.", required=True)
    dec_campo = fields.Integer("Quantidade de casas decimais para campos tipo “N”")
    col_campo = fields.Integer(
        "Largura da coluna no relatório (em quantidade de caracteres)", required=True
    )
    parent_i010_id = fields.Many2one(
        "l10n.br.sped.ecd.i010", string="IDENTIFICAÇÃO DA ESCRITURAÇÃO CONTÁBIL"
    )


class RegistroI550(models.Model):
    _name = "l10n.br.sped.ecd.i550"
    _description = u"""DETALHES DO LIVRO RAZÃO AUXILIAR COM LEIAUTE PARAMETRIZÁVEL"""
    _inherit = "l10n.br.sped.mixin"
    parent_i010_id = fields.Many2one(
        "l10n.br.sped.ecd.i010", string="IDENTIFICAÇÃO DA ESCRITURAÇÃO CONTÁBIL"
    )
    reg_i555_ids = fields.One2many(
        "l10n.br.sped.ecd.i555",
        "parent_i550_id",
        string="TOTAIS NO LIVRO RAZÃO AUXILIAR COM LEIAUTE PARAMETRIZÁVEL",
        help="Bloco I",
    )


class RegistroI555(models.Model):
    _name = "l10n.br.sped.ecd.i555"
    _description = u"""TOTAIS NO LIVRO RAZÃO AUXILIAR COM LEIAUTE PARAMETRIZÁVEL"""
    _inherit = "l10n.br.sped.mixin"
    parent_i550_id = fields.Many2one(
        "l10n.br.sped.ecd.i550",
        string="DETALHES DO LIVRO RAZÃO AUXILIAR COM LEIAUTE PARAMETRIZÁVEL",
    )


class RegistroJ005(models.Model):
    _name = "l10n.br.sped.ecd.j005"
    _description = u"""DEMONSTRAÇÕES CONTÁBEIS"""
    _inherit = "l10n.br.sped.mixin"
    dt_ini = fields.Integer("Data inicial das demonstrações contábeis", required=True)
    dt_fin = fields.Integer("Data final das demonstrações contábeis.", required=True)
    id_dem = fields.Integer("Identificação das demonstrações", required=True)
    cab_dem = fields.Char(
        "Cabeçalho das demonstrações.",
        help="""Cabeçalho das demonstrações.
Ver pagina 130""",
    )
    reg_j100_ids = fields.One2many(
        "l10n.br.sped.ecd.j100",
        "parent_j005_id",
        string="BALANÇO PATRIMONIAL",
        help="Bloco J",
    )
    reg_j150_ids = fields.One2many(
        "l10n.br.sped.ecd.j150",
        "parent_j005_id",
        string="DEMONSTRAÇÃO DOS RESULTADOS",
        help="Bloco J",
    )
    reg_j200_ids = fields.One2many(
        "l10n.br.sped.ecd.j200",
        "parent_j005_id",
        string="TABELA  DE  HISTÓRICO  DE  FATOS  CONTÁBEIS  QUE  MODIFICAM  A  CONTA LUCROS ACUMULADOS OU A CONTA PREJUÍZOS ACUMULADOS OU TODO O PATRIMÔNIO LÍQUIDO",
        help="Bloco J",
    )
    reg_j210_ids = fields.One2many(
        "l10n.br.sped.ecd.j210",
        "parent_j005_id",
        string="DE OU DEMONSTRAÇÃO LUCROS PREJUÍZOS ACUMULADOS DO (DLPA)/DEMONSTRAÇÃO DE  MUTAÇÕES PATRIMÔNIO LÍQUIDO (DMPL)",
        help="Bloco J",
    )
    reg_j800_ids = fields.One2many(
        "l10n.br.sped.ecd.j800",
        "parent_j005_id",
        string="OUTRAS INFORMAÇÕES",
        help="Bloco J",
    )
    reg_j801_ids = fields.One2many(
        "l10n.br.sped.ecd.j801",
        "parent_j005_id",
        string="TERMO DE VERIFICAÇÃO PARA FINS DE SUBSTITUIÇÃO DA ECD",
        help="Bloco J",
    )


class RegistroJ100(models.Model):
    _name = "l10n.br.sped.ecd.j100"
    _description = u"""BALANÇO PATRIMONIAL"""
    _inherit = "l10n.br.sped.mixin"
    cod_agl = fields.Char(
        "Código de aglutinação das contas, atribuído pela pessoa jurídica",
        required=True,
        help="""Código de aglutinação das contas, atribuído pela pessoa jurídica.
Ver pagina 132""",
    )
    nivel_agl = fields.Integer("NIVEL_AGL", required=True)
    ind_grp_bal = fields.Char(
        "Indicador de grupo do balanço",
        required=True,
        help="""Indicador de grupo do balanço: 1 – Ativo; 2 – Passivo e Patrimônio Líquido;
Ver pagina 132""",
    )
    descr_cod_agl = fields.Char(
        "Descrição do Código de aglutinação.",
        required=True,
        help="""Descrição do Código de aglutinação.
Ver pagina 132""",
    )
    vl_cta = fields.Monetary("VL_CTA", required=True, digits=2)
    ind_dc_bal = fields.Char(
        "Indicador da situação do saldo informado no campo anterior",
        required=True,
        help="""Indicador da situação do saldo informado no campo anterior: D - Devedor; C – Credor.
Ver pagina 132""",
    )
    vl_cta_ini = fields.Monetary("VL_CTA_INI", required=True, digits=2)
    ind_dc_bal_ini = fields.Char(
        "IND_DC_BAL_INI",
        required=True,
        help="""Indicador da situação do saldo inicial informado no campo anterior:
Ver pagina 133""",
    )
    nota_exp_ref = fields.Char(
        "Notas explicativas relativas às demonstrações contábeis",
        help="""Notas explicativas relativas às demonstrações contábeis. bservação: Informar um   O
Ver pagina 133""",
    )
    parent_j005_id = fields.Many2one(
        "l10n.br.sped.ecd.j005", string="DEMONSTRAÇÕES CONTÁBEIS"
    )


class RegistroJ150(models.Model):
    _name = "l10n.br.sped.ecd.j150"
    _description = u"""DEMONSTRAÇÃO DOS RESULTADOS"""
    _inherit = "l10n.br.sped.mixin"
    cod_agl = fields.Char(
        "Código de aglutinação das contas, atribuído pela pessoa jurídica",
        help="""Código de aglutinação das contas, atribuído pela pessoa jurídica.
Ver pagina 136""",
    )
    nivel_agl = fields.Integer("NIVEL_AGL", required=True)
    descr_cod_agl = fields.Char(
        "Descrição do Código de aglutinação.",
        required=True,
        help="""Descrição do Código de aglutinação.
Ver pagina 136""",
    )
    vl_cta = fields.Monetary("VL_CTA", required=True, digits=2)
    ind_vl = fields.Char(
        "Indicador da situação do valor informado no campo anterior",
        required=True,
        help="""Indicador da situação do valor informado no campo anterior: D - Despesa ou valor que represente parcela redutora do lucro; R - Receita ou valor que represente incremento do lucro; P - Subtotal ou total positivo; N – Subtotal ou total negativo.
Ver pagina 136""",
    )
    vl_cta_ult_dre = fields.Monetary("VL_CTA_ULT_DRE", digits=2)
    ind_vl_ult_dre = fields.Char(
        "Indicador da situação do valor informado no campo anterior",
        help="""Indicador da situação do valor informado no campo anterior: D - Despesa ou valor que represente parcela redutora do lucro; R - Receita ou valor que represente incremento do lucro; P - Subtotal ou total positivo; N – Subtotal ou
Ver pagina 137""",
    )
    nota_exp_ref = fields.Char(
        "Notas explicativas relativas às demonstrações contábeis",
        help="""Notas explicativas relativas às demonstrações contábeis. bservação: Informar um   O
Ver pagina 137""",
    )
    parent_j005_id = fields.Many2one(
        "l10n.br.sped.ecd.j005", string="DEMONSTRAÇÕES CONTÁBEIS"
    )


class RegistroJ200(models.Model):
    _name = "l10n.br.sped.ecd.j200"
    _description = u"""TABELA  DE  HISTÓRICO  DE  FATOS  CONTÁBEIS  QUE  MODIFICAM  A  CONTA LUCROS ACUMULADOS OU A CONTA PREJUÍZOS ACUMULADOS OU TODO O PATRIMÔNIO LÍQUIDO"""
    _inherit = "l10n.br.sped.mixin"
    cod_hist_fat = fields.Char(
        "Código do histórico do fato contábil.",
        required=True,
        help="""Código do histórico do fato contábil.
Ver pagina 139""",
    )
    desc_fat = fields.Char(
        "Descrição do fato contábil.",
        required=True,
        help="""Descrição do fato contábil.
Ver pagina 139""",
    )
    parent_j005_id = fields.Many2one(
        "l10n.br.sped.ecd.j005", string="DEMONSTRAÇÕES CONTÁBEIS"
    )


class RegistroJ210(models.Model):
    _name = "l10n.br.sped.ecd.j210"
    _description = u"""DE OU DEMONSTRAÇÃO LUCROS PREJUÍZOS ACUMULADOS DO (DLPA)/DEMONSTRAÇÃO DE  MUTAÇÕES PATRIMÔNIO LÍQUIDO (DMPL)"""
    _inherit = "l10n.br.sped.mixin"
    ind_tip = fields.Integer("Indicador do tipo de demonstração", required=True)
    cod_agl = fields.Char(
        "COD_AGL",
        required=True,
        help="""Código de aglutinação das contas do patrimônio líquido, atribuído pela empresa.
Ver pagina 140""",
    )
    descr_cod_agl = fields.Char(
        "Descrição do código de aglutinação",
        required=True,
        help="""Descrição do código de aglutinação
Ver pagina 140""",
    )
    vl_cta = fields.Monetary("VL_CTA", required=True, digits=2)
    ind_dc_cta = fields.Char(
        "Indicador da situação do saldo final informado no campo anterior",
        required=True,
        help="""Indicador da situação do saldo final informado no campo anterior: D – Devedor C – Credor
Ver pagina 140""",
    )
    vl_cta_ini = fields.Monetary("Saldo inicial do", required=True, digits=2)
    ind_dc_cta_ini = fields.Char(
        "Indicador da",
        required=True,
        help="""Indicador da
Ver pagina 141""",
    )
    notas_exp_ref = fields.Char(
        "Notas explicativas relativas às demonstrações contábeis",
        help="""Notas explicativas relativas às demonstrações contábeis. bservação: Informar um   O
Ver pagina 141""",
    )
    parent_j005_id = fields.Many2one(
        "l10n.br.sped.ecd.j005", string="DEMONSTRAÇÕES CONTÁBEIS"
    )
    reg_j215_ids = fields.One2many(
        "l10n.br.sped.ecd.j215",
        "parent_j210_id",
        string="FATO  CONTÁBIL  QUE  ALTERA  A  CONTA  LUCROS  ACUMULADOS  OU  A CONTA PREJUÍZOS ACUMULADOS OU O PATRIMÔNIO LÍQUIDO",
        help="Bloco J",
    )


class RegistroJ215(models.Model):
    _name = "l10n.br.sped.ecd.j215"
    _description = u"""FATO  CONTÁBIL  QUE  ALTERA  A  CONTA  LUCROS  ACUMULADOS  OU  A CONTA PREJUÍZOS ACUMULADOS OU O PATRIMÔNIO LÍQUIDO"""
    _inherit = "l10n.br.sped.mixin"
    cod_hist_fat = fields.Char(
        "Código do histórico do fato contábil.",
        required=True,
        help="""Código do histórico do fato contábil.
Ver pagina 144""",
    )
    vl_fat_cont = fields.Monetary("Valor do fato contábil.", required=True, digits=2)
    ind_dc_fat = fields.Char(
        "Indicador de situação do saldo informado no campo anterior",
        required=True,
        help="""Indicador de situação do saldo informado no campo anterior: D – Devedor C – Credor P – Subtotal ou total positivo N – Subtotal ou total negativo
Ver pagina 144""",
    )
    parent_j210_id = fields.Many2one(
        "l10n.br.sped.ecd.j210",
        string="DE OU DEMONSTRAÇÃO LUCROS PREJUÍZOS ACUMULADOS DO (DLPA)/DEMONSTRAÇÃO DE  MUTAÇÕES PATRIMÔNIO LÍQUIDO (DMPL)",
    )


class RegistroJ800(models.Model):
    _name = "l10n.br.sped.ecd.j800"
    _description = u"""OUTRAS INFORMAÇÕES"""
    _inherit = "l10n.br.sped.mixin"
    tipo_doc = fields.Char(
        "Tipo de documento",
        required=True,
        help="""Tipo de documento: 001: Demonstração do Resultado Abrangente do Período 002: Demonstração dos Fluxos de Caixa 003: Demonstração do Valor Adicionado 010: Notas Explicativas 011: Relatório da Administração 012: Parecer dos Auditores 099: Outros
Ver pagina 146""",
    )
    desc_rtf = fields.Char(
        "Descrição do arquivo .rtf.",
        help="""Descrição do arquivo .rtf.
Ver pagina 146""",
    )
    hash_rtf = fields.Char(
        "Hash do arquivo ",
        help="""Hash do arquivo .rtf incluído. Observação: O HASH é preenchido automaticamente pelo sistema (não é editável e não pode ser alterado).
Ver pagina 147""",
    )
    arq_rtf = fields.Char(
        "ARQ_RTF",
        required=True,
        help="""Sequência de bytes que representem um único  arquivo no formato RTF (Rich Text Format).
Ver pagina 147""",
    )
    ind_fim_rtf = fields.Char(
        "Indicador de fim do arquivo RTF",
        required=True,
        help="""Indicador de fim do arquivo RTF. Texto fixo contendo “J800FIM”.
Ver pagina 147""",
    )
    parent_j005_id = fields.Many2one(
        "l10n.br.sped.ecd.j005", string="DEMONSTRAÇÕES CONTÁBEIS"
    )


class RegistroJ801(models.Model):
    _name = "l10n.br.sped.ecd.j801"
    _description = u"""TERMO DE VERIFICAÇÃO PARA FINS DE SUBSTITUIÇÃO DA ECD"""
    _inherit = "l10n.br.sped.mixin"
    tipo_doc = fields.Char(
        "Tipo de documento",
        required=True,
        help="""Tipo de documento: 001: Termo de Verificação para Fins Substituição da ECD
Ver pagina 149""",
    )
    desc_rtf = fields.Char(
        "Descrição do arquivo .rtf.",
        help="""Descrição do arquivo .rtf.
Ver pagina 149""",
    )
    hash_rtf = fields.Char(
        "Hash do arquivo ",
        help="""Hash do arquivo .rtf incluído. Observação: O HASH é preenchido automaticamente pelo sistema (não é editável e não pode ser alterado).
Ver pagina 149""",
    )
    arq_rtf = fields.Char(
        "ARQ_RTF",
        required=True,
        help="""Sequência de bytes que representem um único arquivo no formato RTF (Rich Text Format).
Ver pagina 149""",
    )
    ind_fim_rtf = fields.Char(
        "Indicador de fim do arquivo RTF",
        required=True,
        help="""Indicador de fim do arquivo RTF. Texto fixo contendo “J801FIM”.
Ver pagina 149""",
    )
    parent_j005_id = fields.Many2one(
        "l10n.br.sped.ecd.j005", string="DEMONSTRAÇÕES CONTÁBEIS"
    )


class RegistroJ900(models.Model):
    _name = "l10n.br.sped.ecd.j900"
    _description = u"""TERMO DE ENCERRAMENTO"""
    _inherit = "l10n.br.sped.mixin"
    dnrc_encer = fields.Char(
        "Texto fixo contendo “TERMO DE ENCERRAMENTO”",
        required=True,
        help="""Texto fixo contendo “TERMO DE ENCERRAMENTO”.
Ver pagina 151""",
    )
    num_ord = fields.Integer(
        "Número de ordem do instrumento de escrituração", required=True
    )
    nat_livro = fields.Char(
        "Natureza do livro; finalidade a que se destinou o instrumento",
        required=True,
        help="""Natureza do livro; finalidade a que se destinou o instrumento.
Ver pagina 151""",
    )
    nome = fields.Char(
        "Nome empresarial.",
        required=True,
        help="""Nome empresarial.
Ver pagina 151""",
    )
    qtd_lin = fields.Integer(
        "Quantidade total de linhas do arquivo digital", required=True
    )
    dt_ini_escr = fields.Integer("Data de início da escrituração.", required=True)
    dt_fin_escr = fields.Integer("Data de término da escrituração.", required=True)
    reg_j930_ids = fields.One2many(
        "l10n.br.sped.ecd.j930",
        "parent_j900_id",
        string="IDENTIFICAÇÃO  DOS  SIGNATÁRIOS  DA  ESCRITURAÇÃO  E  DO  TERMO  DE VERIFICAÇÃO PARA FINS DE SUBSTITUIÇÃO DA ECD",
        help="Bloco J",
    )
    reg_j935_ids = fields.One2many(
        "l10n.br.sped.ecd.j935",
        "parent_j900_id",
        string="IDENTIFICAÇÃO DOS AUDITORES INDEPENDENTES",
        help="Bloco J",
    )


class RegistroJ930(models.Model):
    _name = "l10n.br.sped.ecd.j930"
    _description = u"""IDENTIFICAÇÃO  DOS  SIGNATÁRIOS  DA  ESCRITURAÇÃO  E  DO  TERMO  DE VERIFICAÇÃO PARA FINS DE SUBSTITUIÇÃO DA ECD"""
    _inherit = "l10n.br.sped.mixin"
    ident_nom = fields.Char(
        "Nome do signatário.",
        required=True,
        help="""Nome do signatário.
Ver pagina 155""",
    )
    ident_cpf_cnpj = fields.Integer("CPF ou CNPJ", required=True)
    ident_qualif = fields.Char(
        "Qualificação do assinante, conforme tabela",
        required=True,
        help="""Qualificação do assinante, conforme tabela.
Ver pagina 156""",
    )
    cod_assin = fields.Char(
        "Código de qualificação do assinante, conforme tabela",
        required=True,
        help="""Código de qualificação do assinante, conforme tabela.
Ver pagina 156""",
    )
    ind_crc = fields.Char(
        "IND_CRC",
        help="""Número de inscrição do contabilista no Conselho Regional de Contabilidade.
Ver pagina 156""",
    )
    email = fields.Char(
        "Email do signatário.",
        help="""Email do signatário.
Ver pagina 156""",
    )
    fone = fields.Char(
        "Telefone do signatário.",
        help="""Telefone do signatário.
Ver pagina 156""",
    )
    uf_crc = fields.Char(
        "Indicação da unidade da federação que expediu o CRC",
        help="""Indicação da unidade da federação que expediu o CRC.
Ver pagina 156""",
    )
    num_seq_crc = fields.Char(
        "Número sequencial no seguinte formato",
        help="""Número sequencial no seguinte formato:  UF/ano/número
Ver pagina 156""",
    )
    dt_crc = fields.Integer("Data de validade do CRC do contador.")
    ind_resp_legal = fields.Char(
        "IND_RESP_LEGAL",
        required=True,
        help="""Identificação do signatário que será validado como responsável pela assinatura da ECD, conforme atos societários: S – Sim N – Não
Ver pagina 156""",
    )
    parent_j900_id = fields.Many2one(
        "l10n.br.sped.ecd.j900", string="TERMO DE ENCERRAMENTO"
    )


class RegistroJ935(models.Model):
    _name = "l10n.br.sped.ecd.j935"
    _description = u"""IDENTIFICAÇÃO DOS AUDITORES INDEPENDENTES"""
    _inherit = "l10n.br.sped.mixin"
    nome_auditor = fields.Char(
        "Nome do auditor independente.",
        required=True,
        help="""Nome do auditor independente.
Ver pagina 159""",
    )
    cod_cvm_auditor = fields.Char(
        "Registro do auditor independente na CVM",
        required=True,
        help="""Registro do auditor independente na CVM.
Ver pagina 159""",
    )
    parent_j900_id = fields.Many2one(
        "l10n.br.sped.ecd.j900", string="TERMO DE ENCERRAMENTO"
    )


class RegistroK030(models.Model):
    _name = "l10n.br.sped.ecd.k030"
    _description = u"""PERÍODO DA ESCRITURAÇÃO CONTÁBIL CONSOLIDADA"""
    _inherit = "l10n.br.sped.mixin"
    dt_ini = fields.Integer("Data inicial do período consolidado.", required=True)
    dt_fin = fields.Integer("Data final do período consolidado.", required=True)
    reg_k100_ids = fields.One2many(
        "l10n.br.sped.ecd.k100",
        "parent_k030_id",
        string="RELAÇÃO DAS EMPRESAS CONSOLIDADAS",
        help="Bloco K",
    )


class RegistroK100(models.Model):
    _name = "l10n.br.sped.ecd.k100"
    _description = u"""RELAÇÃO DAS EMPRESAS CONSOLIDADAS"""
    _inherit = "l10n.br.sped.mixin"
    cod_pais = fields.Integer("COD_PAIS", required=True)
    emp_cod = fields.Integer(
        "Código de identificação da empresa participante", required=True
    )
    cnpj = fields.Integer("CNPJ (somente os 8 primeiros dígitos).")
    nome = fields.Char(
        "Nome empresarial.",
        required=True,
        help="""Nome empresarial.
Ver pagina 163""",
    )
    per_part = fields.Monetary("PER_PART", required=True, digits=4)
    evento = fields.Char(
        "Evento societário ocorrido no período",
        required=True,
        help="""Evento societário ocorrido no período: S - Sim N – Não
Ver pagina 164""",
    )
    per_cons = fields.Monetary("PER_CONS", required=True, digits=4)
    data_ini_emp = fields.Integer("DATA_INI_EMP", required=True)
    data_fin_emp = fields.Integer("DATA_FIN_EMP", required=True)
    parent_k030_id = fields.Many2one(
        "l10n.br.sped.ecd.k030", string="PERÍODO DA ESCRITURAÇÃO CONTÁBIL CONSOLIDADA"
    )
    reg_k110_ids = fields.One2many(
        "l10n.br.sped.ecd.k110",
        "parent_k100_id",
        string="RELAÇÃO DOS EVENTOS SOCIETÁRIOS",
        help="Bloco K",
    )


class RegistroK110(models.Model):
    _name = "l10n.br.sped.ecd.k110"
    _description = u"""RELAÇÃO DOS EVENTOS SOCIETÁRIOS"""
    _inherit = "l10n.br.sped.mixin"
    evento = fields.Integer("Evento societário ocorrido no período", required=True)
    dt_evento = fields.Integer("Data do evento societário.", required=True)
    parent_k100_id = fields.Many2one(
        "l10n.br.sped.ecd.k100", string="RELAÇÃO DAS EMPRESAS CONSOLIDADAS"
    )
    reg_k115_ids = fields.One2many(
        "l10n.br.sped.ecd.k115",
        "parent_k110_id",
        string="EMPRESAS PARTICIPANTES DO EVENTO SOCIETÁRIO",
        help="Bloco K",
    )


class RegistroK115(models.Model):
    _name = "l10n.br.sped.ecd.k115"
    _description = u"""EMPRESAS PARTICIPANTES DO EVENTO SOCIETÁRIO"""
    _inherit = "l10n.br.sped.mixin"
    emp_cod_part = fields.Integer(
        "Código da empresa envolvida na operação", required=True
    )
    cond_part = fields.Integer(
        "Condição da empresa relacionada à operação", required=True
    )
    per_evt = fields.Monetary(
        "Percentual da empresa participante envolvida na operação",
        required=True,
        digits=4,
    )
    parent_k110_id = fields.Many2one(
        "l10n.br.sped.ecd.k110", string="RELAÇÃO DOS EVENTOS SOCIETÁRIOS"
    )


class RegistroK200(models.Model):
    _name = "l10n.br.sped.ecd.k200"
    _description = u"""PLANO DE CONTAS CONSOLIDADO"""
    _inherit = "l10n.br.sped.mixin"
    cod_nat = fields.Char(
        "COD_NAT",
        required=True,
        help="""Código da natureza da conta/grupo de contas, conforme tabela publicada pelo Sped.
Ver pagina 171""",
    )
    ind_cta = fields.Char(
        "Indicador do tipo de conta",
        required=True,
        help="""Indicador do tipo de conta: S - Sintética (grupo de contas); A - Analítica (conta).
Ver pagina 171""",
    )
    nivel = fields.Integer("Nível da conta", required=True)
    cod_cta = fields.Char(
        "Código da conta",
        required=True,
        help="""Código da conta
Ver pagina 171""",
    )
    cod_cta_sup = fields.Char(
        "Código da conta superior",
        help="""Código da conta superior
Ver pagina 171""",
    )
    cta = fields.Char(
        "Nome da conta",
        required=True,
        help="""Nome da conta
Ver pagina 171""",
    )
    reg_k210_ids = fields.One2many(
        "l10n.br.sped.ecd.k210",
        "parent_k200_id",
        string="MAPEAMENTO PARA O PLANO DE CONTAS DAS EMPRESAS CONSOLIDADAS",
        help="Bloco K",
    )
    reg_k300_ids = fields.One2many(
        "l10n.br.sped.ecd.k300",
        "parent_k200_id",
        string="SALDOS DAS CONTAS CONSOLIDADAS",
        help="Bloco K",
    )


class RegistroK210(models.Model):
    _name = "l10n.br.sped.ecd.k210"
    _description = u"""MAPEAMENTO PARA O PLANO DE CONTAS DAS EMPRESAS CONSOLIDADAS"""
    _inherit = "l10n.br.sped.mixin"
    cod_emp = fields.Integer(
        "Código de identificação da empresa participante", required=True
    )
    cod_cta_emp = fields.Char(
        "Código da conta da empresa participante",
        required=True,
        help="""Código da conta da empresa participante
Ver pagina 174""",
    )
    parent_k200_id = fields.Many2one(
        "l10n.br.sped.ecd.k200", string="PLANO DE CONTAS CONSOLIDADO"
    )


class RegistroK300(models.Model):
    _name = "l10n.br.sped.ecd.k300"
    _description = u"""SALDOS DAS CONTAS CONSOLIDADAS"""
    _inherit = "l10n.br.sped.mixin"
    cod_cta = fields.Char(
        "Código da conta consolidada",
        required=True,
        help="""Código da conta consolidada
Ver pagina 175""",
    )
    val_ag = fields.Monetary("Valor absoluto aglutinado", required=True, digits=2)
    ind_val_ag = fields.Char(
        "Indicador da situação do valor aglutinado",
        required=True,
        help="""Indicador da situação do valor aglutinado: D – Devedor C – Credor
Ver pagina 175""",
    )
    val_el = fields.Monetary("Valor absoluto das eliminações", required=True, digits=2)
    ind_val_el = fields.Char(
        "Indicador da situação do valor eliminado",
        required=True,
        help="""Indicador da situação do valor eliminado: D – Devedor C – Credor
Ver pagina 175""",
    )
    val_cs = fields.Monetary("Valor absoluto consolidado", required=True, digits=2)
    ind_val_cs = fields.Char(
        "Indicador da situação do valor consolidado",
        required=True,
        help="""Indicador da situação do valor consolidado: D – Devedor C – Credor
Ver pagina 175""",
    )
    parent_k200_id = fields.Many2one(
        "l10n.br.sped.ecd.k200", string="PLANO DE CONTAS CONSOLIDADO"
    )
    reg_k310_ids = fields.One2many(
        "l10n.br.sped.ecd.k310",
        "parent_k300_id",
        string="EMPRESAS DETENTORAS DAS PARCELAS DO VALOR ELIMINADO TOTAL",
        help="Bloco K",
    )


class RegistroK310(models.Model):
    _name = "l10n.br.sped.ecd.k310"
    _description = u"""EMPRESAS DETENTORAS DAS PARCELAS DO VALOR ELIMINADO TOTAL"""
    _inherit = "l10n.br.sped.mixin"
    emp_cod_parte = fields.Integer("EMP_COD_PARTE", required=True)
    valor = fields.Monetary("Parcela do valor eliminado total", required=True, digits=2)
    ind_valor = fields.Char(
        "Indicador da situação do valor eliminado",
        required=True,
        help="""Indicador da situação do valor eliminado: D – Devedor C – Credor
Ver pagina 177""",
    )
    parent_k300_id = fields.Many2one(
        "l10n.br.sped.ecd.k300", string="SALDOS DAS CONTAS CONSOLIDADAS"
    )
    reg_k315_ids = fields.One2many(
        "l10n.br.sped.ecd.k315",
        "parent_k310_id",
        string="EMPRESAS CONTRAPARTES DAS PARCELAS DO VALOR ELIMINADO TOTAL",
        help="Bloco K",
    )


class RegistroK315(models.Model):
    _name = "l10n.br.sped.ecd.k315"
    _description = u"""EMPRESAS CONTRAPARTES DAS PARCELAS DO VALOR ELIMINADO TOTAL"""
    _inherit = "l10n.br.sped.mixin"
    emp_cod_contra = fields.Integer("Código da empresa da contrapartida", required=True)
    cod_contra = fields.Char(
        "Código da conta consolidada da contrapartida",
        required=True,
        help="""Código da conta consolidada da contrapartida
Ver pagina 179""",
    )
    valor = fields.Monetary(
        "Parcela da contrapartida do valor eliminado total", required=True, digits=2
    )
    ind_valor = fields.Char(
        "Indicador da situação do valor eliminado",
        required=True,
        help="""Indicador da situação do valor eliminado: D – Devedor C – Credor
Ver pagina 179""",
    )
    parent_k310_id = fields.Many2one(
        "l10n.br.sped.ecd.k310",
        string="EMPRESAS DETENTORAS DAS PARCELAS DO VALOR ELIMINADO TOTAL",
    )


class Registro9900(models.Model):
    _name = "l10n.br.sped.ecd.9900"
    _description = u"""REGISTROS DO ARQUIVO"""
    _inherit = "l10n.br.sped.mixin"
    reg_blc = fields.Char(
        "Registro que será totalizado no próximo campo",
        required=True,
        help="""Registro que será totalizado no próximo campo.
Ver pagina 183""",
    )
    qtd_reg_blc = fields.Integer(
        "Total de registros do tipo informado no campo anterior", required=True
    )


class Registro9999(models.Model):
    _name = "l10n.br.sped.ecd.9999"
    _description = u"""ENCERRAMENTO DO ARQUIVO DIGITAL"""
    _inherit = "l10n.br.sped.mixin"
    qtd_lin = fields.Integer(
        "Quantidade total de linhas do arquivo digital", required=True
    )
