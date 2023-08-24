#!/bin/bash
adb root
adb remount
adb push replayprebuilt/x86_64/libretrace.so /system/lib64/
adb push replayprebuilt/x86_64/aicreplay /data/
