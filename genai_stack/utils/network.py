import socket
from typing import Optional, cast
from urllib.parse import urlparse

from genai_stack.logger import get_logger

logger = get_logger(__name__)

# default scanning port range for allocating ports
SCAN_PORT_RANGE = (8000, 65535)


def port_available(port: int, address: str = "127.0.0.1") -> bool:
    """Checks if a local port is available.

    Args:
        port: TCP port number
        address: IP address on the local machine

    Returns:
        True if the port is available, otherwise False
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            if hasattr(socket, "SO_REUSEPORT"):
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
            else:
                # The SO_REUSEPORT socket option is not supported on Windows.
                # This if clause exists just for mypy to not complain about
                # missing code paths.
                pass
            s.bind((address, port))
    except socket.error as e:
        logger.debug("Port %d unavailable on %s: %s", port, address, e)
        return False

    return True


def find_available_port() -> int:
    """Finds a local random unoccupied TCP port.

    Returns:
        A random unoccupied TCP port.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        _, port = s.getsockname()

    return cast(int, port)


def scan_for_available_port(start: int = SCAN_PORT_RANGE[0], stop: int = SCAN_PORT_RANGE[1]) -> Optional[int]:
    """Scan the local network for an available port in the given range.

    Args:
        start: the beginning of the port range value to scan
        stop: the (inclusive) end of the port range value to scan

    Returns:
        The first available port in the given range, or None if no available
        port is found.
    """
    for port in range(start, stop + 1):
        if port_available(port):
            return port
    logger.debug(
        "No free TCP ports found in the range %d - %d",
        start,
        stop,
    )
    return None
