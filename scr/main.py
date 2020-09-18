import sqlite3
import os.path

def getDbFilePath() -> str:
    DATABASE_PATH_FROM_ROOT = "db" # Note: requires double (\\) backslashes as divisions in case of multiple directory distance
    DATABASE_NAME = "db.db"

    # Using FP as short for FilePath
    mainFP = os.path.abspath(__file__)
    rootFP = os.path.dirname(os.path.dirname(mainFP))
    dataFP = os.path.join(rootFP, *(name for name in DATABASE_PATH_FROM_ROOT.split("\\")), DATABASE_NAME)

    return dataFP


# Test code using (slightly modifiend) default code from SQLite3 docs.
conn = sqlite3.connect(getDbFilePath())
c = conn.cursor()
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
conn.commit()
conn.close()
