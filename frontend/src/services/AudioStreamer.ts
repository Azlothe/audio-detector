const CONNECTION = 'ws://localhost:8000/inference/ws';

export const UPDATE_INTERVAL = 3000;

// eslint-disable-next-line @typescript-eslint/no-unsafe-function-type
export const connect = async (messageHandler: Function) : Promise<WebSocket> => {
    const socket = new WebSocket(CONNECTION);

    socket.onopen = () => {
        console.log('WebSocket connection established');
    };

    socket.onmessage = (event) => {
        console.log("Received message:", event.data);
        messageHandler(event.data);
    };

    socket.onerror = (error) => {
        console.error('WebSocket error:', error);
    };

    socket.onclose = () => {
        console.log('WebSocket connection closed');
    };

    return socket;
}