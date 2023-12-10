#!/usr/bin/env bash
# Commit message
    echo "What is the commit message: "
    read -r MESSAGE
#Variable to store the number of arguments, if no arguments git adds all the files in the directory
count=$#
if [ "$count" == "0" ]; 
then
    git add .
    git commit -m "$MESSAGE"
    git push
elif [ "$count" -gt 0 ]; 
then
    for arg in "$@"; do
        git add "$arg"
        git commit -m "$MESSAGE: $arg"
        git push
    done
else
    echo "Invalid number of arguments"
fi