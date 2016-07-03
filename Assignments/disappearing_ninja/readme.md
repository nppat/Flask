This exercise will help you practice URL routing, using views, and rendering static content. Start by creating a new project called disappearing_ninjas.

These are the routes that you need to set up:
- On the default page ('localhost:5000'), it should display a view that says "No ninjas here" [x]

- When user visits /ninja, it should display all four Ninja Turtles (Leonardo, Michelangelo, Raphael, and Donatello) [x]

- /ninja/[ninja_color], should display the corresponding Ninja Turtle (grab the color parameter out of the requested URL) [x]
	If user visits /ninja/blue, it should only display the Ninja Turtle Leonardo.
	/ninja/orange - Ninja Turtle Michelangelo.
	/ninja/red - Ninja Turtle Raphael
	/ninja/purple - Ninja Turtle Donatello

-If a user tries to hack into your web app by specifying a color or string [x]
	combination other than the colors (Blue, Orange, Red, and Purple),
	example: /ninja/black or /ninja/123, then display Megan Fox who was
	April O'Neil in the most recent ninja turtles movie.