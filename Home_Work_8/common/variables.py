import logging

DEFAULT_PORT = 7777

DEFAULT_IP_ADDRESS = '127.0.0.1'

MAX_CONNECTIONS = 5

MAX_PACKAGE_LENGTH = 1024

ENCODING = 'utf-8'

LOGGING_LEVEL = logging.DEBUG

ACTION = 'action'
TIME = 'time'
USER = 'user'
ACCOUNT_NAME = 'account_name'
EXIT = 'exit'
DESTINATION = 'to'

SENDER = 'sender'

PRESENCE = 'presence'
RESPONSE = 'response'
ERROR = 'error'
RESPONDEFAULT_IP_ADDRESSSE = 'respondefault_ip_addressse'
MESSAGE = 'message'
MESSAGE_TEXT = 'mess_text'

RESPONSE_200 = {RESPONSE: 200}
RESPONSE_400 = {
    RESPONSE: 400,
    ERROR: None
}
