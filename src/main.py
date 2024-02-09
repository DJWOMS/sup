import uvicorn

from src.app.config.project_config import settings as main_settings
from src.app.config.db_config import settings as db_settings

from src.app import get_application
from migrations.auto_migrate import run_alembic_command

app = get_application()

if db_settings.db_run_auto_migrate:
    run_alembic_command("upgrade head")


if __name__ == "__main__":
    uvicorn.run("main:app", host=main_settings.host, port=main_settings.port, reload=main_settings.debug)
