from database.database import databaseSession
from database.queries import SqlQueries
from database.tables import DatabaseTables
from settingsConfig import g_settingsConfig


class Authorization:
    @staticmethod
    def login(login, password):
        if len(password) != 0 and len(login) != 0:
            if Authorization._checkLoginDetails(login, password):
                print("Вошел")
                return True
            else:
                print("Error: No login")
                return False
        else:
            print("Error")
            return False

    @staticmethod
    def _checkLoginDetails(login, password):
        with databaseSession as db:
            data = db.getData(SqlQueries.selectFromTable(DatabaseTables.USERS, requestData={"Login": login, "Password": password}, args=["Login", "Password", "RoleID"]))
        if bool(data):
            roleID = data[-1]
            g_settingsConfig.role = Authorization.setRole(roleID)
        return bool(data)

    @staticmethod
    def setRole(roleID):
        with databaseSession as db:
            data = db.getData(SqlQueries.selectFromTable(DatabaseTables.ROLES, requestData={"ID": roleID}, args=["Name"]))
        return data[0]
