from pprint import pprint

from app.utils.logger import log
from app.brokers.zerodha_service import ZerodhaService


def main():

    log.info("=" * 60)
    log.info("Starting AlphaEdge Pro")
    log.info("=" * 60)

    broker = ZerodhaService()

    profile = broker.profile()

    log.info("Connected successfully.\n")

    pprint(profile)


if __name__ == "__main__":
    main()