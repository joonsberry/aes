# AES Cipher Key Generation
# Author: Jonathan Kenney (M08837382)

# imports
from sys import argv
from os import urandom

def main():
  
  # get key size from args
  try:
    key_size = int(argv[1])
  except:
    print('\nUsage:\npython3 keygen.py [KEY_SIZE]\n')
    exit(1)

  # check supplied key size
  if key_size not in (16, 24, 32):
    print('ERROR: Invalid key size, must be in {16, 24, 32}\n')
    exit(1)

  # returns random key (bytes) from OS and converts to hex
  key = urandom(key_size).hex()

  # print key (in hex) to stdout
  print('Secret key: %s' % key)

  # store key (in hex) in file
  with open('./data/key.txt', 'w') as f:
    f.write(key)
    f.close()

  return

# main boilerplate
if __name__ == '__main__':
  main()