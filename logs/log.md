```python
[24-Apr-24 00:34] -> initializer.initializer -> [DEBUG]: The database already exists.
[24-Apr-24 00:34] -> connection -> [DEBUG]: Server listening on localhost:9999
[24-Apr-24 00:34] -> connection -> [DEBUG]: Connection from ('127.0.0.1', 53243)
[24-Apr-24 00:34] -> connection -> [DEBUG]: Received: authorization admin admin
[24-Apr-24 00:34] -> connection -> [DEBUG]: Connection from ('127.0.0.1', 53244)
[24-Apr-24 00:34] -> commands.client -> [DEBUG]: Client is authorized -> ID<1>, fullname: None
[24-Apr-24 00:34] -> connection -> [DEBUG]: Response: {"Command": "authorization admin admin", "Status": 0, "Result": {"ID": 1, "Fullname": null, "Role": "Admin"}}
[24-Apr-24 00:34] -> connection -> [DEBUG]: Received: add Пользователи [*] [test,test,2,test]
[24-Apr-24 00:34] -> connection -> [DEBUG]: Response: {"Command": "add Пользователи [*] [test,test,2,test]", "Status": 0, "Result": null}
[24-Apr-24 00:34] -> connection -> [DEBUG]: Received: search Пользователи RoleID=2
[24-Apr-24 00:34] -> connection -> [DEBUG]: Response: {"Command": "search Пользователи RoleID=2", "Status": 0, "Result": [{"ID": 2, "Login": "user", "Password": "user", "RoleID": 2, "Fullname": null}, {"ID": 3, "Login": "test", "Password": "test", "RoleID": 2, "Fullname": "test"}]}
[24-Apr-24 00:34] -> connection -> [DEBUG]: Received: authorization user user
[24-Apr-24 00:34] -> commands.client -> [DEBUG]: Client is authorized -> ID<2>, fullname: None
[24-Apr-24 00:34] -> connection -> [DEBUG]: Response: {"Command": "authorization user user", "Status": 0, "Result": {"ID": 2, "Fullname": null, "Role": "User"}}
[24-Apr-24 00:34] -> connection -> [DEBUG]: Received: add Пользователи [*] [test1,test1,2,test1]
[24-Apr-24 00:34] -> connection -> [DEBUG]: Response: {"Command": "add Пользователи [*] [test1,test1,2,test1]", "Status": 1, "Result": "Access error."}
[24-Apr-24 00:34] -> connection -> [DEBUG]: Received: search Пользователи RoleID=2
[24-Apr-24 00:34] -> connection -> [DEBUG]: Response: {"Command": "search Пользователи RoleID=2", "Status": 0, "Result": [{"ID": 2, "Login": "user", "Password": "user", "RoleID": 2, "Fullname": null}, {"ID": 3, "Login": "test", "Password": "test", "RoleID": 2, "Fullname": "test"}]}
[24-Apr-24 00:35] -> connection -> [DEBUG]: Stopping socket...
[24-Apr-24 00:35] -> connection -> [DEBUG]: Socket stopped.
