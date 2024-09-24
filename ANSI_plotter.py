#!/usr/bin/python3
"""
Script Name: ANSI_plotter.py
Description: Example on how to use ANSI control sequences to plot
Author: Juan F. Moya
Version: 1.0.0
Date: 2024-09-21
License: MIT

Acknowledgements:
- This script is based on the work of Mathias Wandel under MIT License.
  (https://github.com/Matthias-Wandel/AS5600-Raspberry-Pi-Python/)
"""


import time, math, random

def move_cursor(x: int, y: int) -> None: 
    """
    Moves cursor to (x, y) position using ANSI control sequences.
    Args: x, y (int): The x (column) and y (row) coordinates.
    """
    print(f"\033[{y};{x}H", end="")


def main() -> None:
    """
    Main function to plot using ANSI control sequences.
    Draws axes and plots a circle on the terminal.
    """
    # clear screen and hide cursor commands
    print("\033[2J", "\033[?25l", end="")

    # draw axis
    xc = 150//2
    yc = 56//2

    for i in range(-xc, xc):
        move_cursor(xc + i, yc)
        print("-", end="")

    for i in range(-yc, yc):
        move_cursor(xc, yc + i)
        print("!", end="")

    points_len = 150 # number of points to display
    points = [(0,0)] * points_len
    j = 0
    mag = 1

    # Main plotting loop
    for i in range(4000):
        # erase last point from screen
        p_0 = points[j]
        move_cursor(*p_0)               
        if p_0[0] == xc:
            print("!", end="")
        elif p_0[1] == yc:
            print("-", end="")
        else:
            print(" ", end="")

        # generate angle and magnitude
        d_angle = 20                    
        rad = i/d_angle
        d_mag = random.uniform(-0.5, 0.5)/50
        mag += d_mag
        scale = 0.5

        # generate coordinates and update on list      
        p = int(xc + xc * math.cos(rad) * scale * mag),\
            int(yc - yc * math.sin(rad) * scale * mag)
        points[j] = p  

        # update index and reset if list's len reached
        j += 1
        if j == points_len:             
            j = 0

        # displays point info
        move_cursor(0, 0)                
        print(f"Deg: {((180/math.pi)*(rad))%360:6.2f}\272\
        Rad: {rad:6.2f}\
        Magnitude: {mag:5.3f}\
        {xc, yc}", end="")

        # display point marker '*'
        move_cursor(*p)
        print("*", end="", flush=True) # flush = True forces the output buffer to be flushed immediately 

        time.sleep(0.001)

    move_cursor(0, 2)
    # show cursor command
    print("\033[?25h") 


if __name__ == "__main__":
    main()

