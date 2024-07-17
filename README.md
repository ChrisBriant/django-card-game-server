#CARD GAME SERVER

Django project to run a web sockets consumer which will serve a card game

##RUN THE SERVER
uvicorn card_game_server.asgi:application --host 0.0.0.0 --port 8000 --reload
