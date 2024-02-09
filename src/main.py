import uvicorn

from src.app.config.project_config import settings as main_settings

from src.app import get_application
from migrations.auto_migrate import run_alembic_command

run_alembic_command("upgrade head")


app = get_application()

if __name__ == "__main__":
    uvicorn.run("main:app", host=main_settings.host, port=main_settings.port, reload=main_settings.debug)
