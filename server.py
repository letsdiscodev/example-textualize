from textual_serve.server import Server

server = Server(
    "python -m textual",
    host="0.0.0.0",
    port=8000,
    public_url="https://textual.greg.technology",
)
server.serve()
