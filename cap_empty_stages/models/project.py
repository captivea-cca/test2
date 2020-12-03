# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Task(models.Model):
    _inherit = "project.task"

    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        return stages.ids
