# pyping

Simple python script to report lost packets of an internet connection in CSV format. If output is redirected to a CSV file, Excel Pivot Charts can later be used to analyze data.

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

## Usage examples

1. `sudo python3 -u ./pyping.py > outputfile.csv" &`

2. `sudo python3 -u ./pyping.py > "$(pwd -P)/$(date +"%Y%m%d-%H%M").csv" &`

## Output Columns (CSV format)

**Only lost packets** and **packets with a response time over 2.5 times the average** events are logged.

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

## Data Analysis

The output from this script can be redirected to a CSV file and opened in Excel, for example. Excel Pivot Charts is a good tool that can be used to group data and to perform some analysis.

A sample Excel file is available in this repository.

Below is an example of this analysis grouping by day:

![Pivot Chart - Example 1](https://github.com/d-me3/pyping/raw/main/analysis-example-1.png)

And a specific day can be expanded to groupd the lost packets per hour:

![Pivot Chart - Example 2](https://github.com/d-me3/pyping/raw/main/analysis-example-2.png)


