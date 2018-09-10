def custom_paginator(paginator, page_obj, page_numbers_range):
    max_page = len(paginator.page_range)
    current_page = page_obj.number

    current_page_pack = int((current_page - 1) / page_numbers_range)
    end_page_pack = int((max_page - 1) / page_numbers_range)

    start_page = current_page_pack * page_numbers_range
    end_page = start_page + page_numbers_range

    if end_page >= max_page:
        end_page = max_page

    if current_page_pack == end_page_pack:
        has_next_pack = False
    else:
        has_next_pack = True

    if current_page_pack == 0:
        has_previous_pack = False
    else:
        has_previous_pack = True

    custom_page_obj = {
        'page_range': paginator.page_range[start_page:end_page],
        'start_page': start_page,
        'end_page': end_page,
        'max_page': max_page,
        'has_next_pack': has_next_pack,
        'has_previous_pack': has_previous_pack,
    }

    return custom_page_obj
