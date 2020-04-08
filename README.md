# Sources
-General Tutorial: https://www.freecodecamp.org/news/a-visual-reference-for-d3/
-Scatterplot Tutorial: https://bl.ocks.org/d3noob/a44d21b304b9f7260a284b1883232002
-Making D3 responsive: https://brendansudol.com/writing/responsive-d3
-General SVG scaling knowledge: https://css-tricks.com/scale-svg/
-Resizing Window DOM Manipulation: https://developer.mozilla.org/en-US/docs/Web/API/Window/resize_event
-Regression Line: https://observablehq.com/@hydrosquall/simple-linear-regression-scatterplot-with-d3
-Regression Line(first worked from this link but mostly unused): https://bl.ocks.org/ctufts/298bfe4b11989960eeeecc9394e9f118
-Data Filtering in D3: https://www.d3-graph-gallery.com/graph/basic_datamanipulation.html
-Type Color for Pokemon: https://bulbapedia.bulbagarden.net/wiki/Category:Type_color_templates
-Tooltip: https://stackoverflow.com/questions/29357160/add-tooltip-to-d3-scatter-plot
-Tooltip arrow: https://www.w3schools.com/css/css_tooltip.asp
-Tooltip Example: http://bl.ocks.org/williaster/af5b855651ffe29bdca1
-Tooltip Simple Example: https://bl.ocks.org/mbostock/1087001
-getBoundingClientRent Method: https://stackoverflow.com/questions/21990857/d3-js-how-to-get-the-computed-width-and-height-for-an-arbitrary-element
-Dropdown: https://stackoverflow.com/questions/39964570/how-to-filter-data-with-d3-js
-Dropdown Simple Example: http://plnkr.co/edit/HwzD4SpROPyjsW0REkfJ?p=preview&preview
-Enter, Exit, Update, and Join Explained: https://www.d3indepth.com/enterexit/
-Selection Explained: https://bost.ocks.org/mike/selection/
-Enter, Exit, and Update Example: https://bl.ocks.org/NGuernse/9e4b5232394d853bd76d94bde102fa9c
-Enter, Exit, and Update Example: http://bl.ocks.org/alansmithy/e984477a741bc56db5a5
-Data Filtering with Enter, Exit, and Update: https://stackoverflow.com/questions/39964570/how-to-filter-data-with-d3-js
-JS Array Destructuring/Tuple Usage: https://stackoverflow.com/questions/4512405/javascript-variable-assignments-from-tuples
-Blur for better UX with Dropdown Menus in conjunction with tooltips: https://stackoverflow.com/questions/16779247/how-to-force-to-lose-focus-of-all-fields-in-a-form-in-jquery
-Adding background to text inside an SVG: https://bl.ocks.org/uicoded/dec8786d89184c88fa8f2c0abcdc152d
-Adding background to text inside an SVG: https://stackoverflow.com/questions/15500894/background-color-of-text-in-svg



## Chartizard Pitch
----
### Elevator Pitch
Single page website that displays beautiful, interactive charts concerning Pokemon.

### User Stories
-  User looking for statistics concerning Pokemon that wants to interact with resplendent charts to view the information in their own way.

### Wireframes

![Wireframe](/img/wireframe.jpg)

### Planning
![Planning PDF](/img/planning.jpg)


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