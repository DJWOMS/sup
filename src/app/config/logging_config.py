from pydantic import Field

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    logging_on: bool = Field(default=True, alias="LOGGING_ON")
    logging_level: str = Field(default="DEBUG", alias="LOGGING_LEVEL")
    logging_json: bool = Field(default=True, alias="LOGGING_JSON")

    @property
    def log_config(self) -> dict:
        config = {
            "loggers": {
                "uvicorn": {"handlers": ["default"], "level": self.logging_level, "propagate": False},
                "sqlalchemy": {"handlers": ["default"], "level": self.logging_level, "propagate": False},
            }
        }
        return config


def make_logger_conf(*confs, log_level, json_log):
    fmt = "%(asctime)s.%(msecs)03d [%(levelname)s]|[%(name)s]: %(message)s"
    datefmt = "%Y-%m-%d %H:%M:%S"
    config = {
        "version": 1,
        "disable_existing_loggers": True,
        "formatters": {
            "default": {
                "format": fmt,
                "datefmt": datefmt,
            },
            "json": {"format": fmt, "datefmt": datefmt, "class": "pythonjsonlogger.jsonlogger.JsonFormatter"},
        },
        "handlers": {
            "default": {
                "level": log_level,
                "formatter": "json" if json_log else "default",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
            },
        },
        "loggers": {
            "": {"handlers": ["default"], "level": log_level, "propagate": False},
        },
    }
    for conf in confs:
        for key in conf.keys():
            config[key].update(conf[key])

    return config


settings = Settings()
logger_config = make_logger_conf(
    settings.log_config,
    log_level=settings.logging_level,
    json_log=settings.logging_json
)
