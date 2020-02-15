#Commits everything and pushes
#Usage: ./push.sh <COMMIT MSG>
if [ $# -le 0 ]
then
	git add .
	git commit -m \"${0}\"
	git push
else
	echo "Invalid argument. Usage: ./push.sh <COMMIT MSG>"
fi


