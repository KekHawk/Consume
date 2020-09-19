from tests.decorator.testDecorator import testing_function as test

# To-test function
from scr.getDbFilePath import getDbFilePath

EXPECTED_FILE_PATH = r"C:\Users\szymj\Desktop\Consume\db\db.db"

@test(file=__file__)
def main():
    functionReturnedData = getDbFilePath()
    if functionReturnedData == EXPECTED_FILE_PATH:
        return True
    return False

main()
