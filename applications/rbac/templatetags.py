"""
给模板添加一个side_dict变量使用
"""

import copy
import re

from flask import request, session

from . import rbac


@rbac.context_processor
def show_menu():
    def get_side_dict():
        current_url = request.path
        perm_side_list = session.get('PERM_SIDE_LIST')

        # (1) 取出所有可以做“菜单项”的权限URL
        perm_menu_dict = {}
        for dict_item in perm_side_list:
            if not dict_item.get('menu_ref'):
                perm_menu_dict[dict_item.get('id')] = copy.deepcopy(dict_item)

        # (2) 给当前正在访问的权限URL对应的“菜单项URL”或其自身添加'active'属性，用于在CSS中加红
        for dict_item in perm_side_list:
            url = dict_item.get('url')
            re_url = "^{}$".format(url)
            if re.match(re_url, current_url):
                menu_ref_id = dict_item.get('menu_ref')
                if not menu_ref_id:
                    perm_menu_dict[dict_item.get('id')]['active'] = True
                else:
                    perm_menu_dict[menu_ref_id]['active'] = True

        # 给当前有'active'属性的“菜单项URL”对应的菜单添加'active'属性，用于在CSS中设置展开动作
        side_dict = {}
        for dict_item in perm_menu_dict.values():
            menu_id = dict_item.get('menu_id')
            active = dict_item.get('active')
            if menu_id not in side_dict:
                side_dict[menu_id] = {
                    'menu_title': dict_item.get('menu_title'),
                    'menu_active': active,
                    'urls_info': [
                        {'url_title': dict_item.get('url_title'), 'url': dict_item.get('url'), 'active': active}]
                }
            else:
                if active:
                    side_dict[menu_id]['menu_active'] = True
                side_dict[menu_id]['urls_info'].append(
                    {'url_title': dict_item.get('url_title'), 'url': dict_item.get('url'), 'active': active})

        return side_dict

    return dict(get_side_dict=get_side_dict)
