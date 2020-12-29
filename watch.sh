# usage: sh watch.sh <your_command> <parameters> <sleep_duration>
# Exemple : sh watch.sh python test.py 5

while :; 
  do 
  $1 $2
  sleep $3
done
