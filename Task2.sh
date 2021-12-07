#!/bin/sh
read -p "NUMBER 1 " X
read -p "NUMBER 2 " Y
echo "$X"
echo "$Y"
if [ "$X" -eq "$Y" ]
then
	echo "X is equal Than Y"
elif [ "$X" -gt "$Y" ]
then
	echo "X is greater than Y"
elif [ "$X" -lt "$Y" ]
then
	echo "X is less than Y"
fi


Output

pooja77@NHD19SL963:/mnt/c/users/Pooja/desktop$ sh Task2.sh
NUMBER 1 5
NUMBER 2 5
5
5
X is equal to Y
pooja77@NHD19SL963:/mnt/c/users/Pooja/desktop$ sh Task2.sh
NUMBER 1 5
NUMBER 2 8
5
8
X is less than Y
pooja77@NHD19SL963:/mnt/c/users/Pooja/desktop$ 6
6: command not found
pooja77@NHD19SL963:/mnt/c/users/Pooja/desktop$ sh Task2.sh
NUMBER 1 7
NUMBER 2 2
7
2
X is greater than Y
pooja77@NHD19SL963:/mnt/c/users/Pooja/desktop$ sh Task2.sh
NUMBER 1 5
NUMBER 2 5
5
5
X is equal Than Y
pooja77@NHD19SL963:/mnt/c/users/Pooja/desktop$
