from enum import Enum


class PeerStatus(str,Enum):
    """
    Represents status of a peer node
    """
    ONLINE = "online"
    OFFLINE = "offline"
    WRONG_RESPONSE = "wrong response"
