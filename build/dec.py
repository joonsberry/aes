# AES Cipher Decrypt
# Author: Jonathan Kenney (M08837382)

# imports
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

# constants
AES_BLOCK_SIZE = 16   # AES block size (bytes)


def main():

  # initialize vars
  key = b''
  ct = b''

  # fetch the key and convert from hex to bytes
  with open('./data/key.txt', 'r') as f:
    key = bytes.fromhex(f.read())
    f.close()

  # fetch iv from file and convert from hex to bytes
  with open('./data/iv.txt', 'r') as f:
    iv = bytes.fromhex(f.read())
    f.close()

  # fetch ciphertext from ciphertext file
  with open('./data/ciphertext.txt', 'r') as f:
    ct = bytes.fromhex(f.read())
    f.close()

  # generate the AES cipher and decrpytor
  backend = default_backend()
  cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
  decryptor = cipher.decryptor()

  # decrypt the ciphertext and decode
  m_padded = decryptor.update(ct) + decryptor.finalize()

  # unpad the data
  unpadder = padding.PKCS7(AES_BLOCK_SIZE * 8).unpadder()   # NOTE: param here is block size in bits, not bytes
  m = unpadder.update(m_padded) + unpadder.finalize()

  # write decrypted message to file
  with open('./data/result.txt', 'w') as f:
    f.write(m.decode('utf-8'))
    f.close()

  return

# main boilerplate
if __name__ == '__main__':
  main()