#!/bin/sh

MIGRATIONS_PATH="/app/migrations/versions"

if [ "$DB_RUN_AUTO_MIGRATE" = "True" ]; then
  if [ -d "$MIGRATIONS_PATH" ] && [ "$(ls -A $MIGRATIONS_PATH)" ]; then
    echo "Running Alembic migrations..."
      alembic upgrade head
  else
    echo "No migration files found in $MIGRATIONS_PATH. Skipping migrations."
  fi
else
  echo "Skipping Alembic migrations due to DB_RUN_AUTO_MIGRATE flag."
fi

uvicorn src.main:app --host "0.0.0.0" --port "8000" --log-level "debug" --reload --use-colors
