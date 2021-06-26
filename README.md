# pyping

`pyping` is a simple python script to report lost packets of an internet connection in CSV format. If the output is redirected to a CSV file, Excel Pivot Charts can later be used to analyze data.

There are no command line parameters. The target ping address must be edited in the source code (default target IP is Google DNS - 8.8.8.8).

**Only lost packets** and **packets with a response time over 2.5 times the average** are logged.

## Requirements

1. A PC or device running Linux (it may work on Windows but it was not tested). The commands below were tested on Raspberry Pi OS

2. Install or update `python3`
```
sudo apt install python3
```

3. Install or update `pip3`
```
sudo apt install python3-pip
```

4. Install python library `icmplib`
```
sudo pip3 install icmplib
```

5. Edit `pyping.py` and put the target ping address in the variable `gblPingTarget`
```
(...)
gblPingTarget = "8.8.8.8"
(...)
```

## Usage examples

1. `sudo python3 -u ./pyping.py > outputfile.csv" &`

2. `sudo python3 -u ./pyping.py > "$(pwd -P)/$(date +"%Y%m%d-%H%M").csv" &`

## Output Columns (CSV format)

**Only lost packets** and **packets with a response time over 2.5 times the average** events are logged.

### Columns

1. **timestamp**: timestamp of the logged event in the format yyyy-dd-mm hh:mm:ss

2. **address**: ping target IP address (as configured in the variable `gblPingTarget`)

3. **totalSentPackets**: total number of sent packets

4. **totalLostPackets**: total number of lost packets

5. **seqLostPackets**: number of lost packets in a row

6. **totalPctLost**: total percent of lost packets

7. **avgResponseTime**: average response time in milliseconds

8. **lastResponseTime**: response time of last received packet before the event in milliseconds

9. **maxResponseTime**: maximum response time in milliseconds

10. **totalHighResponseTime**: total number of packets with the response time above 2.5 times the average response time

11. **totalPctAboveAvg**: total percent of packets with a response time above 2.5 times the average

### Example:

```
timestamp,address,totalSentPackets,totalLostPackets,seqLostPackets,totalPctLost,avgResponseTime,lastResponseTime,maxResponseTime,totalHighResponseTime,totalPctAboveAvg
2021-06-11 08:58:15,8.8.8.8,1381,1,1,0.07,11.5,12.2,35.5,0,0.00    
2021-06-11 08:58:35,8.8.8.8,1399,2,1,0.14,11.5,14.2,35.5,0,0.00    
2021-06-11 08:59:22,8.8.8.8,1443,3,1,0.21,11.5,11.3,35.5,0,0.00    
2021-06-11 08:59:31,8.8.8.8,1450,4,1,0.28,11.5,15.9,35.5,0,0.00    
2021-06-11 08:59:45,8.8.8.8,1460,6,2,0.41,11.5,21.7,35.5,0,0.00    
2021-06-11 08:59:50,8.8.8.8,1463,7,1,0.48,11.5,17.0,35.5,0,0.00    
2021-06-11 08:59:58,8.8.8.8,1469,8,1,0.54,11.5,12.8,35.5,0,0.00    
2021-06-11 09:00:03,8.8.8.8,1474,8,0,0.54,11.7,250.6,250.6,1,0.07    
2021-06-11 09:00:19,8.8.8.8,1488,9,1,0.60,11.7,12.5,250.6,1,0.07    
2021-06-11 09:02:36,8.8.8.8,1621,10,1,0.62,11.7,15.7,250.6,1,0.06    
(...)
```

## Data Analysis

The output from this script can be redirected to a CSV file and opened in Excel, for example. Excel Pivot Charts is a good tool that can be used to group data and to perform some analysis.

A sample Excel file is available in this repository.

Below is an example of this analysis grouping by day:

![Pivot Chart - Example 1](https://github.com/d-me3/pyping/raw/main/analysis-example-1.png)

And a specific day can be expanded to group lost packets per hour:

![Pivot Chart - Example 2](https://github.com/d-me3/pyping/raw/main/analysis-example-2.png)


