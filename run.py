from os.path import basename, join
import glob
from importlib import import_module
import time

start_time = time.time()
fs_time = '{}:{}:{}'.format(time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec)
print('starting at: {}'.format(fs_time))
modules = glob.glob(join('py', "*.py"))

for f in modules:
    module_name = basename(f)[:-3]
    day_start_time = time.time()
    print('starting {}:'.format(module_name))
    m = import_module('py.' + module_name)
    p_start = time.time()
    s = m.part1('input/' + module_name + '.txt')
    print('     solution part 1: {}\n       complete after {} seconds'.format(s, round(time.time() - p_start, 4)))
    p_start = time.time()
    s = m.part2('input/' + module_name + '.txt')
    print('     solution part 2: {}\n       complete after {} seconds'.format(s, round(time.time() - p_start, 4)))
    print('{} complete after {} seconds\n'.format(module_name, round(time.time() - day_start_time, 4)))
end_time = '{}:{}:{}'.format(time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec)
print('end at: {}\ntotal time {} seconds'.format(end_time, round(time.time() - start_time, 4)))
