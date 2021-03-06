import pickle


class Packet(object):
    def __init__(self, magic_no, p_type, seq_no, data_len, data):
        # Magic number (should be 0x497E)
        self.magic_no = magic_no

        # Packet type must be of dataPacket or acknowledgementPacket
        data_packet = 0
        acknowledgement_packet = 1
        if p_type != data_packet and p_type != acknowledgement_packet:
            raise Exception("Incorrect packet type")
        self.p_type = p_type

        # Sequence value in binary
        self.seq_no = seq_no

        # Data length field, 0 <= x <= 512
        if data_len < 0 or data_len > 512:
            raise Exception("Invalid packet data length")
        self.data_len = data_len

        # Actual packet payload
        self.data = data

        # Checksum made at packet initialisation
        self.checksum = self.magic_no + self.seq_no + self.p_type + self.data_len

    def __str__(self):
        return 'Packet: (MagicNo: {} Type: {} Seq No: {} Data Len: {} Payload: {})'.format(self.get_magic_no(),
                                                                                           self.get_packet_type(),
                                                                                           self.get_packet_sequence_no(),
                                                                                           self.get_data_len(),
                                                                                           self.get_packet_payload())

    def get_magic_no(self):
        return self.magic_no

    def get_packet_type(self):
        # Flag for if connecting packet or final packet (I think??)
        return self.p_type

    def get_packet_sequence_no(self):
        return self.seq_no
    
    def set_data_len(self, val):
        self.data_len = val    

    def get_data_len(self):
        return self.data_len

    def get_packet_payload(self):
        return self.data

    def get_checksum(self):
        return self.checksum


# Helper function to convert packet to bytes
def packet_to_bytes(packetToConvert):
    return pickle.dumps(packetToConvert)


# Helper function to convert bytes to packet
def bytes_to_packet(packetBytes):
    return pickle.loads(packetBytes)


def check_packet_checksum(packetToCheck):
    if (packetToCheck.get_magic_no() + packetToCheck.get_packet_type() + packetToCheck.get_packet_sequence_no()
        + packetToCheck.get_data_len() != packetToCheck.get_checksum()):
        return False
    else:
        return True
    

    
