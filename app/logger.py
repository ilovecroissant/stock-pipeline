import logging, sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),          # print to console
        logging.FileHandler("logs/pipeline.log"),   # also write to file
    ]
)
logger = logging.getLogger("stock-pipeline")
