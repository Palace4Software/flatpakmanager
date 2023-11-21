#!/bin/bash

### Automatic .deb creator for flatpakmanager ###

version=$(cat version.txt)

# move files to deb building folder
mkdir -p deb/usr/lib/flatpakmanager/
cp flatpakmanager.py deb/usr/lib/flatpakmanager/flatpakmanager
cp version.txt deb/usr/lib/flatpakmanager/
cp LICENSE deb/usr/lib/flatpakmanager/
cp README.md deb/usr/lib/flatpakmanager/

mkdir -p deb/usr/share/icons/hicolor/256x256/apps/
cp icon.png deb/usr/share/icons/hicolor/256x256/apps/flatpakmanager.png

mkdir -p deb/usr/share/applications/
cp flatpakmanager.desktop deb/usr/share/applications/

mkdir -p deb/usr/bin/
echo "#!/bin/bash
exec /usr/lib/flatpakmanager/flatpakmanager" > deb/usr/bin/flatpakmanager

# chmod
chmod +x deb/usr/lib/flatpakmanager/flatpakmanager
chmod +x deb/usr/bin/flatpakmanager
chmod 755 deb/DEBIAN

# build
dpkg-deb --build -Zxz deb
mkdir installer
mv deb.deb installer/flatpakmanager-$version.deb

#clearup
rm -r deb/usr
