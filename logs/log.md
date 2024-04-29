```python
[29-Apr-24 10:21] -> initializer.initializer -> [DEBUG]: The database already exists.
[29-Apr-24 10:21] -> connection -> [DEBUG]: Server listening on localhost:9999
[29-Apr-24 10:21] -> connection -> [DEBUG]: Connection from ('127.0.0.1', 52006)
[29-Apr-24 10:21] -> connection -> [DEBUG]: Connection from ('127.0.0.1', 52007)
[29-Apr-24 10:21] -> connection -> [DEBUG]: Received: authorization user user
[29-Apr-24 10:21] -> commands.client -> [DEBUG]: Client is authorized -> ID<2>, fullname: None
[29-Apr-24 10:21] -> connection -> [DEBUG]: Response: {"Command": "authorization user user", "Status": 0, "Result": {"ID": 2, "Fullname": null, "Role": 1}}
[29-Apr-24 10:21] -> connection -> [DEBUG]: Received: authorization admin admin
[29-Apr-24 10:21] -> commands.client -> [DEBUG]: Client is authorized -> ID<1>, fullname: None
[29-Apr-24 10:21] -> connection -> [DEBUG]: Response: {"Command": "authorization admin admin", "Status": 0, "Result": {"ID": 1, "Fullname": null, "Role": 2}}
[29-Apr-24 10:21] -> connection -> [DEBUG]: Received: load Документы_прихода
[29-Apr-24 10:21] -> connection -> [DEBUG]: Response: {"Command": "load Документы_прихода", "Status": 0, "Result": [{"ID": 1, "Counterparty": "1", "ContractNumber": 1, "CreationDate": "2024-04-28 16:19:32", "Comment": "1"}, {"ID": 2, "Counterparty": "1", "ContractNumber": 2, "CreationDate": "2024-04-28 16:19:35", "Comment": "2"}]}
[29-Apr-24 10:21] -> connection -> [DEBUG]: Received: load Документы_прихода
[29-Apr-24 10:21] -> connection -> [DEBUG]: Response: {"Command": "load Документы_прихода", "Status": 0, "Result": [{"ID": 1, "Counterparty": "1", "ContractNumber": 1, "CreationDate": "2024-04-28 16:19:32", "Comment": "1"}, {"ID": 2, "Counterparty": "1", "ContractNumber": 2, "CreationDate": "2024-04-28 16:19:35", "Comment": "2"}]}
[29-Apr-24 10:22] -> connection -> [DEBUG]: Received: load Документы_прихода
[29-Apr-24 10:22] -> connection -> [DEBUG]: Response: {"Command": "load Документы_прихода", "Status": 0, "Result": [{"ID": 3, "Counterparty": "2", "ContractNumber": 1, "CreationDate": "2024-04-28 16:19:40", "Comment": "1"}, {"ID": 4, "Counterparty": "3", "ContractNumber": 1, "CreationDate": "2024-04-28 16:20:17", "Comment": "1"}]}
[29-Apr-24 10:22] -> connection -> [DEBUG]: Received: load Документы_прихода
[29-Apr-24 10:22] -> connection -> [DEBUG]: Response: {"Command": "load Документы_прихода", "Status": 0, "Result": [{"ID": 3, "Counterparty": "2", "ContractNumber": 1, "CreationDate": "2024-04-28 16:19:40", "Comment": "1"}, {"ID": 4, "Counterparty": "3", "ContractNumber": 1, "CreationDate": "2024-04-28 16:20:17", "Comment": "1"}]}
[29-Apr-24 10:22] -> connection -> [DEBUG]: Received: load Документы_прихода
[29-Apr-24 10:22] -> connection -> [DEBUG]: Response: {"Command": "load Документы_прихода", "Status": 0, "Result": [{"ID": 5, "Counterparty": "2", "ContractNumber": 2, "CreationDate": "2024-04-28 18:45:21", "Comment": "1"}]}
[29-Apr-24 10:22] -> connection -> [DEBUG]: Received: load Документы_прихода
[29-Apr-24 10:22] -> connection -> [DEBUG]: Response: {"Command": "load Документы_прихода", "Status": 0, "Result": [{"ID": 5, "Counterparty": "2", "ContractNumber": 2, "CreationDate": "2024-04-28 18:45:21", "Comment": "1"}]}
[29-Apr-24 10:22] -> connection -> [DEBUG]: Client ('127.0.0.1', 52007) disconnected
[29-Apr-24 10:22] -> connection -> [DEBUG]: Client ('127.0.0.1', 52006) disconnected
[29-Apr-24 10:22] -> connection -> [DEBUG]: Connection from ('127.0.0.1', 52012)
[29-Apr-24 10:22] -> connection -> [DEBUG]: Received: authorization admin admin
[29-Apr-24 10:22] -> commands.client -> [DEBUG]: Client is authorized -> ID<1>, fullname: None
[29-Apr-24 10:22] -> connection -> [DEBUG]: Response: {"Command": "authorization admin admin", "Status": 0, "Result": {"ID": 1, "Fullname": null, "Role": 2}}
[29-Apr-24 10:22] -> connection -> [DEBUG]: Received: load Документы_прихода
[29-Apr-24 10:22] -> connection -> [DEBUG]: Response: {"Command": "load Документы_прихода", "Status": 0, "Result": [{"ID": 1, "Counterparty": "1", "ContractNumber": 1, "CreationDate": "2024-04-28 16:19:32", "Comment": "1"}, {"ID": 2, "Counterparty": "1", "ContractNumber": 2, "CreationDate": "2024-04-28 16:19:35", "Comment": "2"}]}
[29-Apr-24 10:22] -> connection -> [DEBUG]: Client ('127.0.0.1', 52012) disconnected
