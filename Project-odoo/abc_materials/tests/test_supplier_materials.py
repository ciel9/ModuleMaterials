import unittest
from odoo.tests.common import SavepointCase

class TestSupplierMaterials(SavepointCase):
    @classmethod
    def setUpClass(cls):
        super(TestSupplierMaterials, cls).setUpClass()

    def test_materials_views(self):
        materials_model = self.env['materials.supplier.models']

        # Test form view
        materials_form = self.env.ref('abc_materials.view_form_materials')
        form_view = materials_form.read()[0]
        self.assertEqual(form_view['name'], 'materials.form.view')
        self.assertEqual(form_view['model'], 'materials.supplier.models')
        self.assertIn('name_material', form_view['arch'])
        self.assertIn('code', form_view['arch'])
        self.assertIn('supplier', form_view['arch'])
        self.assertIn('price', form_view['arch'])
        self.assertIn('type', form_view['arch'])

        # Tes tampilan tree
        materials_tree = self.env.ref('abc_materials.view_materials_tree')
        tree_view = materials_tree.read()[0]
        self.assertEqual(tree_view['name'], 'materials.tree')
        self.assertEqual(tree_view['model'], 'materials.supplier.models')
        self.assertIn('name_material', tree_view['arch'])
        self.assertIn('code', tree_view['arch'])
        self.assertIn('supplier', tree_view['arch'])
        self.assertIn('price', tree_view['arch'])
        self.assertIn('type', tree_view['arch'])

        # Test kanban view
        materials_kanban = self.env.ref('abc_materials.materials_kanban')
        kanban_view = materials_kanban.read()[0]
        self.assertEqual(kanban_view['name'], 'materials.supplier.kanban')
        self.assertEqual(kanban_view['model'], 'materials.supplier.models')
        self.assertIn('name_material', kanban_view['arch'])
        self.assertIn('code', kanban_view['arch'])
        self.assertIn('supplier', kanban_view['arch'])
        self.assertIn('price', kanban_view['arch'])
        self.assertIn('type', kanban_view['arch'])

    def test_materials_model(self):
        materials_model = self.env['materials.supplier.models']

        # Tes constraints price_validation
        # Test when price < 100
        with self.assertRaises(Exception):
            materials_model.create({
                'name_material': 'Test Material',
                'code': 'TEST001',
                'supplier': 1,
                'price': 50,
                'type': '0'
            })

        # Test when price = 100
        material = materials_model.create({
            'name_material': 'Test Material',
            'code': 'TEST001',
            'supplier': 1,
            'price': 100,
            'type': '0'
        })
        self.assertTrue(material)

if __name__ == '__main__':
    unittest.main()
