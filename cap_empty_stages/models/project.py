# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Task(models.Model):
    _inherit = "project.task"

    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        search_domain = [('id', 'in', stages.ids)]
        stage_ids = stages._search(search_domain, order=order, access_rights_uid=SUPERUSER_ID)
        return stages.browse(stage_ids)
