from stem import CircStatus
from stem import CircPurpose
from stem import Signal
from stem.control import Controller

#Connect to control socket on TOR with specified port number
with Controller.from_port(port = 9051) as controller:
    controller.authenticate('16:E0BD65E652CA0F2A60283C691B131B3ED08BA824F10AA484AB6EEE71CC')
    controller.signal(Signal.NEWNYM)
    
    #Get list of active circuits
    for circuit in controller.get_circuits():
    
        #Filter circuit status since FAILED/CLOSED are not of interest. Same for purpose being general
        if circuit.purpose == CircPurpose.GENERAL and circuit.status == CircStatus.BUILT:
        
            #List tuples of the node fingerprint, nickname, and IP address and print them to CL
            relay_fingerprints = [(desc.fingerprint, desc.nickname, desc.address) for desc in controller.get_network_statuses()]
            for node in relay_fingerprints:
                try:
                  print(node[0], node[1], node[2])
                except Exception as exc:
                  print('%s => %s' % (node, exc))
                  
#Some coding assistance from https://stem.torproject.org/tutorials/to_russia_with_love.html