# gppy
python gnuplot binding module

Simple and efficient module to generate gnuplot plots using python.

The module aims to maintain usual gnuplot commands.

## Example:

<pre>
 import gppy<br>
 from math import sin<br>
 g = gppy.gppy()<br>
 x = [i/100. for i in range(0,314)]<br>
 y = [sin(i) for i in x]<br>
 g.addplot("'-' u 1:2 w lines") # include one more plot. '-' is needed if using addplot and adddata<br>
 g.adddata(x,y) #add the data<br>
 g.write("set title 'Example'") #optional command<br>
 g.shoot() #execute the plot<br>
 </pre>
 
## Installation:
 In general you can just have the module living in your project folder.
 
### Ubuntu: 
 Copy the file in :
 /home/user/.local/lib/python2.7/site-packages/

