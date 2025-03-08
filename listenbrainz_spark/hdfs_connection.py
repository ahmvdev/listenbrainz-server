import logging
import os

import hdfs

logger = logging.getLogger(__name__)

logger.info("hdfs contents: %s", dir(hdfs))
client = None


def init_hdfs(namenode_uri, user=None):
    if user is None:
        user = os.environ["USER"]
    global client
    client = hdfs.InsecureClient(namenode_uri, user=user)
