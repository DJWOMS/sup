import os
import subprocess


def run_alembic_command(command):
    alembic_versions_path = "/app/migrations/versions"
    if not os.path.exists(alembic_versions_path):
        os.makedirs(alembic_versions_path)
    subprocess.run(f"python -m alembic {command}", shell=True, check=True)
