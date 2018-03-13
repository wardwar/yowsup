from yowsup.layers import YowProtocolLayer
from .protocolentities import *
import logging
class YowAckProtocolLayer(YowProtocolLayer):
    def __init__(self):
        handleMap = {
            "ack": (self.recvAckNode, self.sendAckEntity)
        }
        super(YowAckProtocolLayer, self).__init__(handleMap)

    def __str__(self):
        return "Ack Layer"

    def sendAckEntity(self, entity):
        self.entityToLower(entity)

    def recvAckNode(self, node):
        logging.debug(node)
        self.toUpper(IncomingAckProtocolEntity.fromProtocolTreeNode(node))
