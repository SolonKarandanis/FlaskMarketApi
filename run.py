from src import create_app, cli, ext_celery

# Checks if the run.py file has executed directly and not imported
if __name__ == '__main__':
    app = create_app()
    celery = ext_celery.celery
    cli.register(app)
    app.run(host="localhost", port=8000)