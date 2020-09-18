import sqlite3
from scr.getDbFilePath import getDbFilePath

EXPECTED_FILE_PATH = r"C:\Users\szymj\Desktop\Consume\db\db.db"

functionReturnedData = getDbFilePath()
if functionReturnedData == EXPECTED_FILE_PATH:
    print("\u001b[32m \t\tPassed")
else:
    print("\u001b[31m \t\tFailed")
print("\u001b[0m", end="")

