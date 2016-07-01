Create a site that when a user loads it creates a random number between 1-100
and stores the number in session. Allow the user to guess at the number and tell
them when they are too high or too low. If they guess the correct number tell them
and offer to play again.

Front-end:
- 1) Create index.html [x]
- 2) Create <h1>, <p> [x]
- 3) Create input box to take user inupt [x]
- 4) Create button to submit [x]
- 5) Create hidden div to display a too low or too high [x]
- 6) Create hidden div to display correct with correct number included in div, as well as a play again button <p> [x]

Back-end:
- 1) Create server.py file [x]
- 2) from flask import Flask [x]
- 3) Import redirect, session, request, render_template [x]
- 4) add secret_key = [x]
- 5) set up root ('/') route [x]
- 6) Define logic to check number input against number created by random number generator [1/2]
	-Half done, cannot get to reset random number on regeneration of index.html
- 7) Error handling []
