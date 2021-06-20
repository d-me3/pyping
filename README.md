# pyping

Simple python script to log lost packets of an internet connection to a CSV format. Excel Pivot Charts can later be used to analyze data.

There is no command line parameter.

The target ping address must be edited in the source code.

## Requirements

1. A PC or device running Linux (it may work on Windows but it was not tested). The commands below were tested with a Raspberry Pi OS

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
