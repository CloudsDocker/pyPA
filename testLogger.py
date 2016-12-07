
import logging
import time

logging.basicConfig(filename=r'0-defaultFile.log',level=logging.DEBUG)

logger=logging.getLogger(__name__)

logging.warning("----------------this use logging object-----------------")
logger.warning("----------------this use logger object-----------------")
logger.debug("---- this not working, as default level is warn-----")

logger.debug("------ this debug log will work as setup logging level-------")
logger.warning("------ this debug log will work as setup logging level, warning-------")
print("hello python\n")
