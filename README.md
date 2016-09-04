# gppy
python gnuplot binding module

Simple and efficient module to generate gnuplot plots using python.

The module aims to maintain usual gnuplot commands.

## Example:


```python
import gppy
from math import sin
g = gppy.gppy()
x = [i/100. for i in range(0,314)]
y = [sin(i) for i in x]
g.addplot("'-' u 1:2 w lines") # include one more plot. '-' is needed if using addplot and adddata
g.adddata(x,y) #add the data
g.write("set title 'Example'") #optional command
g.shoot() #execute the plot
 ```
 
## Installation:
 In general you can just have the module living in your project folder.
 
#### Ubuntu
 Copy the file in :
 /home/user/.local/lib/python2.7/site-packages/
 
## Notes
To keep having the control buttons working on Gnuplot there are two options:
1/ add raw_input() at the end of the script
2/ Run the script using python -i myscript.py

