#Commits everything and pushes
#Usage: ./push.sh <COMMIT MSG>
if [ $# -ge 1 ]
then
	git add .
	git commit -m \"$@\"
	git push
else
	echo "Invalid argument. Usage: ./push.sh <COMMIT MSG>"
fi


