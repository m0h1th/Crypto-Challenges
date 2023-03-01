# Authenticator Write Up

## Method:

- First we will ask to get the tocken.
- We need to have a final json like `{"user":"4n4c15t","admin":"yes"}` 
- We know that the the final token is 32 bytes long so 2 blocks long.
- We know that the last block after decryption is xored with the second last block. we can change the previous block as `xor(decrypted,pre_cipherblock)`
- So first we will decrypt the last block with the give nc and then XOR with the last block of the intened plaintext.
- Then we decrypt the 1st block and then xor with the first block of inteneded plain text this will be our iv .
- Then send the parameters into the nc connection.

  
