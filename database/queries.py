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
    @staticmethod
    def updateTable(tableName, targetElement, targetValue, **kwargs):
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
            return SqlQueries._selectFromTableByWhere(tableName, requestData, limit, offset)
        return SqlQueries._selectFromTableByParams(tableName, args, limit, offset)

    @staticmethod
    def _selectFromTableByParams(tableName, args, limit, offset):
        print("call")
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
    def _selectFromTableByWhere(tableName, requestData, limit, offset):
        conditions = requestData["condition"]
        tableColumns = requestData.get("tableColumns", None)
        if tableColumns is not None:
            columns = []
            data = None
            if isinstance(conditions, list):
                conditionsData = []
                for condition in conditions:
                    conditionData = condition.split()
                    for word in conditionData:
                        if word in tableColumns:
                            columns.append(word)
                            conditionData.remove(word)
                            conditionsData.append(" ".join(conditionData))
                    data = conditionsData
            else:
                conditionData = conditions.split()
                for word in conditionData:
                    if word in tableColumns:
                        columns.append(word)
                        conditionData.remove(word)
                data = " ".join(conditionData)
        if len(columns) == 1:
            columns = ''.join(columns)
        query = f"SELECT * FROM {tableName}"
        if isinstance(data, list):
            if columns:
                query += " WHERE "
                for i, column in enumerate(columns):
                    query += f"{column} {' '.join(data[i].split())}"
                    if i < len(columns) - 1:  # Проверяем, не последний ли это элемент
                        query += " AND "  # Добавляем оператор AND после каждого условия, кроме последнего
            else:
                query += f" WHERE {' '.join(data)}"
        else:
            query += f" WHERE {columns} {''.join(data)}"
        if limit is not None:
            query += f" LIMIT {limit}"
        if offset is not None:
            query += f" OFFSET {offset}"
        return query
