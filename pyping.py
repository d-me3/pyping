#####################################################################################
# Python script to monitor internet lost packets
# Output saved to a CSV file
# Copyright (C) 2020-2021 Dimitri Souza
# https://github.com/dd-me3/pyping
#####################################################################################
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License v3 as published by
# the Free Software Foundation.
#####################################################################################
   

import icmplib
import time,datetime
import os
import math
#import sys


#------------------------------------------------------------------------------
# Ping Globals
#------------------------------------------------------------------------------
#gblPingTarget = "127.0.0.1"
gblPingTarget = "8.8.8.8"
#gblPingTarget = "1.1.1.1"
gblTotalSentPackets = 0
gblTotalReceivedPackets = 0
gblTotalLostPackets = 0
gblTotalErrors = 0
gblSeqLostPackets = 0
gblTimeTotal = 0
gblTimeAvg = 0
glbLastResponseTime = 0
glbMaxResponseTime = 0
gblTotalAboveAvg = 0

#------------------------------------------------------------------------------

def printData():
    global gblPingTarget
    global gblTotalSentPackets
    global gblTotalLostPackets
    global gblSeqLostPackets
    global glbLastResponseTime
    global glbMaxResponseTime
    global gblTotalAboveAvg

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    totalPctLost = gblTotalLostPackets/gblTotalSentPackets*100
    totalPctAboveAvg = gblTotalAboveAvg/gblTotalSentPackets*100

    print ("{:s},{:s},{:d},{:d},{:d},{:.2f},{:.1f},{:.1f},{:.1f},{:d},{:.2f}    ".format(timestamp,gblPingTarget,gblTotalSentPackets,gblTotalLostPackets,gblSeqLostPackets,totalPctLost,gblTimeAvg,glbLastResponseTime,glbMaxResponseTime,gblTotalAboveAvg,totalPctAboveAvg))

#------------------------------------------------------------------------------

def pingTarget():
    global gblPingTarget
    global gblTotalSentPackets
    global gblTotalReceivedPackets
    global gblTotalLostPackets
    global gblTotalErrors
    global gblSeqLostPackets
    global gblTimeTotal
    global gblTimeAvg
    global glbLastResponseTime
    global glbMaxResponseTime
    global gblTotalAboveAvg

    socket = icmplib.ICMPv4Socket()

    # Create an ICMP request
    request = icmplib.ICMPRequest(destination=gblPingTarget,id=0,sequence=1,timeout=1)

    roundTripTime = -1
    glbLastResponseTime = -1
    try:
        # Send the request
        gblTotalSentPackets = gblTotalSentPackets + 1
        socket.send(request)

        # Wait for ICMP reply
        reply = socket.receive()

        # Throw an exception if it is an ICMP error message
        reply.raise_for_status()

        roundTripTime = (reply.time - request.time) * 1000
        glbLastResponseTime = roundTripTime
        if roundTripTime > glbMaxResponseTime:
            glbMaxResponseTime = roundTripTime

        gblTotalReceivedPackets = gblTotalReceivedPackets + 1

        gblTimeTotal = gblTimeTotal + roundTripTime
        gblTimeAvg = gblTimeTotal / gblTotalReceivedPackets

        if gblSeqLostPackets > 0: # Print information only after a sucessfull ping after one or more timedout packets
            printData()
            gblSeqLostPackets = 0
        elif roundTripTime > (2.5*gblTimeAvg): # Else print information when there is a packet with a higher than normal response time
            gblTotalAboveAvg = gblTotalAboveAvg + 1
            printData()



    except icmplib.TimeoutExceeded:
        gblTotalLostPackets = gblTotalLostPackets + 1
        gblSeqLostPackets = gblSeqLostPackets + 1

    except icmplib.ICMPError as err:
        gblTotalErrors = gblTotalErrors + 1

    except icmplib.ICMPLibError:
        gblTotalErrors = gblTotalErrors + 1

#------------------------------------------------------------------------------

try:
    #print (sys.argv)
    #if len(sys.argv) != 2:
    #    print ("Usage: pyping { IP Address | hostname }")
    #    quit ()
    print ("timestamp,address,totalSentPackets,totalLostPackets,seqLostPackets,totalPctLost,avgResponseTime,lastResponseTime,maxResponseTime,totalHighResponseTime,totalPctAboveAvg")
    while True:
        pingTarget()
        time.sleep(1)
except KeyboardInterrupt:
    # Cornercase - print at least one line of information even if no packet was lost
    printData()
    pass


