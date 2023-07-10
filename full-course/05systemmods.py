import os
import logging

logger = logging.getLogger("MAIN")
logging.error("Error happened in the app")
system_info = os.cpu_count
print(system_info)