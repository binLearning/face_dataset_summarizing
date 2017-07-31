'''
Cropped & Aligned
File format: text files, each line is an image record containing 7 columns, 
             delimited by TAB.
Column1: Freebase MID
Column2: ImageSearchRank
Column3: ImageURL
Column4: PageURL
Column5: FaceID
Column6: FaceRectangle_Base64Encoded 
         (four floats, relative coordinates of UpperLeft and BottomRight corner)
Column7: FaceData_Base64Encoded
'''

from __future__ import absolute_import
from __future__ import print_function

import os
import sys
import base64
import struct
import numpy as np
from six.moves import xrange


def main():
  src_file = sys.argv[1]
  save_dir = sys.argv[2]
  
  if not os.path.exists(save_dir):
    os.mkdir(save_dir)
  
  save_rect_dir = os.path.join(save_dir, 'rect_info')
  if not os.path.exists(save_rect_dir):
    os.mkdir(save_rect_dir)
  
  fp_src = open(src_file, 'r')
  
  while True:
    line = fp_src.readline()
    
    if line == '': # EOF
      fp_src.close()
      break
    
    # delimited by TAB
    data_list = line.split('\t')
    
    identity = data_list[0]
    save_sub_dir = os.path.join(save_dir, identity)
    if not os.path.exists(save_sub_dir):
      os.mkdir(save_sub_dir)
    
    # remove 'FaceId-' from data_list[4](FaceID)
    save_name = '{}_{}.jpg'.format(data_list[1], data_list[4][7:])
    save_path = os.path.join(save_sub_dir, save_name)
    
    # save image
    img_data = data_list[6].decode('base64')
    with open(save_path, 'w') as fp_save:
      fp_save.write(img_data)
    
    # save rectengle info
    # four floats, relative coordinates of UpperLeft and BottomRight corner
    rect = struct.unpack('ffff', data_list[5].decode('base64'))
    save_rect_path = os.path.join(save_rect_dir, identity + '.txt')
    with open(save_rect_path, 'a') as fp_rect:
      fp_rect.write('{} {} {} {} {}\n'.format(save_name, rect[0], rect[1], rect[2], rect[3]))
    
  
if __name__ == '__main__':
  main()
