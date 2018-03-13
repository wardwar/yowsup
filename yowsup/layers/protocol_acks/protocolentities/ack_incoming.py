from yowsup.structs import ProtocolEntity, ProtocolTreeNode
from .ack import AckProtocolEntity
import logging
class IncomingAckProtocolEntity(AckProtocolEntity):

    '''
    <ack t="{{TIMESTAMP}}" from="{{FROM_JID}}" id="{{MESSAGE_ID}}" class="{{message | receipt | ?}}">
    </ack>


    '''

    def __init__(self, _id, _class = None, _from = None, timestamp = None):
        super(IncomingAckProtocolEntity, self).__init__(_id, _class)
        self.setIncomingData(_from, timestamp)

    def setIncomingData(self ,_from = None, timestamp = None):
        self._from = _from
        self.timestamp = timestamp
    
    def toProtocolTreeNode(self):
        node = super(IncomingAckProtocolEntity, self).toProtocolTreeNode()
        if(self._from is not None):
            node.setAttribute("from", self._from)
            node.setAttribute("t", self.timestamp)
        return node

    def __str__(self):
        out  = super(IncomingAckProtocolEntity, self).__str__()
        if(self._from is not None):
            out += "From: %s\n" % self._from
            out += "timestamp: %s\n" % self.timestamp
        return out

    @staticmethod
    def fromProtocolTreeNode(node):
        logging.debug("ACK FROM PROTOCOL TREE NODE")
        logging.debug(node)
        logging.debug("-------------------------")
        entity = AckProtocolEntity.fromProtocolTreeNode(node)
        entity.__class__ = IncomingAckProtocolEntity
        entity.setIncomingData(
                node.getAttributeValue("from"),
                node.getAttributeValue("t")
        )
        return entity
