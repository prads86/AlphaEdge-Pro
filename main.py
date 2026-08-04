from app.config.settings import config
from app.utils.logger import log


def main():
    log.info("=" * 50)
    log.info("Starting AlphaEdge Pro...")
    log.info(f"Application Name: {config['app']['name']}")
    log.info(f"Version: {config['app']['version']}")
    log.info("System initialized successfully.")
    log.info("=" * 50)


if __name__ == "__main__":
    main()