#!/bin/sh

if [ "$DB_RUN_AUTO_MIGRATE" = "True" ]; then
  echo "Running Alembic migrations..."
  alembic upgrade head
else
  echo "Skipping Alembic migrations..."
fi

uvicorn src.main:app --host "0.0.0.0" --port "8000" --log-level "debug" --reload --use-colors
