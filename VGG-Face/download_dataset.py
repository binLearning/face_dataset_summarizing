from __future__ import absolute_import
from __future__ import print_function

import os
import sys
import urllib2

import numpy as np
from six.moves import xrange


def main():
  line_type = {'names': ('id', 'url',
                         'lt_x', 'lt_y', # left top
                         'rb_x', 'rb_y', # right bottom
                         'pose', 'score', 'curation'),
               'formats': ('S16', 'S256',
                           np.float, np.float,
                           np.float, np.float,
                           np.float, np.float, np.int)}

  rt_dir_info = sys.argv[1]
  rt_dir_img  = sys.argv[2]

  if not os.path.exists(rt_dir_img):
    os.makedirs(rt_dir_img)

  sub_dir_err = os.path.join(rt_dir_img, '0_ERROR')
  if not os.path.exists(sub_dir_err):
    os.mkdir(sub_dir_err)

  list_info_files = os.listdir(rt_dir_info)

  for info_file_name in list_info_files:
    individual_name,_ = os.path.splitext(info_file_name)

    sub_dir_img = os.path.join(rt_dir_img, individual_name)
    if not os.path.exists(sub_dir_img):
      os.mkdir(sub_dir_img)

    info_file_path = os.path.join(rt_dir_info, info_file_name)

    list_info = np.loadtxt(info_file_path, dtype=line_type, comments=None)
    total_num = list_info.size

    print(individual_name, total_num)
    
    for proc_num in xrange(total_num):
      str_id  = list_info[proc_num]['id']
      str_url = list_info[proc_num]['url']
      
      try:
        request = urllib2.Request(str_url)
        pic = urllib2.urlopen(request)

        img_file_path = os.path.join(sub_dir_img, str_id+'.jpg')
        with open(img_file_path, 'w') as fp:
          fp.write(pic.read())
      except (urllib2.HTTPError, urllib2.URLError, IOError) as e:
        err_file_path = os.path.join(sub_dir_err, info_file_name)
        with open(err_file_path, 'a') as fp:
          print('Download Error:', str_url)
          fp.write('{} {} {}\n'.format(str_id, str_url, e))


if __name__ == '__main__':
  main()
