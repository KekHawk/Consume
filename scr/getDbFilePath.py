import os.path

def getDbFilePath() -> str:
    DATABASE_PATH_FROM_ROOT = r"db" 
    DATABASE_NAME = "db.db"

    # Using FP as short for FilePath
    mainFP = os.path.abspath(__file__)
    rootFP = os.path.dirname(os.path.dirname(mainFP))
    dataFP = os.path.join(rootFP, *(name for name in DATABASE_PATH_FROM_ROOT.split("\\")), DATABASE_NAME)

    return dataFP

