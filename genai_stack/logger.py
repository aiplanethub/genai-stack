import re
import sys
import logging
from typing import Any, Dict


from genai_stack.enums import LoggingLevels
from genai_stack.constants.environment import GENAISTACK_LOGGING_VERBOSITY


class CustomFormatter(logging.Formatter):
    """Formats logs according to custom specifications."""

    grey: str = "\x1b[38;21m"
    pink: str = "\x1b[35m"
    green: str = "\x1b[32m"
    yellow: str = "\x1b[33m"
    red: str = "\x1b[31m"
    cyan: str = "\x1b[1;36m"
    bold_red: str = "\x1b[31;1m"
    purple: str = "\x1b[1;35m"
    reset: str = "\x1b[0m"

    format_template: str = (
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(" "filename)s:%(lineno)d)"
        if LoggingLevels[GENAISTACK_LOGGING_VERBOSITY] == LoggingLevels.DEBUG
        else "%(message)s"
    )

    COLORS: Dict[LoggingLevels, str] = {
        LoggingLevels.DEBUG: grey,
        LoggingLevels.INFO: purple,
        LoggingLevels.WARN: yellow,
        LoggingLevels.ERROR: red,
        LoggingLevels.CRITICAL: bold_red,
    }

    def format(self, record: logging.LogRecord) -> str:
        """Converts a log record to a (colored) string.

        Args:
            record: LogRecord generated by the code.

        Returns:
            A string formatted according to specifications.
        """
        log_fmt = self.COLORS[LoggingLevels(record.levelno)] + self.format_template + self.reset
        formatter = logging.Formatter(log_fmt)
        formatted_message = formatter.format(record)
        quoted_groups = re.findall("`([^`]*)`", formatted_message)
        for quoted in quoted_groups:
            formatted_message = formatted_message.replace(
                "`" + quoted + "`",
                self.reset + self.cyan + quoted + self.COLORS.get(LoggingLevels(record.levelno)),
            )
        return formatted_message


def get_logging_level() -> LoggingLevels:
    """Get logging level from the env variable.

    Returns:
        The logging level.

    Raises:
        KeyError: If the logging level is not found.
    """
    verbosity = GENAISTACK_LOGGING_VERBOSITY.upper()
    if verbosity not in LoggingLevels.__members__:
        raise KeyError(f"Verbosity must be one of {list(LoggingLevels.__members__.keys())}")
    return LoggingLevels[verbosity]


def get_console_handler() -> Any:
    """Get console handler for logging.

    Returns:
        A console handler.
    """
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(CustomFormatter())
    return console_handler


def get_logger(logger_name: str) -> logging.Logger:
    """Main function to get logger name,.

    Args:
        logger_name: Name of logger to initialize.

    Returns:
        A logger object.
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(get_logging_level().value)
    logger.addHandler(get_console_handler())

    logger.propagate = False
    return logger