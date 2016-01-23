#!/usr/bin/python3
from subprocess import Popen, PIPE, call
import platform
import time
import sys

PLOTSTYLE = """
set encoding utf8
unset key

# Color
set style line 1 lc rgb '#8b1a0e' pt 1 ps 1 lt 1 lw 2 # --- red
set style line 2 lc rgb '#5e9c36' pt 6 ps 1 lt 1 lw 2 # --- green
set style line 3 lc rgb '#800000' lt 1 lw 2
set style line 4 lc rgb '#ff0000' lt 1 lw 2
set style line 5 lc rgb '#ff4500' lt 1 lw 2
set style line 6 lc rgb '#ffa500' lt 1 lw 2
set style line 7 lc rgb '#006400' lt 1 lw 2
set style line 8 lc rgb '#0000ff' lt 1 lw 2
set style line 9 lc rgb '#9400d3' lt 1 lw 2

# Grey
set style line 11 lc rgb 'gray30' lt 1 lw 2
set style line 12 lc rgb 'gray40' lt 1 lw 2
set style line 13 lc rgb 'gray70' lt 1 lw 2
set style line 14 lc rgb 'gray90' lt 1 lw 2
set style line 15 lc rgb 'black' lt 1 lw 1.5
set style line 16 lc rgb "black" lt 4 lw 2

# Borders, etc.
set style line 21 lc rgb 'black' lt 1 lw 1.5
set border 3 back ls 21
set tics nomirror
set style line 22 lc rgb 'grey20' lt 0 lw 1
set grid back ls 22

# Palette
set palette maxcolors 3
set palette defined ( 0 '#8b1a0e',\
                      1 '#5e9c36',\
                      2 '#800000' )
set xtics 1
set ytics 1
"""

PLOTSCRIPT = """
load 'style.gp'
set terminal 'pngcairo'
set output '{}'
set key outside
set grid

set xrange [0.0:1.0]
set yrange [0.0:1.0]
set xlabel 'x'
set ylabel 'U'
set title '{}'

plot '{}' using 1:2 w lp ls 2 notitle
quit
"""

class gnuplot:
    """ Gnuplot calling interface """
    def run(script):
        if platform.system() == 'Windows' or platform.system() == 'Linux':
            if platform.system() == 'Windows':
                gnuplot = r'C:\Program Files (x86)\gnuplot\bin\pgnuplot'
            if platform.system() == 'Linux':
                gnuplot = 'gnuplot'
        plot = Popen([gnuplot, '-persist'],
                     stdin = PIPE, stdout = PIPE, stderr = PIPE)
        plot.stdin.write(bytes(script, 'UTF-8'))
        plot.stdin.flush()

print("Plotting...")
startTime = time.time()

for i in range(1,len(sys.argv)):
    gnuplot.run(PLOTSTYLE + PLOTSCRIPT.format(sys.argv[i].replace(".out",".png"),
                                  sys.argv[i], sys.argv[i]))
    if (i % 1000 == 0): print("Step: {} / {}".format(i, len(sys.argv)-1))
print('Done! ({}s)'.format(time.time() - startTime))





#PLOTHIST2DSCRIPT = """
#set cbrange [0.0:0.1]
#count and plot
#set pm3d map
#set pm3d interpolate 0,0
#splot '-' matrix
#{}
#EOF
#quit
#"""
