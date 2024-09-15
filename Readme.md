# Pre-requisites
 - Install requirements.txt in the folder /build/docker
 - ```$ mkdir env && cat sys.env```
 - ```$ echo APISERVER_KEY=SomeKey >> env/sys.env```

# Execution & Deployment
## Development
 ``` bash
./runner/debug.sh
 ```
## Production
 ``` bash
fastapi run app.py -c ./.conf/fastapi.conf
 ```