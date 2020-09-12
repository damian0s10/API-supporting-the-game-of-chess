# REST-API-supporting-the-game-of-chess

 How to run app:
- docker image build -t chess .
- docker run -p 5000:5000 --name chess_app chess

 How to run tests:
- docker exec -it chess_app /bin/bash
- pytest

List of endpoints:
- /api/v1/<chess_figure>/<current_field>: by HTTP GET method -> list of available moves
- /api/v1/<chess_figure>/<current_field>/<destination_field>: by HTTP GET method -> checks if movement is possible
