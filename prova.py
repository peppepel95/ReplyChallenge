from file_interface import read_file, write_file
import numpy as np
from multiprocessing import Pool


files = ['a_solar.txt', 'b_dream.txt', 'c_soup.txt', 'd_maelstrom.txt', 'e_igloos.txt', 'f_glitch.txt']
# for file in files:
#     read_file(file)
read_file(files[0])