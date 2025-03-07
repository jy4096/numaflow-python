import logging
import os
from enum import Enum

from pynumaflow import setup_logging

SIDE_INPUT_DIR_PATH = "/var/numaflow/side-inputs"

# Socket configs
MAP_SOCK_PATH = "/var/run/numaflow/map.sock"
MAP_STREAM_SOCK_PATH = "/var/run/numaflow/mapstream.sock"
REDUCE_SOCK_PATH = "/var/run/numaflow/reduce.sock"
SOURCE_TRANSFORMER_SOCK_PATH = "/var/run/numaflow/sourcetransform.sock"
SINK_SOCK_PATH = "/var/run/numaflow/sink.sock"
SIDE_INPUT_SOCK_PATH = "/var/run/numaflow/sideinput.sock"
SOURCE_SOCK_PATH = "/var/run/numaflow/source.sock"
MULTIPROC_MAP_SOCK_PORT = 55551
MULTIPROC_MAP_SOCK_ADDR = "0.0.0.0"

# Server information file configs
MAP_SERVER_INFO_FILE_PATH = "/var/run/numaflow/mapper-server-info"
MAP_STREAM_SERVER_INFO_FILE_PATH = "/var/run/numaflow/mapstreamer-server-info"
REDUCE_SERVER_INFO_FILE_PATH = "/var/run/numaflow/reducer-server-info"
SOURCE_TRANSFORMER_SERVER_INFO_FILE_PATH = "/var/run/numaflow/sourcetransformer-server-info"
SINK_SERVER_INFO_FILE_PATH = "/var/run/numaflow/sinker-server-info"
SIDE_INPUT_SERVER_INFO_FILE_PATH = "/var/run/numaflow/sideinput-server-info"
SOURCE_SERVER_INFO_FILE_PATH = "/var/run/numaflow/sourcer-server-info"

# TODO: need to make sure the DATUM_KEY value is the same as
# https://github.com/numaproj/numaflow-go/blob/main/pkg/function/configs.go#L6
WIN_START_TIME = "x-numaflow-win-start-time"
WIN_END_TIME = "x-numaflow-win-end-time"
MAX_MESSAGE_SIZE = 1024 * 1024 * 64
# TODO: None instead of "EOF" ?
STREAM_EOF = "EOF"
DELIMITER = ":"
DROP = "U+005C__DROP__"

_PROCESS_COUNT = os.cpu_count()
MAX_THREADS = int(os.getenv("MAX_THREADS", "4"))

_LOGGER = setup_logging(__name__)
if os.getenv("PYTHONDEBUG"):
    _LOGGER.setLevel(logging.DEBUG)


class UDFType(str, Enum):
    """
    Enumerate the type of UDF.
    """

    Map = "map"
    Reduce = "reduce"
    Sink = "sink"
    Source = "source"
    SideInput = "sideinput"
    SourceTransformer = "sourcetransformer"
