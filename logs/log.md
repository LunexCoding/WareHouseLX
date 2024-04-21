```python
[20-Apr-24 23:50] -> initializer.initializer -> [DEBUG]: The database already exists.
[20-Apr-24 23:50] -> connection -> [DEBUG]: Server listening on localhost:9999
[20-Apr-24 23:50] -> connection -> [DEBUG]: Connection from ('127.0.0.1', 62477)
[20-Apr-24 23:50] -> connection -> [DEBUG]: Received: authorization admin admin
[20-Apr-24 23:50] -> connection -> [DEBUG]: Connection from ('127.0.0.1', 62478)
[20-Apr-24 23:50] -> connection -> [DEBUG]: Client is authorized ->  ID<1>, fullname: Иван Иванович
[20-Apr-24 23:50] -> connection -> [DEBUG]: Response: {"Command": "authorization admin admin", "Status": 0, "Result": {"ID": 1, "Fullname": "Иван Иванович", "Role": "Admin"}}
[20-Apr-24 23:50] -> connection -> [DEBUG]: Received: add Пользователи [*] [test,test,2,test]
[20-Apr-24 23:50] -> connection -> [DEBUG]: Response: {"Command": "add Пользователи [*] [test,test,2,test]", "Status": 0, "Result": null}
[20-Apr-24 23:50] -> connection -> [DEBUG]: Received: search Пользователи RoleID=2
[20-Apr-24 23:50] -> connection -> [DEBUG]: Response: {"Command": "search Пользователи RoleID=2", "Status": 0, "Result": [{"ID": 2, "Login": "user", "Password": "user", "RoleID": 2, "Fullname": "Петров Петрович"}, {"ID": 3, "Login": "1", "Password": "1", "RoleID": 2, "Fullname": null}, {"ID": 4, "Login": "2", "Password": "2", "RoleID": 2, "Fullname": null}, {"ID": 5, "Login": "test", "Password": "test", "RoleID": 2, "Fullname": "test"}, {"ID": 6, "Login": "test1", "Password": "test1", "RoleID": 2, "Fullname": "test1"}, {"ID": 7, "Login": "test", "Password": "test", "RoleID": 2, "Fullname": "test"}]}
[20-Apr-24 23:50] -> connection -> [DEBUG]: Received: authorization user user
[20-Apr-24 23:50] -> connection -> [DEBUG]: Client is authorized ->  ID<2>, fullname: Петров Петрович
[20-Apr-24 23:50] -> connection -> [DEBUG]: Response: {"Command": "authorization user user", "Status": 0, "Result": {"ID": 2, "Fullname": "Петров Петрович", "Role": "User"}}
[20-Apr-24 23:50] -> connection -> [DEBUG]: Received: add Пользователи [*] [test1,test1,2,test1]
[20-Apr-24 23:50] -> connection -> [DEBUG]: Response: {"Command": "add Пользователи [*] [test1,test1,2,test1]", "Status": 0, "Result": null}
[20-Apr-24 23:50] -> connection -> [DEBUG]: Received: search Пользователи RoleID=2
[20-Apr-24 23:50] -> connection -> [DEBUG]: Response: {"Command": "search Пользователи RoleID=2", "Status": 0, "Result": [{"ID": 2, "Login": "user", "Password": "user", "RoleID": 2, "Fullname": "Петров Петрович"}, {"ID": 3, "Login": "1", "Password": "1", "RoleID": 2, "Fullname": null}, {"ID": 4, "Login": "2", "Password": "2", "RoleID": 2, "Fullname": null}, {"ID": 5, "Login": "test", "Password": "test", "RoleID": 2, "Fullname": "test"}, {"ID": 6, "Login": "test1", "Password": "test1", "RoleID": 2, "Fullname": "test1"}, {"ID": 7, "Login": "test", "Password": "test", "RoleID": 2, "Fullname": "test"}, {"ID": 8, "Login": "test1", "Password": "test1", "RoleID": 2, "Fullname": "test1"}]}
[20-Apr-24 23:50] -> connection -> [DEBUG]: Stopping socket...
[20-Apr-24 23:50] -> connection -> [DEBUG]: Socket stopped.
