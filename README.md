# Graphics_Tools_Public  
To capture:  
git clone https://github.com/gaoshunli/Graphics_Tools_Public.git  
cd Graphics_Tools_Public  
./AndroidTrace.py trace --appname com.vectorunit.silver.freetime --path captureprebuilt  
Then start this Game.  
And the traced file will be in /data/local/traces/ com.vectorunit.silver.freetime.trace  
./AndroidTrace.py endtrace  
To replay:  
git clone https://github.com/gaoshunli/Graphics_Tools_Public.git  
cd Graphics_Tools_Public  
. /settingupreplay.sh  
adb shell /data/aicreplay /data/genshi.trace -b --samewindow  
  

