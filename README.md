# tau-wallpapers

A set of default and supplemental wallpapers for tauOS.

# Building

> All packages are built on Fedora containers

Build Requirements:
- `fedora-packager`
- `fedora-review`

Download the latest release .tar.gz from GitHub (https://github.com/tau-OS/tau-wallpapers/releases/tag/v1.1)

Setup:
```bash
sudo usermod -a -G mock $(whoami)
# Needed for EL builds
mkdir -p /home/$(whoami)/.config/mock
ln -s /etc/mock/alma+epel-8-x86_64.cfg /home/$(whoami)/.config/mock/epel-8-x86_64.cfg
```

Build:
```bash
# For tauOS builds:
fedpkg --release f36 mockbuild
# For EL builds:
fedpkg --release el8 mockbuild
```