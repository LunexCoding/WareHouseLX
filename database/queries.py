class SqlQueries:
    @staticmethod
    def getTableColumns(tableName):
        return f"""PRAGMA table_info({tableName})"""

    # DELETE A ROW FROM A TABLE #
    @staticmethod
    def deleteFromTable(tableName, targetElement, targetValue):
        return f"""
        DELETE FROM {tableName}
        WHERE {targetElement}={targetValue}
        """

    # UPDATE A ROW IN A TABLE #
    def updateTable(tableName, targetElement, targetValue, *kwargs):
        return f"""
        UPDATE {tableName}
        SET {", ".join([f"{key}=?" for key, value in kwargs.items()])}
        WHERE {targetElement}={targetValue}
        """

    # INSERT A ROW INTO THE REQUIRED TABLE #
    @staticmethod
    def insertIntoTable(tableName,args):
        return f"""
        INSERT INTO {tableName}
        ({', '.join([char for char in args])})
        VALUES ({', '.join(["?" for char in args])})
        """

    # SELECT ROWS FROM TABLE #
    @staticmethod
    def selectFromTable(tableName, requestData, args=None, limit=None, offset=None):
        if requestData == "*":
            return SqlQueries._selectAllFromTable(tableName, limit, offset)
        if (requestData is not None) and (requestData != "*"):
            return SqlQueries._selectFromTableByWhere(tableName, requestData, args, limit, offset)
        return SqlQueries._selectFromTableByParams(tableName, args, limit, offset)

    @staticmethod
    def _selectFromTableByParams(tableName, args, limit, offset):
        query = f"""
           SELECT {', '.join([char for char in args])}
           FROM {tableName}
           """
        if limit is not None:
            query += f"\nLIMIT {limit}"
        if offset is not None:
            query += f"\nOFFSET {offset}"
        return query

    @staticmethod
    def _selectAllFromTable(tableName, limit, offset):
        query = f"""
           SELECT * FROM {tableName}
           """
        if limit is not None:
            query += f"\nLIMIT {limit}"
        if offset is not None:
            query += f"\nOFFSET {offset}"
        return query

    @staticmethod
    def _selectFromTableByWhere(tableName, requestData, args, limit, offset):
        query = f"""
           SELECT {', '.join([char for char in args])}
           FROM {tableName}
           WHERE {' AND '.join([f'{key}="{value}"' for (key, value) in requestData.items()])}
           """
        if limit is not None:
            query += f"\nLIMIT {limit}"
        if offset is not None:
            query += f"\nOFFSET {offset}"
        return query
