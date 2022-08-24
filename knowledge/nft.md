### What are NFT?
### What is an NFT?
Non-fungible tokens (NFT) are unitary pieces of metadata stored in a contract. They are ideal to represent ownership of assets such as a piece of digital content, or a ticket for an event.

### How can I mint an NFT?
### how can i create an nft?
To mint an NFT you need to call the `nft_mint` method on a NFT contract. You will then setup the media and metadata related to the NFT.

### What are royalties in an NFT?
### What are NFT royalties?
In an NFT, royalties enable a user to gain a percentage of the future sells of the NFT.

### How do i use NFT royalties?
When you sell an NFT in your marketplace, make sure to iterate through the royalties and send the specified percentage of the sell to each user.

### How can I transfer an NFT?
Transferring an NFT can happen in two scenarios: (1) you ask to transfer an NFT, or (2) an authorized account asks to transfer the NFT. In both cases, it is necessary to invoke the `nft_transfer` method.

### How can I approve someone to transfer an NFT?
In NFTs, you can authorize other users to transfer an NFT you own. To do this, call the `nft_approve` method in the NFT contract.

### How can I attach NFTs to a call?
### How can I send an NFT and call a method at the same time?
The NFT standard enables to attach a non-fungible tokens in a call by using the NFT-contract as intermediary. This means that, instead of you attaching tokens directly to the call, you ask the NFT-contract to do both a transfer and a method call in your name. For this, call the `nft_transfer_call` in the NFT contract.

### Are there any simple "starting from 0" written walkthroughs or videos for writing contracts that go through line by line, command by command on how to write an NFT contract or just a contract in general in Rust for NEAR?
### Are there any tutorials on NFT
### Do you have an example on NFT
### Do you have an example of NFT marketplace
Please check our NFT tutorial: https://docs.near.org/tutorials/nfts/introduction
