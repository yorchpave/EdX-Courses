weather = open('mean_temp.txt', 'a+') # Open file with append + read ability
weather.write("Rio de Janeiro,Brazil,30.0,18.0\n") # Write line at end of file
weather.seek(0) # Return to beginning of file
headings = weather.readline().split(',')

line = weather.readline() # Read first line of file after headings


while line: # While there is a line to read

    string = line.split(',') # Store city variables in a list
    print(headings[0].title(), "of", string[0], headings[2], "is", string[2], "Celcius") # Give print format
    line = weather.readline() # Check if there is another line to read

weather.close() # Close file
