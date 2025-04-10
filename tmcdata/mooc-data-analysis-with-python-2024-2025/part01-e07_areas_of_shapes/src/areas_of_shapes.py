#!/usr/bin/env python3

import math


def main():
    while True:
        shape=input("Choose a shape (triangle, rectangle, circle):")

        if shape == "":
            break
        elif shape == "triangle":
            base = float(input("Give base of the triangle: "))
            height = float(input("Give height of the triangle:"))
            area = 0.5 * base * height
            print(f"The area is {area:.6f}")
        elif shape == "rectangle":
            length = float(input("Give width of the rectangle: "))
            width = float(input("Give height of the rectangle: "))
            area = length * width
            print(f"The area is {area:.6f}")
        elif shape == "circle":
            radius = float(input("Give radius of the circle: "))
            area = math.pi * radius * radius
            print(f"The area is {area:.6f}")    
        else:
            print("Unknown shape!")
        
    # enter you solution here

if __name__ == "__main__":
    main()
