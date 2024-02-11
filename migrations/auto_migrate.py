import subprocess
import sys


def run_alembic_command():
    alembic_command = ["alembic"]

    if len(sys.argv) > 1:
        alembic_command.extend(sys.argv[1:])
    else:
        alembic_command.extend(["upgrade", "head"])

    subprocess.run(alembic_command, check=True)


if __name__ == "__main__":
    run_alembic_command()
