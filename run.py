from src import create_app, cli

# Checks if the run.py file has executed directly and not imported
if __name__ == '__main__':
    app = create_app()
    cli.register(app)
    app.run(host="localhost", port=8000)