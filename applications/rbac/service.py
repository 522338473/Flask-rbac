from flask import request, session


def init_permission(user_obj):
    tmp_dict = {"id": user_obj.id,
                "username": user_obj.username}
    session["userinfo"] = tmp_dict

    # data_list = user_obj.roles.values('permissions__id', 'permissions__title', 'permissions__url',
    #                                   'permissions__code',
    #                                   'permissions__menu_ref_id', 'permissions__group_id',
    #                                   'permissions__group__menu_id', 'permissions__group__menu__title').distinct()
    #
    # # 权限匹配相关信息，中间件RbacMiddleware中用到
    # # 以权限组为单位打包权限信息，获取codes_list，用于判断页面是否显示添加、编辑、删除等标签
    # perm_info_dict = {}
    # for dict_item in data_list:
    #     group_id = dict_item.get('permissions__group_id')
    #     if group_id not in perm_info_dict:
    #         perm_info_dict[group_id] = {
    #             'urls_info': [{'url_title': dict_item.get('permissions__title'),
    #                            'url': dict_item.get('permissions__url')}],
    #             'codes': [dict_item.get('permissions__code')]
    #         }
    #     else:
    #         perm_info_dict[group_id]['urls_info'].append({'url_title': dict_item.get('permissions__title'),
    #                                                       'url': dict_item.get('permissions__url')})
    #         perm_info_dict[group_id]['codes'].append(dict_item.get('permissions__code'))
    #
    # session[settings.PERM_INFO_DICT] = perm_info_dict
    #
    # # 菜单展示相关信息
    # # data_list中取一部分数据，用于生成侧边栏菜单
    # perm_side_list = []
    # for dict_item in data_list:
    #     tmp_dict = {
    #         'url_id': dict_item.get('permissions__id'),
    #         'url_title': dict_item.get('permissions__title'),
    #         'url': dict_item.get('permissions__url'),
    #         'menu_ref': dict_item.get('permissions__menu_ref_id'),
    #         'menu_id': dict_item.get('permissions__group__menu_id'),
    #         'menu_title': dict_item.get('permissions__group__menu__title')
    #     }
    #     perm_side_list.append(tmp_dict)
    #
    # session[settings.PERM_SIDE_LIST] = perm_side_list
