import argparse
import typing
import aztk.spark
from cli import log
from cli import utils, config


def setup_parser(parser: argparse.ArgumentParser):
    parser.add_argument('--id', dest='cluster_id', required=True,
                        help='The unique id of your spark cluster')
    parser.add_argument('-u', '--username',
                        help='The usernameto access your spark cluster\'s head node')

    auth_group = parser.add_mutually_exclusive_group()
    auth_group.add_argument('-p', '--password',
                            help="The password to access your spark cluster's master node. If not provided will use ssh public key.")
    auth_group.add_argument('--ssh-key',
                            help="The ssh public key to access your spark cluster's master node. You can also set the ssh-key in the configuration file.")
    parser.set_defaults(username="admin")


def execute(args: typing.NamedTuple):
    spark_client = aztk.spark.Client(config.load_aztk_screts())

    log.info('-------------------------------------------')
    log.info('spark cluster id:    {}'.format(args.cluster_id))
    log.info('username:            {}'.format(args.username))
    log.info('-------------------------------------------')

    if args.ssh_key:
        ssh_key = args.ssh_key
    else:
        ssh_key = spark_client.secrets_config.ssh_pub_key

    ssh_key, password = utils.get_ssh_key_or_prompt(ssh_key, args.username, args.password, spark_client.secrets_config)

    spark_client.create_user(
        cluster_id=args.cluster_id,
        username=args.username,
        password=password,
        ssh_key=ssh_key
    )

    if password:
        log.info('password:            %s', '*' * len(password))
    elif ssh_key:
        log.info('ssh public key:      %s', ssh_key)

    log.info('-------------------------------------------')
