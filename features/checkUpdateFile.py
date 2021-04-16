import os
from datetime import datetime
from pathlib import Path


def isFileUpdated(path):
    def fileExists(path):
        returnValue = False
        try:
            f = open(path)
            f.close()
            returnValue = True
        except IOError:
            returnValue = False
        finally:
            return returnValue

    if fileExists(path):
        fmt = '%d-%m-%Y'
        dateNow = datetime.today().strftime(fmt)

        timestamp = os.path.getmtime(path)
        lastDateFileModified = datetime.fromtimestamp(timestamp).strftime(fmt)

        if dateNow == lastDateFileModified:
            print(F"{path} atualizado Hoje!")
            return True
        else:
            print(F"{path} não atualizado Hoje!")
            return False
    else:
        print(F"{path} não encontrado!")
        return False
