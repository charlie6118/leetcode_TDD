# You could directly import these three build in library(Standard Library)
import turtle # Draw
import time # Set timeout, I use this to see the draw process
import csv # module for handle csv file

# csv data type
# edges, color

def main():
    csv_path = None # initialize the variable for csv_path
    while not csv_path: # While csv_path is None then execute the following steps
        csv_path = input("Please enter csv path: ") # Use input() function to get user input, in this case, file name
        try: # try & except is error handling method, try sth, if not success then execute except part of code
            with open(csv_path, 'r') as csvfile: # we open the csv file with user inpur path, put it into variable csvfile
                shapes = [] # initialize a list variable for shapes
                colors = [] # initialize a list variable for colors
                for row in csvfile: # for row in the csvfile we do the folloing things
                    pair = row.split(',') # since the csv means comma-separated value, we cut the string by split ','(comma)
                    shapes.append(pair[0]) # we put the edge part into shapes list
                    colors.append(pair[1].rsplit('\n')[0]) # we put the color part into color list
                t = turtle.Turtle() # Initialize the turtle board, according to the document
                for idx in range(len(shapes)): # we loop through the idx according to the length of shapes (0, 1, 2, ...)
                    t.fillcolor(colors[idx]) # fill the color with colors list
                    t.begin_fill() # according to the document
                    sides = int(shapes[idx])
                    if sides > 0:
                        t.circle(20, steps=sides)
                    else:
                        t.circle(20)
                    t.end_fill()
                    t.up() # rise the pen, according to the document
                    t.goto(0, -50 * (idx + 1)) # move down the pen, according to the document
                    t.down() # pen down, according to the document
                    time.sleep(1) # my habbit to see the picture
        except Exception as err:
            csv_path = None # clean the invalid path name
            print("Can't find proper csv path") # print the error msg
            break

if __name__ == "__main__":
    main() # execute the main() function
