import os

"""
    DOCKER
"""
DEFAULT_DOCKER_REPO = "aztk/base:spark2.2.0"
DEFAULT_DOCKER_REPO_GPU = "aztk/gpu:spark2.2.0"
DOCKER_SPARK_CONTAINER_NAME = "spark"

# DOCKER SPARK
DOCKER_SPARK_WEB_UI_PORT = 8080
DOCKER_SPARK_WORKER_UI_PORT = 8081
DOCKER_SPARK_RSTUDIO_SERVER_PORT = 8787
DOCKER_SPARK_JUPYTER_PORT = 8888
DOCKER_SPARK_JOB_UI_PORT = 4040
DOCKER_SPARK_JOB_UI_HISTORY_PORT = 18080
DOCKER_SPARK_HOME = "/home/spark-current"

# DOCKER HDFS
DOCKER_SPARK_NAMENODE_UI_PORT = 50070

"""
    Root path of this repository
"""
ROOT_PATH = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..'))

"""
    User home directory path
"""
HOME_DIRECTORY_PATH = os.path.expanduser('~')

"""
    Path to the secrets file
"""
DEFAULT_SECRETS_PATH = os.path.join(os.getcwd(), '.aztk/secrets.yaml')

"""
    Paths to the cluster configuration files
"""
GLOBAL_CONFIG_PATH = os.path.join(HOME_DIRECTORY_PATH, '.aztk')
DEFAULT_SSH_CONFIG_PATH = os.path.join(os.getcwd(), '.aztk/ssh.yaml')
DEFAULT_CLUSTER_CONFIG_PATH = os.path.join(os.getcwd(), '.aztk/cluster.yaml')
DEFAULT_SPARK_CONF_SOURCE = os.path.join(os.getcwd(), '.aztk')
DEFAULT_SPARK_CONF_DEST = os.path.join(ROOT_PATH, 'node_scripts', 'conf')
DEFAULT_SPARK_JARS_SOURCE = os.path.join(os.getcwd(), '.aztk', 'jars')
DEFAULT_SPARK_JARS_DEST = os.path.join(ROOT_PATH, 'node_scripts', 'jars')
DEFAULT_SPARK_JOB_CONFIG = os.path.join(os.getcwd(), '.aztk', 'job.yaml')
GLOBAL_SPARK_JOB_CONFIG = os.path.join(HOME_DIRECTORY_PATH, '.aztk', 'job.yaml')

CUSTOM_SCRIPTS_DEST = os.path.join(ROOT_PATH, 'node_scripts', 'custom-scripts')

"""
    Source and destination paths for spark init
"""
INIT_DIRECTORY_SOURCE = os.path.join(ROOT_PATH, 'config')
LOCAL_INIT_DIRECTORY_DEST = os.path.join(os.getcwd(), '.aztk')
GLOBAL_INIT_DIRECTORY_DEST = os.path.join(HOME_DIRECTORY_PATH, '.aztk')

"""
    Key of the metadata entry for the pool that is used to store the master node id
"""
MASTER_NODE_METADATA_KEY = "_spark_master_node"

"""
    Timeout in seconds to wait for the master to be ready
    Value: 20 minutes
"""
WAIT_FOR_MASTER_TIMEOUT = 60 * 20


AZTK_SOFTWARE_METADATA_KEY = "_aztk_software"

TASK_WORKING_DIR = "wd"
SPARK_SUBMIT_LOGS_FILE = "output.log"
