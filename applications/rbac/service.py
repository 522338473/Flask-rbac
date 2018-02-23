from flask import session, current_app


def init_permission(user_obj):
    session[current_app.config['USER_INFO']] = {"id": user_obj.id, "username": user_obj.username}

    permissions_dict = {}
    for role in user_obj.roles:
        for perm in role.permissions:
            perm_id = perm.id
            if perm_id not in permissions_dict:
                permissions_dict[perm_id] = {
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

    session[current_app.config['PERM_INFO_DICT']] = perm_info_dict

    # 菜单展示相关信息
    # 从data_list中取一部分数据，用于生成侧边栏菜单
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

    session[current_app.config['PERM_SIDE_LIST']] = perm_side_list
