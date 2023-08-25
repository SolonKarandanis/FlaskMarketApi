from src import create_app

# Checks if the run.py file has executed directly and not imported
if __name__ == '__main__':
    app = create_app()
    app.run(host="localhost", port=8000)