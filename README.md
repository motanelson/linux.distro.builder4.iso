# linux.distro.builder4.iso


4 kernel cd builder of distro linux


Boot Process Overview: ISOLINUX, vmlinuz and initrd
This project is designed as an educational Linux builder, allowing users to observe, experiment and understand how a Linux system boots and how a distribution is constructed.
This section explains the role of ISOLINUX, vmlinuz, initrd.gz and linuxrd, which are fundamental components of the boot process.
ISOLINUX
ISOLINUX is a bootloader used mainly for bootable ISO images (CD/DVD/USB).
It is part of the SYSLINUX bootloader family.
ISOLINUX is responsible for:
Starting the boot process
Presenting a boot menu (if configured)
Loading the Linux kernel and the initial RAM disk into memory
ISOLINUX does not run Linux itself.
Its only job is to prepare the system and pass control to the Linux kernel.
Typical ISOLINUX configuration files:
isolinux.cfg
menu.cfg
These files define:
Which kernel to boot
Which initrd to load
Kernel parameters (boot options)
vmlinuz (Linux Kernel)
vmlinuz is the compressed Linux kernel.
The kernel is the core of the operating system and is responsible for:
Hardware detection
CPU and memory management
Device drivers
Starting the first user-space process
When ISOLINUX loads vmlinuz, the kernel:
Decompresses itself into memory
Initializes hardware
Looks for an initial root filesystem (initrd / initramfs)
Without a kernel, Linux cannot exist.
initrd.gz / linuxrd (Initial RAM Disk)
initrd.gz (sometimes named linuxrd) is a compressed temporary root filesystem loaded into RAM.
Its purpose is to:
Prepare the system before the real root filesystem is mounted
Load necessary kernel modules (storage, filesystem, USB, etc.)
Locate and mount the real system image
Hand over control to the main system
The initrd usually contains:
A minimal filesystem
BusyBox or similar tools
Boot scripts (init)
Mount logic and hardware detection
After its job is done, the system switches from the initrd to the real root filesystem.
Boot Flow Summary
The boot process works in this order:
BIOS / UEFI starts the bootloader
ISOLINUX loads:
vmlinuz (Linux kernel)
initrd.gz or linuxrd
Linux kernel starts and initializes hardware
initrd runs early boot scripts
The real Linux system is mounted and started
This separation allows experimentation, modular design and educational exploration.
Educational Purpose
By separating:
Bootloader
Kernel
Initial RAM filesystem
System and data images
This builder encourages users to:
Observe how Linux starts
Modify and experiment safely
Create their own Linux distributions
Learn Linux internals through practice
Linux is not a black box — it is a system meant to be studied.
