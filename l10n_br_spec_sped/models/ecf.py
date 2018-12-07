# -*- coding: utf-8 -*-

from odoo import models, fields

from . import spec_models


class Registro0000(models.Model):
    _name = 'l10n.br.sped.ecf.0000'
    _description = u"""Abertura do Arquivo Digital e Identificação da Pessoa Jurídica"""
    _inherit = 'l10n.br.sped.mixin'
    nome_esc = fields.Char("Texto fixo contendo a identificação do tipo de Sped (LECF)", required=True,
        help="""Texto fixo contendo a identificação do tipo de Sped (LECF).
Ver pagina 48""")
    cod_ver = fields.Char("Código da versão do leiaute", required=True,
        help="""Código da versão do leiaute. Observação: Para o ano-calendário 2017 e situações especiais de 2018, o leiaute é o 0004.
Ver pagina 48""")
    cnpj = fields.Integer("CNPJ", required=True)
    nome = fields.Char("NOME", required=True,
        help="""Nome empresarial da pessoa jurídica ou da Sociedade em Conta de Participação (SCP).
Ver pagina 49""")
    ind_sit_ini_per = fields.Integer("Indicador do Início do Período", required=True)
    sit_especial = fields.Char("Indicador de Situação Especial e Outros Eventos", required=True,
        help="""Indicador de Situação Especial e Outros Eventos:  0 – Normal (Sem ocorrência de situação especial ou evento)  1 – Extinção 2 – Fusão 3 – Incorporação \ Incorporada 4 – Incorporação \ Incorporadora 5 – Cisão Total 6 – Cisão Parcial 8 – Desenquadramento de Imune/Isenta;  9 – Inclusão no Simples Nacional
Ver pagina 49""")
    pat_reman_cis = fields.Monetary("Patrimônio Remanescente em Caso de Cisão (%)", digits=4)
    dt_sit_esp = fields.Integer("Data da Situação Especial ou Evento")
    dt_ini = fields.Integer("Data do Início do Período", required=True)
    dt_fin = fields.Integer("Data do Fim do Período", required=True)
    retificadora = fields.Char("RETIFICADORA", required=True,
        help="""A pessoa jurídica deve assinalar este campo no caso de escrituração retificadora ou escrituração com mudança de forma de tributação: S – ECF retificadora N – ECF original F – ECF original com mudança de forma de tributação (Art. 5º da Instrução Normativa nº 166/1999). A pessoa jurídica poderá efetuar a remessa de arquivo em retificação ao arquivo anteriormente remetido, observando-se a permissão, as regras e prazos estabelecidos pela Secretaria da Receita Federal do Brasil (RFB).  Atenção: A substituição das ECF já transmitidas deverá ser feita na sua íntegra, pois a ECF não aceita arquivos complementares para o mesmo período informado. Como há controle de saldos, se houver substituição de uma ECF, pode haver a necessidade de substituição de ECF já transmitidas de anos posteriores.
Ver pagina 50""")
    num_rec = fields.Char("Número do Recibo da ECF Anterior (hashcode)",
        help="""Número do Recibo da ECF Anterior (hashcode): Este campo deve ser preenchido com o número constante no recibo de entrega da última ECF transmitida, nos casos de 0000.RETIFICADORA = “S” ou “F”.
Ver pagina 50""")
    tip_ecf = fields.Integer("Indicador do Tipo da ECF", required=True)
    cod_scp = fields.Integer("CNPJ da SCP (Art")

class Registro0010(models.Model):
    _name = 'l10n.br.sped.ecf.0010'
    _description = u"""Parâmetros de Tributação"""
    _inherit = 'l10n.br.sped.mixin'
    hash_ecf_anterior = fields.Char("HASH_ECF_ANTERIOR",
        help="""Hashcode da ECF do período imediatamente anterior a ser recuperado (Escrituração da qual os saldos da parte B do e-LALUR foram recuperados).  Campo preenchido automaticamente pelo sistema.
Ver pagina 56""")
    opt_refis = fields.Char("Indicador de Optante pelo Refis", required=True,
        help="""Indicador de Optante pelo Refis: S - Sim N – Não A pessoa jurídica deve assinalar este campo quando for optante pelo Programa de Recuperação Fiscal (Refis). Atenção: Este campo só deve ser assinalado pela pessoa jurídica optante pelo Programa de Recuperação Fiscal (Refis), instituído pela Lei nº 9.964, de 10 de abril de 2000,  e que dele não tenha sido excluída. A pessoa jurídica que for apenas optante pelo Parcelamento Especial (Paes) de que trata a Lei nº 10.684, de 30 de maio de 2003, e outros reparcelamentos não deve assinalar este campo.
Ver pagina 56""")
    opt_paes = fields.Char("Indicador de Optante pelo Paes", required=True,
        help="""Indicador de Optante pelo Paes: S – Sim N – Não A pessoa jurídica deve assinalar este campo quando for optante pelo Parcelamento Especial (Paes), de que trata a Lei nº 10.684, de 30 de maio de 2003.
Ver pagina 57""")
    forma_trib = fields.Integer("Forma de Tributação", required=True)
    forma_apur = fields.Char("Indicador do Período de Apuração do IRPJ e da CSLL",
        help="""Indicador do Período de Apuração do IRPJ e da CSLL: T – Trimestral A – Anual
Ver pagina 58""")
    cod_qualif_pj = fields.Integer("Qualificação da Pessoa Jurídica")
    forma_trib_per = fields.Char("Forma de Tributação no Período",
        help="""Forma de Tributação no Período: Forma de tributação no período considerando para cada trimestre no formato XXXX onde X é igual a: 0 – ZERO – Não informado – trimestre não compreendido no período de apuração. R – Real P – Presumido  A – Arbitrado  E – Real Estimativa Observação: Caso 0010.FORMA_TRIB seja igual “3” (Presumido/Real) ou “4” (Presumido/Real/Arbitrado) e houver opção pelo REFIS (0010.OPT_REFIS), o período tributado pelo lucro real deve ter somente a forma de apuração trimestral (Caso em que deve ser utilizado “R” em 0010.FORMA_TRIB_PER) ou somente a forma de apuração correspondente à anual/estimativa (Caso em que deve ser utilizado “E” em 0010.FORMA_TRIB_PER) .
Ver pagina 58""")
    mes_bal_red = fields.Char("Forma de Apuração da Estimativa Mensal",
        help="""Forma de Apuração da Estimativa Mensal: Indicação da forma de apuração da estimativa mensal, quando 0010.FORMA_APUR = “A”, considerando o formato  XXXXXXXXXXXX onde X é referente a um mês e é igual a: 0 –  Fora do Período: Fora do período de apuração/ Forma de tributação diferente de “R” ou “E”. E – Receita Bruta: Estimativa com base na receita bruta e acréscimos. B – Balanço ou Balancete: Estimativa com base no balanço ou balancete de suspensão/redução. Os meses correspondentes a trimestres marcados em 0010.FORMA_TRIB_PER como diferente de “R” e “E” devem estar preenchidos com zero “0”.  Os meses correspondentes a trimestres marcados em 0010.FORMA_TRIB_PER iguais a “R” ou “E” devem estar preenchidos com “E” ou “B”.
Ver pagina 59""")
    tip_esc_pre = fields.Char("TIP_ESC_PRE",
        help="""Escrituração: C – Obrigada a entregar a ECD ou entrega facultativa (haverá recuperação dos dados). L – Não obrigada a entregar a ECD/Livro Caixa (Opção do Lucro Presumido - parágrafo único do art. 45 da Lei nº 8.981, de 1995). tenção:  - Este campo deve ser preenchido pelas pessoas jurídicas tributadas pelo lucro presumido e as imunes ou isentas. - Caso a pessoa jurídica entregue a ECD facultativamente e não queira recuperar os dados da ECD, deve utilizar a opção “L”.   A
Ver pagina 59""")
    tip_ent = fields.Integer("Tipo de Pessoa Jurídica Imune ou Isenta")
    forma_apur_i = fields.Char("Apuração do IRPJ para Imunes ou Isentas",
        help="""Apuração do IRPJ para Imunes ou Isentas: Existência ou não de atividade não abrangida pela imunidade ou isenção e tributada pelo IRPJ (para imunes ou isentas): A – Anual  T – Trimestral D – Desobrigada
Ver pagina 60""")
    apur_csll = fields.Char("Apuração da CSLL para Imunes ou Isentas",
        help="""Apuração da CSLL para Imunes ou Isentas: A – Anual, se optou pela apuração da CSLL sobre a base de cálculo estimada, facultada a opção pelo levantamento de balanço ou balancete de suspensão ou redução. T – Trimestral, no caso de ter adotado a apuração trimestral da CSLL. D – Desobrigada, na hipótese de pessoa jurídica imune ou isenta da CSLL. Atenção: 1) As entidades sem fins lucrativos de que trata o inciso I do art. 12 do Decreto nº 3.048, de 6 de maio de 1999, que não se enquadram na imunidade e isenção da Lei nº 9.532, de 10 de dezembro de 1997, estão sujeitas à CSLL, devendo apurar a base de cálculo e a contribuição devida nos termos da legislação comercial. 2) As associações de poupança e empréstimo devem apurar a contribuição social sobre o lucro líquido. 3) São isentas da CSLL as entidades fechadas de previdência complementar, relativamente aos fatos geradores ocorridos a partir de 1º de janeiro de 2002. Observação: Este campo é obrigatório para 0010.FORMA_TRIB igual a “8” (Imune do IRPJ) ou “9” (Isenta do IRPJ).
Ver pagina 61""")
    ind_rec_receita = fields.Integer("IND_REC_RECEITA")

class Registro0020(models.Model):
    _name = 'l10n.br.sped.ecf.0020'
    _description = u"""Parâmetros Complementares"""
    _inherit = 'l10n.br.sped.mixin'
    ind_aliq_csll = fields.Integer("PJ Sujeita à Alíquota da CSLL de 9% ou 17% ou 20% em 31/12/2015", required=True)
    ind_qte_scp = fields.Integer("Quantidade total de SCP do Sócio Ostensivo de SCP", required=True)
    ind_adm_fun_clu = fields.Char("Administradora de Fundos e Clubes de Investimento", required=True,
        help="""Administradora de Fundos e Clubes de Investimento: S – Sim N – Não
Ver pagina 65""")
    ind_part_cons = fields.Char("Participações em Consórcios de Empresas", required=True,
        help="""Participações em Consórcios de Empresas: S – Sim N – Não A pessoa jurídica participante de consórcio constituído nos termos do disposto nos arts. 278 e 279 da Lei nº 6.404, de 15 de dezembro de 1976, deve assinalar este campo. Atenção: Somente deve ser assinalado este campo quando houver receita de pelo menos uma consorciada.
Ver pagina 66""")
    ind_op_ext = fields.Char("Operações com o Exterior", required=True,
        help="""Operações com o Exterior: S – Sim N – Não A pessoa jurídica, inclusive instituição financeira ou companhia seguradora, conforme relacionadas no § 1º do art. 22 da Lei nº 8.212, de 1991, e no inciso II do art. 14 da Lei nº 9.718, de 1998, que realizou exportação/importação de bens, serviços ou direitos ou auferiu receitas financeiras ou incorreu em despesas financeiras em operações efetuadas com pessoa física ou jurídica residente ou domiciliada no exterior, ainda que essas operações não tenham sido realizadas com pessoa vinculada ou com pessoa residente ou domiciliada em país ou dependência com tributação favorecida ou cuja legislação interna oponha sigilo relativo à composição societária de pessoas jurídicas ou a sua titularidade, deve assinalar este campo. Deve também assinalar este campo a pessoa jurídica, inclusive instituição financeira ou companhia seguradora, que realizar as operações acima referidas por intermédio de interposta pessoa.
Ver pagina 66""")
    ind_op_vinc = fields.Char("IND_OP_VINC", required=True,
        help="""Operações com Pessoa Vinculada/Interposta Pessoa / País com Tributação Favorecida. S – Sim N – Não Deve assinalar este campo, a pessoa jurídica, inclusive instituição financeira ou companhia seguradora, conforme relacionadas no § 1º do art. 22 da Lei nº 8.212, de 1991, e no inciso II do art. 14 da Lei nº 9.718, de 1998, que realizou exportação/importação de bens, serviços ou direitos ou auferiu receitas financeiras ou incorreu em despesas financeiras em operações efetuadas com pessoa física ou jurídica residente ou domiciliada no exterior, considerada pela legislação brasileira: a) pessoa vinculada; b) pessoa residente ou domiciliada em países com tributação favorecida ou cuja legislação interna oponha sigilo relativo à composição societária de pessoas jurídicas ou a sua titularidade; e c) a partir de 1º de janeiro de 2009, pessoa residente ou domiciliada no exterior, que goze, nos termos da legislação, de regime fiscal privilegiado (Art. 24-A da Lei nº 9.430, de 1996, instituído pela Lei nº 11.727, de 2008). Deve também assinalar este campo a pessoa jurídica, inclusive instituição financeira ou companhia seguradora, que realizar as operações acima referidas por intermédio de interposta pessoa.
Ver pagina 67""")
    ind_pj_enquad = fields.Char("IND_PJ_ENQUAD", required=True,
        help="""PJ Enquadrada nos artigos 48 ou 49 da Instrução Normativa RFB nº 1.312/2012: S – Sim N – Não
Ver pagina 67""")
    ind_part_ext = fields.Char("Participações no Exterior", required=True,
        help="""Participações no Exterior: A pessoa jurídica deve assinalar este campo, caso tenha participações no exterior. S – Sim N – Não
Ver pagina 67""")
    ind_ativ_rural = fields.Char("IND_ATIV_RURAL", required=True,
        help="""Atividade Rural: A pessoa jurídica deve assinalar este campo, caso explore atividade rural. S – Sim N – Não
Ver pagina 67""")
    ind_luc_exp = fields.Char("Existência de Lucro da Exploração", required=True,
        help="""Existência de Lucro da Exploração: S – Sim N – Não Este campo deve ser assinalado pelas pessoas jurídicas que adotam a forma de tributação pelo lucro real, inclusive se optantes pelo Refis, que gozem de benefícios fiscais calculados com base no lucro da exploração.
Ver pagina 67""")
    ind_red_isen = fields.Char("Isenção e Redução do Imposto para Lucro Presumido", required=True,
        help="""Isenção e Redução do Imposto para Lucro Presumido: S – Sim N – Não A pessoa jurídica tributada pelo lucro presumido e optante pelo Refis deve assinalar este campo caso usufrua benefícios fiscais relativos a isenção ou redução do imposto de renda.
Ver pagina 68""")
    ind_fin = fields.Char("Indicativo da Existência de FINOR/FINAM", required=True,
        help="""Indicativo da Existência de FINOR/FINAM: S – Sim N – Não Este campo deve ser assinalado pelas pessoas jurídicas ou grupos de empresas coligadas de que trata o art. 9º da Lei nº 8.167, de 1991, alterado pela Medida Provisória nº 2.199-14, de 24 de agosto de 2001, titulares de empreendimento de setor da economia considerado, em ato do Poder Executivo, prioritário para o desenvolvimento regional, aprovado ou protocolizado até 2 de maio de 2001 nas áreas da Sudam e da Sudene ou do Grupo Executivo para Recuperação Econômica do Estado do Espírito Santo (Geres) (MP nº 2.199-14, de 2001, art. 4º, e MP nº 2.145, de 2 de maio de 2001, art. 50, XX, atuais MP nº 2.156-5, de 2001, art. 32, XVIII, e nº 2.157-5, de 2001, art. 32, IV).
Ver pagina 68""")
    ind_doa_eleit = fields.Char("Doações a Campanhas Eleitorais", required=True,
        help="""Doações a Campanhas Eleitorais: S – Sim N – Não A pessoa jurídica deve assinalar este campo, caso tenha efetuado, durante o ano-calendário, doações a candidatos, comitês financeiros e partidos políticos, ainda que na forma de fornecimento de mercadorias ou prestação de serviços para campanhas eleitorais.
Ver pagina 68""")
    ind_part_colig = fields.Char("Participação Avaliada pelo Método de Equivalência Patrimonial", required=True,
        help="""Participação Avaliada pelo Método de Equivalência Patrimonial: S – Sim N – Não A pessoa jurídica domiciliada no Brasil, que teve participações permanentes, no ano-calendário, em capital de pessoa jurídica domiciliada no Brasil ou no exterior, considerada, pela legislação brasileira, avaliada pelo método de equivalência patrimonial, deve assinalar este campo.
Ver pagina 68""")
    ind_vend_exp = fields.Char("IND_VEND_EXP", required=True,
        help="""PJ Efetuou Vendas a Empresa Comercial Exportadora com Fim Específico de Exportação:  S – Sim N – Não Este campo deve ser assinalado pela pessoa jurídica que efetuou vendas, no ano-calendário, a empresas comerciais exportadoras.
Ver pagina 68""")
    ind_rec_ext = fields.Char("Recebimentos do Exterior ou de Não Residentes", required=True,
        help="""Recebimentos do Exterior ou de Não Residentes:  S – Sim N – Não Deve assinalar este campo, a pessoa jurídica que recebeu, durante o ano-calendário, de pessoas físicas ou jurídicas, residentes ou domiciliadas no exterior ou de não-residentes:  - quaisquer valores mediante operações de câmbio de qualquer natureza;  - quaisquer valores por intermédio de transferências internacionais em reais (TIR), ou seja,
Ver pagina 69""")
    ind_ativ_ext = fields.Char("Ativos no Exterior", required=True,
        help="""Ativos no Exterior: S – Sim  N – Não Preenchida por todas as pessoas jurídicas (Sim), salvo quando o valor contábil total dos ativos a declarar, convertido para Reais no final do período abrangido pela ECF, for inferior a R$ 100.000,00 (cem mil reais) (Não).
Ver pagina 69""")
    ind_com_exp = fields.Char("PJ Comercial Exportadora", required=True,
        help="""PJ Comercial Exportadora:  S – Sim  N – Não Este campo deve ser assinalado pela empresa comercial exportadora que comprou produtos com o fim específico de exportação ou exportou, no ano-calendário, produtos adquiridos com esta finalidade.
Ver pagina 69""")
    ind_pgto_ext = fields.Char("Pagamentos ao Exterior ou a Não Residentes", required=True,
        help="""Pagamentos ao Exterior ou a Não Residentes:  S – Sim  N – Não Deve assinalar este campo, a pessoa jurídica que tiver pagado, creditado, entregado, empregado ou remetido, durante o ano-calendário, a pessoas físicas ou jurídicas, residentes ou domiciliadas no exterior ou a não-residentes:  - quaisquer valores mediante operações de câmbio de qualquer natureza; - quaisquer valores por intermédio de transferências internacionais em reais (TIR), ou seja, pela utilização de reais (R$) para crédito de conta bancária titulada por não-residentes; - valores iguais ou superiores a R$ 120.000,00 (cento e vinte mil reais), equivalentes a R$ 10.000,00 por mês, por intermédio de cartões de crédito;  - quaisquer valores mediante a utilização de recursos mantidos no exterior.
Ver pagina 69""")
    ind_e_com_ti = fields.Char("Comércio Eletrônico e Tecnologia da Informação", required=True,
        help="""Comércio Eletrônico e Tecnologia da Informação:  S – Sim  N – Não A pessoa jurídica que efetuou durante o ano-calendário vendas de bens (tangíveis ou intangíveis) ou tiver prestado serviços, por meio da Internet, para pessoas físicas e jurídicas, residentes ou domiciliadas no Brasil ou no exterior, deve assinalar este campo. Ao assinalar este campo, são disponibilizados os registros X400 (Comércio Eletrônico e
Ver pagina 70""")
    ind_roy_rec = fields.Char("Royalties Recebidos do Brasil e do Exterior", required=True,
        help="""Royalties Recebidos do Brasil e do Exterior:  S – Sim  N – Não A pessoa jurídica que tiver recebido, durante o ano-calendário, de pessoas físicas ou jurídicas, residentes ou domiciliadas no Brasil ou no exterior, rendimentos a título de royalties relativos a: exploração econômica dos direitos patrimoniais do autor, de marcas, de patentes e de desenho industrial; exploração de know-how; exploração de franquias e exploração dos direitos relativos à propriedade intelectual referente a cultivares, deve preencher este campo com “Sim”.
Ver pagina 70""")
    ind_roy_pag = fields.Char("Royalties Pagos a Beneficiários do Brasil e do Exterior", required=True,
        help="""Royalties Pagos a Beneficiários do Brasil e do Exterior: S – Sim  N – Não  A pessoa jurídica que tiver efetuado pagamento ou remessa, durante o ano-calendário, a pessoas físicas ou jurídicas, residentes ou domiciliadas no Brasil ou no exterior, a título de royalties relativos a: exploração econômica dos direitos patrimoniais do autor, de marcas, de patentes e de desenho industrial; exploração de know-how; exploração de franquias e exploração dos direitos relativos à propriedade intelectual referente a cultivares, deve preencher este campo com “Sim”.
Ver pagina 70""")
    ind_rend_serv = fields.Char("IND_REND_SERV", required=True,
        help="""Rendimentos Relativos a Serviços, Juros e Dividendos Recebidos do Brasil e do Exterior:  S – Sim  N – Não A pessoa jurídica que tiver recebido, durante o ano-calendário, de pessoas físicas ou jurídicas, residentes ou domiciliadas no Brasil ou no exterior, rendimentos relativos a: serviços de assistência técnica, científica, administrativa e semelhantes que impliquem transferência de tecnologia; serviços técnicos e de assistência que não impliquem transferência de tecnologia; juros sobre capital próprio, bem como juros decorrentes de contratos de mútuo entre empresas ligadas e juros decorrentes de contratos de financiamento; dividendos decorrentes de participações em outras empresas, deve preencher este campo com “Sim”.
Ver pagina 71""")
    ind_pgto_rem = fields.Char("IND_PGTO_REM", required=True,
        help="""Pagamentos ou Remessas a Título de Serviços, Juros e Dividendos a Beneficiários do Brasil e do Exterior:  S – Sim  N – Não A pessoa jurídica que tiver pagado ou remetido, durante o ano-calendário, a pessoas físicas ou jurídicas, residentes ou domiciliadas no Brasil ou no exterior, valores relativos a: serviços de assistência técnica, científica, administrativa e semelhantes que impliquem transferência de tecnologia; serviços técnicos e de assistência que não impliquem transferência de tecnologia; juros sobre capital próprio, bem como juros decorrentes de contratos de mútuo entre empresas ligadas e juros decorrentes de contratos de financiamento; dividendos decorrentes de participações em outras empresas, deve preencher este campo com “Sim”.
Ver pagina 71""")
    ind_inov_tec = fields.Char("Inovação Tecnológica e Desenvolvimento Tecnológico", required=True,
        help="""Inovação Tecnológica e Desenvolvimento Tecnológico:  S – Sim  N – Não A pessoa jurídica beneficiária de incentivos fiscais relativos às atividades de pesquisa tecnológica e desenvolvimento de inovação tecnológica de que tratam os arts. 17 a 26 da Lei nº 11.196, de 21 de novembro de 2005, ou a pessoa jurídica executora dos programas de desenvolvimento tecnológico industrial ou agropecuário (PDTI/PDTA) de que trata a Lei nº 8.661, de 1993, aprovados até 31 de dezembro de 2005, que não tenha migrado para o regime estabelecido nos arts. 17 a 26 da Lei nº 11.196, de 2005, deve preencher este campo com “Sim”.
Ver pagina 71""")
    ind_cap_inf = fields.Char("Capacitação de Informática e Inclusão Digital", required=True,
        help="""Capacitação de Informática e Inclusão Digital:  S – Sim  N – Não A pessoa jurídica que tiver investido em atividades de pesquisa e desenvolvimento em tecnologia da informação no âmbito dos programas de capacitação e competitividade dos setores de informática e automação e tecnologias da informação de que trata a Lei nº 8.248, de 23 de outubro de 1991, a Lei nº 10.176, de 11 de janeiro de 2001, e a Lei nº 11.077, de 30 de dezembro de 2004, regulamentadas pelo Decreto nº 5.906, de 26 de setembro de 2006, ou tiver efetuado venda a varejo nos termos dos arts. 28 a 30 da Lei nº 11.196, de 2005, que dispõem sobre o programa de inclusão digital, deve preencher este campo com “Sim”.
Ver pagina 72""")
    ind_pj_hab = fields.Char("IND_PJ_HAB", required=True,
        help="""PJ Habilitada no Repes, Recap, Padis, PATVD, Reidi, Repenec, Reicomp, Retaero, Recine, Resíduos Sólidos, Recopa, Copa do Mundo, Retid, REPNBL-Redes, Reif e Olimpíadas:  S – Sim  N – Não A pessoa jurídica habilitada no Regime Especial de Tributação para a Plataforma de Exportação de Serviços de Tecnologia da Informação (Repes) ou no Regime Especial de Aquisição de Bens de Capital para Empresas Exportadoras (Recap) instituídos pela Lei nº 11.196, de 2005, regulamentados pelos Decretos nº 5.712, de 2 de março de 2006, e nº 5.649, de 29 de dezembro de 2005, respectivamente, deve assinalar este campo. Também deve assinalar este campo a pessoa jurídica executora de projeto aprovado no âmbito do Programa de Apoio ao Desenvolvimento Tecnológico da Indústria de Semicondutores (Padis) ou do Programa de Apoio ao Desenvolvimento Tecnológico da Indústria de Equipamentos para TV Digital (PATVD), instituídos pela Lei nº 11.484, de 2007. Este campo deve também ser assinalado pela pessoa jurídica habilitada ou co-habilitada no Regime Especial de Incentivos e Desenvolvimento da Infraestrutura (Reidi), instituído pela Lei nº 11.488, de 15 de junho de 2007, e regulamentado pelo Decreto nº 6.144, de 3 de julho de 2007, com alterações introduzidas pelo Decreto nº 6.167, de 24 de julho de 2007. Habilitada ou co-habilitada no Regime Especial de Incentivos para o Desenvolvimento da Infraestrutura da Indústria Petrolífera das Regiões Norte, Nordeste e Centro-Oeste (Repenec), instituído pela Lei nº 12.249, de 2010, regulamentado pelo Decreto nº 7.320, de 28 de setembro de 2010. Habilitada no Regime Especial de Incentivo a Computadores para Uso Educacional (REICOMP), instituído pela Lei nº 12.715, de 17 de setembro de 2012. Habilitada no Regime Especial para a Indústria Aeronáutica Brasileira (Retaero), instituído pela Lei nº 12.249, de 2010.
Ver pagina 72""")
    ind_polo_am = fields.Char("Pólo Industrial de Manaus e Amazônia Ocidental", required=True,
        help="""Pólo Industrial de Manaus e Amazônia Ocidental:  S – Sim  N – Não A pessoa jurídica que estiver localizada na área de atuação da Superintendência da Zona Franca de Manaus (Suframa) que seja beneficiária dos incentivos de que trata o Decreto-lei nº 288, de 28 de fevereiro de 1967, e alterações posteriores; a Lei nº 8.387, de 30 de dezembro de 1991, e alterações posteriores; ou o Decreto-lei nº 356, de 15 de agosto de 1968, e alterações posteriores (Amazônia Ocidental), deve preencher este campo com “Sim”.
Ver pagina 73""")
    ind_zon_exp = fields.Char("Zonas de Processamento de Exportação", required=True,
        help="""Zonas de Processamento de Exportação:  S – Sim  N – Não A pessoa jurídica autorizada a operar em Zonas de Processamento de Exportação, voltadas para a produção de bens a serem comercializados no exterior, de acordo com o estabelecido pela Lei nº 11.508, de 20 de julho de 2007 e pela Lei nº 11.732, de 30 de junho de 2008, deve preencher este campo com “Sim”.
Ver pagina 73""")
    ind_area_com = fields.Char("", required=True,
        help="""
Ver pagina 74""")
    ind_pais_a_pais = fields.Char("", required=True,
        help="""
Ver pagina 74""")
    ind_derex = fields.Char("IND_DEREX", required=True,
        help="""Declaração sobre utilização dos recursosem moeda estrangeira decorrentes do recebimento
de exportações (DEREX)
S – Sim
N – Não
Ver pagina 74""")

class Registro0021(models.Model):
    _name = 'l10n.br.sped.ecf.0021'
    _description = u"""Parâmetros de Identificação dos Tipos de Programa"""
    _inherit = 'l10n.br.sped.mixin'
    ind_repes = fields.Char("IND_REPES",
        help="""Regime Especial de Tributação para a Plataforma de Exportação de Serviços de Tecnologia da Informação (Repes): S - Sim N - Não
Ver pagina 79""")
    ind_recap = fields.Char("IND_RECAP",
        help="""Regime Especial de Aquisição de Bens de Capital para Empresas Exportadoras (Recap): S - Sim N - Não
Ver pagina 79""")
    ind_padis = fields.Char("IND_PADIS",
        help="""Programa de Apoio ao Desenvolvimento Tecnológico da Indústria de Semicondutores (Padis): S - Sim N - Não
Ver pagina 79""")
    ind_patvd = fields.Char("IND_PATVD",
        help="""Programa de Apoio ao Desenvolvimento Tecnológico da Indústria de Equipamentos para TV Digital (PATVD): S - Sim N - Não
Ver pagina 79""")
    ind_reidi = fields.Char("IND_REIDI",
        help="""Regime Especial de Incentivos para o Desenvolvimento da Infraestrutura (Reidi): S - Sim N - Não
Ver pagina 79""")
    ind_repenec = fields.Char("IND_REPENEC",
        help="""Regime Especial de Incentivos para o Desenvolvimento da Infraestrutura da Indústria Petrolífera das Regiões Norte, Nordeste e Centro-Oeste (Repenec): S - Sim N - Não
Ver pagina 79""")
    ind_reicomp = fields.Char("IND_REICOMP",
        help="""Regime Especial de Incentivo a Computadores para Uso Educacional (Reicomp): S - Sim N - Não
Ver pagina 80""")
    ind_retaero = fields.Char("IND_RETAERO",
        help="""Regime Especial para a Indústria Aeronáutica Brasileira (Retaero): S - Sim N - Não
Ver pagina 80""")
    ind_recine = fields.Char("IND_RECINE",
        help="""Regime Especial de Tributação para Desenvolvimento da Atividade de Exibição Cinematográfica (Recine): S - Sim N - Não
Ver pagina 80""")
    ind_residuos_solidos = fields.Char("IND_RESIDUOS_SOLIDOS",
        help="""Estabelecimentos industriais façam jus a crédito presumido do IPI na aquisição de resíduos sólidos, de que trata a Lei nº 12.375, de 30 de dezembro de 2010: S - Sim N - Não
Ver pagina 80""")
    ind_recopa = fields.Char("IND_RECOPA",
        help="""Regime Especial de Tributação para construção, ampliação, reforma ou modernização de estádios de futebol (Recopa): S - Sim N - Não
Ver pagina 80""")
    ind_copa_do_mundo = fields.Char("IND_COPA_DO_MUNDO",
        help="""Habilitada para fins de fruição dos benefícios fiscais, não abrangidos na alínea anterior, relativos à realização, no Brasil, da Copa das Confederações FIFA 2013 e da Copa do Mundo FIFA 2014, de que trata a Lei nº 12.350, de 2010, regulamentada pelo Decreto nº 7.578, e 11 de outubro de 2011: S - Sim N - Não
Ver pagina 80""")
    ind_retid = fields.Char("Regime Especial Tributário para a Indústria de Defesa (Retid)",
        help="""Regime Especial Tributário para a Indústria de Defesa (Retid): S - Sim N - Não
Ver pagina 80""")
    ind_repnbl_redes = fields.Char("IND_REPNBL_REDES",
        help="""Regime Especial de Tributação do Programa Nacional de Banda Larga para Implantação de Redes de Telecomunicações (REPNBL-Redes): S - Sim N - Não
Ver pagina 80""")
    ind_reif = fields.Char("Fertilizantes (REIF):",
        help="""Fertilizantes (REIF):
Ver pagina 80""")
    ind_olimpiadas = fields.Char("IND_OLIMPIADAS",
        help="""Habilitada para fins de fruição dos benefícios fiscais, relativos à realização, no Brasil, dos Jogos Olímpicos de 2016 e dos Jogos Paraolímpicos de 2016, de que trata a Lei nº 12.780, de 2013: S - Sim N - Não
Ver pagina 81""")

class Registro0030(models.Model):
    _name = 'l10n.br.sped.ecf.0030'
    _description = u"""Dados Cadastrais"""
    _inherit = 'l10n.br.sped.mixin'
    cod_nat = fields.Integer("COD_NAT", required=True)
    cnae_fiscal = fields.Integer("CNAE_FISCAL", required=True)
    endereco = fields.Char("Endereço da pessoa jurídica.", required=True,
        help="""Endereço da pessoa jurídica.
Ver pagina 82""")
    num = fields.Char("Número", required=True,
        help="""Número
Ver pagina 82""")
    compl = fields.Char("Complemento",
        help="""Complemento
Ver pagina 82""")
    bairro = fields.Char("Bairro/Distrito", required=True,
        help="""Bairro/Distrito
Ver pagina 82""")
    uf = fields.Char("UF", required=True,
        help="""UF, conforme do tabela do Sped (Disponibilizada no programa da ECF no diretório Arquivos de
Ver pagina 82""")
    cod_mun = fields.Char("COD_MUN", required=True,
        help="""Código do Município, conforme tabela do Sped (Disponibilizada no programa da ECF no diretório
Ver pagina 82""")
    cep = fields.Char("Código de Endereçamento Postal (CEP)", required=True,
        help="""Código de Endereçamento Postal (CEP)
Ver pagina 82""")
    num_tel = fields.Integer("DDD + Número do Telefone")
    email = fields.Char("Correio eletrônico", required=True,
        help="""Correio eletrônico
Ver pagina 82""")

class Registro0035(models.Model):
    _name = 'l10n.br.sped.ecf.0035'
    _description = u"""Identificação das SCP"""
    _inherit = 'l10n.br.sped.mixin'
    cod_scp = fields.Char("CNPJ da SCP (Art", required=True,
        help="""CNPJ da SCP (Art. 4º, XVII, da Instrução Normativa RFB nº 1.634, de 6 de maio de 2016).
Ver pagina 84""")
    nome_scp = fields.Char("Descrição da SCP",
        help="""Descrição da SCP
Ver pagina 84""")

class Registro0930(models.Model):
    _name = 'l10n.br.sped.ecf.0930'
    _description = u"""Identificação dos Signatários da ECF"""
    _inherit = 'l10n.br.sped.mixin'
    ident_nom = fields.Char("Nome do Signatário", required=True,
        help="""Nome do Signatário
Ver pagina 86""")
    ident_cpf_cnpj = fields.Integer("IDENT_CPF_CNPJ", required=True)
    ident_qualif = fields.Char("IDENT_QUALIF", required=True,
        help="""Código de qualificação do assinante, conforme tabela do Sped (Disponibilizada no programa da
Ver pagina 86""")
    ind_crc = fields.Char("IND_CRC",
        help="""Número de inscrição do contabilista no Conselho Regional de Contabilidade.
Ver pagina 86""")
    email = fields.Char("E-mail do signatário", required=True,
        help="""E-mail do signatário
Ver pagina 86""")
    fone = fields.Char("DDD e telefone do signatário", required=True,
        help="""DDD e telefone do signatário
Ver pagina 86""")

class RegistroC040(models.Model):
    _name = 'l10n.br.sped.ecf.c040'
    _description = u"""Identificador da ECD"""
    _inherit = 'l10n.br.sped.mixin'
    hash_ecd = fields.Char("Hashcode ECD Utilizada", required=True,
        help="""Hashcode ECD Utilizada
Ver pagina 91""")
    dt_ini = fields.Integer("Data de Início da ECD", required=True)
    dt_fin = fields.Integer("Data Final da ECD", required=True)
    ind_sit_esp = fields.Integer("Indicador de Situação Especial")
    cnpj = fields.Integer("CNPJ", required=True)
    num_ord = fields.Integer("Número de Ordem do Instrumento de Escrituração", required=True)
    nire = fields.Integer("NIRE")
    nat_livr = fields.Char("Natureza do Livro", required=True,
        help="""Natureza do Livro: finalidade a que se destina o instrumento
Ver pagina 91""")
    cod_ver_lc = fields.Char("Código da Versão do Leiaute Contábil", required=True,
        help="""Código da Versão do Leiaute Contábil
Ver pagina 91""")
    ind_esc = fields.Char("Indicador da Forma de Escrituração Contábil", required=True,
        help="""Indicador da Forma de Escrituração Contábil: G - Livro Diário (Completo sem escrituração auxiliar) R - Livro Diário com Escrituração Resumida (com escrituração auxiliar) B - Livro Balancetes Diários e Balanços
Ver pagina 91""")
    reg_c050_ids = fields.One2many('l10n.br.sped.ecf.c050','parent_c040_id',
                               string="Plano de Contas da ECD",
                               help='Bloco C')
    reg_c100_ids = fields.One2many('l10n.br.sped.ecf.c100','parent_c040_id',
                               string="Centro de Custos",
                               help='Bloco C')
    reg_c150_ids = fields.One2many('l10n.br.sped.ecf.c150','parent_c040_id',
                               string="Identificação  do  Período  dos  Saldos  Periódicos  das Contas Patrimoniais",
                               help='Bloco C')
    reg_c350_ids = fields.One2many('l10n.br.sped.ecf.c350','parent_c040_id',
                               string="Identificação  da  Data  dos  Saldos  das  Contas  de Resultado Antes do Encerramento",
                               help='Bloco C')

class RegistroC050(models.Model):
    _name = 'l10n.br.sped.ecf.c050'
    _description = u"""Plano de Contas da ECD"""
    _inherit = 'l10n.br.sped.mixin'
    dt_alt = fields.Integer("Data de Atualização (inclusão/ alteração)", required=True)
    cod_nat = fields.Char("Código da Natureza da Conta/Grupo de Contas", required=True,
        help="""Código da Natureza da Conta/Grupo de Contas.
Ver pagina 92""")
    ind_cta = fields.Char("Indicador do Tipo de Conta", required=True,
        help="""Indicador do Tipo de Conta: S - Sintética (grupo de contas)
Ver pagina 92""")
    nivel = fields.Integer("Nível da Conta Analítica/Sintética.", required=True)
    cod_cta = fields.Char("Código da Conta Analítica/Sintética.", required=True,
        help="""Código da Conta Analítica/Sintética.
Ver pagina 92""")
    cod_cta_sup = fields.Char("Código da Conta Sintética de Nível Imediatamente Superior",
        help="""Código da Conta Sintética de Nível Imediatamente Superior.
Ver pagina 92""")
    cta = fields.Char("Nome da Conta Analítica.", required=True,
        help="""Nome da Conta Analítica.
Ver pagina 92""")
    parent_c040_id = fields.Many2one('l10n.br.sped.ecf.c040',
                                     string="Identificador da ECD")
    reg_c051_ids = fields.One2many('l10n.br.sped.ecf.c051','parent_c050_id',
                               string="Plano de Contas Referencial Preenchido na ECD",
                               help='Bloco C')
    reg_c053_ids = fields.One2many('l10n.br.sped.ecf.c053','parent_c050_id',
                               string="Subcontas Correlatas",
                               help='Bloco C')

class RegistroC051(models.Model):
    _name = 'l10n.br.sped.ecf.c051'
    _description = u"""Plano de Contas Referencial Preenchido na ECD"""
    _inherit = 'l10n.br.sped.mixin'
    cod_ent_ref = fields.Char("COD_ENT_REF", required=True,
        help="""Código da Instituição Responsável pela Manutenção do Plano de Contas Referencial.
Ver pagina 93""")
    cod_ccus = fields.Char("Código do Centro de Custos.",
        help="""Código do Centro de Custos.
Ver pagina 93""")
    cod_cta_ref = fields.Char("Código da Conta no Plano de Contas Referencial", required=True,
        help="""Código da Conta no Plano de Contas Referencial.
Ver pagina 93""")
    parent_c050_id = fields.Many2one('l10n.br.sped.ecf.c050',
                                     string="Plano de Contas da ECD")

class RegistroC053(models.Model):
    _name = 'l10n.br.sped.ecf.c053'
    _description = u"""Subcontas Correlatas"""
    _inherit = 'l10n.br.sped.mixin'
    cod_idt = fields.Char("Código de Identificação do Grupo de Conta-Subconta(a)", required=True,
        help="""Código de Identificação do Grupo de Conta-Subconta(a).
Ver pagina 94""")
    cod_cnt_corr = fields.Char("Código da Subconta Correlata  (Deve estar no plano de contas)", required=True,
        help="""Código da Subconta Correlata  (Deve estar no plano de contas)
Ver pagina 94""")
    nat_sub_cnt = fields.Char("Natureza da Subconta Correlata", required=True,
        help="""Natureza da Subconta Correlata
Ver pagina 94""")
    parent_c050_id = fields.Many2one('l10n.br.sped.ecf.c050',
                                     string="Plano de Contas da ECD")

class RegistroC100(models.Model):
    _name = 'l10n.br.sped.ecf.c100'
    _description = u"""Centro de Custos"""
    _inherit = 'l10n.br.sped.mixin'
    dt_alt = fields.Integer("Data da Inclusão/Alteração.", required=True)
    cod_ccus = fields.Char("Código do Centro de Custos.", required=True,
        help="""Código do Centro de Custos.
Ver pagina 95""")
    ccus = fields.Char("Nome do Centro de Custos.", required=True,
        help="""Nome do Centro de Custos.
Ver pagina 95""")
    parent_c040_id = fields.Many2one('l10n.br.sped.ecf.c040',
                                     string="Identificador da ECD")

class RegistroC150(models.Model):
    _name = 'l10n.br.sped.ecf.c150'
    _description = u"""Identificação  do  Período  dos  Saldos  Periódicos  das Contas Patrimoniais"""
    _inherit = 'l10n.br.sped.mixin'
    dt_ini = fields.Integer("Data do Início do período.", required=True)
    dt_fin = fields.Integer("Data do Fim do período.", required=True)
    parent_c040_id = fields.Many2one('l10n.br.sped.ecf.c040',
                                     string="Identificador da ECD")
    reg_c155_ids = fields.One2many('l10n.br.sped.ecf.c155','parent_c150_id',
                               string="Detalhes dos Saldos Contábeis das Contas Patrimoniais",
                               help='Bloco C')

class RegistroC155(models.Model):
    _name = 'l10n.br.sped.ecf.c155'
    _description = u"""Detalhes dos Saldos Contábeis das Contas Patrimoniais"""
    _inherit = 'l10n.br.sped.mixin'
    cod_cta = fields.Char("Código da Conta Analítica.", required=True,
        help="""Código da Conta Analítica.
Ver pagina 97""")
    cod_ccus = fields.Char("Código do Centro de Custos.",
        help="""Código do Centro de Custos.
Ver pagina 97""")
    vl_sld_ini = fields.Monetary("Valor do Saldo Inicial do Período.", required=True, digits=2)
    ind_vl_sld_ini = fields.Char("Indicador da Situação do Saldo Inicial", required=True,
        help="""Indicador da Situação do Saldo Inicial: D – Devedor  C – Credor
Ver pagina 97""")
    vl_deb = fields.Monetary("Valor Total dos Débitos no Período.", required=True, digits=2)
    vl_cred = fields.Monetary("Valor Total dos Créditos no Período.", required=True, digits=2)
    vl_sld_fin = fields.Monetary("Valor do Saldo Final do Período.", required=True, digits=2)
    ind_vl_sld_fin = fields.Char("Indicador da Situação do Saldo Final", required=True,
        help="""Indicador da Situação do Saldo Final: D – Devedor  C – Credor
Ver pagina 97""")
    linha_ecd = fields.Integer("Número da Linha do Arquivo da ECD", required=True)
    parent_c150_id = fields.Many2one('l10n.br.sped.ecf.c150',
                                     string="Identificação  do  Período  dos  Saldos  Periódicos  das Contas Patrimoniais")
    reg_c157_ids = fields.One2many('l10n.br.sped.ecf.c157','parent_c155_id',
                               string="Transferência de Saldos do Plano de Contas Anterior",
                               help='Bloco C')

class RegistroC157(models.Model):
    _name = 'l10n.br.sped.ecf.c157'
    _description = u"""Transferência de Saldos do Plano de Contas Anterior"""
    _inherit = 'l10n.br.sped.mixin'
    cod_cta = fields.Char("Código da Conta Analítica.", required=True,
        help="""Código da Conta Analítica.
Ver pagina 98""")
    cod_ccus = fields.Char("Código do Centro de Custos.",
        help="""Código do Centro de Custos.
Ver pagina 98""")
    vl_sld_fin = fields.Monetary("Valor do Saldo Final do Período Transferido", required=True, digits=2)
    ind_vl_sld_fin = fields.Char("Indicador da Situação do Saldo Dinal",
        help="""Indicador da Situação do Saldo Dinal: D - Devedor C – Credor
Ver pagina 98""")
    linha_ecd = fields.Integer("Número da Linha do Arquivo da ECD  Obs", required=True)
    parent_c155_id = fields.Many2one('l10n.br.sped.ecf.c155',
                                     string="Detalhes dos Saldos Contábeis das Contas Patrimoniais")

class RegistroC350(models.Model):
    _name = 'l10n.br.sped.ecf.c350'
    _description = u"""Identificação  da  Data  dos  Saldos  das  Contas  de Resultado Antes do Encerramento"""
    _inherit = 'l10n.br.sped.mixin'
    dt_res = fields.Integer("Data da Apuração do Resultado", required=True)
    parent_c040_id = fields.Many2one('l10n.br.sped.ecf.c040',
                                     string="Identificador da ECD")
    reg_c355_ids = fields.One2many('l10n.br.sped.ecf.c355','parent_c350_id',
                               string="Detalhes dos Saldos das Contas de Resultado Antes do Encerramento",
                               help='Bloco C')

class RegistroC355(models.Model):
    _name = 'l10n.br.sped.ecf.c355'
    _description = u"""Detalhes dos Saldos das Contas de Resultado Antes do Encerramento"""
    _inherit = 'l10n.br.sped.mixin'
    cod_cta = fields.Char("Código da Conta Analítica de Resultado.", required=True,
        help="""Código da Conta Analítica de Resultado.
Ver pagina 100""")
    cod_ccus = fields.Char("Código do Centro de Custos.",
        help="""Código do Centro de Custos.
Ver pagina 100""")
    vl_cta = fields.Monetary("Valor do Saldo Final Antes do Lançamento de Encerramento", required=True, digits=2)
    ind_vl_cta = fields.Char("Indicador da Situação do Saldo Final", required=True,
        help="""Indicador da Situação do Saldo Final: D – Devedor. C – Credor.
Ver pagina 100""")
    linha_ecd = fields.Integer("Número da Linha do Arquivo da ECD  Obs", required=True)
    parent_c350_id = fields.Many2one('l10n.br.sped.ecf.c350',
                                     string="Identificação  da  Data  dos  Saldos  das  Contas  de Resultado Antes do Encerramento")

class RegistroE010(models.Model):
    _name = 'l10n.br.sped.ecf.e010'
    _description = u"""Saldos Finais Recuperados da ECF Anterior"""
    _inherit = 'l10n.br.sped.mixin'
    cod_nat = fields.Char("Natureza da Conta.", required=True,
        help="""Natureza da Conta.
Ver pagina 103""")
    cod_cta_ref = fields.Char("Código da Conta Referencial (Analíticas e Sintéticas)", required=True,
        help="""Código da Conta Referencial (Analíticas e Sintéticas).
Ver pagina 103""")
    desc_cta_ref = fields.Char("Descrição da Conta Referencial.", required=True,
        help="""Descrição da Conta Referencial.
Ver pagina 103""")
    val_cta_ref = fields.Monetary("Valor Total da Conta Referencial.", required=True, digits=2)
    ind_val_cta_ref = fields.Char("Indicador do Valor Total da Conta Referencial", required=True,
        help="""Indicador do Valor Total da Conta Referencial: C – Credor D – Devedor
Ver pagina 103""")
    reg_e015_ids = fields.One2many('l10n.br.sped.ecf.e015','parent_e010_id',
                               string="Contas Contábeis Mapeadas",
                               help='Bloco E')

class RegistroE015(models.Model):
    _name = 'l10n.br.sped.ecf.e015'
    _description = u"""Contas Contábeis Mapeadas"""
    _inherit = 'l10n.br.sped.mixin'
    cod_cta = fields.Char("Código da Conta Contábil Analítica (K155)", required=True,
        help="""Código da Conta Contábil Analítica (K155).
Ver pagina 104""")
    cod_ccus = fields.Char("Código do Centro de Custos.",
        help="""Código do Centro de Custos.
Ver pagina 104""")
    desc_cta = fields.Char("Descrição da Conta.", required=True,
        help="""Descrição da Conta.
Ver pagina 104""")
    val_cta = fields.Monetary("Saldo Final da Conta", required=True, digits=2)
    ind_val_cta = fields.Char("Indicador do Saldo Final da Conta", required=True,
        help="""Indicador do Saldo Final da Conta: C – Credor D – Devedor
Ver pagina 104""")
    parent_e010_id = fields.Many2one('l10n.br.sped.ecf.e010',
                                     string="Saldos Finais Recuperados da ECF Anterior")

class RegistroE020(models.Model):
    _name = 'l10n.br.sped.ecf.e020'
    _description = u"""Saldos Finais das Contas da Parte B do e-Lalur da ECF Imediatamente Anterior"""
    _inherit = 'l10n.br.sped.mixin'
    cod_cta_b = fields.Char("Código da Conta da Parte B", required=True,
        help="""Código da Conta da Parte B: Código unívoco atribuído pela empresa à conta no e-Lalur.
Ver pagina 106""")
    desc_cta_lal = fields.Char("Descrição da Conta.",
        help="""Descrição da Conta.
Ver pagina 106""")
    dt_ap_lal = fields.Char("DT_AP_LAL",
        help="""Data de Criação: Data final do período de apuração em que a conta foi criada.
Ver pagina 106""")
    cod_lan_orig = fields.Integer("Tipo de Lançamento")
    desc_lan_orig = fields.Char("DESC_LAN_ORIG",
        help="""Descrição do Tipo de Lançamento no e-Lalur que Deu Origem à Conta.
Ver pagina 106""")
    dt_lim_lal = fields.Char("DT_LIM_LAL",
        help="""Data Limite para a Exclusão, Adição ou Compensação do Valor Controlado, se houver.
Ver pagina 106""")
    tributo = fields.Char("Indicador de Tributo da Adição/Exclusão",
        help="""Indicador de Tributo da Adição/Exclusão: I – Imposto de Renda Pessoa Jurídica C – Contribuição Social sobre o Lucro Líquido A – Ambos (IRPJ e CSLL)
Ver pagina 106""")
    vl_saldo_fin = fields.Monetary("Saldo Final do Período Anterior.", digits=2)
    ind_vl_saldo_fin = fields.Char("Indicador de Saldo Final do Período Anterior",
        help="""Indicador de Saldo Final do Período Anterior: D – Para prejuízos ou valores que reduzam o lucro real ou a base de cálculo da contribuição social em períodos subsequentes. C – Para valores que aumentam o lucro real ou a base de cálculo na contribuição social em períodos subsequentes.
Ver pagina 106""")

class RegistroE030(models.Model):
    _name = 'l10n.br.sped.ecf.e030'
    _description = u"""Identificação do Período"""
    _inherit = 'l10n.br.sped.mixin'
    dt_ini = fields.Integer("Data do Início do Período", required=True)
    dt_fin = fields.Integer("Data do Fim do período", required=True)
    per_apur = fields.Char("Período de Apuração [para 0010", required=True,
        help="""Período de Apuração [para 0010.FORMA_APUR = “A”]:  A00 – Anual A01 – Rec. Bruta de janeiro /Balanço suspensão redução até janeiro  A02 – Rec. Bruta de fevereiro /Balanço suspensão redução até fevereiro A03 – Rec. Bruta de março /Balanço suspensão redução até março A04 – Rec. Bruta de abril /Balanço suspensão redução até abril  A05 – Rec. Bruta de maio /Balanço suspensão redução até maio A06 – Rec. Bruta de junho /Balanço suspensão redução até junho A07 – Rec. Bruta de julho /Balanço suspensão redução até julho A08 – Rec. Bruta de agosto /Balanço suspensão redução até agosto A09 – Rec. Bruta de setembro /Balanço suspensão redução até setembro A10 – Rec. Bruta de outubro/Balanço suspensão redução até outubro A11 – Rec. Bruta de novembro /Balanço suspensão redução até novembro A12 – Rec. Bruta de dezembro/Balanço suspensão redução até dezembro ndicador do período de referência [para 0010.FORMA_APUR = “T” OU (0010.FORMA_APUR = “A” E 0010.FORMA_TRIB = “2”)]: T01 – 1º Trimestre T02 – 2º Trimestre T03 – 3º Trimestre  T04 – 4º Trimestre Regra: O período deve estar compreendido entre a data início e data fim da escrituração. egra: SE 0010.FORMA_APUR = “A”  - Deve existir um registro A00. - Deve existir um registro [A01..A012] para cada mês marcado no 0010.MES_BAL_RED [1..12] como “B” E 0010.FORMA_APUR = “T”  - Deve existir um registro [T01..T04] para cada trimestre marcado no 0010.FORMA_TRIB_PER[1..4] como “R”   I  R  S
Ver pagina 108""")
    reg_e155_ids = fields.One2many('l10n.br.sped.ecf.e155','parent_e030_id',
                               string="Detalhes dos Saldos  Contábeis Calculados com Base nas ECD",
                               help='Bloco E')
    reg_e355_ids = fields.One2many('l10n.br.sped.ecf.e355','parent_e030_id',
                               string="Detalhes dos Saldos das Contas de Resultado Antes do Encerramento",
                               help='Bloco E')

class RegistroE155(models.Model):
    _name = 'l10n.br.sped.ecf.e155'
    _description = u"""Detalhes dos Saldos  Contábeis Calculados com Base nas ECD"""
    _inherit = 'l10n.br.sped.mixin'
    cod_cta = fields.Char("Código da Conta Analítica.", required=True,
        help="""Código da Conta Analítica.
Ver pagina 109""")
    cod_ccus = fields.Char("Código do Centro de Custos.",
        help="""Código do Centro de Custos.
Ver pagina 109""")
    vl_sld_ini = fields.Monetary("Valor do Saldo Inicial do Período.", required=True, digits=2)
    ind_vl_sld_ini = fields.Char("Indicador da Situação do Saldo Inicial", required=True,
        help="""Indicador da Situação do Saldo Inicial: D – Devedor  C – Credor
Ver pagina 109""")
    vl_deb = fields.Monetary("Valor Total dos Débitos no Período.", required=True, digits=2)
    vl_cred = fields.Monetary("Valor Total dos Créditos no Período.", required=True, digits=2)
    vl_sld_fin = fields.Monetary("Valor do Saldo Final do Período.", required=True, digits=2)
    ind_vl_sld_fin = fields.Char("Indicador da Situação do Saldo Final", required=True,
        help="""Indicador da Situação do Saldo Final: D – Devedor  C – Credor
Ver pagina 109""")
    parent_e030_id = fields.Many2one('l10n.br.sped.ecf.e030',
                                     string="Identificação do Período")

class RegistroE355(models.Model):
    _name = 'l10n.br.sped.ecf.e355'
    _description = u"""Detalhes dos Saldos das Contas de Resultado Antes do Encerramento"""
    _inherit = 'l10n.br.sped.mixin'
    cod_cta = fields.Char("Código da Conta Analítica de Resultado.", required=True,
        help="""Código da Conta Analítica de Resultado.
Ver pagina 110""")
    cod_ccus = fields.Char("Código do Centro de Custos.",
        help="""Código do Centro de Custos.
Ver pagina 110""")
    vl_sld_fin = fields.Monetary("Valor do Saldo Final Antes do Lançamento de Encerramento", required=True, digits=2)
    ind_vl_sld_fin = fields.Char("Indicador da Situação do Saldo Final", required=True,
        help="""Indicador da Situação do Saldo Final: D – Devedor. C – Credor.
Ver pagina 110""")
    parent_e030_id = fields.Many2one('l10n.br.sped.ecf.e030',
                                     string="Identificação do Período")

class RegistroJ050(models.Model):
    _name = 'l10n.br.sped.ecf.j050'
    _description = u"""Plano de Contas do Contribuinte"""
    _inherit = 'l10n.br.sped.mixin'
    dt_alt = fields.Integer("Data de Atualização (inclusão/ alteração)", required=True)
    cod_nat = fields.Char("Código da Natureza da Conta Analítica ou Sintética", required=True,
        help="""Código da Natureza da Conta Analítica ou Sintética: 01 – Contas do Ativo 02 – Contas do Passivo 03 – Contas do Patrimônio Líquido 04 – Contas de Resultado 05 – Contas de Compensação 09 – Outras
Ver pagina 113""")
    ind_cta = fields.Char("Indicador do Tipo de Conta", required=True,
        help="""Indicador do Tipo de Conta: S - Sintética (grupo de contas)
Ver pagina 113""")
    nivel = fields.Integer("Nível da Conta Analítica/Sintética", required=True)
    cod_cta = fields.Char("Código da Conta Analítica/Sintética.", required=True,
        help="""Código da Conta Analítica/Sintética.
Ver pagina 113""")
    cod_cta_sup = fields.Char("Código da Conta Sintética de Nível Imediatamente Superior",
        help="""Código da Conta Sintética de Nível Imediatamente Superior.
Ver pagina 113""")
    cta = fields.Char("Nome da Conta Analítica.", required=True,
        help="""Nome da Conta Analítica.
Ver pagina 113""")
    reg_j051_ids = fields.One2many('l10n.br.sped.ecf.j051','parent_j050_id',
                               string="Plano de Contas Referencial",
                               help='Bloco J')
    reg_j053_ids = fields.One2many('l10n.br.sped.ecf.j053','parent_j050_id',
                               string="Subcontas Correlatas",
                               help='Bloco J')

class RegistroJ051(models.Model):
    _name = 'l10n.br.sped.ecf.j051'
    _description = u"""Plano de Contas Referencial"""
    _inherit = 'l10n.br.sped.mixin'
    cod_ccus = fields.Char("Código do Centro de Custos.",
        help="""Código do Centro de Custos.
Ver pagina 116""")
    cod_cta_ref = fields.Char("Código da Conta no Plano de Contas Referencial Definido em 0010", required=True,
        help="""Código da Conta no Plano de Contas Referencial Definido em 0010.COD_QUALIF_PJ, conforme tabela publicada no Sped.
Ver pagina 116""")
    parent_j050_id = fields.Many2one('l10n.br.sped.ecf.j050',
                                     string="Plano de Contas do Contribuinte")

class RegistroJ053(models.Model):
    _name = 'l10n.br.sped.ecf.j053'
    _description = u"""Subcontas Correlatas"""
    _inherit = 'l10n.br.sped.mixin'
    cod_idt = fields.Char("Código de Identificação do Grupo Formado por Conta-Subconta(s)", required=True,
        help="""Código de Identificação do Grupo Formado por Conta-Subconta(s). (Criado pela pessoa jurídica).
Ver pagina 118""")
    cod_cnt_corr = fields.Char("Código da Subconta Correlata", required=True,
        help="""Código da Subconta Correlata. (Deve estar no plano de contas e só pode estar relacionada a um único grupo)
Ver pagina 118""")
    nat_sub_cnt = fields.Char("Natureza da Subconta Correlata", required=True,
        help="""Natureza da Subconta Correlata. (Conforme tabela de natureza da subconta )
Ver pagina 118""")
    parent_j050_id = fields.Many2one('l10n.br.sped.ecf.j050',
                                     string="Plano de Contas do Contribuinte")

class RegistroJ100(models.Model):
    _name = 'l10n.br.sped.ecf.j100'
    _description = u"""Centro de Custos"""
    _inherit = 'l10n.br.sped.mixin'
    dt_alt = fields.Integer("Data da Inclusão/Alteração.", required=True)
    cod_ccus = fields.Char("Código do Centro de Custos.", required=True,
        help="""Código do Centro de Custos.
Ver pagina 121""")
    ccus = fields.Char("Nome do Centro de Custos.", required=True,
        help="""Nome do Centro de Custos.
Ver pagina 121""")

class RegistroK030(models.Model):
    _name = 'l10n.br.sped.ecf.k030'
    _description = u"""Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL no Ano-Calendário"""
    _inherit = 'l10n.br.sped.mixin'
    dt_ini = fields.Integer("Data do Início do Período", required=True)
    dt_fin = fields.Integer("Data do Fim do período", required=True)
    per_apur = fields.Char("Período de Apuração [para 0010", required=True,
        help="""Período de Apuração [para 0010.FORMA_APUR = “A” ou (0010.FORMA_APUR_I = “A” OU 0010.APUR_CSLL = “A” E 0010.TIP_ESC_PRE = “C”)]:  A00 – Anual A01 – Rec. Bruta de janeiro /Balanço suspensão redução até janeiro  A02 – Rec. Bruta de fevereiro /Balanço suspensão redução até fevereiro A03 – Rec. Bruta de março /Balanço suspensão redução até março A04 – Rec. Bruta de abril /Balanço suspensão redução até abril  A05 – Rec. Bruta de maio /Balanço suspensão redução até maio A06 – Rec. Bruta de junho /Balanço suspensão redução até junho A07 – Rec. Bruta de julho /Balanço suspensão redução até julho A08 – Rec. Bruta de agosto /Balanço suspensão redução até agosto A09 – Rec. Bruta de setembro /Balanço suspensão redução até setembro A10 – Rec. Bruta de outubro/Balanço suspensão redução até outubro A11 – Rec. Bruta de novembro /Balanço suspensão redução até novembro A12 – Rec. Bruta de dezembro/Balanço suspensão redução até dezembro ndicador do período de referência [para 0010.FORMA_APUR = “T” OU (0010.FORMA_APUR = “A” E 0010.FORMA_TRIB = “2”) ou (0010.FORMA_APUR_I = “T” OU 0010.APUR_CSLL = “T” E 0010.TIP_ESC_PRE = “C”)]: T01 – 1º Trimestre T02 – 2º Trimestre T03 – 3º Trimestre  T04 – 4º Trimestre Regra: O período deve estar compreendido entre a data início e data fim da escrituração. eríodo de Apuração [para 0010.FORMA_APUR_I = “D” OU 0010.APUR_CSLL = “D” E 0010.TIP_ESC_PRE = “C”)]:  A00 – Anual   I  P
Ver pagina 125""")
    reg_k155_ids = fields.One2many('l10n.br.sped.ecf.k155','parent_k030_id',
                               string="Detalhes dos Saldos Contábeis (Depois do Encerramento do Resultado do Período)",
                               help='Bloco K')
    reg_k355_ids = fields.One2many('l10n.br.sped.ecf.k355','parent_k030_id',
                               string="Saldos  Finais  das  Contas  Contábeis  de  Resultado Antes do Encerramento",
                               help='Bloco K')

class RegistroK155(models.Model):
    _name = 'l10n.br.sped.ecf.k155'
    _description = u"""Detalhes dos Saldos Contábeis (Depois do Encerramento do Resultado do Período)"""
    _inherit = 'l10n.br.sped.mixin'
    cod_cta = fields.Char("Código da Conta Analítica Patrimonial.", required=True,
        help="""Código da Conta Analítica Patrimonial.
Ver pagina 128""")
    cod_ccus = fields.Char("Código do Centro de Custos.",
        help="""Código do Centro de Custos.
Ver pagina 128""")
    vl_sld_ini = fields.Monetary("Valor do Saldo Inicial do Período.", required=True, digits=2)
    ind_vl_sld_ini = fields.Char("Indicador da Situação do Saldo Inicial", required=True,
        help="""Indicador da Situação do Saldo Inicial: D – Devedor  C – Credor
Ver pagina 128""")
    vl_deb = fields.Monetary("Valor Total dos Débitos no Período.", required=True, digits=2)
    vl_cred = fields.Monetary("Valor Total dos Créditos no Período.", required=True, digits=2)
    vl_sld_fin = fields.Monetary("Valor do Saldo Final do Período.", required=True, digits=2)
    ind_vl_sld_fin = fields.Char("Indicador da Situação do Saldo Final", required=True,
        help="""Indicador da Situação do Saldo Final: D – Devedor  C – Credor
Ver pagina 128""")
    parent_k030_id = fields.Many2one('l10n.br.sped.ecf.k030',
                                     string="Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL no Ano-Calendário")
    reg_k156_ids = fields.One2many('l10n.br.sped.ecf.k156','parent_k155_id',
                               string="Mapeamento Referencial do Saldo Final",
                               help='Bloco K')

class RegistroK156(models.Model):
    _name = 'l10n.br.sped.ecf.k156'
    _description = u"""Mapeamento Referencial do Saldo Final"""
    _inherit = 'l10n.br.sped.mixin'
    cod_cta_ref = fields.Char("COD_CTA_REF", required=True,
        help="""Código da Conta no Plano de Contas Referencial, conforme tabela do Sped.
Ver pagina 131""")
    vl_sld_fin = fields.Monetary("Valor do Saldo Final Mapeado.", required=True, digits=2)
    ind_vl_sld_fin = fields.Char("Indicador da Situação do Saldo Final", required=True,
        help="""Indicador da Situação do Saldo Final: D – Devedor C – Credor
Ver pagina 131""")
    parent_k155_id = fields.Many2one('l10n.br.sped.ecf.k155',
                                     string="Detalhes dos Saldos Contábeis (Depois do Encerramento do Resultado do Período)")

class RegistroK355(models.Model):
    _name = 'l10n.br.sped.ecf.k355'
    _description = u"""Saldos  Finais  das  Contas  Contábeis  de  Resultado Antes do Encerramento"""
    _inherit = 'l10n.br.sped.mixin'
    cod_cta = fields.Char("Código da Conta Analítica de Resultado.", required=True,
        help="""Código da Conta Analítica de Resultado.
Ver pagina 133""")
    cod_ccus = fields.Char("Código do Centro de Custos.",
        help="""Código do Centro de Custos.
Ver pagina 133""")
    vl_sld_fin = fields.Monetary("Valor do Saldo Final Antes do Lançamento de Encerramento", required=True, digits=2)
    ind_vl_sld_fin = fields.Char("Indicador da Situação do Saldo Final", required=True,
        help="""Indicador da Situação do Saldo Final: D – Devedor. C – Credor.
Ver pagina 133""")
    parent_k030_id = fields.Many2one('l10n.br.sped.ecf.k030',
                                     string="Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL no Ano-Calendário")
    reg_k356_ids = fields.One2many('l10n.br.sped.ecf.k356','parent_k355_id',
                               string="Mapeamento Referencial dos Saldos Finais das Contas de Resultado Antes do Encerramento",
                               help='Bloco K')

class RegistroK356(models.Model):
    _name = 'l10n.br.sped.ecf.k356'
    _description = u"""Mapeamento Referencial dos Saldos Finais das Contas de Resultado Antes do Encerramento"""
    _inherit = 'l10n.br.sped.mixin'
    cod_cta_ref = fields.Char("COD_CTA_REF", required=True,
        help="""Código da Conta no Plano de Contas Referencial, conforme tabela do Sped.
Ver pagina 135""")
    vl_sld_fin = fields.Monetary("Valor do Saldo Final Antes do Lançamento de Encerramento", required=True, digits=2)
    ind_vl_sld_fin = fields.Char("Indicador da Situação do Saldo Final", required=True,
        help="""Indicador da Situação do Saldo Final: D – Devedor C – Credor
Ver pagina 135""")
    parent_k355_id = fields.Many2one('l10n.br.sped.ecf.k355',
                                     string="Saldos  Finais  das  Contas  Contábeis  de  Resultado Antes do Encerramento")

class RegistroL030(models.Model):
    _name = 'l10n.br.sped.ecf.l030'
    _description = u"""Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL no Ano-Calendário"""
    _inherit = 'l10n.br.sped.mixin'
    dt_ini = fields.Integer("Data do Início do Período", required=True)
    dt_fin = fields.Integer("Data do Fim do período", required=True)
    per_apur = fields.Char("Período de apuração [para 0010", required=True,
        help="""Período de apuração [para 0010.FORMA_APUR = “A”]:  A00 – Receita Bruta/ Balanço de Suspensão e Redução Anual A01 – Balanço de Suspensão e Redução até Janeiro  A02 – Balanço de Suspensão e Redução até Fevereiro A03 – Balanço de Suspensão e Redução até Março A04 – Balanço de Suspensão e Redução até Abril  A05 – Balanço de Suspensão e Redução até Maio A06 – Balanço de Suspensão e Redução até Junho  A07 – Balanço de Suspensão e Redução até Julho A08 – Balanço de Suspensão e Redução até Agosto  A09 – Balanço de Suspensão e Redução até Setembro  A10 – Balanço de Suspensão e Redução até Outubro  A11 – Balanço de Suspensão e Redução até Novembro   A12 – Balanço de Suspensão e Redução até Dezembro  Indicador do período de referência [para 0010.FORMA_APUR = “T” OU (0010.FORMA_APUR = “A” E 0010.FORMA_TRIB = “2”)]:  T01 – 1º Trimestre T02 – 2º Trimestre T03 – 3º Trimestre  T04 – 4º Trimestre Regra: O período deve estar compreendido entre a data início e data fim da escrituração. Regra: SE 0010.FORMA_APUR = “A”  - Deve existir um registro A00. - Deve existir um registro [A01..A012] para cada mês marcado no 0010.MES_BAL_RED [1..12] como “B” SE 0010.FORMA_APUR = “T”  - Deve existir um registro [T01..T04] para cada trimestre marcado no 0010.FORMA_TRIB_PER[1..4] como “R”
Ver pagina 197""")
    reg_l100_ids = fields.One2many('l10n.br.sped.ecf.l100','parent_l030_id',
                               string="Balanço Patrimonial",
                               help='Bloco L')
    reg_l200_ids = fields.One2many('l10n.br.sped.ecf.l200','parent_l030_id',
                               string="Método de Avaliação do Estoque Final",
                               help='Bloco L')
    reg_l210_ids = fields.One2many('l10n.br.sped.ecf.l210','parent_l030_id',
                               string="Informativo da Composição de Custos",
                               help='Bloco L')
    reg_l300_ids = fields.One2many('l10n.br.sped.ecf.l300','parent_l030_id',
                               string="Demonstração do Resultado Líquido no Período Fiscal",
                               help='Bloco L')

class RegistroL100(models.Model):
    _name = 'l10n.br.sped.ecf.l100'
    _description = u"""Balanço Patrimonial"""
    _inherit = 'l10n.br.sped.mixin'
    codigo = fields.Char("CODIGO", required=True,
        help="""Código da Conta Referencial (Analíticas e Sintéticas), conforme tabela dinâmica do Sped (Disponibilizada no item II deste registro e no programa da ECF, no diretório
Ver pagina 199""")
    descricao = fields.Char("Descrição da Conta Referencial.",
        help="""Descrição da Conta Referencial.
Ver pagina 199""")
    tipo = fields.Char("Indicador do Tipo de Conta", required=True,
        help="""Indicador do Tipo de Conta: S – Sintética A – Analítica
Ver pagina 199""")
    nivel = fields.Integer("Nível da Conta.")
    cod_nat = fields.Char("COD_NAT",
        help="""Natureza da Conta, conforme tabela do Sped (Disponibilizada no programa da ECF
Ver pagina 199""")
    cod_cta_sup = fields.Char("Código da Conta Sintética de Nível Imediatamente Superior",
        help="""Código da Conta Sintética de Nível Imediatamente Superior.
Ver pagina 199""")
    val_cta_ref_ini = fields.Monetary("Saldo Inicial da Conta Referencial.", required=True, digits=2)
    ind_val_cta_ref_ini = fields.Char("Indicador da Situação do Saldo Inicial", required=True,
        help="""Indicador da Situação do Saldo Inicial: D – Devedor C – Credor
Ver pagina 199""")
    val_cta_ref_fin = fields.Char("Saldo Final da Conta Referencial", required=True,
        help="""Saldo Final da Conta Referencial
Ver pagina 199""")
    ind_val_cta_ref_fin = fields.Char("Indicador da Situação do Saldo Final", required=True,
        help="""Indicador da Situação do Saldo Final: D – Devedor C – Credor
Ver pagina 200""")
    parent_l030_id = fields.Many2one('l10n.br.sped.ecf.l030',
                                     string="Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL no Ano-Calendário")

class RegistroL200(models.Model):
    _name = 'l10n.br.sped.ecf.l200'
    _description = u"""Método de Avaliação do Estoque Final"""
    _inherit = 'l10n.br.sped.mixin'
    ind_aval_estoq = fields.Char("Método de Avaliação do Estoque Final", required=True,
        help="""Método de Avaliação do Estoque Final: 1 – Custo Médio Ponderado  2 – PEPS (Primeiro que entra, primeiro que sai) 3 – Arbitramento - art. 296, Inc. I e II, do RIR/99 4 – Custo Específico 5 – Valor Realizável Líquido 6 – Inventário Periódico 7 – Outros 8 – Não há (Exemplo: Empresas Prestadoras de Serviços)
Ver pagina 203""")
    parent_l030_id = fields.Many2one('l10n.br.sped.ecf.l030',
                                     string="Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL no Ano-Calendário")

class RegistroL210(models.Model):
    _name = 'l10n.br.sped.ecf.l210'
    _description = u"""Informativo da Composição de Custos"""
    _inherit = 'l10n.br.sped.mixin'
    codigo = fields.Char("CODIGO", required=True,
        help="""Código da Conta de Custos (Analítica), conforme tabela dinâmica do Sped.
Ver pagina 204""")
    descricao = fields.Char("Descrição da Conta de Custos.",
        help="""Descrição da Conta de Custos.
Ver pagina 204""")
    valor = fields.Monetary("Saldo Final da Conta de Custos Antes do Encerramento", digits=2)
    parent_l030_id = fields.Many2one('l10n.br.sped.ecf.l030',
                                     string="Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL no Ano-Calendário")

class RegistroL300(models.Model):
    _name = 'l10n.br.sped.ecf.l300'
    _description = u"""Demonstração do Resultado Líquido no Período Fiscal"""
    _inherit = 'l10n.br.sped.mixin'
    codigo = fields.Char("", required=True,
        help="""
Ver pagina 206""")
    descricao = fields.Char("Descrição da Conta Referencial.",
        help="""Descrição da Conta Referencial.
Ver pagina 206""")
    tipo = fields.Char("Indicador do Tipo de Conta", required=True,
        help="""Indicador do Tipo de Conta: S – Sintética  A – Analítica
Ver pagina 206""")
    nivel = fields.Integer("Nível da Conta.")
    cod_nat = fields.Char("Natureza da Conta",
        help="""Natureza da Conta: 04 – Contas de Resultado
Ver pagina 206""")
    cod_cta_sup = fields.Char("Código da Conta Sintética de Nível Imediatamente Superior",
        help="""Código da Conta Sintética de Nível Imediatamente Superior.
Ver pagina 206""")
    valor = fields.Monetary("Saldo Final da Conta Referencial.", required=True, digits=2)
    ind_valor = fields.Char("Indicador do Sinal do Saldo Final", required=True,
        help="""Indicador do Sinal do Saldo Final:  C – Credor D – Devedor
Ver pagina 206""")
    parent_l030_id = fields.Many2one('l10n.br.sped.ecf.l030',
                                     string="Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL no Ano-Calendário")

class RegistroM010(models.Model):
    _name = 'l10n.br.sped.ecf.m010'
    _description = u"""Identificação da Conta na Parte B e-Lalur e do e-Lacs"""
    _inherit = 'l10n.br.sped.mixin'
    cod_cta_b = fields.Char("Código Unívoco Atribuído pela Pessoa Jurídica à Conta no e-Lalur", required=True,
        help="""Código Unívoco Atribuído pela Pessoa Jurídica à Conta no e-Lalur
Ver pagina 211""")
    desc_cta_lal = fields.Char("Descrição da Conta.", required=True,
        help="""Descrição da Conta.
Ver pagina 211""")
    dt_ap_lal = fields.Char("DT_AP_LAL", required=True,
        help="""Data Final: Data final do período de apuração em que a conta foi criada.
Ver pagina 211""")
    cod_lan_orig = fields.Char("Código do Lançamento",
        help="""Código do Lançamento: Código do lançamento na parte A do e-Lalur e/ou do e-Lacs que deu origem à conta.
Ver pagina 211""")
    desc_lan_orig = fields.Char("DESC_LAN_ORIG",
        help="""Descrição: Descrição do tipo de lançamento na parte A do e-Lalur e/ou do e-Lacs que deu origem à conta.
Ver pagina 211""")
    dt_lim_lal = fields.Char("DT_LIM_LAL",
        help="""Data Limite: Data limite para a exclusão, adição ou compensação do valor controlado, se houver.
Ver pagina 211""")
    cod_tributo = fields.Char("Indicador do Tributo da Adição/Exclusão", required=True,
        help="""Indicador do Tributo da Adição/Exclusão: I – Imposto de Renda Pessoa Jurídica C – Contribuição Social sobre o Lucro Líquido;
Ver pagina 211""")
    vl_saldo_ini = fields.Monetary("Saldo Inicial: Saldo no período inicial desta escrituração", required=True, digits=2)

class RegistroM030(models.Model):
    _name = 'l10n.br.sped.ecf.m030'
    _description = u"""Identificação do Período e Forma de Apuração do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Real"""
    _inherit = 'l10n.br.sped.mixin'
    dt_ini = fields.Integer("Data do Início do Período", required=True)
    dt_fin = fields.Integer("Data do Fim do período", required=True)
    per_apur = fields.Char("Período de apuração [para 0010", required=True,
        help="""Período de apuração [para 0010.FORMA_APUR = “A”]:  A00 – Receita Bruta/ Balanço de Suspensão e Redução Anual A01 – Balanço de Suspensão e Redução até Janeiro  A02 – Balanço de Suspensão e Redução até Fevereiro A03 – Balanço de Suspensão e Redução até Março A04 – Balanço de Suspensão e Redução até Abril  A05 – Balanço de Suspensão e Redução até Maio A06 – Balanço de Suspensão e Redução até Junho  A07 – Balanço de Suspensão e Redução até Julho A08 – Balanço de Suspensão e Redução até Agosto  A09 – Balanço de Suspensão e Redução até Setembro  A10 – Balanço de Suspensão e Redução até Outubro  A11 – Balanço de Suspensão e Redução até Novembro   A12 – Balanço de Suspensão e Redução até Dezembro  ndicador do período de referência [para 0010.FORMA_APUR = “T” OU (0010.FORMA_APUR = “A” E 0010.FORMA_TRIB = “2”)]: T01 – 1º Trimestre T02 – 2º Trimestre T03 – 3º Trimestre  T04 – 4º Trimestre Regra: O período deve estar compreendido entre a data início e data fim da escrituração. Regra: SE 0010.FORMA_APUR = “A”  - Deve existir um registro A00. - Deve existir um registro [A01..A012] para cada mês marcado no 0010.MES_BAL_RED [1..12] como “B” E 0010.FORMA_APUR = “T”  - Deve existir um registro [T01..T04] para cada trimestre marcado no 0010.FORMA_TRIB_PER[1..4] como “R”   I  S
Ver pagina 215""")
    reg_m300_ids = fields.One2many('l10n.br.sped.ecf.m300','parent_m030_id',
                               string="Demonstração do Lucro Real",
                               help='Bloco M')
    reg_m350_ids = fields.One2many('l10n.br.sped.ecf.m350','parent_m030_id',
                               string="Demonstração da Base de Cálculo da CSLL",
                               help='Bloco M')
    reg_m410_ids = fields.One2many('l10n.br.sped.ecf.m410','parent_m030_id',
                               string="Lançamentos na Conta da Parte B do e-Lalur e do e-Lacs Sem Reflexo na Parte A",
                               help='Bloco M')
    reg_m500_ids = fields.One2many('l10n.br.sped.ecf.m500','parent_m030_id',
                               string="Controle de Saldos das Contas da Parte B do e-Lalur e do e-Lacs",
                               help='Bloco M')

class RegistroM300(models.Model):
    _name = 'l10n.br.sped.ecf.m300'
    _description = u"""Demonstração do Lucro Real"""
    _inherit = 'l10n.br.sped.mixin'
    codigo = fields.Char("CODIGO", required=True,
        help="""Código do Lançamento no e-Lalur, conforme tabela dinâmica do Sped (Disponibilizada
Ver pagina 217""")
    descricao = fields.Char("DESCRICAO",
        help="""Descrição do Tipo de Lançamento no e-Lalur, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro e no programa da ECF no diretório Arquivos
Ver pagina 218""")
    tipo_lancamento = fields.Char("Indicador do Tipo de Lançamento",
        help="""Indicador do Tipo de Lançamento: A- Adição E - Exclusão. P - Compensação de Prejuízo L - Lucro bservação: O tipo “R” (Rótulo) é para linhas de títulos, que aparecem na interface do programa. Portanto, não deve ser utilizado neste campo.   O
Ver pagina 218""")
    ind_relacao = fields.Integer("Indicador de Relacionamento do Lançamento da Parte A")
    valor = fields.Monetary("Valor do Lançamento no e-Lalur", digits=2)
    hist_lan_lal = fields.Char("Histórico do Lançamento no e-Lalur",
        help="""Histórico do Lançamento no e-Lalur
Ver pagina 218""")
    parent_m030_id = fields.Many2one('l10n.br.sped.ecf.m030',
                                     string="Identificação do Período e Forma de Apuração do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Real")
    reg_m305_ids = fields.One2many('l10n.br.sped.ecf.m305','parent_m300_id',
                               string="Contas  da  Parte  B  Relacionadas  ao  Lançamento  da Parte A do e-Lalur",
                               help='Bloco M')
    reg_m310_ids = fields.One2many('l10n.br.sped.ecf.m310','parent_m300_id',
                               string="Contas  Contábeis  Relacionadas  ao  Lançamento  da Parte A do e-Lalur",
                               help='Bloco M')
    reg_m315_ids = fields.One2many('l10n.br.sped.ecf.m315','parent_m300_id',
                               string="Identificação de Processos Judiciais e Administrativos Referentes ao Lançamento",
                               help='Bloco M')

class RegistroM305(models.Model):
    _name = 'l10n.br.sped.ecf.m305'
    _description = u"""Contas  da  Parte  B  Relacionadas  ao  Lançamento  da Parte A do e-Lalur"""
    _inherit = 'l10n.br.sped.mixin'
    cod_cta_b = fields.Char("Código da Conta na Parte B", required=True,
        help="""Código da Conta na Parte B: Código unívoco atribuído pelo contribuinte à conta no e-Lalur no registro M010.
Ver pagina 223""")
    vl_cta = fields.Monetary("Valor Total dos Lançamentos", required=True, digits=2)
    ind_vl_cta = fields.Char("Indicador do Valor Total dos Lançamentos", required=True,
        help="""Indicador do Valor Total dos Lançamentos: D – Para prejuízos ou valores que reduzam o lucro real em períodos subsequentes. C – Para valores que aumentam o lucro real em períodos subsequentes.
Ver pagina 223""")
    parent_m300_id = fields.Many2one('l10n.br.sped.ecf.m300',
                                     string="Demonstração do Lucro Real")

class RegistroM310(models.Model):
    _name = 'l10n.br.sped.ecf.m310'
    _description = u"""Contas  Contábeis  Relacionadas  ao  Lançamento  da Parte A do e-Lalur"""
    _inherit = 'l10n.br.sped.mixin'
    cod_cta = fields.Char("Código da Conta Contábil (Plano de Contas da Pessoa Jurídica)", required=True,
        help="""Código da Conta Contábil (Plano de Contas da Pessoa Jurídica): Código da conta ou subconta contábil onde está registrado o valor a ser adicionado ou excluído, quando possível sua identificação (deve existir no J050).
Ver pagina 225""")
    cod_ccus = fields.Char("Código do Centro de Custos (deve existir no J100)",
        help="""Código do Centro de Custos (deve existir no J100).
Ver pagina 225""")
    vl_cta = fields.Monetary("Valor da Conta Utilizado no Lançamento da Parte A", required=True, digits=2)
    ind_vl_cta = fields.Char("Indicador do Valor do Lançamento", required=True,
        help="""Indicador do Valor do Lançamento: D – Devedor. C – Credor.
Ver pagina 225""")
    parent_m300_id = fields.Many2one('l10n.br.sped.ecf.m300',
                                     string="Demonstração do Lucro Real")
    reg_m312_ids = fields.One2many('l10n.br.sped.ecf.m312','parent_m310_id',
                               string="Números  dos  Lançamentos  Relacionados  à  Conta Contábil",
                               help='Bloco M')

class RegistroM312(models.Model):
    _name = 'l10n.br.sped.ecf.m312'
    _description = u"""Números  dos  Lançamentos  Relacionados  à  Conta Contábil"""
    _inherit = 'l10n.br.sped.mixin'
    num_lcto = fields.Char("NUM_LCTO", required=True,
        help="""Número do Lançamento Descrito na ECD (Escrituração Contábil Digital) no campo 2 (NUM_LCTO) registro “I200 – Lançamento Contábil”.
Ver pagina 227""")
    parent_m310_id = fields.Many2one('l10n.br.sped.ecf.m310',
                                     string="Contas  Contábeis  Relacionadas  ao  Lançamento  da Parte A do e-Lalur")

class RegistroM315(models.Model):
    _name = 'l10n.br.sped.ecf.m315'
    _description = u"""Identificação de Processos Judiciais e Administrativos Referentes ao Lançamento"""
    _inherit = 'l10n.br.sped.mixin'
    ind_proc = fields.Char("Tipo do Processo", required=True,
        help="""Tipo do Processo: 1 - Judicial  2 – Administrativo
Ver pagina 228""")
    num_proc = fields.Char("Número do Processo.", required=True,
        help="""Número do Processo.
Ver pagina 228""")
    parent_m300_id = fields.Many2one('l10n.br.sped.ecf.m300',
                                     string="Demonstração do Lucro Real")

class RegistroM350(models.Model):
    _name = 'l10n.br.sped.ecf.m350'
    _description = u"""Demonstração da Base de Cálculo da CSLL"""
    _inherit = 'l10n.br.sped.mixin'
    codigo = fields.Char("CODIGO", required=True,
        help="""Código do Lançamento no e-Lalur, conforme tabela dinâmica do Sped (Disponibilizada
Ver pagina 229""")
    descricao = fields.Char("DESCRICAO",
        help="""Descrição do Tipo de Lançamento no e-Lalur, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro e no programa da ECF no diretório Arquivos
Ver pagina 230""")
    tipo_lancamento = fields.Char("Indicador do Tipo de Lançamento",
        help="""Indicador do Tipo de Lançamento: A- Adição E - Exclusão. P - Compensação de Prejuízo L - Lucro bservação: O tipo “R” (Rótulo) é para linhas de títulos, que aparecem na interface do programa. Portanto, não deve ser utilizado neste campo.   O
Ver pagina 230""")
    ind_relacao = fields.Integer("Indicador de Relacionamento do Lançamento da Parte A")
    valor = fields.Monetary("Valor do Lançamento no e-Lalur", digits=2)
    hist_lan_lal = fields.Char("Histórico do Lançamento no e-Lalur",
        help="""Histórico do Lançamento no e-Lalur
Ver pagina 230""")
    parent_m030_id = fields.Many2one('l10n.br.sped.ecf.m030',
                                     string="Identificação do Período e Forma de Apuração do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Real")
    reg_m355_ids = fields.One2many('l10n.br.sped.ecf.m355','parent_m350_id',
                               string="Contas da Parte B Relacionadas ao ao Lançamento da Parte A do e-Lacs",
                               help='Bloco M')
    reg_m360_ids = fields.One2many('l10n.br.sped.ecf.m360','parent_m350_id',
                               string="Contas  Contábeis  Relacionadas  ao  Lançamento  da Parte A do e-Lacs",
                               help='Bloco M')
    reg_m365_ids = fields.One2many('l10n.br.sped.ecf.m365','parent_m350_id',
                               string="Identificação de Processos Judiciais e Administrativos Referentes ao Lançamento",
                               help='Bloco M')

class RegistroM355(models.Model):
    _name = 'l10n.br.sped.ecf.m355'
    _description = u"""Contas da Parte B Relacionadas ao ao Lançamento da Parte A do e-Lacs"""
    _inherit = 'l10n.br.sped.mixin'
    cod_cta_b = fields.Char("Código da Conta na Parte B", required=True,
        help="""Código da Conta na Parte B: Código unívoco atribuído pelo contribuinte à conta no e-Lacs no registro M010.
Ver pagina 235""")
    vl_cta = fields.Monetary("Valor Total dos Lançamentos", required=True, digits=2)
    ind_vl_cta = fields.Char("Indicador do Valor Total dos Lançamentos", required=True,
        help="""Indicador do Valor Total dos Lançamentos: D – Para prejuízos ou valores que reduzam o lucro real em períodos subsequentes. C – Para valores que aumentam o lucro real em períodos subsequentes.
Ver pagina 235""")
    parent_m350_id = fields.Many2one('l10n.br.sped.ecf.m350',
                                     string="Demonstração da Base de Cálculo da CSLL")

class RegistroM360(models.Model):
    _name = 'l10n.br.sped.ecf.m360'
    _description = u"""Contas  Contábeis  Relacionadas  ao  Lançamento  da Parte A do e-Lacs"""
    _inherit = 'l10n.br.sped.mixin'
    cod_cta = fields.Char("Código da Conta Contábil (Plano de Contas da Pessoa Jurídica)", required=True,
        help="""Código da Conta Contábil (Plano de Contas da Pessoa Jurídica): Código da conta ou subconta contábil onde está registrado o valor a ser adicionado ou excluído, quando possível sua identificação (deve existir no J050).
Ver pagina 237""")
    cod_ccus = fields.Char("Código do Centro de Custos (deve existir no J100)",
        help="""Código do Centro de Custos (deve existir no J100).
Ver pagina 237""")
    vl_cta = fields.Monetary("Valor da Conta Utilizado no Lançamento da Parte A", required=True, digits=2)
    ind_vl_cta = fields.Char("Indicador do Valor do Lançamento", required=True,
        help="""Indicador do Valor do Lançamento: D – Devedor. C – Credor.
Ver pagina 237""")
    parent_m350_id = fields.Many2one('l10n.br.sped.ecf.m350',
                                     string="Demonstração da Base de Cálculo da CSLL")
    reg_m362_ids = fields.One2many('l10n.br.sped.ecf.m362','parent_m360_id',
                               string="Números  dos  Lançamentos  Relacionados  à  Conta Contábil",
                               help='Bloco M')

class RegistroM362(models.Model):
    _name = 'l10n.br.sped.ecf.m362'
    _description = u"""Números  dos  Lançamentos  Relacionados  à  Conta Contábil"""
    _inherit = 'l10n.br.sped.mixin'
    num_lcto = fields.Char("NUM_LCTO", required=True,
        help="""Número do Lançamento Descrito na ECD (Escrituração Contábil Digital) no campo 2 (NUM_LCTO) registro “I200 – Lançamento Contábil”.
Ver pagina 239""")
    parent_m360_id = fields.Many2one('l10n.br.sped.ecf.m360',
                                     string="Contas  Contábeis  Relacionadas  ao  Lançamento  da Parte A do e-Lacs")

class RegistroM365(models.Model):
    _name = 'l10n.br.sped.ecf.m365'
    _description = u"""Identificação de Processos Judiciais e Administrativos Referentes ao Lançamento"""
    _inherit = 'l10n.br.sped.mixin'
    ind_proc = fields.Char("Tipo do Processo", required=True,
        help="""Tipo do Processo: 1 - Judicial  2 – Administrativo
Ver pagina 240""")
    num_proc = fields.Char("Número do Processo.", required=True,
        help="""Número do Processo.
Ver pagina 240""")
    parent_m350_id = fields.Many2one('l10n.br.sped.ecf.m350',
                                     string="Demonstração da Base de Cálculo da CSLL")

class RegistroM410(models.Model):
    _name = 'l10n.br.sped.ecf.m410'
    _description = u"""Lançamentos na Conta da Parte B do e-Lalur e do e-Lacs Sem Reflexo na Parte A"""
    _inherit = 'l10n.br.sped.mixin'
    cod_cta_b = fields.Char("Código da Conta do Lançamento (conta da Parte B)",
        help="""Código da Conta do Lançamento (conta da Parte B)
Ver pagina 241""")
    cod_tributo = fields.Char("Código do Tributo", required=True,
        help="""Código do Tributo: I – Imposto de Renda C – Contribuição Social sobre o Lucro Líquido
Ver pagina 241""")
    val_lan_lalb_pb = fields.Monetary("Valor do Lançamento.", required=True, digits=2)
    ind_val_lan_lalb_pb = fields.Char("Indicador do Lançamento", required=True,
        help="""Indicador do Lançamento: CR – Crédito DB – Débito PF - Prejuízo do exercício. BC - Base de cálculo negativa da CSLL. Observação: O indicador PF refere-se ao prejuízo apurado no exercício em curso.
Ver pagina 241""")
    cod_cta_b_ctp = fields.Char("COD_CTA_B_CTP",
        help="""Código Unívoco da Contrapartida (conta da Parte B), caso seja necessária a transferência de saldo de uma conta na parte B para outra conta na parte B. Não preencher quando: IND_VAL_LAN_LA_LB_PB for igual a “PF” ou “BC”.
Ver pagina 241""")
    hist_lan_lalb = fields.Char("Histórico do Lançamento.", required=True,
        help="""Histórico do Lançamento.
Ver pagina 241""")
    ind_lan_ant = fields.Char("IND_LAN_ANT", required=True,
        help="""Lançamento para Realização de Valores Cuja Tributação Tenha Sido Diferida: S – Sim N – Não  Observação: Marca-se “Sim” neste campo quando o contribuinte, em período anterior, realizou valores controlados na parte B do e-Lalur/e-Lacs e deve reajustar os saldos das contas em início de período de apuração tributado pelo lucro real.
Ver pagina 241""")
    parent_m030_id = fields.Many2one('l10n.br.sped.ecf.m030',
                                     string="Identificação do Período e Forma de Apuração do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Real")
    reg_m415_ids = fields.One2many('l10n.br.sped.ecf.m415','parent_m410_id',
                               string="Identificação de Processos Judiciais e Administrativos Referentes ao Lançamento",
                               help='Bloco M')

class RegistroM415(models.Model):
    _name = 'l10n.br.sped.ecf.m415'
    _description = u"""Identificação de Processos Judiciais e Administrativos Referentes ao Lançamento"""
    _inherit = 'l10n.br.sped.mixin'
    ind_proc = fields.Char("Tipo do Processo", required=True,
        help="""Tipo do Processo: 1 - Judicial  2 – Administrativo
Ver pagina 243""")
    num_proc = fields.Char("Número do Processo.", required=True,
        help="""Número do Processo.
Ver pagina 243""")
    parent_m410_id = fields.Many2one('l10n.br.sped.ecf.m410',
                                     string="Lançamentos na Conta da Parte B do e-Lalur e do e-Lacs Sem Reflexo na Parte A")

class RegistroM500(models.Model):
    _name = 'l10n.br.sped.ecf.m500'
    _description = u"""Controle de Saldos das Contas da Parte B do e-Lalur e do e-Lacs"""
    _inherit = 'l10n.br.sped.mixin'
    cod_cta_b = fields.Char("COD_CTA_B", required=True,
        help="""Código Unívoco Atribuído Pelo Contribuinte à Conta no e-Lalur e no e-Lacs (deve existir no M010.COD_CTA_B)
Ver pagina 244""")
    cod_tributo = fields.Char("Código do Tributo", required=True,
        help="""Código do Tributo: I – Imposto de Renda C – Contribuição Social Sobre o Lucro Líquido
Ver pagina 244""")
    sd_ini_lal = fields.Monetary("Saldo Inicial da Conta no Período de Apuração", required=True, digits=2)
    ind_sd_ini_lal = fields.Char("Indicador de Saldo Inicial", required=True,
        help="""Indicador de Saldo Inicial: D – Para prejuízos ou valores que serão excluídos do lucro real ou da base de cálculo da contribuição social em períodos subsequentes. C – Para valores que serão adicionados ao lucro real ou à base de cálculo da contribuição social em períodos subsequentes.
Ver pagina 244""")
    vl_lcto_parte_a = fields.Monetary("VL_LCTO_PARTE_A", required=True, digits=2)
    ind_vl_lcto_parte_a = fields.Char("IND_VL_LCTO_PARTE_A", required=True,
        help="""Indicador do Somatório dos Lançamentos da Parte B com Reflexo na Parte A no período: C – Para prejuízos ou valores que serão excluídos do lucro real ou da base de cálculo da contribuição social em períodos subsequentes. D – Para valores que serão adicionados ao lucro real ou à base de cálculo da contribuição social em períodos subsequentes.
Ver pagina 244""")
    vl_lcto_parte_b = fields.Monetary("VL_LCTO_PARTE_B", required=True, digits=2)
    ind_vl_lcto_parte_b = fields.Char("IND_VL_LCTO_PARTE_B", required=True,
        help="""Indicador Somatório dos Lançamentos da Parte B Sem Reflexo na Parte A no Período (entre contas da parte B): C – Para prejuízos ou valores que serão excluídos do lucro real ou da base de cálculo da contribuição social em períodos subsequentes. D – Para valores que serão adicionados ao lucro real ou à base de cálculo da contribuição social em períodos subsequentes.
Ver pagina 245""")
    sd_fim_lal = fields.Monetary("Saldo Final da Conta no Período de Apuração", required=True, digits=2)
    ind_sd_fim_lal = fields.Char("Indicador de Saldo Final", required=True,
        help="""Indicador de Saldo Final: D – Para prejuízos ou valores que serão excluídos do lucro real ou da base de cálculo da contribuição social em períodos subsequentes. C – Para valores que serão adicionados ao lucro real ou à base de cálculo da contribuição social em períodos subsequentes.
Ver pagina 245""")
    parent_m030_id = fields.Many2one('l10n.br.sped.ecf.m030',
                                     string="Identificação do Período e Forma de Apuração do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Real")

class RegistroN030(models.Model):
    _name = 'l10n.br.sped.ecf.n030'
    _description = u"""Identificação do Período e Forma de Apuração do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Real"""
    _inherit = 'l10n.br.sped.mixin'
    dt_ini = fields.Integer("Data do Início do Período", required=True)
    dt_fin = fields.Integer("Data do Fim do período", required=True)
    per_apur = fields.Char("Período de apuração [para 0010", required=True,
        help="""Período de apuração [para 0010.FORMA_APUR = “A”]:  A00 – Receita Bruta/ Balanço de Suspensão e Redução Anual A01 – Balanço de Suspensão e Redução até Janeiro  A02 – Balanço de Suspensão e Redução até Fevereiro A03 – Balanço de Suspensão e Redução até Março A04 – Balanço de Suspensão e Redução até Abril  A05 – Balanço de Suspensão e Redução até Maio A06 – Balanço de Suspensão e Redução até Junho  A07 – Balanço de Suspensão e Redução até Julho A08 – Balanço de Suspensão e Redução até Agosto  A09 – Balanço de Suspensão e Redução até Setembro  A10 – Balanço de Suspensão e Redução até Outubro  A11 – Balanço de Suspensão e Redução até Novembro   A12 – Balanço de Suspensão e Redução até Dezembro  ndicador do período de referência [para 0010.FORMA_APUR = “T” OU (0010.FORMA_APUR = “A” E 0010.FORMA_TRIB = “2”)]: T01 – 1º Trimestre T02 – 2º Trimestre T03 – 3º Trimestre  T04 – 4º Trimestre Regra: O período deve estar compreendido entre a data início e data fim da escrituração. Regra: SE 0010.FORMA_APUR = “A”  - Deve existir um registro A00. - Deve existir um registro [A01..A012] para cada mês marcado no 0010.MES_BAL_RED [1..12] como “B” ou "E". E 0010.FORMA_APUR = “T”  - Deve existir um registro [T01..T04] para cada trimestre marcado no 0010.FORMA_TRIB_PER[1..4] como “R”   I  S
Ver pagina 249""")
    reg_n500_ids = fields.One2many('l10n.br.sped.ecf.n500','parent_n030_id',
                               string="Base de Cálculo do IRPJ Sobre o Lucro Real Após as Compensações de Prejuízos",
                               help='Bloco N')
    reg_n600_ids = fields.One2many('l10n.br.sped.ecf.n600','parent_n030_id',
                               string="Demonstração do Lucro da Exploração",
                               help='Bloco N')
    reg_n610_ids = fields.One2many('l10n.br.sped.ecf.n610','parent_n030_id',
                               string="Cálculo da Isenção e Redução do Imposto sobre Lucro Real",
                               help='Bloco N')
    reg_n615_ids = fields.One2many('l10n.br.sped.ecf.n615','parent_n030_id',
                               string="Informações da Base de Cálculo de Incentivos Fiscais",
                               help='Bloco N')
    reg_n620_ids = fields.One2many('l10n.br.sped.ecf.n620','parent_n030_id',
                               string="Apuração do IRPJ Mensal por Estimativa",
                               help='Bloco N')
    reg_n630_ids = fields.One2many('l10n.br.sped.ecf.n630','parent_n030_id',
                               string="Apuração do IRPJ Com Base no Lucro Real",
                               help='Bloco N')
    reg_n650_ids = fields.One2many('l10n.br.sped.ecf.n650','parent_n030_id',
                               string="Base  de  Cálculo  da  CSLL  Após  Compensações  das Bases de Cálculo Negativa",
                               help='Bloco N')
    reg_n660_ids = fields.One2many('l10n.br.sped.ecf.n660','parent_n030_id',
                               string="Apuração da CSLL Mensal por Estimativa",
                               help='Bloco N')
    reg_n670_ids = fields.One2many('l10n.br.sped.ecf.n670','parent_n030_id',
                               string="Apuração da CSLL Com Base no Lucro Real",
                               help='Bloco N')

class RegistroN500(models.Model):
    _name = 'l10n.br.sped.ecf.n500'
    _description = u"""Base de Cálculo do IRPJ Sobre o Lucro Real Após as Compensações de Prejuízos"""
    _inherit = 'l10n.br.sped.mixin'
    codigo = fields.Char("CODIGO", required=True,
        help="""Código, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro e
Ver pagina 251""")
    descricao = fields.Char("DESCRICAO",
        help="""Descrição, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro
Ver pagina 251""")
    valor = fields.Monetary("Valor", digits=2)
    parent_n030_id = fields.Many2one('l10n.br.sped.ecf.n030',
                                     string="Identificação do Período e Forma de Apuração do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Real")

class RegistroN600(models.Model):
    _name = 'l10n.br.sped.ecf.n600'
    _description = u"""Demonstração do Lucro da Exploração"""
    _inherit = 'l10n.br.sped.mixin'
    codigo = fields.Char("CODIGO", required=True,
        help="""Código, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro e
Ver pagina 254""")
    descricao = fields.Char("DESCRICAO",
        help="""Descrição, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro
Ver pagina 254""")
    valor = fields.Monetary("Valor", digits=2)
    parent_n030_id = fields.Many2one('l10n.br.sped.ecf.n030',
                                     string="Identificação do Período e Forma de Apuração do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Real")

class RegistroN610(models.Model):
    _name = 'l10n.br.sped.ecf.n610'
    _description = u"""Cálculo da Isenção e Redução do Imposto sobre Lucro Real"""
    _inherit = 'l10n.br.sped.mixin'
    codigo = fields.Char("CODIGO", required=True,
        help="""Código, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro e
Ver pagina 258""")
    descricao = fields.Char("DESCRICAO",
        help="""Descrição, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro
Ver pagina 258""")
    valor = fields.Monetary("Valor", digits=2)
    parent_n030_id = fields.Many2one('l10n.br.sped.ecf.n030',
                                     string="Identificação do Período e Forma de Apuração do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Real")

class RegistroN615(models.Model):
    _name = 'l10n.br.sped.ecf.n615'
    _description = u"""Informações da Base de Cálculo de Incentivos Fiscais"""
    _inherit = 'l10n.br.sped.mixin'
    base_calc = fields.Monetary("BASE_CALC", required=True, digits=2)
    per_incen_finor = fields.Monetary("Percentual do Incentivo FINOR (até 6%).", required=True, digits=4)
    vl_liq_incen_finor = fields.Monetary("Valor Líquido do Incentivo FINOR.", required=True, digits=2)
    per_incen_finam = fields.Monetary("Percentual do Incentivo FINAM (até 6%).", required=True, digits=4)
    vl_liq_incen_finam = fields.Monetary("Valor Líquido do Incentivo FINAM.", required=True, digits=2)
    vl_total = fields.Monetary("Total dos Incentivos.", required=True, digits=2)
    parent_n030_id = fields.Many2one('l10n.br.sped.ecf.n030',
                                     string="Identificação do Período e Forma de Apuração do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Real")

class RegistroN620(models.Model):
    _name = 'l10n.br.sped.ecf.n620'
    _description = u"""Apuração do IRPJ Mensal por Estimativa"""
    _inherit = 'l10n.br.sped.mixin'
    codigo = fields.Char("CODIGO", required=True,
        help="""Código, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro e
Ver pagina 265""")
    descricao = fields.Char("DESCRICAO",
        help="""Descrição, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro
Ver pagina 265""")
    valor = fields.Monetary("Valor", digits=2)
    parent_n030_id = fields.Many2one('l10n.br.sped.ecf.n030',
                                     string="Identificação do Período e Forma de Apuração do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Real")

class RegistroN630(models.Model):
    _name = 'l10n.br.sped.ecf.n630'
    _description = u"""Apuração do IRPJ Com Base no Lucro Real"""
    _inherit = 'l10n.br.sped.mixin'
    codigo = fields.Char("CODIGO", required=True,
        help="""Código, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro e
Ver pagina 267""")
    descricao = fields.Char("DESCRICAO",
        help="""Descrição, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro
Ver pagina 267""")
    valor = fields.Monetary("Valor", digits=2)
    parent_n030_id = fields.Many2one('l10n.br.sped.ecf.n030',
                                     string="Identificação do Período e Forma de Apuração do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Real")

class RegistroN650(models.Model):
    _name = 'l10n.br.sped.ecf.n650'
    _description = u"""Base  de  Cálculo  da  CSLL  Após  Compensações  das Bases de Cálculo Negativa"""
    _inherit = 'l10n.br.sped.mixin'
    codigo = fields.Char("CODIGO", required=True,
        help="""Código, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro e
Ver pagina 270""")
    descricao = fields.Char("DESCRICAO",
        help="""Descrição, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro
Ver pagina 270""")
    valor = fields.Monetary("Valor", digits=2)
    parent_n030_id = fields.Many2one('l10n.br.sped.ecf.n030',
                                     string="Identificação do Período e Forma de Apuração do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Real")

class RegistroN660(models.Model):
    _name = 'l10n.br.sped.ecf.n660'
    _description = u"""Apuração da CSLL Mensal por Estimativa"""
    _inherit = 'l10n.br.sped.mixin'
    codigo = fields.Char("CODIGO", required=True,
        help="""Código, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro e
Ver pagina 274""")
    descricao = fields.Char("DESCRICAO",
        help="""Descrição, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro
Ver pagina 274""")
    valor = fields.Monetary("Valor", digits=2)
    parent_n030_id = fields.Many2one('l10n.br.sped.ecf.n030',
                                     string="Identificação do Período e Forma de Apuração do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Real")

class RegistroN670(models.Model):
    _name = 'l10n.br.sped.ecf.n670'
    _description = u"""Apuração da CSLL Com Base no Lucro Real"""
    _inherit = 'l10n.br.sped.mixin'
    codigo = fields.Char("CODIGO", required=True,
        help="""Código, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro e
Ver pagina 276""")
    descricao = fields.Char("DESCRICAO",
        help="""Descrição, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro
Ver pagina 276""")
    valor = fields.Monetary("Valor", digits=2)
    parent_n030_id = fields.Many2one('l10n.br.sped.ecf.n030',
                                     string="Identificação do Período e Forma de Apuração do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Real")

class RegistroP030(models.Model):
    _name = 'l10n.br.sped.ecf.p030'
    _description = u"""Identificação  dos  Períodos  e  Forma  de  Apuração  do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Presumido"""
    _inherit = 'l10n.br.sped.mixin'
    dt_ini = fields.Integer("Data do Início do Período", required=True)
    dt_fin = fields.Integer("Data do Fim do período", required=True)
    per_apur = fields.Char("PER_APUR", required=True,
        help="""A00 – Anual (para registrar o Balanço Patrimonial anual e a DRE anual) T01 – 1º Trimestre T02 – 2º Trimestre T03 – 3º Trimestre  T04 – 4º Trimestre Regra: O período deve estar compreendido entre a data início e data fim da escrituração. SE 0010.FORMA_APUR = “T”  - Deve existir um registro [T01..T04] para cada trimestre marcado no 0010.FORMA_TRIB_PER[1..4] como “P”
Ver pagina 293""")
    reg_p100_ids = fields.One2many('l10n.br.sped.ecf.p100','parent_p030_id',
                               string="Balanço Patrimonial",
                               help='Bloco P')
    reg_p130_ids = fields.One2many('l10n.br.sped.ecf.p130','parent_p030_id',
                               string="Demonstração  das  Receitas  Incentivadas  do  Lucro Presumido",
                               help='Bloco P')
    reg_p150_ids = fields.One2many('l10n.br.sped.ecf.p150','parent_p030_id',
                               string="Demonstração do Resultado",
                               help='Bloco P')
    reg_p200_ids = fields.One2many('l10n.br.sped.ecf.p200','parent_p030_id',
                               string="Apuração da Base de Cálculo do Lucro Presumido",
                               help='Bloco P')
    reg_p230_ids = fields.One2many('l10n.br.sped.ecf.p230','parent_p030_id',
                               string="Cálculo da Isenção e Redução do Lucro Presumido",
                               help='Bloco P')
    reg_p300_ids = fields.One2many('l10n.br.sped.ecf.p300','parent_p030_id',
                               string="Cálculo do IRPJ com Base no Lucro Presumido",
                               help='Bloco P')
    reg_p400_ids = fields.One2many('l10n.br.sped.ecf.p400','parent_p030_id',
                               string="Apuração da Base de Cálculo da CSLL com Base no Lucro Presumido",
                               help='Bloco P')
    reg_p500_ids = fields.One2many('l10n.br.sped.ecf.p500','parent_p030_id',
                               string="Cálculo da CSLL com Base no Lucro Líquido",
                               help='Bloco P')

class RegistroP100(models.Model):
    _name = 'l10n.br.sped.ecf.p100'
    _description = u"""Balanço Patrimonial"""
    _inherit = 'l10n.br.sped.mixin'
    codigo = fields.Char("CODIGO", required=True,
        help="""Código da Conta Referencial (Analíticas e Sintéticas), conforme tabela dinâmica do Sped (Disponibilizada no item II deste registro e no programa da ECF, no diretório
Ver pagina 295""")
    descricao = fields.Char("Descrição da Conta Referencial.",
        help="""Descrição da Conta Referencial.
Ver pagina 295""")
    tipo = fields.Char("Indicador do Tipo de Conta", required=True,
        help="""Indicador do Tipo de Conta: S – Sintética A – Analítica
Ver pagina 295""")
    nivel = fields.Integer("Nível da Conta.")
    cod_nat = fields.Char("COD_NAT",
        help="""Natureza da Conta, conforme tabela do Sped (Disponibilizada no programa da ECF
Ver pagina 295""")
    cod_cta_sup = fields.Char("Código da Conta Sintética de Nível Imediatamente Superior",
        help="""Código da Conta Sintética de Nível Imediatamente Superior.
Ver pagina 295""")
    val_cta_ref_ini = fields.Monetary("Saldo Inicial da Conta Referencial.", required=True, digits=2)
    ind_val_cta_ref_ini = fields.Char("Indicador da Situação do Saldo Inicial", required=True,
        help="""Indicador da Situação do Saldo Inicial: D – Devedor C – Credor
Ver pagina 295""")
    val_cta_ref_fin = fields.Char("Saldo Final da Conta Referencial", required=True,
        help="""Saldo Final da Conta Referencial
Ver pagina 296""")
    ind_val_cta_ref_fin = fields.Char("Indicador da Situação do Saldo Final", required=True,
        help="""Indicador da Situação do Saldo Final: D – Devedor C – Credor
Ver pagina 296""")
    parent_p030_id = fields.Many2one('l10n.br.sped.ecf.p030',
                                     string="Identificação  dos  Períodos  e  Forma  de  Apuração  do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Presumido")

class RegistroP130(models.Model):
    _name = 'l10n.br.sped.ecf.p130'
    _description = u"""Demonstração  das  Receitas  Incentivadas  do  Lucro Presumido"""
    _inherit = 'l10n.br.sped.mixin'
    codigo = fields.Char("CODIGO", required=True,
        help="""Código, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro e
Ver pagina 299""")
    descricao = fields.Char("DESCRICAO",
        help="""Descrição, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro
Ver pagina 299""")
    valor = fields.Monetary("Valor", digits=2)
    parent_p030_id = fields.Many2one('l10n.br.sped.ecf.p030',
                                     string="Identificação  dos  Períodos  e  Forma  de  Apuração  do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Presumido")

class RegistroP150(models.Model):
    _name = 'l10n.br.sped.ecf.p150'
    _description = u"""Demonstração do Resultado"""
    _inherit = 'l10n.br.sped.mixin'
    codigo = fields.Char("", required=True,
        help="""
Ver pagina 301""")
    descricao = fields.Char("Descrição da Conta Referencial.",
        help="""Descrição da Conta Referencial.
Ver pagina 301""")
    tipo = fields.Char("Indicador do Tipo de Conta", required=True,
        help="""Indicador do Tipo de Conta: S – Sintética  A – Analítica
Ver pagina 301""")
    nivel = fields.Integer("Nível da Conta.")
    cod_nat = fields.Char("Natureza da Conta",
        help="""Natureza da Conta: 04 – Contas de Resultado
Ver pagina 301""")
    cod_cta_sup = fields.Char("Código da Conta Sintética de Nível Imediatamente Superior",
        help="""Código da Conta Sintética de Nível Imediatamente Superior.
Ver pagina 301""")
    valor = fields.Monetary("Saldo Final da Conta Referencial.", required=True, digits=2)
    ind_valor = fields.Char("Indicador do Sinal do Saldo Final", required=True,
        help="""Indicador do Sinal do Saldo Final:  C – Credor D – Devedor
Ver pagina 301""")
    parent_p030_id = fields.Many2one('l10n.br.sped.ecf.p030',
                                     string="Identificação  dos  Períodos  e  Forma  de  Apuração  do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Presumido")

class RegistroP200(models.Model):
    _name = 'l10n.br.sped.ecf.p200'
    _description = u"""Apuração da Base de Cálculo do Lucro Presumido"""
    _inherit = 'l10n.br.sped.mixin'
    codigo = fields.Char("CODIGO", required=True,
        help="""Código, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro e
Ver pagina 304""")
    descricao = fields.Char("DESCRICAO",
        help="""Descrição, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro
Ver pagina 304""")
    valor = fields.Monetary("Valor", digits=2)
    parent_p030_id = fields.Many2one('l10n.br.sped.ecf.p030',
                                     string="Identificação  dos  Períodos  e  Forma  de  Apuração  do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Presumido")

class RegistroP230(models.Model):
    _name = 'l10n.br.sped.ecf.p230'
    _description = u"""Cálculo da Isenção e Redução do Lucro Presumido"""
    _inherit = 'l10n.br.sped.mixin'
    codigo = fields.Char("CODIGO", required=True,
        help="""Código, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro e
Ver pagina 306""")
    descricao = fields.Char("DESCRICAO",
        help="""Descrição, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro
Ver pagina 306""")
    valor = fields.Monetary("Valor", digits=2)
    parent_p030_id = fields.Many2one('l10n.br.sped.ecf.p030',
                                     string="Identificação  dos  Períodos  e  Forma  de  Apuração  do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Presumido")

class RegistroP300(models.Model):
    _name = 'l10n.br.sped.ecf.p300'
    _description = u"""Cálculo do IRPJ com Base no Lucro Presumido"""
    _inherit = 'l10n.br.sped.mixin'
    codigo = fields.Char("CODIGO", required=True,
        help="""Código, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro e
Ver pagina 308""")
    descricao = fields.Char("DESCRICAO",
        help="""Descrição, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro
Ver pagina 308""")
    valor = fields.Monetary("Valor", digits=2)
    parent_p030_id = fields.Many2one('l10n.br.sped.ecf.p030',
                                     string="Identificação  dos  Períodos  e  Forma  de  Apuração  do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Presumido")

class RegistroP400(models.Model):
    _name = 'l10n.br.sped.ecf.p400'
    _description = u"""Apuração da Base de Cálculo da CSLL com Base no Lucro Presumido"""
    _inherit = 'l10n.br.sped.mixin'
    codigo = fields.Char("CODIGO", required=True,
        help="""Código, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro e
Ver pagina 310""")
    descricao = fields.Char("DESCRICAO",
        help="""Descrição, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro
Ver pagina 310""")
    valor = fields.Monetary("Valor", digits=2)
    parent_p030_id = fields.Many2one('l10n.br.sped.ecf.p030',
                                     string="Identificação  dos  Períodos  e  Forma  de  Apuração  do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Presumido")

class RegistroP500(models.Model):
    _name = 'l10n.br.sped.ecf.p500'
    _description = u"""Cálculo da CSLL com Base no Lucro Líquido"""
    _inherit = 'l10n.br.sped.mixin'
    codigo = fields.Char("CODIGO", required=True,
        help="""Código, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro e
Ver pagina 312""")
    descricao = fields.Char("DESCRICAO",
        help="""Descrição, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro
Ver pagina 312""")
    valor = fields.Monetary("Valor", digits=2)
    parent_p030_id = fields.Many2one('l10n.br.sped.ecf.p030',
                                     string="Identificação  dos  Períodos  e  Forma  de  Apuração  do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Presumido")

class RegistroQ100(models.Model):
    _name = 'l10n.br.sped.ecf.q100'
    _description = u"""Demonstrativo do Livro Caixa"""
    _inherit = 'l10n.br.sped.mixin'
    data = fields.Integer("Data da entrada ou da saída dos recursos", required=True)
    num_doc = fields.Char("Número do documento.",
        help="""Número do documento.
Ver pagina 316""")
    hist = fields.Char("Histórico", required=True,
        help="""Histórico
Ver pagina 316""")
    vl_entrada = fields.Monetary("Valor de entrada dos recursos.", digits=2)
    vl_saida = fields.Monetary("Valor de saída dos recursos.", digits=2)
    sld_fin = fields.Monetary("Saldo Final.", required=True, digits=2)

class RegistroT030(models.Model):
    _name = 'l10n.br.sped.ecf.t030'
    _description = u"""Identificação  dos  Períodos  e  Forma  de  Apuração  do IRPJ  e  CSLL  das  Empresas  Tributadas  pelo  Lucro Arbitrado"""
    _inherit = 'l10n.br.sped.mixin'
    dt_ini = fields.Integer("Data do Início do Período", required=True)
    dt_fin = fields.Integer("Data do Fim do período", required=True)
    per_apur = fields.Char("PER_APUR", required=True,
        help="""T01 – 1º Trimestre T02 – 2º Trimestre T03 – 3º Trimestre  T04 – 4º Trimestre Regra: o período deve estar compreendido entre a data início e data fim da escrituração. E 0010.FORMA_APUR = “T”  - Deve existir um registro [T01..T04] para cada trimestre marcado no 0010.FORMA_TRIB_PER[1..4] como “A”   S
Ver pagina 330""")
    reg_t120_ids = fields.One2many('l10n.br.sped.ecf.t120','parent_t030_id',
                               string="Apuração  da  Base  de  Cálculo  do  IRPJ  com  Base  no Lucro Arbitrado",
                               help='Bloco T')
    reg_t150_ids = fields.One2many('l10n.br.sped.ecf.t150','parent_t030_id',
                               string="Cálculo  do  Imposto  de  Renda  com  Base  no  Lucro Arbitrado",
                               help='Bloco T')
    reg_t170_ids = fields.One2many('l10n.br.sped.ecf.t170','parent_t030_id',
                               string="Apuração da Base de Cálculo da CSLL com Base no Lucro Arbitrado",
                               help='Bloco T')
    reg_t181_ids = fields.One2many('l10n.br.sped.ecf.t181','parent_t030_id',
                               string="Cálculo da CSLL com Base no Lucro Arbitrado",
                               help='Bloco T')

class RegistroT120(models.Model):
    _name = 'l10n.br.sped.ecf.t120'
    _description = u"""Apuração  da  Base  de  Cálculo  do  IRPJ  com  Base  no Lucro Arbitrado"""
    _inherit = 'l10n.br.sped.mixin'
    codigo = fields.Char("CODIGO", required=True,
        help="""Código, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro e
Ver pagina 332""")
    descricao = fields.Char("DESCRICAO",
        help="""Descrição, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro
Ver pagina 332""")
    valor = fields.Monetary("Valor", digits=2)
    parent_t030_id = fields.Many2one('l10n.br.sped.ecf.t030',
                                     string="Identificação  dos  Períodos  e  Forma  de  Apuração  do IRPJ  e  CSLL  das  Empresas  Tributadas  pelo  Lucro Arbitrado")

class RegistroT150(models.Model):
    _name = 'l10n.br.sped.ecf.t150'
    _description = u"""Cálculo  do  Imposto  de  Renda  com  Base  no  Lucro Arbitrado"""
    _inherit = 'l10n.br.sped.mixin'
    codigo = fields.Char("CODIGO", required=True,
        help="""Código, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro e
Ver pagina 334""")
    descricao = fields.Char("DESCRICAO",
        help="""Descrição, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro
Ver pagina 334""")
    valor = fields.Monetary("Valor", digits=2)
    parent_t030_id = fields.Many2one('l10n.br.sped.ecf.t030',
                                     string="Identificação  dos  Períodos  e  Forma  de  Apuração  do IRPJ  e  CSLL  das  Empresas  Tributadas  pelo  Lucro Arbitrado")

class RegistroT170(models.Model):
    _name = 'l10n.br.sped.ecf.t170'
    _description = u"""Apuração da Base de Cálculo da CSLL com Base no Lucro Arbitrado"""
    _inherit = 'l10n.br.sped.mixin'
    codigo = fields.Char("CODIGO", required=True,
        help="""Código, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro e
Ver pagina 336""")
    descricao = fields.Char("DESCRICAO",
        help="""Descrição, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro
Ver pagina 336""")
    valor = fields.Monetary("Valor", digits=2)
    parent_t030_id = fields.Many2one('l10n.br.sped.ecf.t030',
                                     string="Identificação  dos  Períodos  e  Forma  de  Apuração  do IRPJ  e  CSLL  das  Empresas  Tributadas  pelo  Lucro Arbitrado")

class RegistroT181(models.Model):
    _name = 'l10n.br.sped.ecf.t181'
    _description = u"""Cálculo da CSLL com Base no Lucro Arbitrado"""
    _inherit = 'l10n.br.sped.mixin'
    codigo = fields.Char("CODIGO", required=True,
        help="""Código, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro e
Ver pagina 338""")
    descricao = fields.Char("DESCRICAO",
        help="""Descrição, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro
Ver pagina 338""")
    valor = fields.Monetary("Valor", digits=2)
    parent_t030_id = fields.Many2one('l10n.br.sped.ecf.t030',
                                     string="Identificação  dos  Períodos  e  Forma  de  Apuração  do IRPJ  e  CSLL  das  Empresas  Tributadas  pelo  Lucro Arbitrado")

class RegistroU030(models.Model):
    _name = 'l10n.br.sped.ecf.u030'
    _description = u"""Identificação dos Períodos e Formas de Apuração do IPRJ e da CSLL das Empresas Imunes e Isentas"""
    _inherit = 'l10n.br.sped.mixin'
    dt_ini = fields.Integer("Data do Início do Período", required=True)
    dt_fin = fields.Integer("Data do Fim do período", required=True)
    per_apur = fields.Char("Período de apuração (para 0010", required=True,
        help="""Período de apuração (para 0010.APUR_CSLL = “A”):  A00 – Anual A01 – Rec. Bruta de janeiro /Balanço suspensão redução até janeiro  A02 – Rec. Bruta de fevereiro /Balanço suspensão redução até fevereiro A03 – Rec. Bruta de março /Balanço suspensão redução até março A04 – Rec. Bruta de abril /Balanço suspensão redução até abril  A05 – Rec. Bruta de maio /Balanço suspensão redução até maio A06 – Rec. Bruta de junho /Balanço suspensão redução até junho A07 – Rec. Bruta de julho /Balanço suspensão redução até julho A08 – Rec. Bruta de agosto /Balanço suspensão redução até agosto A09 – Rec. Bruta de setembro /Balanço suspensão redução até setembro A10 – Rec. Bruta de outubro/Balanço suspensão redução até outubro A11 – Rec. Bruta de novembro /Balanço suspensão redução até novembro A12 – Rec. Bruta de dezembro/Balanço suspensão redução até dezembro Período de apuração (para 0010.APUR_CSLL = “T”):  T01 – 1º Trimestre T02 – 2º Trimestre T03 – 3º Trimestre  T04 – 4º Trimestre
Ver pagina 347""")
    reg_u100_ids = fields.One2many('l10n.br.sped.ecf.u100','parent_u030_id',
                               string="Balanço Patrimonial",
                               help='Bloco U')
    reg_u150_ids = fields.One2many('l10n.br.sped.ecf.u150','parent_u030_id',
                               string="Demonstração do Resultado",
                               help='Bloco U')
    reg_u180_ids = fields.One2many('l10n.br.sped.ecf.u180','parent_u030_id',
                               string="Cálculo do IRPJ das Empresas Imunes ou Isentas",
                               help='Bloco U')
    reg_u182_ids = fields.One2many('l10n.br.sped.ecf.u182','parent_u030_id',
                               string="Cálculo da CSLL das Empresas Imunes ou Isentas",
                               help='Bloco U')

class RegistroU100(models.Model):
    _name = 'l10n.br.sped.ecf.u100'
    _description = u"""Balanço Patrimonial"""
    _inherit = 'l10n.br.sped.mixin'
    codigo = fields.Char("CODIGO", required=True,
        help="""Código da Conta Referencial (Analíticas e Sintéticas), conforme tabela dinâmica do Sped (Disponibilizada no item II deste registro e no programa da ECF, no diretório
Ver pagina 349""")
    descricao = fields.Char("Descrição da Conta Referencial.",
        help="""Descrição da Conta Referencial.
Ver pagina 349""")
    tipo = fields.Char("Indicador do Tipo de Conta", required=True,
        help="""Indicador do Tipo de Conta: S – Sintética A – Analítica
Ver pagina 349""")
    nivel = fields.Integer("Nível da Conta.")
    cod_nat = fields.Char("COD_NAT",
        help="""Natureza da Conta, conforme tabela do Sped (Disponibilizada no programa da ECF
Ver pagina 349""")
    cod_cta_sup = fields.Char("Código da Conta Sintética de Nível Imediatamente Superior",
        help="""Código da Conta Sintética de Nível Imediatamente Superior.
Ver pagina 349""")
    val_cta_ref_ini = fields.Monetary("Saldo Inicial da Conta Referencial.", required=True, digits=2)
    ind_val_cta_ref_ini = fields.Char("Indicador da Situação do Saldo Inicial", required=True,
        help="""Indicador da Situação do Saldo Inicial: D – Devedor C – Credor
Ver pagina 349""")
    val_cta_ref_fin = fields.Char("Saldo Final da Conta Referencial", required=True,
        help="""Saldo Final da Conta Referencial
Ver pagina 349""")
    ind_val_cta_ref_fin = fields.Char("Indicador da Situação do Saldo Final", required=True,
        help="""Indicador da Situação do Saldo Final: D – Devedor C – Credor
Ver pagina 350""")
    parent_u030_id = fields.Many2one('l10n.br.sped.ecf.u030',
                                     string="Identificação dos Períodos e Formas de Apuração do IPRJ e da CSLL das Empresas Imunes e Isentas")

class RegistroU150(models.Model):
    _name = 'l10n.br.sped.ecf.u150'
    _description = u"""Demonstração do Resultado"""
    _inherit = 'l10n.br.sped.mixin'
    codigo = fields.Char("", required=True,
        help="""
Ver pagina 353""")
    descricao = fields.Char("Descrição da Conta Referencial.",
        help="""Descrição da Conta Referencial.
Ver pagina 353""")
    tipo = fields.Char("Indicador do Tipo de Conta", required=True,
        help="""Indicador do Tipo de Conta: S – Sintética  A – Analítica
Ver pagina 353""")
    nivel = fields.Integer("Nível da Conta.")
    cod_nat = fields.Char("Natureza da Conta",
        help="""Natureza da Conta: 04 – Contas de Resultado
Ver pagina 353""")
    cod_cta_sup = fields.Char("Código da Conta Sintética de Nível Imediatamente Superior",
        help="""Código da Conta Sintética de Nível Imediatamente Superior.
Ver pagina 353""")
    valor = fields.Monetary("Saldo Final da Conta Referencial.", required=True, digits=2)
    ind_valor = fields.Char("Indicador do Sinal do Saldo Final", required=True,
        help="""Indicador do Sinal do Saldo Final:  C – Credor D – Devedor
Ver pagina 353""")
    parent_u030_id = fields.Many2one('l10n.br.sped.ecf.u030',
                                     string="Identificação dos Períodos e Formas de Apuração do IPRJ e da CSLL das Empresas Imunes e Isentas")

class RegistroU180(models.Model):
    _name = 'l10n.br.sped.ecf.u180'
    _description = u"""Cálculo do IRPJ das Empresas Imunes ou Isentas"""
    _inherit = 'l10n.br.sped.mixin'
    codigo = fields.Char("CODIGO", required=True,
        help="""Código, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro e
Ver pagina 357""")
    descricao = fields.Char("DESCRICAO",
        help="""Descrição, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro
Ver pagina 357""")
    valor = fields.Monetary("Valor", digits=2)
    parent_u030_id = fields.Many2one('l10n.br.sped.ecf.u030',
                                     string="Identificação dos Períodos e Formas de Apuração do IPRJ e da CSLL das Empresas Imunes e Isentas")

class RegistroU182(models.Model):
    _name = 'l10n.br.sped.ecf.u182'
    _description = u"""Cálculo da CSLL das Empresas Imunes ou Isentas"""
    _inherit = 'l10n.br.sped.mixin'
    codigo = fields.Char("CODIGO", required=True,
        help="""Código, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro e
Ver pagina 359""")
    descricao = fields.Char("DESCRICAO",
        help="""Descrição, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro
Ver pagina 359""")
    valor = fields.Monetary("Valor", digits=2)
    parent_u030_id = fields.Many2one('l10n.br.sped.ecf.u030',
                                     string="Identificação dos Períodos e Formas de Apuração do IPRJ e da CSLL das Empresas Imunes e Isentas")
    reg_w250_ids = fields.One2many('l10n.br.sped.ecf.w250','parent_u182_id',
                               string="Declaração País a País - Entidades Integrantes",
                               help='Bloco W')

class RegistroW250(models.Model):
    _name = 'l10n.br.sped.ecf.w250'
    _description = u"""Declaração País a País - Entidades Integrantes"""
    _inherit = 'l10n.br.sped.mixin'
    jur_diferente = fields.Char("JUR_DIFERENTE",
        help="""Jurisdição Tributária de Organização ou Incorporação, se diferente da jurisdição de residência para fins tributários, conforme tabela do Sped (Disponibilizada no programa da ECF no diretório Arquivos de Programas/Programas Sped/ECf/SpedEcf/Recursos/Tabelas): A entidade declarante deve informar a jurisdição
Ver pagina 398""")
    nome = fields.Char("Nome/Razão Social da Entidade Integrante", required=True,
        help="""Nome/Razão Social da Entidade Integrante: Nome legal completo da entidade, incluindo a designação doméstica da forma legal, conforme indicado em seus documentos de constituição ou similares.  Caso a entidade seja um estabelecimento permanente, deverá ser reportada com referência à jurisdição onde está situada, e seu nome deve ser seguido por (P.E.), designação que significa, em inglês, “Permanent Establishment” (Estabelecimento
Ver pagina 398""")
    tin = fields.Char("Tax Identification Number (TIN)", required=True,
        help="""Tax Identification Number (TIN): Número de identificação fiscal utilizado pela
Ver pagina 399""")
    jurisdicao_tin = fields.Char("JURISDICAO_TIN",
        help="""Jurisdição de Emissão do TIN, conforme tabela do Sped (Disponibilizada no programa da
Ver pagina 399""")
    ni = fields.Char("Número de Identificação (NI)",
        help="""Número de Identificação (NI): O campo deve ser preenchido em caso de existência de outro número de identificação da entidade, como um número de registro ou um número de identificação global da entidade (“Global Entity Identification Number” – EIN).
Ver pagina 399""")
    jurisdicao_ni = fields.Char("JURISDICAO_NI",
        help="""Jurisdição de Emissão do NI, conforme tabela do Sped (Disponibilizada no programa da
Ver pagina 399""")
    tipo_ni = fields.Char("TIPO_NI",
        help="""Tipo do NI: Deve ser descrito, em texto livre, o tipo do número de identificação (NI) informado no W250.NI.  Exemplo: número de identificação global da entidade (“Global Entity Identification Number” – EIN).
Ver pagina 399""")
    tip_end = fields.Char("Tipo do Endereço", required=True,
        help="""Tipo do Endereço: A entidade declarante deve indicar, dentre as opções disponíveis de preenchimento do campo, o tipo do endereço da entidade integrante que está sendo reportada, o qual deverá ser descrito no campo seguinte. ECD302 - Residencial OECD303 - Comercial   O
Ver pagina 399""")
    endereco = fields.Char("ENDERECO", required=True,
        help="""Deve ser fornecido, em texto livre, o endereço completo de residência permanente da entidade integrante reportada.
Ver pagina 399""")
    num_tel = fields.Char("Número de telefone completo da entidade integrante reportada",
        help="""Número de telefone completo da entidade integrante reportada.
Ver pagina 399""")
    email = fields.Char("EMAIL",
        help="""Endereço de e-mail para contato com a entidade integrante reportada.
Ver pagina 399""")
    ativ_1 = fields.Char("Pesquisa e Desenvolvimento", required=True,
        help="""Pesquisa e Desenvolvimento: S - Sim N - Não
Ver pagina 399""")
    ativ_2 = fields.Char("Gestão de Propriedade Intelectual", required=True,
        help="""Gestão de Propriedade Intelectual: S - Sim N - Não
Ver pagina 400""")
    ativ_3 = fields.Char("Compras: S - Sim N - Não", required=True,
        help="""Compras: S - Sim N - Não
Ver pagina 400""")
    ativ_4 = fields.Char("Manufatura ou Produção: S - Sim N - Não", required=True,
        help="""Manufatura ou Produção: S - Sim N - Não
Ver pagina 400""")
    ativ_5 = fields.Char("Vendas, Marketing ou Distribuição", required=True,
        help="""Vendas, Marketing ou Distribuição: S - Sim N - Não
Ver pagina 400""")
    ativ_6 = fields.Char("Serviços Administrativos, de Gestão ou de Suporte", required=True,
        help="""Serviços Administrativos, de Gestão ou de Suporte: S - Sim N - Não
Ver pagina 400""")
    ativ_7 = fields.Char("Prestação de Serviços a Partes Não Relacionadas", required=True,
        help="""Prestação de Serviços a Partes Não Relacionadas: S - Sim N - Não
Ver pagina 400""")
    ativ_8 = fields.Char("Departamento Financeiro do Grupo", required=True,
        help="""Departamento Financeiro do Grupo: S - Sim N - Não
Ver pagina 400""")
    ativ_9 = fields.Char("Serviços Financeiros Regulamentados", required=True,
        help="""Serviços Financeiros Regulamentados: S - Sim N - Não
Ver pagina 400""")
    ativ_10 = fields.Char("Seguro: S - Sim N - Não", required=True,
        help="""Seguro: S - Sim N - Não
Ver pagina 400""")
    ativ_11 = fields.Char("Gestão de Ações e Outros Instrumentos de Capital", required=True,
        help="""Gestão de Ações e Outros Instrumentos de Capital: S - Sim N - Não
Ver pagina 400""")
    ativ_12 = fields.Char("Inativa: S - Sim N - Não", required=True,
        help="""Inativa: S - Sim N - Não
Ver pagina 400""")
    ativ_13 = fields.Char("Outros: S - Sim N - Não", required=True,
        help="""Outros: S - Sim N - Não
Ver pagina 401""")
    desc_outros = fields.Char("Descrição da Atividade Econômica Desempenhada, no caso de W250",
        help="""Descrição da Atividade Econômica Desempenhada, no caso de W250.ATIV_13 (Outros) igual a "Sim": Campo em texto livre para que a entidade declarante descreva as atividades econômicas desempenhadas pela entidade integrante reportada que não estejam especificadas dentre as opções disponíveis nos campos anteriores. onforme previsto na Instrução Normativa RFB nº 1.681/2016, artigo 9, § 3º, todas as informações em texto livre da Declaração País-a-País deverão ser fornecidas em um único idioma, a ser escolhido pela entidade declarante dentre as opções de português, inglês e espanhol.   C
Ver pagina 401""")
    observacao = fields.Char("Outras Informações",
        help="""Outras Informações: Campo de utilização opcional, para o fornecimento de informações
Ver pagina 401""")
    parent_u182_id = fields.Many2one('l10n.br.sped.ecf.u182',
                                     string="Cálculo da CSLL das Empresas Imunes ou Isentas")

class RegistroW300(models.Model):
    _name = 'l10n.br.sped.ecf.w300'
    _description = u"""Observações Adicionais"""
    _inherit = 'l10n.br.sped.mixin'
    jurisdicao = fields.Char("JURISDICAO",
        help="""Indicação da jurisdição tributária a que se referem as observações adicionais. Código do país, conforme tabela do Sped (Disponibilizada no programa da ECF no
Ver pagina 404""")
    ind_rec_nao_rel = fields.Char("O campo 'Receitas Provenientes de Partes Não Relacionadas' (W200",
        help="""O campo "Receitas Provenientes de Partes Não Relacionadas" (W200.VL_REC_NAO_REL) é tratado nestas observações adicionais? S - Sim N - Não
Ver pagina 404""")
    ind_rec_rel = fields.Char("O campo 'Receitas Provenientes de Partes Relacionadas' (W200",
        help="""O campo "Receitas Provenientes de Partes Relacionadas" (W200.VL_REC_REL) é tratado nestas observações adicionais? S - Sim N - Não
Ver pagina 404""")
    ind_rec_total = fields.Char("O campo 'Receita Total' (W200",
        help="""O campo "Receita Total" (W200.VL_REC_TOTAL) é tratado nestas observações adicionais? S - Sim N - Não
Ver pagina 405""")
    ind_luc_prej_antes_ir = fields.Char("O campo 'Lucro ou Prejuízo antes do IR' (W200",
        help="""O campo "Lucro ou Prejuízo antes do IR" (W200.VL_LUC_PREJ_ANTES_IR) é tratado nestas observações adicionais? S - Sim N - Não
Ver pagina 405""")
    ind_ir_pago = fields.Char("O campo 'Imposto de Renda Pago' (W200",
        help="""O campo "Imposto de Renda Pago" (W200.VL_IR_PAGO) é tratado nestas observações adicionais? S - Sim N - Não
Ver pagina 405""")
    ind_ir_devido = fields.Char("O campo 'Imposto de Renda Devido' (W200",
        help="""O campo "Imposto de Renda Devido" (W200.VL_IR_DEVIDO) é tratado nestas observações adicionais? S - Sim N - Não
Ver pagina 405""")
    ind_cap_soc = fields.Char("O campo 'Capital Social' (W200",
        help="""O campo "Capital Social" (W200.VL_CAP_SOC) é tratado nestas observações adicionais? S - Sim N - Não
Ver pagina 405""")
    ind_luc_acum = fields.Char("O campo 'Lucros Acumulados' (W200",
        help="""O campo "Lucros Acumulados" (W200.VL_LUC_ACUM) é tratado nestas observações adicionais? S - Sim N - Não
Ver pagina 405""")
    ind_ativ_tang = fields.Char("O campo 'Ativos Tangíveis' (W200",
        help="""O campo "Ativos Tangíveis" (W200.VL_ATIV_TANG) é tratado nestas observações adicionais? S - Sim N - Não
Ver pagina 405""")
    ind_num_emp = fields.Char("O campo 'Número de Empregados' (W200",
        help="""O campo "Número de Empregados" (W200.NUM_EMP) é tratado nestas observações adicionais? S - Sim N - Não
Ver pagina 405""")
    observacao = fields.Char("Observações.", required=True,
        help="""Observações.
Ver pagina 405""")
    fim_observacao = fields.Char("Indicador de fim das observações",
        help="""Indicador de fim das observações. Texto fixo contendo “W300FIM”.
Ver pagina 405""")

class RegistroX280(models.Model):
    _name = 'l10n.br.sped.ecf.x280'
    _description = u"""Atividades Incentivadas - PJ em Geral"""
    _inherit = 'l10n.br.sped.mixin'
    ind_ativ = fields.Char("Benefício fiscal", required=True,
        help="""Benefício fiscal: 00 – Não preenchido  01 – Isenção  02 – Redução de 100%  03 – Redução de 75%  04 – Redução de 70%  05 – Redução de 50%  06 – Redução de 33,33%  07 – Redução de 25% 08 – Redução de 12,5% 09 – Redução por Reinvestimento Selecionar no campo Benefício Fiscal o tipo de benefício (isenção ou redução do IRPJ) em relação a cada projeto aprovado no órgão competente, conforme lista disponível na Caixa de Combinação. E, para cada projeto aprovado selecionar no campo Projeto se o mesmo corresponde a "Novo Empreendimento", "Modernização", "Ampliação",
Ver pagina 410""")
    ind_proj = fields.Char("IND_PROJ", required=True,
        help="""Projeto: 00 – Não preenchido  01 – Novo Empreendimento  02 – Modernização  03 – Ampliação  04 – Diversificação  05 – Manutenção do Empreendimento 06 – Prouni  07 - Padis 08 – Eventos Fifa 09 – Serviços da Fifa (SPE) 10 – Eventos CIO 11 – Serviços do CIO (SPE) 99 – Outros
Ver pagina 416""")
    ato_conc = fields.Char("Ato Concessório - Natureza e Número", required=True,
        help="""Ato Concessório - Natureza e Número: Informar neste campo o número do ato concessório do benefício fiscal. Atenção: No caso de projeto nas áreas de atuação da Sudam e da Sudene, informar neste campo o número do ato da unidade da RFB editado para reconhecimento do direito ao benefício fiscal.
Ver pagina 416""")
    vig_ini = fields.Date("VIG_INI", required=True)
    vig_fim = fields.Date("VIG_FIM", required=True)

class RegistroX291(models.Model):
    _name = 'l10n.br.sped.ecf.x291'
    _description = u"""Operações com o Exterior - Pessoa Vinculada/Interposta/País com Tributação Favorecida"""
    _inherit = 'l10n.br.sped.mixin'
    codigo = fields.Char("CODIGO", required=True,
        help="""Código, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro e
Ver pagina 420""")
    descricao = fields.Char("DESCRICAO",
        help="""Descrição, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro
Ver pagina 420""")
    valor = fields.Monetary("Valor", digits=2)

class RegistroX292(models.Model):
    _name = 'l10n.br.sped.ecf.x292'
    _description = u"""Operações  com  o  Exterior  -  Pessoa  Não  Vinculada/ Não Interposta/País sem Tributação Favorecida"""
    _inherit = 'l10n.br.sped.mixin'
    codigo = fields.Char("CODIGO", required=True,
        help="""Código, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro e
Ver pagina 422""")
    descricao = fields.Char("DESCRICAO",
        help="""Descrição, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro
Ver pagina 422""")
    valor = fields.Monetary("Valor", digits=2)

class RegistroX300(models.Model):
    _name = 'l10n.br.sped.ecf.x300'
    _description = u"""Operações com o Exterior - Exportações (Entradas de Divisas)"""
    _inherit = 'l10n.br.sped.mixin'
    num_ordem = fields.Char("Número de Ordem das Operações", required=True,
        help="""Número de Ordem das Operações
Ver pagina 426""")
    tip_exp = fields.Integer("Tipo das Exportações", required=True)
    desc_exp = fields.Char("Descrição das Exportações",
        help="""Descrição das Exportações: Agrupar os bens, serviços ou direitos idênticos, descrevendo cada grupo de modo a permitir a sua perfeita identificação, informando elementos, tais como: marca, tipo, modelo, espécie, etc. Obrigatório somente quando TIP_EXP = Bens, Serviços ou Direitos
Ver pagina 426""")
    tot_oper = fields.Monetary("Total das Operações", digits=2)
    cod_ncm = fields.Integer("COD_NCM")
    qtde = fields.Monetary("QTDE", digits=2)
    uni_med = fields.Char("Unidade de Medida",
        help="""Unidade de Medida: Obrigatório somente quando TIP_EXP = Bens Conforme tabela de unidades de medida do Sped. A pessoa jurídica deve selecionar dentre as opções aquela que corresponde à unidade de medida comercial dos bens exportados, tais como: dúzia, grama, litro, metro etc.
Ver pagina 427""")
    ind_oper = fields.Char("IND_OPER",
        help="""Indicador de Operação Sujeita a Arbitramento S - Sim N - Não Obrigatório somente quando TIP_EXP = Bens, Serviços ou Direitos O campo deve ser assinalado, caso o preço médio de venda do bem, serviço ou direito das exportações efetuadas durante o respectivo período de apuração da base de cálculo do imposto de renda, for inferior a noventa por cento do preço médio praticado na venda do mesmo bem, serviço ou direito no mercado brasileiro, durante o mesmo período, em condições de pagamento semelhantes Atenção: Caso a pessoa jurídica não efetue operações de venda no mercado interno, a determinação dos preços médios é efetuada com dados de outras empresas que pratiquem a venda de bens, serviços ou direitos, idênticos ou similares, no mercado interno (§ 2º, art. 20 da Instrução Normativa RFB nº 1.312, de 28 de dezembro de 2012).
Ver pagina 428""")
    tip_met = fields.Char("TIP_MET",
        help="""Método: PVE - Preço de Venda nas Exportações  PGE - Preço de Venda por Atacado menos Lucro  PVV - Preço de Venda a Varejo menos Lucro  CAP - Custo de Aquisição/Produção mais Tributos e Lucro PECEX - Preço sob Cotação na Exportação A pessoa jurídica deve assinalar o método utilizado na determinação do "Preço
Ver pagina 428""")
    vl_par = fields.Monetary("VL_PAR", digits=2)
    vl_prat = fields.Monetary("VL_PRAT", digits=2)
    vl_aj = fields.Monetary("VL_AJ", digits=2)
    vl_jur = fields.Monetary("VL_JUR", digits=2)
    vl_jur_min = fields.Monetary("Taxa de Juros Mínima", digits=4)
    vl_jur_max = fields.Monetary("Taxa de Juros Máxima", digits=4)
    cod_cnc = fields.Integer("COD_CNC")
    tip_moeda = fields.Char("TIP_MOEDA",
        help="""Moeda , conforme tabela do Sped (Disponibilizada no programa da ECF no diretório
Ver pagina 430""")
    reg_x310_ids = fields.One2many('l10n.br.sped.ecf.x310','parent_x300_id',
                               string="Operações com o Exterior -  Contratantes das Exportações",
                               help='Bloco X')

class RegistroX310(models.Model):
    _name = 'l10n.br.sped.ecf.x310'
    _description = u"""Operações com o Exterior -  Contratantes das Exportações"""
    _inherit = 'l10n.br.sped.mixin'
    nome = fields.Char("NOME", required=True,
        help="""Nome: Nome ou razão social da pessoa física ou jurídica contratante da transação, que seja domiciliada no exterior.
Ver pagina 435""")
    pais = fields.Char("PAIS", required=True,
        help="""País: País onde a pessoa física ou jurídica contratante, no exterior, é domiciliada. Código do país, conforme tabela do Sped (Disponibilizada no programa da ECF no
Ver pagina 435""")
    vl_oper = fields.Monetary("Valor da Operação", required=True, digits=2)
    cond_pes = fields.Integer("Condição da Pessoa Envolvida na Operação", required=True)
    parent_x300_id = fields.Many2one('l10n.br.sped.ecf.x300',
                                     string="Operações com o Exterior - Exportações (Entradas de Divisas)")

class RegistroX320(models.Model):
    _name = 'l10n.br.sped.ecf.x320'
    _description = u"""Operações  com  o  Exterior  -  Importações  (Saídas  de Divisas)"""
    _inherit = 'l10n.br.sped.mixin'
    num_ord = fields.Char("Número de Ordem: Número de ordem para identificar a operação", required=True,
        help="""Número de Ordem: Número de ordem para identificar a operação
Ver pagina 439""")
    tip_imp = fields.Integer("Tipo das Importações", required=True)
    desc_imp = fields.Char("DESC_IMP",
        help="""Descrição: Agrupar os bens, serviços ou direitos idênticos, descrevendo cada grupo de modo a permitir a sua perfeita identificação, informando elementos, tais como: marca, tipo, modelo, espécie, etc. Obrigatório somente quando TIP_EXP = Bens, Serviços ou Direitos
Ver pagina 439""")
    tot_oper = fields.Monetary("Total da Operação", digits=2)
    cod_ncm = fields.Integer("COD_NCM")
    qtde = fields.Monetary("QTDE", digits=2)
    uni_med = fields.Char("Unidade de Medida",
        help="""Unidade de Medida: Obrigatório somente quando TIP_EXP = Bens 01 – Bilhão de Unidade Internacional 02 – Dúzia 03 – Grama 04 – Litro 05 – Megawatt Hora 06 – Metro 07 – Metro Cúbico 08 – Metro Quadrado 09 – Mil Unidades 10 – Pares 11 – Quilate 12 – Quilograma Bruto 13 – Quilograma Líquido 14 – Tonelada Métrica Líquida 15 – Unidade 16 – Outras  Selecionar dentre as opções aquela que corresponde à unidade de medida comercial dos bens importados, tais como: dúzia, grama, litro, metro etc.
Ver pagina 441""")
    tip_met = fields.Char("TIP_MET",
        help="""Método: PIC00 – Preços Independentes Comparados PRL20 - Preço de Revenda Menos Lucro 20% PRL30 - Preço de Revenda Menos Lucro 30% PRL40 - Preço de Revenda Menos Lucro 40% CPL00 – Custo de Produção Mais Lucro PCI00 – Preço sob Cotação na Importação Assinalar o método utilizado na determinação do "Preço Parâmetro", a saber:  PIC Método dos Preços Independentes Comparados (inciso I do art. 18 da Lei nº 9.430, de 1996 e IN RFB nº 1.312, de 28 de dezembro de 2012, arts. 8 a 11);  PRL 20% Método do Preço de Revenda menos Lucro (Inciso III do § 12 do art. 18 da Lei nº 9.430, de 1996, e IN RFB nº 1.312, de 28 de dezembro de 2012, art. 12, § 10)  PRL 30% Método do Preço de Revenda menos Lucro Revenda (Inciso II do § 12 do art. 18 da Lei nº 9.430, de 1996 e IN RFB nº 1.312, de 28 de dezembro de 2012, art. 12, § 10); PRL 40% Método do Preço de Revenda menos Lucro Revenda (Inciso I do § 12 do art. 18 da Lei nº 9.430, de 1996 e IN RFB nº 1.312, de 28 de dezembro de 2012, art. 12, § 10); CPL Método do Custo de Produção mais Lucro (inciso III do art. 18 da Lei nº 9.430, de 1996, e IN RFB nº 1.312, de 28 de dezembro de 2012, art. 15).  PCI Preço sob Cotação na Importação (art. 18-A da Lei nº 9.430, de 1996, e art. 16 da IN RFB nº 1.312, de 2012, alterado pelo art. 1º da IN RFB nº 1.395, de 2013). Atenção: O método do Preço de Revenda menos Lucro mediante a utilização da margem
Ver pagina 442""")
    vl_par = fields.Monetary("VL_PAR", digits=2)
    vl_prat = fields.Monetary("VL_PRAT", digits=2)
    vl_aj = fields.Monetary("VL_AJ", required=True, digits=2)
    vl_jur = fields.Monetary("VL_JUR", digits=2)
    vl_jur_min = fields.Monetary("Taxa de Juros Mínima", digits=4)
    vl_jur_max = fields.Monetary("Taxa de Juros Máxima", digits=4)
    cod_cnc = fields.Char("COD_CNC",
        help="""Código CNC: Código da natureza-fato específico correspondente à motivação do recebimento/pagamento, conforme § 1o do artigo 23 da Lei no 4.131, de 03 de setembro de 1962, e que consta na Circular no 3.690, de 16 de dezembro de 2013, do Banco Central do Brasil. Atenção: No caso dos recursos não terem sido enviados ao exterior, o enquadramento se faz, consoante apuração contábil, como se remetidos fossem. Tendo ocorrido a efetiva remessa, esses valores são de igual modo classificados, independentemente do instrumento de formalização cambial utilizado no Banco Central do Brasil: contrato de câmbio e/ou transferência internacional em moeda nacional.  Obrigatório apenas para TIP_EXP = Operações Financeiras Observação: O registro X320 não possui informação de data em seus campos. Portanto, os códigos utilizados no campo X320.COD_CNC devem ser os vigentes na data final da
Ver pagina 445""")
    tip_moeda = fields.Char("TIP_MOEDA",
        help="""Moeda: Pessoa jurídica deve selecionar dentre as opções a moeda de negociação. Obrigatório apenas para TIP_EXP=Operações Financeiras
Ver pagina 445""")
    reg_x330_ids = fields.One2many('l10n.br.sped.ecf.x330','parent_x320_id',
                               string="Operações com o Exterior -  Contratantes das Importações",
                               help='Bloco X')

class RegistroX330(models.Model):
    _name = 'l10n.br.sped.ecf.x330'
    _description = u"""Operações com o Exterior -  Contratantes das Importações"""
    _inherit = 'l10n.br.sped.mixin'
    nome = fields.Char("NOME", required=True,
        help="""Nome: Nome ou razão social da pessoa física ou jurídica contratante da transação, que seja domiciliada no exterior.
Ver pagina 448""")
    pais = fields.Char("PAIS", required=True,
        help="""País: País onde a pessoa física ou jurídica contratante, no exterior, é domiciliada. Código do país, conforme tabela do Sped (Disponibilizada no programa da ECF no
Ver pagina 448""")
    vl_oper = fields.Monetary("Valor da Operação", required=True, digits=2)
    cond_pes = fields.Integer("Condição da Pessoa Envolvida na Operação", required=True)
    parent_x320_id = fields.Many2one('l10n.br.sped.ecf.x320',
                                     string="Operações  com  o  Exterior  -  Importações  (Saídas  de Divisas)")

class RegistroX340(models.Model):
    _name = 'l10n.br.sped.ecf.x340'
    _description = u"""Identificação da Participação no Exterior"""
    _inherit = 'l10n.br.sped.mixin'
    raz_social = fields.Char("RAZ_SOCIAL", required=True,
        help="""Razão Social: Razão social de cada controlada, direta ou indireta, equiparada ou coligada em regime de competência.
Ver pagina 450""")
    nif = fields.Char("NIF", required=True,
        help="""NIF: Número de identificação fiscal de cada investida (“CNPJ” da investida no exterior). Observação:  1 – Caso a investida não possua NIF, utilize “0000” 2 – Para investidas de um mesmo país difernte do Braisl que não possuam NIF, utilizar
Ver pagina 451""")
    ind_controle = fields.Integer("IND_CONTROLE", required=True)
    pais = fields.Integer("PAIS", required=True)
    ind_isen_petr = fields.Char("Indicador de Prospecção e Exploração de Petróleo e Gás", required=True,
        help="""Indicador de Prospecção e Exploração de Petróleo e Gás: Informar parcela de lucro decorrente de afretamento por tempo ou casco nu, arrendamento mercantil operacional, aluguel, empréstimo de bens ou prestação de serviços diretamente relacionados à prospecção e exploração de petróleo e gás, em território brasileiro, que goze de isenção nos termos do art. 77, §3º, da Lei nº 12.973 de 13 de maio de 2014: S = Sim N = Não
Ver pagina 451""")
    ind_consol = fields.Char("Indicador de Consolidação", required=True,
        help="""Indicador de Consolidação: Informar se a investida terá os resultados positivos e negativos consolidados: S = Sim N = Não
Ver pagina 451""")
    mot_nao_consol = fields.Integer("Motivo da Não Consolidação")
    cnpj = fields.Integer("CNPJ da Investida no Brasil")
    tip_moeda = fields.Char("Moeda do País de Domicílio.",
        help="""Moeda do País de Domicílio.
Ver pagina 452""")
    reg_x350_ids = fields.One2many('l10n.br.sped.ecf.x350','parent_x340_id',
                               string="Participações  no  Exterior  -  Resultado  do  Período  de Apuração",
                               help='Bloco X')
    reg_x351_ids = fields.One2many('l10n.br.sped.ecf.x351','parent_x340_id',
                               string="Demonstrativo de Resultados e de Imposto a Pagar no Exterior",
                               help='Bloco X')
    reg_x352_ids = fields.One2many('l10n.br.sped.ecf.x352','parent_x340_id',
                               string="Demonstrativo  de  Resultados  no  Exterior  Auferidos por Intermédio de Coligadas em Regime de Caixa",
                               help='Bloco X')
    reg_x353_ids = fields.One2many('l10n.br.sped.ecf.x353','parent_x340_id',
                               string="Demonstrativo de Consolidação",
                               help='Bloco X')
    reg_x354_ids = fields.One2many('l10n.br.sped.ecf.x354','parent_x340_id',
                               string="Demonstrativo de Prejuízos Acumulados",
                               help='Bloco X')
    reg_x355_ids = fields.One2many('l10n.br.sped.ecf.x355','parent_x340_id',
                               string="Demonstrativo de Rendas Ativas e Passivas",
                               help='Bloco X')
    reg_x356_ids = fields.One2many('l10n.br.sped.ecf.x356','parent_x340_id',
                               string="Demonstrativo de Estrutura Societária",
                               help='Bloco X')

class RegistroX350(models.Model):
    _name = 'l10n.br.sped.ecf.x350'
    _description = u"""Participações  no  Exterior  -  Resultado  do  Período  de Apuração"""
    _inherit = 'l10n.br.sped.mixin'
    rec_liq = fields.Monetary("REC_LIQ", digits=2)
    custos = fields.Monetary("Custos dos Bens e Serviços Vendidos", digits=2)
    luc_bruto = fields.Monetary("Lucro Bruto: Deve ser igual a (X350", digits=2)
    rec_auferidas = fields.Monetary("Receitas Financeiras Auferidas com a Vinculada no Brasil", digits=2)
    rec_outras_oper = fields.Monetary("Outras Receitas Operacionais", digits=2)
    desp_brasil = fields.Monetary("Despesas Financeiras Pagas ou Creditadas à Vinculada no Brasil", digits=2)
    desp_oper = fields.Monetary("Despesa Operacionais", digits=2)
    luc_oper = fields.Monetary("Lucro Operacional", digits=2)
    rec_partic = fields.Monetary("REC_PARTIC", digits=2)
    rec_outras = fields.Monetary("REC_OUTRAS", digits=2)
    desp_outras = fields.Monetary("DESP_OUTRAS", digits=2)
    luc_liq_ant_ir = fields.Monetary("Lucro Líquido Antes do Imposto de Renda", digits=2)
    imp_dev = fields.Monetary("IMP_DEV", digits=2)
    luc_liq = fields.Monetary("Lucro líquido do Período de Apuração", digits=2)
    parent_x340_id = fields.Many2one('l10n.br.sped.ecf.x340',
                                     string="Identificação da Participação no Exterior")

class RegistroX351(models.Model):
    _name = 'l10n.br.sped.ecf.x351'
    _description = u"""Demonstrativo de Resultados e de Imposto a Pagar no Exterior"""
    _inherit = 'l10n.br.sped.mixin'
    res_inv_per = fields.Monetary("RES_INV_PER", digits=2)
    res_inv_per_real = fields.Monetary("Resultado (positivo ou negativo) da Própria Investida em Reais", digits=2)
    res_isen_petr_per = fields.Monetary("RES_ISEN_PETR_PER", digits=2)
    res_isen_petr_per_real = fields.Monetary("RES_ISEN_PETR_PER_REAL", digits=2)
    res_neg_acum = fields.Monetary("Resultado Negativo Acumulado de Anos Anteriores", digits=2)
    res_pos_trib = fields.Monetary("Resultado Positivo a Tributar", digits=2)
    res_pos_trib_real = fields.Monetary("Resultado Positivo a Tributar em Reais (R$)", digits=2)
    imp_lucr = fields.Monetary("Imposto Efetivamente Pago", digits=2)
    imp_lucr_real = fields.Monetary("Imposto Efetivamente Pago em Reais (R$)", digits=2)
    imp_pag_rend = fields.Monetary("IMP_PAG_REND", digits=2)
    imp_pag_rend_real = fields.Monetary("IMP_PAG_REND_REAL", digits=2)
    imp_ret_ext = fields.Monetary("Imposto Retido na Fonte no Exterior", digits=2)
    imp_ret_ext_real = fields.Monetary("Imposto Retido na Fonte no Exterior em Reais", digits=2)
    imp_ret_br = fields.Monetary("Imposto Retido na Fonte no Brasil", digits=2)
    parent_x340_id = fields.Many2one('l10n.br.sped.ecf.x340',
                                     string="Identificação da Participação no Exterior")

class RegistroX352(models.Model):
    _name = 'l10n.br.sped.ecf.x352'
    _description = u"""Demonstrativo  de  Resultados  no  Exterior  Auferidos por Intermédio de Coligadas em Regime de Caixa"""
    _inherit = 'l10n.br.sped.mixin'
    res_per = fields.Monetary("RES_PER", digits=2)
    res_per_real = fields.Monetary("Resultado (positivo ou negativo) do Período em Reais", digits=2)
    luc_disp = fields.Monetary("Lucro Disponibilizado no Período na Moeda do País de Domicílio", digits=2)
    luc_disp_real = fields.Monetary("Lucro Disponibilizado no Período em Reais", digits=2)
    parent_x340_id = fields.Many2one('l10n.br.sped.ecf.x340',
                                     string="Identificação da Participação no Exterior")

class RegistroX353(models.Model):
    _name = 'l10n.br.sped.ecf.x353'
    _description = u"""Demonstrativo de Consolidação"""
    _inherit = 'l10n.br.sped.mixin'
    res_neg_util = fields.Monetary("Resultado Negativo Utilizado na Consolidação na Moeda do País de", digits=2)
    res_neg_util_real = fields.Monetary("Resultado Negativo Utilizado na Consolidação em Reais", digits=2)
    saldo_res_neg_nao_util = fields.Monetary("Saldo do Resultado Negativo Não Utilizado na Moeda do País de", digits=2)
    parent_x340_id = fields.Many2one('l10n.br.sped.ecf.x340',
                                     string="Identificação da Participação no Exterior")

class RegistroX354(models.Model):
    _name = 'l10n.br.sped.ecf.x354'
    _description = u"""Demonstrativo de Prejuízos Acumulados"""
    _inherit = 'l10n.br.sped.mixin'
    res_neg = fields.Monetary("RES_NEG", digits=2)
    res_neg_real = fields.Monetary("RES_NEG_REAL", digits=2)
    saldo_res_neg = fields.Monetary("SALDO_RES_NEG", digits=2)
    parent_x340_id = fields.Many2one('l10n.br.sped.ecf.x340',
                                     string="Identificação da Participação no Exterior")

class RegistroX355(models.Model):
    _name = 'l10n.br.sped.ecf.x355'
    _description = u"""Demonstrativo de Rendas Ativas e Passivas"""
    _inherit = 'l10n.br.sped.mixin'
    rend_pass_prop = fields.Monetary("REND_PASS_PROP", digits=2)
    parent_x340_id = fields.Many2one('l10n.br.sped.ecf.x340',
                                     string="Identificação da Participação no Exterior")

class RegistroX356(models.Model):
    _name = 'l10n.br.sped.ecf.x356'
    _description = u"""Demonstrativo de Estrutura Societária"""
    _inherit = 'l10n.br.sped.mixin'
    perc_part = fields.Monetary("Percentual de Participação da Investidora Direta (%)", digits=4)
    ativo_total = fields.Monetary("Ativo Total em Reais", digits=2)
    pat_liquido = fields.Monetary("Patrimônio Líquido em Reais", digits=2)
    parent_x340_id = fields.Many2one('l10n.br.sped.ecf.x340',
                                     string="Identificação da Participação no Exterior")

class RegistroX390(models.Model):
    _name = 'l10n.br.sped.ecf.x390'
    _description = u"""Origem e Aplicação de Recursos - Imunes ou Isentas"""
    _inherit = 'l10n.br.sped.mixin'
    codigo = fields.Char("CODIGO", required=True,
        help="""Código, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro e
Ver pagina 466""")
    descricao = fields.Char("DESCRICAO",
        help="""Descrição, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro
Ver pagina 466""")
    valor = fields.Monetary("Valor", digits=2)

class RegistroX400(models.Model):
    _name = 'l10n.br.sped.ecf.x400'
    _description = u"""Comércio  Eletrônico  e  Tecnologia  da  Informação  – Informações das Vendas"""
    _inherit = 'l10n.br.sped.mixin'
    codigo = fields.Char("CODIGO", required=True,
        help="""Código, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro e
Ver pagina 468""")
    descricao = fields.Char("DESCRICAO",
        help="""Descrição, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro
Ver pagina 469""")
    valor = fields.Monetary("Valor", digits=2)

class RegistroX410(models.Model):
    _name = 'l10n.br.sped.ecf.x410'
    _description = u"""Comércio Eletrônico – Informação de Homepage/Servidor"""
    _inherit = 'l10n.br.sped.mixin'
    pais = fields.Integer("PAIS", required=True)
    ind_home_disp = fields.Char("Indicador de Homepage Disponível", required=True,
        help="""Indicador de Homepage Disponível: S – Sim N – Não A pessoa jurídica deverá marcar “Sim” ou “Não”, para cada país selecionado, onde tenha o domínio de sua homepage registrado, caso disponibilize, ou não, efetivamente sua homepage. A disponibilização efetiva da homepage se dá por meio do conhecer ao público de seu conteúdo. Atenção: Deve assinalar “Não” neste campo, a pessoa jurídica que tenha efetuado somente o registro de sua homepage num determinado país e não tenha construído ou disponibilizado efetivamente essa homepage para o público.
Ver pagina 471""")
    ind_serv_disp = fields.Char("Indicador de Disponibilidade de Servidor", required=True,
        help="""Indicador de Disponibilidade de Servidor: S – Sim N – Não A pessoa jurídica que, por meio de sua homepage, aceite pedidos de compra, receba pagamentos, preste serviços ou efetue a entrega de bens digitais por meio de download deve selecionar “Sim” neste campo, para cada país selecionado, para informar o país onde mantém os servidores que estão à sua disposição. Para que um servidor seja considerado à sua disposição basta que ele seja o meio pelo qual a pessoa jurídica atue no comércio eletrônico. Esses servidores podem pertencer à pessoa jurídica, como podem ser alugados, arrendados ou cedidos a título gratuito ou oneroso.
Ver pagina 472""")

class RegistroX420(models.Model):
    _name = 'l10n.br.sped.ecf.x420'
    _description = u"""Royalties  Recebidos  ou  Pagos  a  Beneficiários  do Brasil e do Exterior"""
    _inherit = 'l10n.br.sped.mixin'
    tip_roy = fields.Char("TIP_ROY", required=True,
        help="""Indicar se são roylaties recebidos ou pagos a benfeciários no Brasil e no exterior. Tipo dos royalties: R - Recebido P – Pago
Ver pagina 473""")
    pais = fields.Integer("PAIS", required=True)
    vl_expl_dir_sw = fields.Monetary("VL_EXPL_DIR_SW", digits=2)
    vl_expl_dir_aut = fields.Monetary("VL_EXPL_DIR_AUT", digits=2)
    vl_expl_marca = fields.Monetary("VL_EXPL_MARCA", digits=2)
    vl_expl_pat = fields.Monetary("VL_EXPL_PAT", digits=2)
    vl_expl_know = fields.Monetary("Valor da Exploração de Know-How", digits=2)
    vl_expl_franq = fields.Monetary("Valor da Exploração de Franquias", digits=2)
    vl_expl_int = fields.Monetary("VL_EXPL_INT", digits=2)

class RegistroX430(models.Model):
    _name = 'l10n.br.sped.ecf.x430'
    _description = u"""Rendimentos Relativos a Serviços, Juros e Dividendos Recebidos do Brasil e do Exterior"""
    _inherit = 'l10n.br.sped.mixin'
    pais = fields.Integer("PAIS", required=True)
    vl_serv_assist = fields.Integer("VL_SERV_ASSIST")
    vl_serv_sem_assist = fields.Monetary("constituírem transferência de tecnologia, tais como", digits=2)
    vl_serv_sem_assist_ext = fields.Monetary("constituírem transferência de tecnologia, tais como", digits=2)
    vl_juro = fields.Monetary("Valor dos Juros sobre o Capital Próprio", digits=2)
    vl_demais_juros = fields.Monetary("Valor dos Demais Juros", digits=2)
    vl_divid = fields.Monetary("Valor dos Dividendos", digits=2)

class RegistroX450(models.Model):
    _name = 'l10n.br.sped.ecf.x450'
    _description = u"""Pagamentos ou Remessas Relativos a Serviços, Juros e Dividendos a Beneficiários do Brasil e do Exterior"""
    _inherit = 'l10n.br.sped.mixin'
    pais = fields.Integer("PAIS", required=True)
    vl_serv_assist = fields.Monetary("VL_SERV_ASSIST", digits=2)
    vl_serv_sem_assist = fields.Monetary("constituírem transferência de tecnologia, tais como", digits=2)
    vl_serv_sem_assist_ext = fields.Monetary("constituírem transferência de tecnologia, tais como", digits=2)
    vl_juro_pf = fields.Monetary("Valor dos Juros sobre o Capital Próprio Pagos a Pessoa Física", digits=2)
    vl_juro_pj = fields.Monetary("Valor dos Juros sobre o Capital Próprio Pagos a Pessoa Jurídica", digits=2)
    vl_demais_juros = fields.Monetary("Valor dos Demais Juros", digits=2)
    vl_divid_pf = fields.Monetary("Dividendos Pagos a Pessoa Física", digits=2)
    vl_divid_pj = fields.Monetary("Dividendos Pagos a Pessoa Jurídica", digits=2)

class RegistroX460(models.Model):
    _name = 'l10n.br.sped.ecf.x460'
    _description = u"""Inovação Tecnológica e Desenvolvimento Tecnológico"""
    _inherit = 'l10n.br.sped.mixin'
    codigo = fields.Char("CODIGO", required=True,
        help="""Código, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro e no programa da ECF no diretório Arquivos de Programas/Programas Sped/ECf/SpedEcf/Recursos/Tabelas).
Ver pagina 494""")
    descricao = fields.Char("DESCRICAO",
        help="""Descrição, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro
Ver pagina 494""")
    valor = fields.Monetary("Valor", digits=2)

class RegistroX470(models.Model):
    _name = 'l10n.br.sped.ecf.x470'
    _description = u"""Capacitação de Informática e Inclusão Digital"""
    _inherit = 'l10n.br.sped.mixin'
    codigo = fields.Char("CODIGO", required=True,
        help="""Código, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro e
Ver pagina 496""")
    descricao = fields.Char("DESCRICAO",
        help="""Descrição, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro
Ver pagina 496""")
    valor = fields.Monetary("Valor", digits=2)

class RegistroX480(models.Model):
    _name = 'l10n.br.sped.ecf.x480'
    _description = u"""Repes,  Recap, Padis, PATVD,  Reidi,  Repenec, Reicomp, Retaero, Recine, Resíduos Sólidos, Recopa, Copa  do  Mundo,  Retid,  REPNBL-Redes,  Reif  e Olimpíadas"""
    _inherit = 'l10n.br.sped.mixin'
    codigo = fields.Char("CODIGO", required=True,
        help="""Código, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro e
Ver pagina 499""")
    descricao = fields.Char("DESCRICAO",
        help="""Descrição, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro
Ver pagina 499""")
    valor = fields.Monetary("Valor", digits=2)

class RegistroX490(models.Model):
    _name = 'l10n.br.sped.ecf.x490'
    _description = u"""Pólo Industrial de Manaus e Amazônia Ocidental"""
    _inherit = 'l10n.br.sped.mixin'
    codigo = fields.Char("CODIGO", required=True,
        help="""Código, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro e
Ver pagina 501""")
    descricao = fields.Char("DESCRICAO",
        help="""Descrição, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro
Ver pagina 501""")
    valor = fields.Monetary("Valor", digits=2)

class RegistroX500(models.Model):
    _name = 'l10n.br.sped.ecf.x500'
    _description = u"""Zonas de Processamento de Exportação (ZPE)"""
    _inherit = 'l10n.br.sped.mixin'
    codigo = fields.Char("CODIGO", required=True,
        help="""Código, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro e
Ver pagina 503""")
    descricao = fields.Char("DESCRICAO",
        help="""Descrição, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro
Ver pagina 503""")
    valor = fields.Monetary("Valor", digits=2)

class RegistroX510(models.Model):
    _name = 'l10n.br.sped.ecf.x510'
    _description = u"""Áreas de Livre Comércio (ALC)"""
    _inherit = 'l10n.br.sped.mixin'
    codigo = fields.Char("CODIGO", required=True,
        help="""Código, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro e
Ver pagina 505""")
    descricao = fields.Char("DESCRICAO",
        help="""Descrição, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro
Ver pagina 505""")
    valor = fields.Monetary("Valor", digits=2)

class RegistroY520(models.Model):
    _name = 'l10n.br.sped.ecf.y520'
    _description = u"""Pagamentos/Recebimentos  do  Exterior  ou  de  Não Residentes"""
    _inherit = 'l10n.br.sped.mixin'
    tip_ext = fields.Char("Tipo: R - Rendimentos Recebidos P – Pagamentos", required=True,
        help="""Tipo: R - Rendimentos Recebidos P – Pagamentos
Ver pagina 509""")
    pais = fields.Integer("PAIS", required=True)
    forma = fields.Integer("Forma de Recebimento/Pagamento", required=True)
    nat_oper = fields.Integer("Natureza da Operação", required=True)
    vl_periodo = fields.Monetary("VL_PERIODO", required=True, digits=2)

class RegistroY540(models.Model):
    _name = 'l10n.br.sped.ecf.y540'
    _description = u"""Discriminação da Receita de Vendas dos Estabelecimentos por Atividade Econômica"""
    _inherit = 'l10n.br.sped.mixin'
    cnpj_estab = fields.Char("CNPJ_ESTAB", required=True,
        help="""CNPJ da matriz e de cada um dos estabelecimentos da pessoa jurídica (os 8 primeiros dígitos devem ser idênticos ao campo 0000.CNPJ).
Ver pagina 512""")
    vl_rec_estab = fields.Monetary("Receita de Vendas", required=True, digits=2)
    cnae = fields.Integer("CNAE", required=True)

class RegistroY550(models.Model):
    _name = 'l10n.br.sped.ecf.y550'
    _description = u"""Vendas a Comercial Exportadora com Fim Específico de Exportação"""
    _inherit = 'l10n.br.sped.mixin'
    cnpj_exp = fields.Char("CNPJ: CNPJ da Comercial Exportadora adquirente", required=True,
        help="""CNPJ: CNPJ da Comercial Exportadora adquirente.
Ver pagina 514""")
    cod_ncm = fields.Integer("Código NCM (Nomenclatura Comum do Mercosul)", required=True)
    vl_venda = fields.Monetary("Valor da Venda: Valor da mercadoria vendida", required=True, digits=2)

class RegistroY560(models.Model):
    _name = 'l10n.br.sped.ecf.y560'
    _description = u"""Detalhamento das Exportações da Comercial Exportadora"""
    _inherit = 'l10n.br.sped.mixin'
    cnpj = fields.Char("CNPJ: CNPJ da empresa produtora ou vendedora", required=True,
        help="""CNPJ: CNPJ da empresa produtora ou vendedora.  Observação: Em caso de aquisição de produtor rural sem CNPJ, quando o contribuinte é obrigado a emitir nota fiscal de entrada referente à aquisição das mercadorias, utilizar o CNPJ da declarante.
Ver pagina 515""")
    cod_ncm = fields.Integer("Código NCM (Nomenclatura Comum do Mercosul)", required=True)
    vl_compra = fields.Monetary("Valor da Compra: Valor de aquisição do produto", digits=2)
    vl_exp = fields.Monetary("Valor da Exportação", digits=2)

class RegistroY570(models.Model):
    _name = 'l10n.br.sped.ecf.y570'
    _description = u"""Demonstrativo do Imposto de Renda e CSLL Retidos na Fonte"""
    _inherit = 'l10n.br.sped.mixin'
    cnpj_fon = fields.Char("CNPJ: CNPJ da fonte pagadora", required=True,
        help="""CNPJ: CNPJ da fonte pagadora
Ver pagina 517""")
    nom_emp = fields.Char("Nome Empresarial", required=True,
        help="""Nome Empresarial: Nome da pessoa jurídica responsável pela retenção e recolhimento da fonte que estiver sendo compensado.
Ver pagina 517""")
    ind_org_pub = fields.Char("Indicador de Órgão Público", required=True,
        help="""Indicador de Órgão Público: S - Sim N – Não Selecione “Sim” ou “Não” em relação à pessoa jurídica responsável pela retenção e recolhimento da fonte que estiver sendo compensado. Ao selecionar "Sim" serão disponibilizados os códigos de recolhimento utilizados pelos Órgãos Públicos Federais ou Entidades da Administração Pública Federal, ao selecionar "Não", serão disponibilizados
Ver pagina 517""")
    cod_rec = fields.Integer("COD_REC", required=True)
    vl_rend = fields.Monetary("Rendimento Bruto", required=True, digits=2)
    ir_ret = fields.Monetary("IR Retido na Fonte", digits=2)
    csll_ret = fields.Monetary("CSLL Retida na Fonte", digits=2)

class RegistroY580(models.Model):
    _name = 'l10n.br.sped.ecf.y580'
    _description = u"""Doações a Campanhas Eleitorais"""
    _inherit = 'l10n.br.sped.mixin'
    cnpj = fields.Char("CNPJ do Beneficiário", required=True,
        help="""CNPJ do Beneficiário: Número de inscrição no Cadastro Nacional da Pessoa Jurídica (CNPJ) do partido político, do comitê financeiro de partido político ou do candidato a cargo eletivo beneficiário da doação.
Ver pagina 521""")
    tip_benef = fields.Integer("Tipo de Beneficiário da Doação", required=True)
    form_doa = fields.Integer("FORM_DOA", required=True)
    vl_doa = fields.Monetary("Valor: Valor da doação efetuada", required=True, digits=2)

class RegistroY590(models.Model):
    _name = 'l10n.br.sped.ecf.y590'
    _description = u"""Ativos no Exterior"""
    _inherit = 'l10n.br.sped.mixin'
    tip_ativo = fields.Char("TIP_ATIVO", required=True,
        help="""Tipo do Ativo que Possui no Exterior, conforme tabela do Sped (Disponibilizada no
Ver pagina 523""")
    pais = fields.Integer("PAIS", required=True)
    discriminacao = fields.Char("DISCRIMINACAO", required=True,
        help="""Discriminação: Detalhar, neste campo, as informações correspondentes aos ativos, tais como: tipo, localização, data de aquisição e de venda, de quem foi adquirido, a quem foi alienado, instituição que intermediou a operação, valor de aquisição e/ou de venda em moeda estrangeira, instituição financeira e agência, tratando-se de aplicação financeira ou depósito e, na hipótese de participações societárias, espécie de participação e empresa investida.
Ver pagina 523""")
    vl_ant = fields.Monetary("VL_ANT", required=True, digits=2)
    vl_atual = fields.Monetary("Valor Atual: Valor contábil do ativo no final do período atual", required=True, digits=2)

class RegistroY600(models.Model):
    _name = 'l10n.br.sped.ecf.y600'
    _description = u"""Identificação  e  Remuneração  de  Sócios,  Titulares, Dirigentes e Conselheiro"""
    _inherit = 'l10n.br.sped.mixin'
    dt_alt_soc = fields.Integer("Data da Alteração no Quadro Societário", required=True)
    dt_fim_soc = fields.Integer("Data da Saída do Quadro Societário")
    pais = fields.Integer("País de Residência ou Domicílio da Pessoa Física ou Jurídica", required=True)
    ind_qualif = fields.Char("IND_QUALIF", required=True,
        help="""Indicador de Qualificação do Sócio, Titular, Dirigente ou Conselheiro: PF - Pessoa Física PJ - Pessoa Jurídica FI – Fundo de Investimento
Ver pagina 526""")
    cpf_cnpj = fields.Integer("CPF ou CNPJ do Sócio, Titular, Dirigente ou Conselheiro")
    nom_emp = fields.Char("NOM_EMP", required=True,
        help="""Nome/Nome empresarial do Sócio, Titular, Dirigente ou Conselheiro.
Ver pagina 526""")
    qualif = fields.Char("Qualificação do Sócio, Titular, Dirigente ou Conselheiro", required=True,
        help="""Qualificação do Sócio, Titular, Dirigente ou Conselheiro. Se PAIS = “105” (Brasil) E IND_QUALIF_SOCIO = “PF”:  01 – Acionista Pessoa Física Domiciliado no Brasil  02 – Sócio Pessoa Física Domiciliado no Brasil  09 – Titular  10 – Administrador sem Vínculo Empregatício 11 – Diretor sem Vínculo Empregatício 12 – Presidente sem Vínculo Empregatício 13 – Administrador com Vínculo Empregatício 14 – Conselheiro de Administração ou Fiscal 15 – Diretor com Vínculo Empregatício 16 – Fundador 17 – Presidente com Vínculo Empregatício 03 - Acionista Pessoa Jurídica Domiciliado no Brasil  04 - Sócio Pessoa Jurídica Domiciliado no Brasil  e PAIS diferente de “105” (Brasil) E IND_QUALIF_SOCIO = "PF": 05 - Acionista Pessoa Física Residente ou Domiciliado no Exterior  06 - Sócio Pessoa Física Residente ou Domiciliado no Exterior  14 – Conselheiro de Administração ou Fiscal e PAIS diferente de “105” (Brasil) E IND_QUALIF_SOCIO = "PJ": 07 - Acionista Pessoa Jurídica Residente ou Domiciliado no Exterior    S  S  S
Ver pagina 527""")
    perc_cap_tot = fields.Monetary("PERC_CAP_TOT", required=True, digits=4)
    perc_cap_vot = fields.Monetary("PERC_CAP_VOT", required=True, digits=4)
    cpf_rep_leg = fields.Integer("CPF do Representante Legal")
    qualif_rep_leg = fields.Integer("Qualificação do Representante Legal")
    vl_rem_trab = fields.Monetary("Remuneração do Trabalho", digits=2)
    vl_luc_div = fields.Monetary("Lucros/Dividendos", digits=2)
    vl_jur_cap = fields.Monetary("Juros Sobre o Capital Próprio", digits=2)
    vl_dem_rend = fields.Monetary("Demais Rendimentos", digits=2)
    vl_ir_ret = fields.Monetary("IR Retido na Fonte", digits=2)

class RegistroY612(models.Model):
    _name = 'l10n.br.sped.ecf.y612'
    _description = u"""Identificação e Rendimentos de Dirigentes e Conselheiros - Imunes ou Isentas"""
    _inherit = 'l10n.br.sped.mixin'
    cpf = fields.Integer("CPF", required=True)
    nome = fields.Char("NOME", required=True,
        help="""Nome: Nome do dirigente ou conselheiro beneficiário dos rendimentos.
Ver pagina 531""")
    qualif = fields.Integer("QUALIF", required=True)
    vl_rem_trab = fields.Monetary("Rendimentos do Trabalho", digits=2)
    vl_dem_rend = fields.Monetary("Demais Rendimentos", digits=2)
    vl_ir_ret = fields.Monetary("IR Retido na Fonte", digits=2)

class RegistroY620(models.Model):
    _name = 'l10n.br.sped.ecf.y620'
    _description = u"""Participações Avaliadas pelo Método de Equivalência Patrimonial"""
    _inherit = 'l10n.br.sped.mixin'
    dt_evento = fields.Integer("DT_EVENTO", required=True)
    ind_relac = fields.Integer("Indicador do Tipo de Relacionamento", required=True)
    pais = fields.Integer("País: País onde a coligada ou controlada está domiciliada", required=True)
    cnpj = fields.Char("CNPJ: CNPJ da coligada ou controlada",
        help="""CNPJ: CNPJ da coligada ou controlada. Obrigatório se PAIS = 105 (Brasil) Caso contrário, o campo deve ser nulo
Ver pagina 534""")
    nom_emp = fields.Char("Nome Empresarial", required=True,
        help="""Nome Empresarial: Nome empresarial da coligada ou controlada.
Ver pagina 534""")
    valor_reais = fields.Monetary("Valor Total da Participação em Reais (Cotação da data do evento)", required=True, digits=2)
    valor_estr = fields.Monetary("VALOR_ESTR", required=True, digits=2)
    perc_cap_tot = fields.Monetary("PERC_CAP_TOT", required=True, digits=4)
    perc_cap_vot = fields.Monetary("PERC_CAP_VOT", required=True, digits=4)
    res_eq_pat = fields.Monetary("Resultado de Equivalência Patrimonial", digits=2)
    data_aquis = fields.Char("Data da Primeira Aquisição da Participação Societária Observação", required=True,
        help="""Data da Primeira Aquisição da Participação Societária Observação: Poderá ser igual a Y600.DT_EVENTO se a primeira aquisição foi causa do MEP.
Ver pagina 534""")
    ind_proc_cart = fields.Char("Sumário em Cartório", required=True,
        help="""Sumário em Cartório: Informar se houve sumário registrado em cartório relativo ao Laudo de Avaliação do Valor Justo dos Ativos Líquidos da Investida (Mais-valia ou menos-valia) de acordo com o art. 178 da Instrução Normativa RFB nº 1.700, de 14 de março de 2017: S – Sim N = Não
Ver pagina 534""")
    num_proc_cart = fields.Char("Número do Registro no Cartório",
        help="""Número do Registro no Cartório: Informar o número do registro em cartório do sumário relativo ao Laudo de Avaliação do Valor Justo dos Ativos Líquidos da Investida (Mais-valia ou menos-valia) de acordo com o art. 178 da Instrução Normativa RFB nº 1.700, de 14 de março de 2017.
Ver pagina 534""")
    nome_cart = fields.Char("Nome do Cartório",
        help="""Nome do Cartório: Informar o nome e endereço do cartório onde foi registrado o sumário relativo ao Laudo de Avaliação do Valor Justo dos Ativos Líquidos da Investida (Mais-valia ou menos-valia) de acordo com o art. 178 da Instrução Normativa RFB nº 1.700, de 14 de março de 2017.
Ver pagina 535""")
    ind_proc_rfb = fields.Char("Laudo Protocolado na RFB", required=True,
        help="""Laudo Protocolado na RFB: Informar se houve Laudo de Avaliação do Valor Justo dos Ativos Líquidos da Investida (Mais-valia ou menos-valia) de acordo com o art. 178 da Instrução Normativa RFB nº 1.700, de 14 de março de 2017, protocolado na RFB: S – Sim N = Não Observação: Deverá ser informado também para os casos de aquisição ou venda ocorridos antes do período a que se refere essa ECF.
Ver pagina 535""")
    num_proc_rfb = fields.Char("Número do Processo",
        help="""Número do Processo: Informar o número do processo eletrônico do Laudo de Avaliação do Valor Justo dos Ativos Líquidos da Investida protocolado na RFB (Mais-valia ou menos-valia) de acordo com o art. 178 da Instrução Normativa RFB nº 1.700, de 14 de março de 2017.
Ver pagina 535""")

class RegistroY630(models.Model):
    _name = 'l10n.br.sped.ecf.y630'
    _description = u"""Fundos/Clubes de Investimento"""
    _inherit = 'l10n.br.sped.mixin'
    cnpj = fields.Char("CNPJ", required=True,
        help="""CNPJ: As administradoras de Fundos ou Clubes de Investimento devem informar, neste campo, o CNPJ de cada Fundo ou Clube de Investimento.Os fundos de investimento imobiliário de que trata a Lei no 8.668, de 1993, alterada pelos arts. 2o a 4o e 22 da Lei no 9.779, de 1999, devem informar o próprio CNPJ.
Ver pagina 537""")
    qte_quot = fields.Integer("Quantidade de Quotistas no Final do Período", required=True)
    qte_quota = fields.Integer("Quantidade de Quotas no Final do Período", required=True)
    patr_fin_per = fields.Monetary("Patrimônio no Final do Período", required=True, digits=2)
    dat_abert = fields.Integer("Data de Abertura", required=True)
    dat_encer = fields.Integer("Data de Encerramento")

class RegistroY640(models.Model):
    _name = 'l10n.br.sped.ecf.y640'
    _description = u"""Participações em Consórcios de Empresas"""
    _inherit = 'l10n.br.sped.mixin'
    cnpj = fields.Char("CNPJ", required=True,
        help="""CNPJ: CNPJ do consórcio no qual a pessoa jurídica participou no período a que se refere esta declaração.
Ver pagina 539""")
    cond_decl = fields.Integer("Condição do Declarante no Consórcio", required=True)
    vl_cons = fields.Monetary("Receita do Consórcio", digits=2)
    cnpj_lid = fields.Char("CNPJ da Empresa Líder do Consórcio.", required=True,
        help="""CNPJ da Empresa Líder do Consórcio.
Ver pagina 539""")
    vl_decl = fields.Monetary("Receita do Declarante no Consórcio", required=True, digits=2)

class RegistroY650(models.Model):
    _name = 'l10n.br.sped.ecf.y650'
    _description = u"""Participantes do Consórcio"""
    _inherit = 'l10n.br.sped.mixin'
    cnpj = fields.Char("CNPJ da Empresa Participante do Consórcio", required=True,
        help="""CNPJ da Empresa Participante do Consórcio.
Ver pagina 541""")
    vl_part = fields.Monetary("Receita do Participante do Consórcio.", digits=2)

class RegistroY660(models.Model):
    _name = 'l10n.br.sped.ecf.y660'
    _description = u"""Dados de Sucessoras"""
    _inherit = 'l10n.br.sped.mixin'
    cnpj = fields.Char("CNPJ da Pessoa Jurídica Resultante do Evento", required=True,
        help="""CNPJ da Pessoa Jurídica Resultante do Evento.
Ver pagina 542""")
    nom_emp = fields.Char("Nome Empresarial da Pessoa Jurídica Resultante do Evento", required=True,
        help="""Nome Empresarial da Pessoa Jurídica Resultante do Evento.
Ver pagina 542""")
    perc_pat_liq = fields.Monetary("Percentual do Patrimônio Líquido Destinado", digits=4)

class RegistroY671(models.Model):
    _name = 'l10n.br.sped.ecf.y671'
    _description = u"""Outras Informações"""
    _inherit = 'l10n.br.sped.mixin'
    vl_aq_maq = fields.Monetary("VL_AQ_MAQ", digits=2)
    vl_doa_crianca = fields.Monetary("Doação aos Fundos dos Direitos da Criança e do Adolescente", digits=2)
    vl_doa_idoso = fields.Monetary("Doação aos Fundos Nacional, Estaduais ou Municipais do Idoso", digits=2)
    vl_aq_imobilizado = fields.Monetary("Aquisições para o Ativo Imobilizado", digits=2)
    vl_bx_imobilizado = fields.Monetary("Baixas do Ativo Imobilizado", digits=2)
    vl_inc_ini = fields.Monetary("Bens Sujeitos ao Incentivo de que Trata a Lei no 11", digits=2)
    vl_inc_fin = fields.Monetary("Bens Sujeitos ao Incentivo de que Trata a Lei no 11", digits=2)
    vl_csll_deprec_ini = fields.Monetary("Saldo de Créditos de CSLL sobre Depreciação no Início do Período", digits=2)
    vl_oc_sem_iof = fields.Monetary("Valor das Operações de Câmbio com Isenção de IOF", digits=2)
    vl_folha_aliq_red = fields.Monetary("VL_FOLHA_ALIQ_RED", digits=2)
    vl_aliq_red = fields.Monetary("Alíquota Reduzida de que Trata a Lei no 11", digits=4)
    ind_alter_capital = fields.Integer("Alteração de Capital na Forma dos art")
    ind_bcn_csll = fields.Integer("IND_BCN_CSLL")

class RegistroY672(models.Model):
    _name = 'l10n.br.sped.ecf.y672'
    _description = u"""Outras Informações (Lucro  Presumido ou  Lucro Arbitrado)"""
    _inherit = 'l10n.br.sped.mixin'
    vl_capital_ant = fields.Monetary("Capital Registrado do Ano Anterior", digits=2)
    vl_capital = fields.Monetary("Capital Registrado", digits=2)
    vl_estoque_ant = fields.Monetary("Estoques do Ano Anterior", digits=2)
    vl_estoques = fields.Monetary("Estoques: Valor dos estoques no fim do “Ano da Escrituração”", digits=2)
    vl_caixa_ant = fields.Monetary("Saldo de Caixa e Bancos do Ano Anterior", digits=2)
    vl_caixa = fields.Monetary("Saldo de Caixa e Bancos", digits=2)
    vl_aplic_fin_ant = fields.Monetary("Saldo de Aplicações Financeiras do Ano Anterior", digits=2)
    vl_aplic_fin = fields.Monetary("Saldo de Aplicações Financeiras", digits=2)
    vl_cta_rec_ant = fields.Monetary("Contas a Receber do Ano Anterior", digits=2)
    vl_cta_rec = fields.Monetary("Contas a Receber", digits=2)
    vl_cta_pag_ant = fields.Monetary("Contas a Pagar do Ano Anterior", digits=2)
    vl_cta_pag = fields.Monetary("VL_CTA_PAG", digits=2)
    vl_compra_merc = fields.Monetary("Compras de Mercadorias no Ano-Calendário", digits=2)
    vl_compra_ativo = fields.Monetary("VL_COMPRA_ATIVO", digits=2)
    vl_receitas = fields.Monetary("VL_RECEITAS", digits=2)
    tot_ativo = fields.Monetary("TOT_ATIVO", digits=2)
    vl_folha = fields.Monetary("VL_FOLHA", digits=2)
    vl_aliq_red = fields.Monetary("Alíquota Reduzida de que Trata a Lei no 11", digits=4)
    ind_aval_estoq = fields.Char("Método de Avaliação de Estoques",
        help="""Método de Avaliação de Estoques: 1 – Custo Médio Ponderado  2 – PEPS (Primeiro que entra, primeiro que sai) 3 – Arbitramento - art. 296, Inc. I e II, do RIR/99 4 – Custo Específico 5 – Valor Realizável Líquido 6 – Inventário Periódico 7 – Outros 8 – Não há (Exemplo: Empresas Prestadoras de Serviços)
Ver pagina 550""")

class RegistroY680(models.Model):
    _name = 'l10n.br.sped.ecf.y680'
    _description = u"""Mês  das  Informações  de  Optantes  pelo  Refis  (Lucro Real, Presumido e Arbitrado)"""
    _inherit = 'l10n.br.sped.mixin'
    mes = fields.Char("MES", required=True,
        help="""Mês: 01 – Janeiro 02 – Fevereiro 03 – Março 04 – Abril 05 – Maio 06 – Junho 07 – Julho 08 – Agosto 09 – Setembro 10 – Outubro 11 – Novembro 12 – Dezembro
Ver pagina 553""")
    reg_y681_ids = fields.One2many('l10n.br.sped.ecf.y681','parent_y680_id',
                               string="Informações  de  Optantes  pelo  Refis (Lucro  Real, Presumido e Arbitrado)",
                               help='Bloco Y')

class RegistroY681(models.Model):
    _name = 'l10n.br.sped.ecf.y681'
    _description = u"""Informações  de  Optantes  pelo  Refis (Lucro  Real, Presumido e Arbitrado)"""
    _inherit = 'l10n.br.sped.mixin'
    codigo = fields.Char("CODIGO", required=True,
        help="""Código, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro e
Ver pagina 554""")
    descricao = fields.Char("DESCRICAO",
        help="""Descrição, conforme tabela dinâmica do Sped (Disponibilizada no item III deste registro
Ver pagina 554""")
    valor = fields.Monetary("Valor", digits=2)
    parent_y680_id = fields.Many2one('l10n.br.sped.ecf.y680',
                                     string="Mês  das  Informações  de  Optantes  pelo  Refis  (Lucro Real, Presumido e Arbitrado)")

class RegistroY682(models.Model):
    _name = 'l10n.br.sped.ecf.y682'
    _description = u"""Informações  de  Optantes  pelo  Refis - Imunes  ou Isentas"""
    _inherit = 'l10n.br.sped.mixin'
    mes = fields.Char("MES", required=True,
        help="""Mês: 01 – Janeiro 02 – Fevereiro 03 – Março 04 – Abril 05 – Maio 06 – Junho 07 – Julho 08 – Agosto 09 – Setembro 10 – Outubro 11 – Novembro 12 – Dezembro
Ver pagina 556""")
    acres_patr = fields.Monetary("Acréscimo Patrimonial no Mês.", required=True, digits=2)

class RegistroY690(models.Model):
    _name = 'l10n.br.sped.ecf.y690'
    _description = u"""Informações de Optantes pelo Paes"""
    _inherit = 'l10n.br.sped.mixin'
    mes = fields.Char("MES", required=True,
        help="""Mês: 01 – Janeiro 02 – Fevereiro 03 – Março 04 – Abril 05 – Maio 06 – Junho 07 – Julho 08 – Agosto 09 – Setembro 10 – Outubro 11 – Novembro 12 – Dezembro
Ver pagina 558""")
    vl_rec_bru = fields.Monetary("Receita bruta no mês", required=True, digits=2)

class RegistroY720(models.Model):
    _name = 'l10n.br.sped.ecf.y720'
    _description = u"""Informações de Períodos Anteriores"""
    _inherit = 'l10n.br.sped.mixin'
    luc_liq = fields.Monetary("LUC_LIQ", required=True, digits=2)
    dt_luc_liq = fields.Integer("DT_LUC_LIQ", required=True)
    rec_brut_ant = fields.Monetary("Receita bruta do período anterior.", required=True, digits=2)

class RegistroY800(models.Model):
    _name = 'l10n.br.sped.ecf.y800'
    _description = u"""Outras Informações"""
    _inherit = 'l10n.br.sped.mixin'
    tipo_doc = fields.Integer("Tipo do Documento", required=True)
    descricao = fields.Char("Descrição do Conteúdo do Documento.", required=True,
        help="""Descrição do Conteúdo do Documento.
Ver pagina 563""")
    hash = fields.Char("Hash do arquivo incluído na escrituração", required=True,
        help="""Hash do arquivo incluído na escrituração. Este campo não deve ser informado no arquivo de importação pois será calculado pelo sistema.
Ver pagina 563""")
    arq_rtf = fields.Char("Sequência de Bytes", required=True,
        help="""Sequência de Bytes: Sequência de bytes que representem um único arquivo no formato RTF (Rich Text Format).
Ver pagina 563""")
    ind_fim_rtf = fields.Char("Indicador de Fim do Arquivo RTF", required=True,
        help="""Indicador de Fim do Arquivo RTF. Texto fixo contendo “Y800FIM”.
Ver pagina 563""")

class Registro9100(models.Model):
    _name = 'l10n.br.sped.ecf.9100'
    _description = u"""Avisos da Escrituração"""
    _inherit = 'l10n.br.sped.mixin'
    nom_regra = fields.Integer("Identificação da regra.", required=True)
    msg_regra = fields.Char("Mensagem: Mensagem associada ao aviso.",
        help="""Mensagem: Mensagem associada ao aviso.
Ver pagina 566""")
    registro = fields.Char("Registro: Registro onde ocorreu o aviso", required=True,
        help="""Registro: Registro onde ocorreu o aviso.
Ver pagina 566""")
    campo = fields.Char("Campo: Nome do campo no registro onde ocorreu",
        help="""Campo: Nome do campo no registro onde ocorreu.
Ver pagina 566""")
    valor_esperado = fields.Monetary("Valor Original ou Calculado", digits=2)
    conteudo = fields.Monetary("Conteúdo: Conteúdo do campo – Valor preenchido pelo usuário", digits=2)

class Registro9900(models.Model):
    _name = 'l10n.br.sped.ecf.9900'
    _description = u"""Registros do Arquivo"""
    _inherit = 'l10n.br.sped.mixin'
    reg_blc = fields.Char("Registro: Registro que será totalizado em 9900", required=True,
        help="""Registro: Registro que será totalizado em 9900.QTD_REG_BLC.
Ver pagina 567""")
    qtd_reg_blc = fields.Integer("Total de Registros por Tipo", required=True)
    versao = fields.Char("Versão: Versão da tabela dinâmica utilizada",
        help="""Versão: Versão da tabela dinâmica utilizada. Será preenchido somente para registros
Ver pagina 567""")
    id_tab_din = fields.Char("Identificação da Tabela Dinâmica Utilizada",
        help="""Identificação da Tabela Dinâmica Utilizada.
Ver pagina 567""")

class Registro9999(models.Model):
    _name = 'l10n.br.sped.ecf.9999'
    _description = u"""Encerramento do Arquivo Digital"""
    _inherit = 'l10n.br.sped.mixin'
    qtd_lin = fields.Integer("Quantidade total de registros do arquivo", required=True)
