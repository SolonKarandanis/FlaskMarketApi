from src import app

# Checks if the run.py file has executed directly and not imported
if __name__ == '__main__':
    app.run(host="localhost", port=8000)