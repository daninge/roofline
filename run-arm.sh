adb root > /dev/null
adb shell "mkdir -p /data/local/tmp/roofline && chmod 777 /data/local/tmp/roofline" > /dev/null
adb push ./libs/arm64-v8a/gables /data/local/tmp/roofline > /dev/null 
adb shell "cd /data/local/tmp/roofline && chmod 777 ./gables && export OMP_PROC_BIND=spread && export OMP_PLACES=threads && ./gables 1 1 1000"
