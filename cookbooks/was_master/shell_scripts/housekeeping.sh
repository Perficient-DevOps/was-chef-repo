#!/bin/bash
function show_help() {
    cat << ENDHELP

#****************************************************************************************************************
# Script     : 	housekeeping.sh 
#
# Description:	This is a housekeeping job that deletes files older than retentionPeriod
#                    from a directory while making sure we atleast have minimumBackupsToRetain
# 
# Arguments  :	
#			1) directotyPath		: Complete path of the directory that needs cleanup.        
#			2) retentionPeriod		: Retention period (duration of time in number of days 
#							  for which the files should be maintained or "retained"
#							  in requested "directotyPath".
#			3) minimumBackupsToRetain	: Minimum number of backups to retain in any case.
#
# Usage      :       ./housekeeping.sh [directotyPath] [retentionPeriod] [minimumBackupsToRetain]
#
# Example    :       ./housekeeping.sh "/apps01/IBM/was-config/environment/sandbox/backups1" 1 4 
#
# Author     :	Sumit Malvi  03/26/18
#****************************************************************************************************************
ENDHELP
}

(
if [ $# -eq 0 ]
  then
    echo "NO ARGUMENTS SUPPLIED"
    echo "Run $0 --help to get usage information"
  else
	if [ -z $1 ] || [ -z $2 ] || [ -z $3 ]; then
		  if [ $1 == "--help" ]; then
			show_help
		  else
			echo "MISSING ARGUMENTS : JOB EXPECTS THREE ARGUMENTS"
    			echo "Run $0 --help to get usage information"
		  fi
	else
		  echo "HOUSEKEEPING:: Script Start -- $(date +%Y%m%d_%H%M)"	
		  echo RUNNING WITH ARGUMENTS : $1 and $2 and $3
		  echo "=========================================="

		  directotyPath=$1
		  retentionPeriod=$2
		  minimumBackupsToRetain=$3

		  totalCount=`find $directotyPath -type f | wc -l`
		  echo initial totalCount : $totalCount
		  while [ "$totalCount " -gt "$minimumBackupsToRetain" ]
		  do 
			 readarray -t rmFileArr < <(find $directotyPath -type f -mtime +$retentionPeriod | xargs ls -t )
#			 printf '%s\n' "${rmFileArr[@]}"
			 if [ -z "${rmFileArr[0]}" ]; then
				echo "nothing found to be deleted."
			 else
			 	echo removing "${rmFileArr[-1]}"
			 	rm "${rmFileArr[-1]}"
			fi
		 	totalCount=$((--totalCount))
		 	echo totalCount : $totalCount
		  done
		  echo "Either minimum backup count reached or there is nothing older than $2 days to be deleted."
		  echo "HOUSEKEEPING :: Script End -- $(date +%Y%m%d_%H%M)"
		  echo ================= HOUSEKEEPING COMPLETE ==================
	fi
fi
)
