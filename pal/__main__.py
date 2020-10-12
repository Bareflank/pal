import sys

from pal.cmd_args import parse_cmd_args
from pal.logger import logger
from pal.writer.writer_factory import make_writer
from pal.generator.generator_factory import make_generators
from pal.runner.runner_factory import make_runners


def pal_main():
    config = parse_cmd_args(sys.argv[1:])
    config.validate()
    logger.set_log_level(config.log_level)

    # A writer handles line-level generation tasks
    writer = make_writer(config)

    # One or more generators handle file and directory-level generation tasks
    generators = make_generators(config, writer)

    # One or more runners handle library-level generation tasks
    runners = make_runners(config)
    for runner in runners:
        runner.run(generators)

pal_main()
