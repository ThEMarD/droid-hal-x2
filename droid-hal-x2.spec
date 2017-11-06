# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device x2
%define vendor leeco

%define vendor_pretty LeEco
%define device_pretty Le Max 2

%define installable_zip 1

%define droid_target_aarch64 1

%define straggler_files \
/bugreport\
/d\
/file_contexts.bin\
/init.qcom.bt.sh\
/init.qcom.sh\
/init.qcom.usb.sh\
/property_contexts\
/qfp_boot.sh\
/sdcard\
/selinux_version\
/service_contexts\
/vendor\
/default.prop\
/etc/udev/rules.d/60-persistent-v4l.rules\
/init-debug\
/init.cm.rc\
/init.device.rc\
/init.environ.rc\
/init.qcom.power.rc\
/init.qcom.rc\
/init.qcom.usb.rc\
/init.rc\
/init.usb.configfs.rc\
/init.usb.rc\
/init.zygote32.rc\
/init.zygote64_32.rc\
/lib/systemd/system/bt_firmware.mount\
/lib/systemd/system/config.mount\
/lib/systemd/system/dev-bfqio.mount\
/lib/systemd/system/dev-cpuctl.mount\
/lib/systemd/system/dev-cpuset.mount\
/lib/systemd/system/dev-stune.mount\
/lib/systemd/system/dsp.mount\
/lib/systemd/system/firmware.mount\
/lib/systemd/system/mnt.mount\
/lib/systemd/system/persist.mount\
/lib/systemd/system/sys-fs-pstore.mount\
/lib/systemd/system/system.mount\
/lib/udev/rules.d/999-android-system.rules\
/sbin/adbd\
/sbin/droid-hal-init\
/sbin/healthd\
/sbin/ueventd\
/sbin/watchdogd\
/ueventd.qcom.rc\
/ueventd.rc\
/usr/lib/droid/all-units.txt\
/usr/lib/droid/droid-user-add.sh\
/usr/lib/droid/droid-user-remove.sh\
/usr/lib/droid/droid-user-remove.sh.installed\
/usr/lib/droid/generated-post-scripts.sh\
/usr/libexec/droid-hybris/lib-dev-alog/libcutils.so\
/usr/libexec/droid-hybris/lib-dev-alog/liblog.so\
/usr/libexec/droid-hybris/lib64-dev-alog/libcutils.so\
/usr/libexec/droid-hybris/lib64-dev-alog/liblog.so\
/usr/libexec/droid-hybris/system/bin/linker\
/usr/libexec/droid-hybris/system/bin/linker64\
/usr/libexec/droid-hybris/system/bin/logcat\
/usr/libexec/droid-hybris/system/bin/servicemanager\
/usr/libexec/droid-hybris/system/bin/updater\
/usr/libexec/droid-hybris/system/lib/libEGL.so\
/usr/libexec/droid-hybris/system/lib/libGLESv1_CM.so\
/usr/libexec/droid-hybris/system/lib/libGLESv2.so\
/usr/libexec/droid-hybris/system/lib/libbacktrace.so\
/usr/libexec/droid-hybris/system/lib/libbase.so\
/usr/libexec/droid-hybris/system/lib/libbinder.so\
/usr/libexec/droid-hybris/system/lib/libc++.so\
/usr/libexec/droid-hybris/system/lib/libc.so\
/usr/libexec/droid-hybris/system/lib/libcutils.so\
/usr/libexec/droid-hybris/system/lib/libdl.so\
/usr/libexec/droid-hybris/system/lib/libdsyscalls.so\
/usr/libexec/droid-hybris/system/lib/libhardware.so\
/usr/libexec/droid-hybris/system/lib/liblog.so\
/usr/libexec/droid-hybris/system/lib/liblzma.so\
/usr/libexec/droid-hybris/system/lib/libm.so\
/usr/libexec/droid-hybris/system/lib/libsync.so\
/usr/libexec/droid-hybris/system/lib/libui.so\
/usr/libexec/droid-hybris/system/lib/libunwind.so\
/usr/libexec/droid-hybris/system/lib/libutils.so\
/usr/libexec/droid-hybris/system/lib64/libEGL.so\
/usr/libexec/droid-hybris/system/lib64/libGLESv1_CM.so\
/usr/libexec/droid-hybris/system/lib64/libGLESv2.so\
/usr/libexec/droid-hybris/system/lib64/libbacktrace.so\
/usr/libexec/droid-hybris/system/lib64/libbase.so\
/usr/libexec/droid-hybris/system/lib64/libbinder.so\
/usr/libexec/droid-hybris/system/lib64/libc++.so\
/usr/libexec/droid-hybris/system/lib64/libc.so\
/usr/libexec/droid-hybris/system/lib64/libcrypto.so\
/usr/libexec/droid-hybris/system/lib64/libcutils.so\
/usr/libexec/droid-hybris/system/lib64/libdl.so\
/usr/libexec/droid-hybris/system/lib64/libdsyscalls.so\
/usr/libexec/droid-hybris/system/lib64/libhardware.so\
/usr/libexec/droid-hybris/system/lib64/liblog.so\
/usr/libexec/droid-hybris/system/lib64/liblzma.so\
/usr/libexec/droid-hybris/system/lib64/libm.so\
/usr/libexec/droid-hybris/system/lib64/libpackagelistparser.so\
/usr/libexec/droid-hybris/system/lib64/libpcre.so\
/usr/libexec/droid-hybris/system/lib64/libpcrecpp.so\
/usr/libexec/droid-hybris/system/lib64/libselinux.so\
/usr/libexec/droid-hybris/system/lib64/libsync.so\
/usr/libexec/droid-hybris/system/lib64/libui.so\
/usr/libexec/droid-hybris/system/lib64/libunwind.so\
/usr/libexec/droid-hybris/system/lib64/libutils.so\
%(nil)

%include rpm/dhd/droid-hal-device.inc


# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

