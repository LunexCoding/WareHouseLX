```python
[28-Apr-24 16:22] -> initializer.initializer -> [DEBUG]: The database already exists.
[28-Apr-24 16:22] -> connection -> [DEBUG]: Server listening on localhost:9999
[28-Apr-24 16:22] -> connection -> [DEBUG]: Connection from ('127.0.0.1', 61492)
[28-Apr-24 16:25] -> connection -> [DEBUG]: Connection from ('127.0.0.1', 61514)
[28-Apr-24 16:25] -> connection -> [DEBUG]: Received: authorization admin admin
[28-Apr-24 16:25] -> commands.client -> [DEBUG]: Client is authorized -> ID<1>, fullname: None
[28-Apr-24 16:25] -> connection -> [DEBUG]: Response: {"Command": "authorization admin admin", "Status": 0, "Result": {"ID": 1, "Fullname": null, "Role": 2}}
[28-Apr-24 16:25] -> connection -> [DEBUG]: Received: load Документы_прихода
[28-Apr-24 16:25] -> connection -> [DEBUG]: Response: {"Command": "load Документы_прихода", "Status": 0, "Result": [{"ID": 1, "Counterparty": "1", "ContractNumber": 1, "CreationDate": "2024-04-28 16:19:32", "Comment": "1"}, {"ID": 2, "Counterparty": "1", "ContractNumber": 2, "CreationDate": "2024-04-28 16:19:35", "Comment": "2"}]}
