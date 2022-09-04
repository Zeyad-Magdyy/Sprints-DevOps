echo"Enter Waned Port Number"
read PORTNUM
if [ ${PORTNUM} -gt 0 ] && [ ${PORTNUM} -lt 65536 ]
then
	echo " The enetered Port number is Valid and accepted"
else
	echo " The entered Port number is Out of Range"
fi

