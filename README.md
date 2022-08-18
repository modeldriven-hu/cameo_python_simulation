# Accessing a server written in Python from Cameo activity diagram simulation

## Problem statement

During simulation some members of the Systems Engineering Professionals Discord server realized that although it is possible to create an opaque action containing Python code in Cameo, but they are unable to use external libraries (like numpy). We came up with an idea how to solve this problem: create a separate application in Python exposing an HTTP interface and write custom opaque actions in Cameo for communication purposes.

## Explanation

This is a Proof Of Concept of calling an HTTP server written in Python from Cameo during simulation.

The application will open a TCP port on localhost and accepts HTTP requests, and sends responses. 
In the model (see model/PythonSimulation.mdzip) we have custom opaque actions that are able to:

- Create a JSON structure
- Send the JSON structure to the server
- Receive and process the response received from the server

This is strictly a proof of concept and not intended to be used directly in a real system.

## Installation

Requirements:

 - Python latest
 - PIP latest
 
Execute the following commands:

- `pip install -r requirements.txt` to install all the requirements
- `python app.py` to start the application

To check whether the application is running, enter `http://localhost:5000/` in your browser and see the response.
