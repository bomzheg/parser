import logging.config

from app.config.db import load_db_config
from app.models.config import Config
from app.models.config.main import Paths

logger = logging.getLogger(__name__)


def load_config(paths: Paths) -> Config:
    return Config(
        paths=paths,
        db=load_db_config(paths.config_path),
    )
