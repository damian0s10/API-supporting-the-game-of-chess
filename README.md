# REST-API-supporting-the-game-of-chess

# How to run:

- docker image build -t chess .

- docker run -p 5000:5000 --name chess_app chess


# Run tests:
- docker exec -it chess_app /bin/bash
- pytest
