from src import create_app

# Checks if the run.py file has executed directly and not imported
if __name__ == '__main__':
    application = create_app()
    application.run(host="localhost", port=8000)