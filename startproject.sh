#!/bin/bash
path="path" # direct path of the parent directory of your project

cd $path
code .

# Open first Terminal and Start server side
gnome-terminal --window --title="server" -- bash -c 'cd server && npm start; exec bash'
# my start script has nodemon index.js so npm start is used
# you can use nodemon index.js directly

# Open the second terminal and start client side
gnome-terminal --window --title="client" -- bash -c 'cd client && npm start; exec bash'
