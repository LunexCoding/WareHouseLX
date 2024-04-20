```python
[18-Apr-24 23:57] -> connection -> [DEBUG]: Server listening on localhost:9999
[18-Apr-24 23:57] -> connection -> [DEBUG]: Connection from ('127.0.0.1', 50060)
[18-Apr-24 23:57] -> connection -> [DEBUG]: Received: long_run
[18-Apr-24 23:57] -> connection -> [DEBUG]: Response: {"Command": "long_run", "Status": 1, "Result": "Not authorized."}
[18-Apr-24 23:57] -> connection -> [DEBUG]: Received: search Пользователи RoleID=2
[18-Apr-24 23:57] -> connection -> [DEBUG]: Response: {"Command": "search Пользователи RoleID=2", "Status": 1, "Result": "Not authorized."}
[18-Apr-24 23:57] -> connection -> [DEBUG]: Received: search Пользователи RoleID=2|ID<3
[18-Apr-24 23:57] -> connection -> [DEBUG]: Connection from ('127.0.0.1', 50061)
[18-Apr-24 23:57] -> connection -> [DEBUG]: Response: {"Command": "search Пользователи RoleID=2|ID<3", "Status": 1, "Result": "Not authorized."}
[18-Apr-24 23:57] -> connection -> [DEBUG]: Received: add
[18-Apr-24 23:57] -> connection -> [ERROR]: Command <add> not found!
[18-Apr-24 23:57] -> connection -> [DEBUG]: Response: {"Command": "add", "Status": 1, "Result": "Command <add> not found!"}
[18-Apr-24 23:57] -> connection -> [DEBUG]: Received: authorization admin admin
[18-Apr-24 23:57] -> connection -> [DEBUG]: Client is authorized ->  ID<1>, fullname: Иван Иванович
[18-Apr-24 23:57] -> connection -> [DEBUG]: Response: {"Command": "authorization admin admin", "Status": 0, "Result": {"ID": 1, "Fullname": "Иван Иванович", "Role": "Admin"}}
[18-Apr-24 23:57] -> connection -> [DEBUG]: Received: search Пользователи RoleID=2
[18-Apr-24 23:57] -> connection -> [DEBUG]: Response: {"Command": "search Пользователи RoleID=2", "Status": 0, "Result": [{"ID": 2, "Login": "user", "Password": "user", "RoleID": 2, "Fullname": "Петров Петрович"}, {"ID": 3, "Login": "1", "Password": "1", "RoleID": 2, "Fullname": null}, {"ID": 4, "Login": "2", "Password": "2", "RoleID": 2, "Fullname": null}]}
[18-Apr-24 23:57] -> connection -> [DEBUG]: Received: long_run
[18-Apr-24 23:57] -> connection -> [DEBUG]: Response: {"Command": "long_run", "Status": 1, "Result": "Not authorized."}
[18-Apr-24 23:57] -> connection -> [DEBUG]: Received: search Пользователи RoleID=2
[18-Apr-24 23:57] -> connection -> [DEBUG]: Response: {"Command": "search Пользователи RoleID=2", "Status": 1, "Result": "Not authorized."}
[18-Apr-24 23:57] -> connection -> [DEBUG]: Received: search Пользователи RoleID=2|ID<3
[18-Apr-24 23:57] -> connection -> [DEBUG]: Response: {"Command": "search Пользователи RoleID=2|ID<3", "Status": 1, "Result": "Not authorized."}
[18-Apr-24 23:57] -> connection -> [DEBUG]: Received: add
[18-Apr-24 23:57] -> connection -> [ERROR]: Command <add> not found!
[18-Apr-24 23:57] -> connection -> [DEBUG]: Response: {"Command": "add", "Status": 1, "Result": "Command <add> not found!"}
[18-Apr-24 23:57] -> connection -> [DEBUG]: Received: authorization user user
[18-Apr-24 23:57] -> connection -> [DEBUG]: Client is authorized ->  ID<2>, fullname: Петров Петрович
[18-Apr-24 23:57] -> connection -> [DEBUG]: Response: {"Command": "authorization user user", "Status": 0, "Result": {"ID": 2, "Fullname": "Петров Петрович", "Role": "User"}}
[18-Apr-24 23:57] -> connection -> [DEBUG]: Received: search Пользователи RoleID=2
[18-Apr-24 23:57] -> connection -> [DEBUG]: Response: {"Command": "search Пользователи RoleID=2", "Status": 0, "Result": [{"ID": 2, "Login": "user", "Password": "user", "RoleID": 2, "Fullname": "Петров Петрович"}, {"ID": 3, "Login": "1", "Password": "1", "RoleID": 2, "Fullname": null}, {"ID": 4, "Login": "2", "Password": "2", "RoleID": 2, "Fullname": null}]}
[18-Apr-24 23:57] -> connection -> [DEBUG]: Stopping socket...
[18-Apr-24 23:57] -> connection -> [DEBUG]: Socket stopped.
