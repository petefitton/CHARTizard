# Deployed Website

Live Website can be found here:

# Screenshots

![Landing Page Screenshot](/img/screenshots/Landing.png)
![Splash Page Screenshot](/img/screenshots/Splash.png)
![Splash Page Screenshot](/img/screenshots/Splash2.png)
![Chart Screenshot](/img/screenshots/Chart.png)
![Chart Screenshot](/img/screenshots/Chart2.png)
![Chart Screenshot](/img/screenshots/Chart3.png)
![Chart Screenshot](/img/screenshots/Chart4.png)
![Footer Screenshot](/img/screenshots/Footer.png)


# Technologies Used

The primary technology used in this project was D3.JS, a framework/library that manipulates the DOM.  This technology requires understanding its set of built-in methods in order to develop charts beyond something simple and static.

I initially explored the dataset with Jupyter notebook scripts and tested serving the index.html file with a simple script that had been integrated into the project. I decided that the actual filtering and data manipulation would be more better handled with javacsript as that allowed me to focus more on learning D3 instead of spreading myself too thin with additional technologies/skills.

The server was built with Flask. I have implemented a landing page that displays a warning for users who may have photosensitive epilepsy. This page allows user interaction to bring you to the main page of the site. I designed this page to be one long page with a splash page section, chart section, and footer.

The frontend beyond D3 was built with basic HTML/CSS.

I also used Photosensitive Epilepsy Analysis Tool to test for the potential to trigger photosensitive epilepsy episodes.  The analysis showed that the site is used, but I opted to continue displaying a warning to be extra careful.  The tool is available for free here: https://trace.umd.edu/peat


# General Approach to Project/Reflection

I originally intended to collaborate with a data scientist on this project; however, he got very sick around the time that I was beginning this project, so I had to reassess the handling of the data for this project.  I went ahead and spent some time exploring the data inside of a Jupyter notebook with Pandas and tested integrating some data processing inside of my flask server.  I decided that I would adjust my plan to process the data inside of the d3 files with Javascript rather than with Pandas and Python.

I found learning D3 to be more difficult than I anticipated.  I knew that it had somewhat of a reputation for being hard to learn, but one particular challenge I faced was dealing with tutorials and examples written with D3 versions 3 and 4. Some parts of the code in those examples work with v5 of D3 (which is what I used), but oftentimes the specific part that I was looking for would not.  It did give me the opportunity to learn D3 a little bit more in depth as I would often seek out understanding from the documentation to see what methods/functionality were listed in v5 and learned more about those pieces as a result.

I also spent a bit more time on the design of this website than on previous projects, specifically on animation.  I think the animations very quickly improved the quality of the user experience for this site.  I recognized as well that there would be a potential problem for those with photosensitive epilepsy, so I created a warning page on entry to the site.  I also specifically crafted the animations to be softer in order to mitigate potential seizures.  I used PEAT to test the website and confirmed that the site should be safe to use in that regard.

# Dependencies

See requirements.txt file for pip modules needed to run this project
See also runtime.txt file for version of python3 used in deployment


# Sources

-Splash Image: https://i.redd.it/gqnzk6788v411.png https://www.reddit.com/r/wimmelbilder/comments/8s55wz/pokemon_color_spectrum_featuring_all_pokemon_in/
-Charizard Image: https://cdn.weasyl.com/static/media/52/67/7f/52677ffe59d86ec32b87cd11ea45ce45e15ec6fb855237776c922b45ac02214b.png


-D3 Documentation: https://github.com/d3/d3/blob/master/API.md
-D3 Github: https://github.com/d3
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
-Checkboxes in D3: https://bl.ocks.org/johnnygizmo/3d593d3bf631e102a2dbee64f62d9de4
-Grid in D3: https://observablehq.com/@d3/scatterplot-with-shapes
-Using JS to manipulate colors: https://css-tricks.com/converting-color-spaces-in-javascript/
-Darken/Lighten colors in JS: https://jonlabelle.com/snippets/view/javascript/lighten-and-darken-colors-in-javascript
-Text color gradient: https://stackoverflow.com/questions/37831837/gradient-text-color
-CSS arrow: https://www.w3schools.com/howto/howto_css_arrows.asp
-Skew and scaleY: https://codepen.io/Mihnutzen/pen/EvpwF
-Scroll behavior smooth: https://stackoverflow.com/questions/7717527/smooth-scrolling-when-clicking-an-anchor-link
-D3 join: https://observablehq.com/@d3/selection-join
-D3 join: https://github.com/d3/d3-selection/blob/v1.4.1/README.md#joining-data
-D3 update pattern: https://www.dashingd3js.com/lessons/d3-basic-general-update-pattern
-D3 example regression line animation: https://bl.ocks.org/ctufts/674ece47de093f6e0cd5af22d7ee9b9b
-Simple Statistics Documentation: https://simplestatistics.org/docs/#linearregression
-Axis transition Example: https://bl.ocks.org/HarryStevens/678935d06d4601c25cb141bacd4068ce
-Scroll event Documentation: https://developer.mozilla.org/en-US/docs/Web/API/Document/scroll_event
-CSS Animation Documentation: https://www.w3schools.com/css/css3_animations.asp
-CSS Animation Documentation: https://drafts.csswg.org/css-animations/
-Example of scrolling color gradient: https://codepen.io/nohoid/pen/kIfto
-Seizure Warning example: https://en.wikipedia.org/wiki/Template:Seizure_warning
-Force Landscope Mode on Mobile: https://stackoverflow.com/questions/14360581/force-landscape-orientation-mode
-Frozen Flask Deployment Issue: https://www.reddit.com/r/flask/comments/335cyi/a_problem_with_frozenflask/
-Simple Deployment Ex with Flask, Frozen-Flask, and Netlify: https://medium.com/@francescaguiducci/how-to-build-a-simple-personal-website-with-python-flask-and-netlify-d800c97c283d
-PEAT: https://trace.umd.edu/peat


# Chartizard Pitch
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

Chart built in D3: D3.JS framework/library will be used to manipulate the DOM to display all aspects of chart.  This technology is new to me and will take a large amount of time to learn and manipulate in ways that are aesthetically stellar.

I will explore the dataset with Jupyter notebook scripts. I will perform actual filtering and data manipulation with javacsript and will be using this dataset:

https://www.kaggle.com/rounakbanik/pokemon

Backend built with Flask: there is only one page displayed, and Python is useful because of the data scripting. I intend design to be one long page with scrolling down from a simple landing area to the chart(s).

Frontend built in HTML/CSS: no real need for complicated styling as charts will be built in D3

### MVP (working list for in class)
 - Single web page that displays one interactive, beautiful chart
 - Mobile First design
 - Stretch goals include creating a second chart