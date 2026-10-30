# -*- coding: utf-8 -*-
{
    'name': 'FSM Equipment Custom Fields',
    'version': '17.0.1.0.0',
    'summary': 'Thêm các trường tùy chỉnh cho thiết bị Field Service',
    'description': """
        Module này thêm các trường tùy chỉnh vào model fsm.equipment:
        - Dự án (x_project)
        - Số lượng (x_quantity)
        - Hãng sản xuất (x_manufacturer)
    """,
    'category': 'Field Service',
    'author': 'Custom',
    'depends': ['fieldservice', 'project', 'fieldservice_equipment_warranty','fieldservice_agreement'],
    'data': [
        'views/fsm_warranty_views.xml',
        'views/fsm_equipment_custom_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}