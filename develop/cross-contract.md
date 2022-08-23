### What is a cross-contract call?
### Can I call other contracts?
### How can I call another contract?
Cross-contract calls allow to interact with other contracts to query or send information.  In NEAR, cross-contract calls are independent and asynchronous.


### Can I call another contract and get the result in the same method?
No, cross-contract calls to query data always involve two promises: (1) to call the external contract, and (2) to callback a method in your contract. These promises execute independently.

### Why are cross-contract calls asynchronous?
### Why I cannot call a contract and get the promise in the same method?
### Why the callback takes time?
Cross-contract calls are async in NEAR because this enables to scale the network infinitely. Since a contract does not need to wait for the result, the virtual machine running it can be put to sleep, therefore consuming less resources.