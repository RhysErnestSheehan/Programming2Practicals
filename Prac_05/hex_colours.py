"""Rhys Sheehan CP1404 Practical 05 Hex Colours"""

hex_colours = {"aliceblue": "#f0f8ff", "azure1": "#f0ffff", "blue1": "#0000ff", "brown": "#a52a2a",
               "chartreuse1": "#7fff00", "chocolate": "#d2691e", "coral": "#ff7f50", "cyan1": "#00ffff"}

colour_name = input("Please enter a colour name: ").lower()
while hex_colours != "":
    if colour_name in hex_colours:
        print(colour_name, "is", hex_colours[colour_name])
    colour_name = input("Please enter a colour name: ").lower()
