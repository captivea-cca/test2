# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ClientPricing(models.Model):
    _name = "client_pricing.pricing"
    _inherit = "project.task"

    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        stage_ids = self.env['stage.stage'].search([])
        return stage_ids
