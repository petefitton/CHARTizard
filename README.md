# Sources
-General Tutorial: https://www.freecodecamp.org/news/a-visual-reference-for-d3/
-Scatterplot Tutorial: https://bl.ocks.org/d3noob/a44d21b304b9f7260a284b1883232002
-Making D3 responsive: https://brendansudol.com/writing/responsive-d3
-General SVG scaling knowledge: https://css-tricks.com/scale-svg/
-Resizing Window DOM Manipulation: https://developer.mozilla.org/en-US/docs/Web/API/Window/resize_event
-Regression Line: https://observablehq.com/@hydrosquall/simple-linear-regression-scatterplot-with-d3
-Regression Line(first worked from this link but mostly unused): https://bl.ocks.org/ctufts/298bfe4b11989960eeeecc9394e9f118

## Chartizard Pitch
----
### Elevator Pitch
Single page website that displays beautiful, interactive charts concerning Pokemon.

### User Stories
-  User looking for statistics concerning Pokemon that wants to interact with resplendent charts to view the information in their own way.

### Wireframes

![Wireframe](/img/wireframe.pdf)

### Planning
![Planning PDF](/img/planning.pdf)


### Proposed Architecture

Charts built in D3: D3.JS framework/library will be used to manipulate the DOM to display all aspects of chart(s).  This technology is new to me and will take a large amount of time to learn and manipulate in ways that are aesthetically stellar.

I will write Jupyter notebook scripts and integrate them with the server (refactoring to work within functions). I will be using this dataset:

https://www.kaggle.com/rounakbanik/pokemon

Backend built with Flask: there is only one page displayed, and Python is useful because of the data scripting. I intend design to be one long page with scrolling down from a simple landing area to the chart(s).

Frontend built in HTML/CSS: no real need for complicated styling as charts will be built in D3

### MVP (working list for in class)
 - Single web page that displays one interactive, beautiful chart
 - Mobile First design
 - Stretch goals include creating a second and third chart