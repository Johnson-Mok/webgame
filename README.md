# webgame

## Build and Containerize the Web Game
To containerize and deploy the game on the web, you'll need to have **Docker Desktop** installed and running. If you'd like to debug the container during development, you can optionally install the **Docker extension** for additional debugging capabilities.

### Steps to Build the Container:
1. **Ensure Docker is Running**: Make sure Docker Desktop is up and running before proceeding.
2. **Make the `run.sh` Script Executable** (if necessary): If you encounter issues running the `run.sh` script, check if it's executable. You can make it executable by running the following command in your bash terminal:
```bash
chmod +x run.sh
```
3. **Build the Docker Container**: Once everything is set, you can build the container by executing the `run.sh` script: 
```bash
./run.sh
```

## Backlog

### Features 
- [x] Create front end
- [x] Make the app deployable on docker (WIP run.sh and Dockerfile). To run use the git bash terminal and execute './run.sh'

### Enhancements
- [ ] Insert new questions

### Technical Debt
- [ ]