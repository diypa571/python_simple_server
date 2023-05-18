#Diyar Parwana, Diypa571

import asyncio
import websockets

# Function to handle incoming WebSocket connections and messages
async def handle_websocket(websocket, path):
    # Print a message when a new connection is established
    print("New WebSocket connection established")

    try:
        # Keep listening for incoming messages from the client
        async for message in websocket:
            # Process the received message
            # Here, you can perform any desired logic on the received message
            # For simplicity, let's just echo the message back to the client
            await websocket.send(message)
    except websockets.exceptions.ConnectionClosedOK:
        # Connection closed by the client
        print("WebSocket connection closed")
    except Exception as e:
        # Handle any other exceptions
        print(f"WebSocket error: {e}")

# Start the WebSocket server
start_server = websockets.serve(handle_websocket, "localhost", 3000)

# Run the server indefinitely
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
