from __future__ import absolute_import
from __future__ import print_function

import os
import sys

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
  dir_urls = sys.argv[2]
  if not os.path.exists(dir_urls):
    os.mkdir(dir_urls)

  list_info_files = os.listdir(rt_dir_info)

  for info_file_name in list_info_files[:]:
    individual_name,_ = os.path.splitext(info_file_name)

    info_file_path = os.path.join(rt_dir_info, info_file_name)

    list_info = np.loadtxt(info_file_path, dtype=line_type, comments=None)
    total_num = list_info.size

    print(individual_name, total_num)
    
    save_path = os.path.join(dir_urls, info_file_name)
    with open(save_path, 'w') as fp:
      for proc_num in xrange(total_num):
        str_url = list_info[proc_num]['url']
        fp.write('{}\n'.format(str_url))


if __name__ == '__main__':
  main()
