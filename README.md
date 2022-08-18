# cameo_python_simulation

This is a Proof Of Concept of calling an HTTP server written in Python from Cameo during simulation.

The application will open a TCP port on localhost and accepts HTTP requests, and sends responses. 
In the model (see model/PythonSimulation.mdzip) we have custom opaque actions that are able to:

- Create a JSON structure
- Send the JSON structure to the server
- Receive and process the response received from the server

This is strictly a proof of concept and not intended to be used directly in a real system.
