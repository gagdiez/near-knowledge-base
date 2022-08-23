### What are the advantages of having multiple keys?
### Why accounts have multiple keys?
### What are access keys useful for?
NEAR accounts can have multiple keys, each with their own set of permissions. This allows to share individual keys with third-parties, limiting their potential impact in your account, and allowing to replace any compromised key.

### What are the key types ?
### Which types of access keys are available?
### What keys can an account have?
NEAR implements two types of access keys: FullAccess keys and FunctionCall keys

### What are Full Access keys?
FullAccess keys have full control of an account, similar to having administrator privileges on your operating system. Particularly, Full Access keys can sign transactions doing any action in your account's behalf such as transferring funds, deploying a contract or calling other methods.

### What are Function Call keys?
FunctionCall keys are like OAuths: they only give permission to call non-payable methods on contracts. You can create one and give it to third-parties so they can make some method calls in your name.

### How do I create new access keys?
### How do I add an access keys?
The first full-access key is added when you create the account. After, you need to use a full-access key in order to add other keys to your account. For this you can use near-cli or near-api-js.

### How Can I lock an account?
### How can i lock a smart contract?
### how can i stop a contract for being updated?
You can delete all keys from the account, leaving it locked.

### What is a locked account
If you remove all keys from an account, then the account will become locked, meaning that it cannot sign transactions. In practice, this means that only the account's smart contract can transfer assets, create sub-accounts, or update its own code.

### Why locking an account?
Locking an account is very useful when one wants to deploy a contract, and let the community be assured that only the contract is in control of the account.