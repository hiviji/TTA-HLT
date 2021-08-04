import sys

# prompt for the input dimensions
window_width=float(input("Width (m):"))
if window_width>3.5 or window_width<0.5:
      print("Error - the width is out of range.")
      sys.exit(1) # can't continue with rest of program

window_height=float(input("Height (m):"))
if window_height>2 or window_width<0.5:
      print("Error - the height is out of range.")
      sys.exit(1) # can't continue with rest of program

# measurements of the glass
height_of_the_glass=window_height-(0.0254*2)
#print(height_of_the_glass)
width_of_the_glass=float(window_width)-(0.0254*2)
#print(width_of_the_glass)
glass_required=width_of_the_glass*height_of_the_glass
print(f"Glass required is {glass_required} sq. metres")

#measurement for wood
wood_width_in_ft = float(window_width) // .3048
#wood_width_in_inches = float(window_width) / .3048 % 1 * 12
wood_width_in_inches = ( (float (window_width) / .3048)*12 ) %12
wood_width_in_inches=round(wood_width_in_inches,3)
#print("The wood width is", wood_width_in_ft,"feet and",wood_width_in_inches, "inches")

wood_height_in_ft = float(window_height) // .3048
wood_height_in_inches = (float(window_height) / .3048 * 12) %12
wood_height_in_inches = (round(wood_height_in_inches,3))-2
#print("Wood height is", wood_height_in_ft,"feet and",wood_height_in_inches, "inches")

print(f"Wood required is \n Top and bottom {wood_width_in_ft} feet {wood_width_in_inches} inches")
print(f" Left and right {wood_height_in_ft} feet {wood_height_in_inches} inches")
