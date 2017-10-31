# ChainLinks

Necessary cryptographic primatives:
- hashe functions (takes string of any size and produces a fixed-size output)
- digital signatures
- apps that use the above to build crypto currencies


** Need hash functions that cryptographically secure;
* Must be efficiently computable;


cryptographic properties of hash functions:
- collision free
** Nobody can find x and y s.t.: x!=y and H(x)=H(y) ;

Compare hashes to run diff between two files;

Collisions do exist: input possibilities out number possibilities of outputs;
Are there any that are findable?
How to find a collision?

Hiding properties:
values of x must be spread out s.t. no value of x is highly likely;
H(r|x) = takes all the bits of r and put after them all the bits of x;
Given the hash or r together with x, its infeasible to find x;
** high min entropy **
There's no particular value of r that would occur with more than negible probability;


commitment - taking a value and sealing it in an envelop;
> put the envelop out on the table where everyone can see it;
key
message
verify(com, key, msg)


Committing to one message and later, claiming that you committed to another WILL NOT VERIFY:
msg != msg' s.t. verify(com(msg), msg') = true
** hiding
** binding
** puzzle friendly

Implement commitments

commit(msg) := ( H(key | msg), key )
verify( com, key, msg ) := ( H(key | msg) == com )
> hiding: Given H(key | msg), msg is infeasible to find;
> binding: infeasiable to find msg != msg' s.t. H(key | msg) == H(key | msg') << also collision free property;
> puzzle friendly


Build a search puzzle where searching a very large space in order to find a solution
and there are no short cuts other than searching this large space:
** Given puzzle_id (from a high min entropy distribution) && a target set Y
try to find x s.t. H(puzzle_id | x) is an element in {Y};


[SHA-256]
Takes the msg and breaks it up into blocks of 256 bits in size
(needs padding b/c the msg isn't going to necessarily be a multiple of the block size)
- IV
- msg blocks
- compression function C
At the end, will have consumed all the blocks of the msg and the padding = 256 bit hash output;
If C is collision free, then the entire hash function is collision free;


Change the contents of a block >> mismatch between itself and it's hashpointer;
** tamper evident log built out of a blockchain;

binary tree with hashpoints = Merkel tree
** to prove that any given block belongs in the chain,
only need to check matches up the branch to the root: O(log n) items;

** verifying membership in cyclic and acyclic data structures **

Digital signatures:
- unforgability property




Store blockchain data

Generate an initial block

Sync a node up with local blockchain data

Display the blockchain to be used for syncing future nodes

Create new blocks which are valid 

