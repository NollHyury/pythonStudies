import os
from datetime import datetime
from pathlib import Path
import pandas as pd
from unidecode import unidecode
import re


def transformJobToDataFrame(jobPath):
    orders = getOrders(jobPath)
    dataFrame = pd.DataFrame(orders)
    return dataFrame


def getOrders(jobPath):
    data = []
    f = open(jobPath, mode="r", encoding="latin1")

    def transformElement(value):
        value = str(value).strip()
        return unidecode(value)

    def transformTypes(value):
        def tryTransformDate(value):
            try:
                dateStr = value + ' 00:00:00'
                return datetime.strptime(dateStr,"%d.%m.%Y %H:%M:%S")
            except:
                return None

        date = tryTransformDate(value)
        if date != None:
            return date

        return str(value)


    orders = []
    for line in f:
        if line[0] == '|' and line[1] != '-':
            lineValues = list(
                map(lambda element: transformElement(element), line.split('|')))
            orders.append(lineValues)

    f.close()

    keys = []
    for index, element in enumerate(orders):
        if index == 0:
            for key in element:
                if key != '':
                    keys.append(key)
            break

    for index, elements in enumerate(orders):
        values = []
        if index > 0:
            elements.pop(0)
            dictObj = dict(zip(keys, list(map(
                lambda element: transformTypes(element), elements
            )
            )))
            data.append(dictObj)

    return data
