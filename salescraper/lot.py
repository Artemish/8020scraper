from . import constants

import re

series_regex = re.compile('[Ss]eries\s+(\d+)')
inch_dim_regex = re.compile('(\d+)\s+[xX]\s+(\d+)')
mm_dim_regex = re.compile('(\d+)\s+[xX]\s+(\d+)')

length_inch_regex = re.compile('(\d+)"\s+[lL]ong')
length_mm_regex = re.compile('(\d+)mm\s+[lL]ong')

def description_to_lot(description):
    ret = {}

    series = series_regex.search(description)
    if series is None:
        return None

    ret['Series'] = series.groups()[0]

    inch_dim = inch_dim_regex.search(description)

    if inch_dim is None:
        mm_dim = mm_dim_regex.search(description)
        if mm_dim is None:
            return None
        dims = constants.mm_to_inch * mm_dim.groups()
    else:
        dims = inch_dim.groups()

    ret['Dimensions'] = dims

    inch_len = length_inch_regex.search(description)

    if inch_len is None:
        mm_len = inch_mm_regex.search(description)
        if mm_len is None:
            return None
        length = constants.mm_to_inch * mm_len.groups()[0]
    else:
        length = inch_len.groups()[0]

    ret['Length'] = length

    return ret
