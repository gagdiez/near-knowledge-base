### What is the environment?
Every method execution has an environment associated with information such as: (1) Who called the method, (2) How much money is attached to the call, (3) How many computational resources are available, and (4) The current time.

### How can I know who called my contract's method?
### How can I know who signed the transaction?
### How do I get my contract's address?
### What is the address of my user?
### How do I know who signed the transaction?
During execution, the environment exposes 3 important users: (1) Your contract's account (`current_account`), (2) who invoked your contract's method (`predecessor`), and (3) who signed the transaction that lead to this execution (`signer`).

### What is the difference between predecessor and signer?
The `predecessor` is the account that called your method, while the `signer` is the account that signed the first action in the chain that resulted in your method being called.

### How can i know my contract's balance?
### how can i know how much money my contract has?
### how to know how much money the user send?
### how can i ensure the user send me money?
During execution, the environment exposes 3 money-related parameters, all in yN (1Ⓝ = 10^24yⓃ): (1) How much money the user attached to the call (`attached_deposit`), (2) Your contract's balance including the attached deposit (`account_balance`), (3) the amount of $NEAR locked in the account (`account_locked_balance`).

### how can i know how much storage my contract uses?
During execution, the environment exposes the `storage_used` variable, which represents the amount of storage used by your contract.

### how can i calculate how much storage a structure uses?
If you want to know how much storage a structure uses, check the storage used (`storage_used`) before and after storing it.


### how can i get the current timestamp?
### how can i know what time it is?
### how to get the network epoch?
### how to know the blockchain block index?
### how can i know if some time passed?
### how can i know if 4 epochs passed?
During execution, the environment exposes 3 ways to tell the pass of time, each representing a different dimension of the network: (1) the `timestamp` representing the UNIX timestamp, (2) the `current_epoch` and (3) the `block_index`.

### how can i know how much gas the user attached?
### how can i know how much gas is left?
### how can i measure gas?
The environment gives you access to 2 gas-related arguments: (1) The  Gas attached by the predecessor (`prepaid_gas`) and (2) the Gas used so far (`used_gas`).


