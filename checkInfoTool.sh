#!/bin/sh
TMPSTR="reach user.warn kernel: sil902x_ioctl(cmd = 3)!"
LOGFILE="/opt/Rec/sysCheckInfo.log"
DMESGLOG="/opt/Rec/sysDmesgInfo.log"
SleepTime=5
num=0;

if [ -f $LOGFILE  ];then
	rm -f $LOGFILE
fi

#while (("$int < 3"))
while [ 1 = 1 ]
do

        curtime="`date \"+%G-%m-%d %H:%M:%S\"`"
		cpuload=(`cat /var/log/messages | awk '{print $4,$5,$6,$7,$8,$9}'`)
	
:<<!
		2）.采集cpu负载
		采集算法：读取/proc/loadavg得到机器的1/5/15分钟平均负载，再乘以100		
!
		
		cpuload=(`cat /proc/loadavg | awk '{print $1,$2,$3}'`)
		load1=${cpuload[0]}
		load5=${cpuload[1]}
		load15=${cpuload[2]}

#系统内存使用量  sysMemUse系统已经使用了多少物理内存  sysMemFree系统还剩多少物理内存
		sysmem=(`free -m | awk '/Mem/{print $3, $4}'`)
		sysMemUse=${sysmem[0]}
		sysMemFree=${sysmem[1]}

#当前进程内存使用量   processMemUse当前所有进程使用了多少物理内存  processMemFree当前所有进程还剩多少物理内存
		processmem=(`free -m|grep 'buffers/cache'|awk '{print $3,$4}'`)
		processMemUse=${sysmem[0]}
		processMemFree=${sysmem[1]}
		
		
		#数据打印	
		((num++));
		
		data="$curtime, $num, $load1, $num, $load5, $num, $load15, $num, $sysMemUse, $num, $sysMemFree, $num, $processMemUse, $num, $processMemFree"
		echo "$data" >> $LOGFILE
		
		sleep $SleepTime

done
					
					
					
					