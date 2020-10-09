#
# This simply sends monitored udp packets to specified destination
# (ipaddress, udp port)
#
import packethandler
import socket
import sys


PSM_IP = "10.10.6.3"
Port = 5470

DESTINATION = (PSM_IP, Port)


class UDPTransporterPacketHandler(packethandler.UDPPacketHandler):
	def __init__(self, path):
		packethandler.PacketHandler.__init__(self, path)
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		print("Staring Custom Snooper")
	def handle_udpdata(self, data, props):
		#print "Sending to PSM %s %d " % (PSM_IP , Port)
		self.socket.sendto(data, DESTINATION)
		
ph = UDPTransporterPacketHandler(sys.argv[1])
ph.run()