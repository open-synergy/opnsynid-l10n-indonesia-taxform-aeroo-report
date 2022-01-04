# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models


class Parser(models.AbstractModel):
    _inherit = "report.report_aeroo.abstract"
    _name = "l10n_id.report_faktur_pajak_keluaran_export"
