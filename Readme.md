# Websocket ping pong app

## Client
    Client is event function which is endlessly running in asyncio event loop and pings server

## Server
    Server is fastapi's ws endpoint which responses to ping with pong

## How to run
### 1. Build docker images
*make build*

### 2. Run docker containers
*make up*

### 3. Run tests
*make test*
