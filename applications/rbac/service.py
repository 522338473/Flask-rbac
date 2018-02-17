from flask import request, session


def init_permission(user_obj):
    tmp_dict = {"id": user_obj.id,
                "username": user_obj.username}
    session["userinfo"] = tmp_dict

    permissions_dict = {}
    for role in user_obj.roles:
        for perm in role.permissions:
            if perm.id not in permissions_dict:
                permissions_dict[perm.id] = {
                    "url_title": perm.title,
                    "url": perm.url,
                    "code": perm.code,
                    "menu_ref": perm.menu_ref,
                    "group_id": perm.group_id,
                    "menu_id": perm.perm_group.menu_id,
                    "menu_title": perm.perm_group.menu.title,
                }

    # 权限匹配相关信息，Auth插件中用到
    # 以权限组为单位打包权限信息，获取codes_list，用于判断页面是否显示添加、编辑、删除等标签
    perm_info_dict = {}
    for perm_id, perm_dict in permissions_dict.items():
        group_id = perm_dict.get('group_id')
        if group_id not in perm_info_dict:
            perm_info_dict[group_id] = {
                'urls_info': [{'url_title': perm_dict.get('url_title'),
                               'url': perm_dict.get('url')}],
                'codes': [perm_dict.get('code')]
            }
        else:
            perm_info_dict[group_id]['urls_info'].append({'url_title': perm_dict.get('url_title'),
                                                          'url': perm_dict.get('url')})
            perm_info_dict[group_id]['codes'].append(perm_dict.get('code'))

    session["PERM_INFO_DICT"] = perm_info_dict
    # print(perm_info_dict)
    # perm_info_dict = {1: {'urls_info': [{'url_title': '编辑用户', 'url': '/userinfo/edit/(\\d+)/'},
    #                                     {'url_title': '添加用户', 'url': '/userinfo/add/'},
    #                                     {'url_title': '删除用户', 'url': '/userinfo/del/(\\d+)/'},
    #                                     {'url_title': '用户列表', 'url': '/userinfo/'}],
    #                       'codes': ['edit', 'add', 'del', 'list']},
    #                   2: {
    #                       'urls_info': [{'url_title': '订单列表', 'url': '/order/'},
    #                                     {'url_title': '添加订单', 'url': '/order/add/'},
    #                                     {'url_title': '编辑订单', 'url': '/order/edit/(\\d+)/'},
    #                                     {'url_title': '删除订单', 'url': '/order/del/(\\d+)/'}],
    #                       'codes': ['list', 'add', 'edit', 'del']}}

    # 菜单展示相关信息
    # data_list中取一部分数据，用于生成侧边栏菜单
    perm_side_list = []
    for perm_id, perm_dict in permissions_dict.items():
        tmp_dict = {
            'id': perm_id,
            'url_title': perm_dict.get('url_title'),
            'url': perm_dict.get('url'),
            'menu_ref': perm_dict.get('menu_ref'),
            'menu_id': perm_dict.get('menu_id'),
            'menu_title': perm_dict.get('menu_title')
        }
        perm_side_list.append(tmp_dict)

    session["PERM_SIDE_LIST"] = perm_side_list
    # print(perm_side_list)
    # perm_side_list = [{'id': 3, 'url_title': '编辑用户', 'url': '/userinfo/edit/(\\d+)/', 'menu_ref': 1, 'menu_id': 1,
    #                    'menu_title': '菜单一'},
    #                   {'id': 2, 'url_title': '添加用户', 'url': '/userinfo/add/', 'menu_ref': 1, 'menu_id': 1,
    #                    'menu_title': '菜单一'},
    #                   {'id': 4, 'url_title': '删除用户', 'url': '/userinfo/del/(\\d+)/', 'menu_ref': 1, 'menu_id': 1,
    #                    'menu_title': '菜单一'},
    #                   {'id': 5, 'url_title': '订单列表', 'url': '/order/', 'menu_ref': None, 'menu_id': 2,
    #                    'menu_title': '菜单二'},
    #                   {'id': 6, 'url_title': '添加订单', 'url': '/order/add/', 'menu_ref': 5, 'menu_id': 2,
    #                    'menu_title': '菜单二'},
    #                   {'id': 7, 'url_title': '编辑订单', 'url': '/order/edit/(\\d+)/', 'menu_ref': 5, 'menu_id': 2,
    #                    'menu_title': '菜单二'},
    #                   {'id': 1, 'url_title': '用户列表', 'url': '/userinfo/', 'menu_ref': None, 'menu_id': 1,
    #                    'menu_title': '菜单一'},
    #                   {'id': 8, 'url_title': '删除订单', 'url': '/order/del/(\\d+)/', 'menu_ref': 5, 'menu_id': 2,
    #                    'menu_title': '菜单二'}]
