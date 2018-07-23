# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from . import lot

import re

class FirstPassFilterPipeline(object):
    def __init__(self):
        self.seen = set()

    def process_item(self, item, spider):
        lower = item['description'].lower()

        for required in ['extru', 'slot']:
            if required not in lower:
                raise DropItem

        if lower in self.seen:
            raise DropItem

        self.seen.add(lower)

        return item

class PageToLotPipeline(object):
    def process_item(self, item, spider):
        description = item['description']

        if 'Lot' in description:
            raise DropItem("No parsing lots yet")

        l = lot.description_to_lot(description)

        if l is None:
            raise DropItem("Failed to parse lot: " + str(l))

        l['original'] = description

        return l
