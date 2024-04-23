```python
[23-Apr-24 23:49] -> initializer.initializer -> [DEBUG]: Creating a directory for the database...
[23-Apr-24 23:49] -> initializer.initializer -> [DEBUG]: Initializing the Database...
[23-Apr-24 23:49] -> initializer.initializer -> [DEBUG]: Database creation...
[23-Apr-24 23:49] -> initializer.initializer -> [DEBUG]: Creating triggers...
[23-Apr-24 23:49] -> initializer.initializer -> [DEBUG]: Data recording...
[23-Apr-24 23:49] -> initializer.initializer -> [DEBUG]: Database initialized.
[23-Apr-24 23:49] -> connection -> [DEBUG]: Server listening on localhost:9999
[23-Apr-24 23:49] -> connection -> [DEBUG]: Connection from ('127.0.0.1', 52371)
[23-Apr-24 23:49] -> connection -> [DEBUG]: Received: authorization admin admin
[23-Apr-24 23:49] -> connection -> [DEBUG]: Connection from ('127.0.0.1', 52372)
[23-Apr-24 23:49] -> connection -> [DEBUG]: Client is authorized ->  ID<1>, fullname: None
[23-Apr-24 23:49] -> connection -> [DEBUG]: Response: {"Command": "authorization admin admin", "Status": 0, "Result": {"ID": 1, "Fullname": null, "Role": "Admin"}}
[23-Apr-24 23:49] -> connection -> [DEBUG]: Received: add Пользователи [*] [test,test,2,test]
[23-Apr-24 23:49] -> connection -> [DEBUG]: Response: {"Command": "add Пользователи [*] [test,test,2,test]", "Status": 0, "Result": null}
[23-Apr-24 23:49] -> connection -> [DEBUG]: Received: search Пользователи RoleID=2
[23-Apr-24 23:49] -> connection -> [DEBUG]: Response: {"Command": "search Пользователи RoleID=2", "Status": 0, "Result": [{"ID": 2, "Login": "user", "Password": "user", "RoleID": 2, "Fullname": null}, {"ID": 3, "Login": "test", "Password": "test", "RoleID": 2, "Fullname": "test"}]}
[23-Apr-24 23:49] -> connection -> [DEBUG]: Received: authorization user user
[23-Apr-24 23:49] -> connection -> [DEBUG]: Client is authorized ->  ID<2>, fullname: None
[23-Apr-24 23:49] -> connection -> [DEBUG]: Response: {"Command": "authorization user user", "Status": 0, "Result": {"ID": 2, "Fullname": null, "Role": "User"}}
[23-Apr-24 23:49] -> connection -> [DEBUG]: Received: add Пользователи [*] [test1,test1,2,test1]
[23-Apr-24 23:49] -> connection -> [DEBUG]: Response: {"Command": "add Пользователи [*] [test1,test1,2,test1]", "Status": 1, "Result": "Access error."}
[23-Apr-24 23:49] -> connection -> [DEBUG]: Received: search Пользователи RoleID=2
[23-Apr-24 23:49] -> connection -> [DEBUG]: Response: {"Command": "search Пользователи RoleID=2", "Status": 0, "Result": [{"ID": 2, "Login": "user", "Password": "user", "RoleID": 2, "Fullname": null}, {"ID": 3, "Login": "test", "Password": "test", "RoleID": 2, "Fullname": "test"}]}
[23-Apr-24 23:50] -> connection -> [DEBUG]: Connection from ('127.0.0.1', 52375)
[23-Apr-24 23:50] -> connection -> [DEBUG]: Received: authorization admin admin
[23-Apr-24 23:50] -> connection -> [DEBUG]: Connection from ('127.0.0.1', 52376)
[23-Apr-24 23:50] -> connection -> [DEBUG]: Client is authorized ->  ID<1>, fullname: None
[23-Apr-24 23:50] -> connection -> [DEBUG]: Response: {"Command": "authorization admin admin", "Status": 0, "Result": {"ID": 1, "Fullname": null, "Role": "Admin"}}
[23-Apr-24 23:50] -> connection -> [DEBUG]: Received: add Пользователи [*] [test,test,2,test]
[23-Apr-24 23:50] -> connection -> [DEBUG]: Response: {"Command": "add Пользователи [*] [test,test,2,test]", "Status": 0, "Result": null}
[23-Apr-24 23:50] -> connection -> [DEBUG]: Received: search Пользователи RoleID=2
[23-Apr-24 23:50] -> connection -> [DEBUG]: Response: {"Command": "search Пользователи RoleID=2", "Status": 0, "Result": [{"ID": 2, "Login": "user", "Password": "user", "RoleID": 2, "Fullname": null}, {"ID": 3, "Login": "test", "Password": "test", "RoleID": 2, "Fullname": "test"}]}
[23-Apr-24 23:50] -> connection -> [DEBUG]: Received: authorization user user
[23-Apr-24 23:50] -> connection -> [DEBUG]: Client is authorized ->  ID<2>, fullname: None
[23-Apr-24 23:50] -> connection -> [DEBUG]: Response: {"Command": "authorization user user", "Status": 0, "Result": {"ID": 2, "Fullname": null, "Role": "User"}}
[23-Apr-24 23:50] -> connection -> [DEBUG]: Received: add Пользователи [*] [test1,test1,2,test1]
[23-Apr-24 23:50] -> connection -> [DEBUG]: Response: {"Command": "add Пользователи [*] [test1,test1,2,test1]", "Status": 1, "Result": "Access error."}
[23-Apr-24 23:50] -> connection -> [DEBUG]: Received: search Пользователи RoleID=2
[23-Apr-24 23:50] -> connection -> [DEBUG]: Response: {"Command": "search Пользователи RoleID=2", "Status": 0, "Result": [{"ID": 2, "Login": "user", "Password": "user", "RoleID": 2, "Fullname": null}, {"ID": 3, "Login": "test", "Password": "test", "RoleID": 2, "Fullname": "test"}]}
[23-Apr-24 23:50] -> connection -> [DEBUG]: Stopping socket...
[23-Apr-24 23:50] -> connection -> [DEBUG]: Socket stopped.
