# Real-Time Deepfake Audio Detector

## Build and Run
Make sure you have the following installed:
- [Docker](https://www.docker.com/)
- [Git](https://git-scm.com/)
- [Node.js](https://nodejs.org/en/)

### Clone and navigate to the project
```
git clone https://github.com/Azlothe/audio-detector.git
cd audio-detector
```

### Set up the backend
```
docker compose up --build
```

### Set up the frontend
```
cd frontend
npm install
npm start
```
### Optional
If you would like to connect your own frontend, configure your WebSockets connection to 
```
'ws://localhost:8000/inference/ws'
```
