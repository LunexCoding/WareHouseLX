```python
[11-Apr-24 17:49] -> connection -> [DEBUG]: Server listening on localhost:9999
[11-Apr-24 17:49] -> connection -> [DEBUG]: Connection from ('127.0.0.1', 60671)
[11-Apr-24 17:49] -> connection -> [DEBUG]: Received: search Пользователи RoleID=2
[11-Apr-24 17:49] -> connection -> [DEBUG]: Response: [{"ID": 2, "Login": "user", "Password": "user", "RoleID": 2, "Fullname": null}, {"ID": 3, "Login": "1", "Password": "1", "RoleID": 2, "Fullname": null}, {"ID": 4, "Login": "2", "Password": "2", "RoleID": 2, "Fullname": null}]
[11-Apr-24 17:49] -> connection -> [DEBUG]: Received: search Пользователи RoleID=2|ID<3
[11-Apr-24 17:49] -> connection -> [DEBUG]: Response: [{"ID": 2, "Login": "user", "Password": "user", "RoleID": 2, "Fullname": null}]
[11-Apr-24 17:49] -> connection -> [DEBUG]: Received: 
[11-Apr-24 17:49] -> connection -> [DEBUG]: Empty data received, closing connection
[11-Apr-24 17:49] -> connection -> [DEBUG]: Connection from ('127.0.0.1', 60673)
[11-Apr-24 17:49] -> connection -> [DEBUG]: Received: search Пользователи RoleID=2|ID<3
[11-Apr-24 17:49] -> connection -> [DEBUG]: Response: [{"ID": 2, "Login": "user", "Password": "user", "RoleID": 2, "Fullname": null}]
[11-Apr-24 17:49] -> connection -> [DEBUG]: Received: 
[11-Apr-24 17:49] -> connection -> [DEBUG]: Empty data received, closing connection
[11-Apr-24 17:49] -> connection -> [DEBUG]: Stopping socket...
[11-Apr-24 17:49] -> connection -> [DEBUG]: Force closing remaining client connections...
[11-Apr-24 17:49] -> connection -> [DEBUG]: Socket stopped.
