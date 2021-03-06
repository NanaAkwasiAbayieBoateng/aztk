import argparse
import typing
import time
import aztk.spark
from cli import config, utils, log
from cli.config import JobConfig


def setup_parser(parser: argparse.ArgumentParser):
    parser.add_argument('--id',
                        dest='job_id',
                        required=False,
                        help='The unique id of your Spark Job. Defaults to the id value in .aztk/job.yaml')
    parser.add_argument('--configuration' '-c',
                        dest='job_conf',
                        required=False,
                        help='Path to the job.yaml configuration file. Defaults to .aztk/job.yaml')


def execute(args: typing.NamedTuple):
    spark_client = aztk.spark.Client(config.load_aztk_screts())
    job_conf = JobConfig()

    job_conf.merge(args.job_id, args.job_conf)

    aztk_applications = []
    for application in job_conf.applications:
        aztk_applications.append(
            aztk.spark.models.ApplicationConfiguration(
                name=application.get('name'),
                application=application.get('application'),
                application_args=application.get('application_args'),
                main_class=application.get('main_class'),
                jars=[],
                py_files=[],
                files=[],
                driver_java_options=application.get('driver_java_options'),
                driver_library_path=application.get('driver_library_path'),
                driver_class_path=application.get('driver_class_path'),
                driver_memory=application.get('driver_memory'),
                executor_memory=application.get('executor_memory'),
                driver_cores=application.get('driver_cores'),
                executor_cores=application.get('executor_cores')
            )
        )
    spark_configuration = aztk.spark.models.SparkConfiguration(
        spark_defaults_conf=job_conf.spark_defaults_conf,
        spark_env_sh=job_conf.spark_env_sh,
        core_site_xml=job_conf.core_site_xml
    )
    job_configuration = aztk.spark.models.JobConfiguration(
        id=job_conf.id,
        applications=aztk_applications,
        custom_scripts=job_conf.custom_scripts,
        spark_configuration=spark_configuration,
        vm_size=job_conf.vm_size,
        docker_repo=job_conf.docker_repo,
        max_dedicated_nodes=job_conf.max_dedicated_nodes,
        max_low_pri_nodes=job_conf.max_low_pri_nodes
    )

    #TODO: utils.print_job_conf(job_configuration)
    spark_client.submit_job(job_configuration)
