# AES Cipher Encrypt
# Author: Jonathan Kenney (M08837382)

# imports
from os import urandom
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

# constants
AES_BLOCK_SIZE = 16   # AES block size (bytes)

def main():

  # initialize vars
  key = b''
  m = b''

  # fetch the key and convert from hex to bytes
  with open('./data/key.txt', 'r') as f:
    key = bytes.fromhex(f.read())
    f.close()

  # fetch message from plaintext file and convert to bytes
  with open('./data/plaintext.txt', 'r') as f:
    m = f.read().encode('utf-8')
    f.close()

  # pad the data
  padder = padding.PKCS7(AES_BLOCK_SIZE * 8).padder()   # NOTE: param here is block size in bits, not bytes
  m_padded = padder.update(m) + padder.finalize()

  # generate initialization vector
  iv = urandom(AES_BLOCK_SIZE)

  # generate the AES cipher and encrpytor
  backend = default_backend()
  cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
  encryptor = cipher.encryptor()
  
  # generate the ciphertext and convert to hex
  ct = encryptor.update(m_padded) + encryptor.finalize()

  # write iv to file in hex
  with open('./data/iv.txt', 'w') as f:
    f.write(iv.hex())
    f.close()

  # write ciphertext to file in hex
  with open('./data/ciphertext.txt', 'w') as f:
    f.write(ct.hex())
    f.close()

  return

# main boilerplate
if __name__ == '__main__':
  main()