# set the base image. Since we're running 
FROM golang:alpine
# set a key-value label for the Docker image
LABEL AppType="Web App using go"
# copy files from the host to the container filesystem. 
# For example, all the files in the current directory
# to the  `/app` directory in the container
COPY . /go/src/app
#  defines the working directory within the container
WORKDIR /go/src/app
# run commands within the container. 
#RUN go mod init
# if module file wasn't there before 
#RUN go build -o ./main.go
EXPOSE 6111   
## go port we don't have to bind ports between host and container 
# provide a command to run on container start. 
CMD ["go","run","./main.go"]
