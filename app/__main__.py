import logging
from pathlib import Path

from app.config import load_config
from app.config.logging_config import setup_logging
from app.models.config.main import Paths
from app.services.foo import foo


logger = logging.getLogger(__name__)


def main():
    paths = Paths(Path(__file__).parent.parent)
    setup_logging(paths)

    config = load_config(paths)

    logger.info("started")

    foo(config)


if __name__ == '__main__':
    main()
