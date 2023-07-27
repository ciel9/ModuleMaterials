from odoo import http
from odoo.http import request

class SupplierController(http.Controller):
    @http.route('/supplier_list', auth='public', website=True)
    def supplier_list(self, **kw):
        suppliers = request.env['models.supplier'].sudo().search([])
        return http.request.render('supplier_materials.supplier_list_template', {'suppliers': suppliers})
