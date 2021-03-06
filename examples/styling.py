#!/usr/bin/env python
from print_extended import print

print.black("black")
print.red("red")
print.green("green")
print.blue("blue")
print.yellow("yellow")
print.magenta("magenta")
print.cyan("cyan")
print.white("white")
print.on_black("black")
print.on_red("red")
print.on_green("green")
print.on_blue("blue")
print.on_yellow("yellow")
print.on_magenta("magenta")
print.on_cyan("cyan")
print.on_white("white")

print.rgb(255, 127, 0)("orange (rgb(255, 127, 0))")

for g in range(0, 256, 16):
    print.on_rgb(255, g, 0)(" ", end="")
for r in range(255, -1, -16):
    print.on_rgb(r, 255, 0)(" ", end="")
for b in range(0, 256, 16):
    print.on_rgb(0, 255, b)(" ", end="")
for g in range(255, -1, -16):
    print.on_rgb(0, g, 255)(" ", end="")
print()

print.bold("bold")
print.italic("italic")
print.underline("underline")

print.red.bold.italic("red, bold, and italic")
