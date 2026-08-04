from pathlib import Path
from loguru import logger

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

logger.remove()

logger.add(
    LOG_DIR / "alphaedge.log",
    rotation="10 MB",
    retention="30 days",
    level="INFO",
)

logger.add(
    lambda msg: print(msg, end=""),
    level="INFO",
)

log = logger