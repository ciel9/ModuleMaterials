from odoo import models, fields, api, exceptions

class MaterialsObject(models.Model):
    _name = 'materials.supplier.models'
    _description = 'Materials Supplier Model'
    _rec_name = 'name_material'

    name_material = fields.Char(required=True, string="Material Name")
    code = fields.Char(required=True, string="Material Code")
    price = fields.Integer(required=True, string="Material Buy Price")
    type = fields.Selection([
        ('0', 'Fabric'),
        ('1', 'Jeans'),
        ('2', 'Cotton')], default='0', required=True, string="Material Type")
    supplier = fields.Many2one('models.supplier', string='Related Supplier', required=True,
                               default=lambda self: self._default_supplier())

    def _default_supplier(self):
        # Ganti return value berikut dengan ID supplier default yang Anda inginkan
        default_supplier_id = 1
        return self.env['models.supplier'].browse(default_supplier_id)

    @api.constrains('price')
    def price_validation(self):
        for record in self:
            if record.price < 100:
                raise exceptions.ValidationError("Price must be greater than or equal to 100.")

class SupplierObject(models.Model):
    _name = 'models.supplier'
    supplier = fields.Char(required=True, string="Supplier Name")

    def name_get(self):
        result = []
        for record in self:
            name = record.supplier or ''
            result.append((record.id, name))
        return result
