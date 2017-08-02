'''
        #classes     #images
total     79077      5049824
>=20      70116      4948292
>=50      47544      4169288
>=80      26231      2796454
>=100     12883      1606638
'''

from __future__ import print_function

import os
import sys
import random


def main():
  rt_dir = sys.argv[1]
  required_min_num = int(sys.argv[2])

  # get valid identities
  all_subdirs = [dirs for dirs in os.listdir(rt_dir)]
  valid_subdirs = []
  for subdir in all_subdirs:
    for rt,_,files in os.walk(os.path.join(rt_dir, subdir)):
      if len(files) >= required_min_num:
        valid_subdirs.append(subdir)
  
  # select test & train samples
  TEST_NUM_PER_CLASS = 5
  test_samples  = []
  train_samples = []

  label = 0
  for subdir in valid_subdirs:
    for rt,_,files in os.walk(os.path.join(rt_dir, subdir)):
      random.shuffle(files)
      test_samples.extend('{} {}'.format(os.path.join(rt,f), label) for f in files[:TEST_NUM_PER_CLASS])
      train_samples.extend('{} {}'.format(os.path.join(rt,f), label) for f in files[TEST_NUM_PER_CLASS:])
    label += 1
  
  random.shuffle(test_samples)
  random.shuffle(train_samples)

  # save samples info 
  info_file_test  = 'images_test.txt'
  info_file_train = 'images_train.txt'
  fp_test  = open(info_file_test, 'w')
  fp_train = open(info_file_train, 'w')

  for item in test_samples:
    fp_test.write('{}\n'.format(item))
  for item in train_samples:
    fp_train.write('{}\n'.format(item))

  fp_test.close()
  fp_train.close()
  

if __name__ == '__main__':
  main()
