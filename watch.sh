# usage: watch.sh <your_command> <sleep_duration>

while :; 
  do 
  $1
  sleep $2
done
