### What is the environment?
Every method execution has an environment associated with information such as: (1) Who called the method, (2) How much money is attached to the call, (3) How many computational resources are available, and (4) The current time.

### How can I know who called my contract's method?
### How can I know who signed the transaction?
### How do I get my contract's address?
### What is the address of my user?
During execution, the environment gives you access to 3 important users: (1) Your contract's account (`current_account`), (2) who invoked your contract's method (`predecessor`), and (3) who signed the transaction that lead to this execution (`signer`).