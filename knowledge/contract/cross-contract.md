### What is a cross-contract call?
### Can I call other contracts?
### How can I call another contract?
Cross-contract calls allow to interact with other contracts to query or send information. In NEAR, cross-contract calls are independent and asynchronous.

### Can I call another contract and get the result in the same method?
### How do I wait the result of a cross-contract call?
### how do i wait for another contract to answer me?
### how do i get the result of a contract call without interruption?
Cross-contract calls always involve two promises: (1) to call the external contract, and (2) to callback a method in your contract. These promises execute independently.

### Why are cross-contract calls asynchronous?
### Why I cannot call a contract and get the promise in the same method?
### Why the callback takes time?
Cross-contract calls are async because this enables to scale the network infinitely. Since a contract does not need to wait for the result, the virtual machine running it can be put to sleep, thus consuming less resources.

### does someone have a example or nice ref on how to await to get the response of a cross contract call?
### is there an example contract that calls external contract?
### Anyone have any reasonable examples of cross-contract calls with NEAR that return values
### do you have an example on cross-contract calls?
Please check our cross-contract call example: https://docs.near.org/tutorials/examples/xcc