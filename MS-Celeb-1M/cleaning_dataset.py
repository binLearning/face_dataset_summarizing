'''
The MS-Celeb-1M clean list: https://drive.google.com/file/d/0ByNaVHFekDPRbFg1YTNiMUxNYXc/view
                         or http://pan.baidu.com/s/1gfxB0iB
From: https://github.com/AlfredXiangWu/LightCNN
'''

from __future__ import absolute_import
from __future__ import print_function

import os
import sys
from shutil import copyfile
#from scipy.misc import imread, imsave, imresize


def main():
  clean_file = sys.argv[1]
  rt_dir     = sys.argv[2]
  clean_dir  = sys.argv[3]

  if not os.path.exists(clean_dir):
    os.mkdir(clean_dir)

  fp_clean = open(clean_file, 'r')

  NEW_SIZE = (112,96,3)

  cnt = 0
  while True:
    line = fp_clean.readline()

    if line == '': # EOF
      fp_clean.close()
      break

    list_info = line[:-1].split(' ')

    new_class = '{:0>6}'.format(list_info[1])
    new_name  = list_info[0].replace('/', '-')

    clean_subdir = os.path.join(clean_dir, new_class)
    if not os.path.exists(clean_subdir):
      os.mkdir(clean_subdir)

    src_path = os.path.join(rt_dir, list_info[0])
    dst_path = os.path.join(clean_subdir, new_name)

    #image_src = imread(src_path, mode='RGB')
    #image_resize = imresize(image_src, NEW_SIZE)
    #imsave(dst_path, image_resize)

    copyfile(src_path, dst_path)
    
    cnt += 1
    if cnt % 10000 == 0:
      print(cnt)
  print(cnt)


if __name__ == '__main__':
  main()
