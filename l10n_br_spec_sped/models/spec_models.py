from lxml.builder import E

from odoo import api, fields, models


class SpedMixin(models.AbstractModel):
    _name = "l10n.br.sped.mixin"

    # TODO copy from KMEE ./l10n_br_base/models/sped_base.py, check
    currency_id = fields.Many2one(
        comodel_name="res.currency",
        string="Moeda",
        compute="_compute_currency_id",
        default=lambda self: self.env.ref("base.BRL").id,
    )

    def _compute_currency_id(self):
        for item in self:
            item.currency_id = self.env.ref("base.BRL").id

    #            item.currency_aliquota_id = self.env.ref(
    #                'l10n_br_base.SIMBOLO_ALIQUOTA').id
    #            item.currency_aliquota_rateio_id = self.env.ref(
    #                'l10n_br_base.SIMBOLO_ALIQUOTA_RATEIO').id
    #            item.currency_unitario_id = self.env.ref(
    #                'l10n_br_base.SIMBOLO_VALOR_UNITARIO').id
    #            item.currency_peso_id = self.env.ref(
    #                'l10n_br_base.SIMBOLO_PESO').id

    @api.model
    def _get_default_tree_view(self):
        """ Generates a single-field tree view, based on _rec_name.

        :returns: a tree view as an lxml document
        :rtype: etree._Element
        """
        desc = self._description
        # (patch for Python 2)
        #        if type(desc) == str:
        #            desc = desc.decode('utf-8')
        tree = E.tree(string=desc)
        c = 0
        required_fields_num = len([f[1] for f in self._fields.items() if f[1].required])
        for fname, field in self._fields.items():
            if field.automatic or fname == "currency_id":
                continue
            if len(self._fields) > 7 and required_fields_num > 2 and not field.required:
                continue
            else:
                tree.append(E.field(name=fname))
            if c > 12:
                break
            c += 1
        return tree

    @api.model
    def _get_default_form_view(self):
        """ Generates a default single-line form view using all fields
        Overriden to skip XSD fields that will be added later
        """
        group = E.group()
        for fname, field in self._fields.items():
            if field.automatic:
                continue
            if fname.startswith("parent_registro") and fname.endswith("_id"):
                # FIXME TODO make robust: this is to skip related m2o fields
                continue
            if fname == "currency_id":
                continue
            elif field.type in ("one2many", "many2many", "text", "html"):
                group.append(E.newline())
                group.append(E.field(name=fname, colspan="4"))
                group.append(E.newline())
            else:
                group.append(E.field(name=fname))
        group.append(E.separator())
        return E.form(E.sheet(group, string=self._description))
