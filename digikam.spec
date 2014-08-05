#
%define		qtver	4.8.3
%define		kdever	4.10.0

Summary:	A KDE frontend for gphoto2
Summary(pl.UTF-8):	Interfejs KDE do gphoto2
Name:		digikam
Version:	4.2.0
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://download.kde.org/stable/digikam/%{name}-%{version}.tar.bz2
# Source0-md5:	8e12775115604dd4e1d91d345781214b
Patch0:		%{name}-build.patch
URL:		http://www.digikam.org/
BuildRequires:	ImageMagick-devel
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtDesigner-devel >= %{qtver}
BuildRequires:	QtSql-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	QtXmlPatterns-devel >= %{qtver}
BuildRequires:	automoc4
BuildRequires:	clapack-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	eigen3
BuildRequires:	gettext-devel
BuildRequires:	jasper-devel
BuildRequires:	java-opencv
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	kde4-kdepimlibs-devel >= %{kdever}
BuildRequires:	lcms-devel
BuildRequires:	lensfun-devel >= 0.2.6
BuildRequires:	libf2c-devel >= 20110801
BuildRequires:	libgphoto2-devel
BuildRequires:	kde4-libkdcraw-devel >= %{kdever}
BuildRequires:	kde4-libkdeedu-devel >= %{kdever}
BuildRequires:	kde4-libkexiv2-devel >= %{kdever}
BuildRequires:	kde4-libkipi-devel >= %{kdever}
BuildRequires:	kde4-libksane-devel >= %{kdever}
BuildRequires:	liblqr-devel >= 0.4.0
BuildRequires:	libpgf-devel
BuildRequires:	libtiff-devel
BuildRequires:	kde4-marble-devel >= %{kdever}
# fixed mysql_install_db in this version
BuildRequires:	mysql-extras >= 5.5.9-2
BuildRequires:	opencv-devel
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	qjson-devel >= 0.5
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	qt-gstreamer-devel
BuildRequires:	rpmbuild(macros) >= 1.606
BuildRequires:	sed >= 4.0
BuildRequires:	shared-desktop-ontologies-devel >= 0.2
BuildRequires:	soprano-devel
Requires:	QtSql-sqlite3
Obsoletes:	digikamimageplugins
Obsoletes:	kipi-plugins
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Designed to be a standalone application to preview and download images
from a digital camera on a Linux machine.

%description -l pl.UTF-8
Samodzielna aplikacja do oglądania i ściągania obrazków z aparatów
cyfrowych pod Linuksem.

%package devel
Summary:	A KDE frontend for gphoto2 - header files
Summary(pl.UTF-8):	Interfejs KDE do gphoto2 - pliki nagłówkowe
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
A KDE frontend for gphoto2 - header files.

%description devel -l pl.UTF-8
Interfejs KDE do gphoto2 - pliki nagłówkowe.

%prep
%setup -q
%patch0 -p1

# use kde one
mv cmake/modules/FindKipi.cmake cmake/modules/FindKipi.cmake.ORIG

%build
install -d build
cd build
%cmake \
	-DSERVERCMD_MYSQL=%{_sbindir}/mysqld \
	-DENABLE_RAWSPEED=ON \
	-DDIGIKAMSC_USE_PRIVATE_KDEGRAPHICS=OFF \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

%find_lang %{name} --with-kde --all-name

# libkipi belongs to kde4-libkipi and libkipi.mo belongs to kde4-l10n
%{__sed} -i -e '/.*\/libkipi.mo$/d' %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/cleanup_digikamdb
%attr(755,root,root) %{_bindir}/digikam
%attr(755,root,root) %{_bindir}/dngconverter
%attr(755,root,root) %{_bindir}/dnginfo
%attr(755,root,root) %{_bindir}/expoblending
%attr(755,root,root) %{_bindir}/panoramagui
%attr(755,root,root) %{_bindir}/photolayoutseditor
%attr(755,root,root) %{_bindir}/scangui
%dir %{_datadir}/apps/digikam/utils
%attr(755,root,root) %{_datadir}/apps/digikam/utils/digikam-camera
%dir %{_datadir}/apps/digikam/database
%{_datadir}/apps/digikam/database/dbconfig.xml
%{_datadir}/apps/digikam/database/mysql-global.conf
%{_datadir}/apps/kconf_update/adjustlevelstool.upd
%attr(755,root,root) %{_bindir}/digitaglinktree
%attr(755,root,root) %{_bindir}/showfoto
#%attr(755,root,root) %ghost %{_libdir}/libdigikamdatabase.so.4
%attr(755,root,root) %{_libdir}/libdigikamdatabase.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libdigikamcore.so.4
%attr(755,root,root) %{_libdir}/libkface.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkface.so.2
%attr(755,root,root) %{_libdir}/libkgeomap.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkgeomap.so.1
%attr(755,root,root) %{_libdir}/libkipiplugins.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libkipiplugins.so.4
%attr(755,root,root) %{_libdir}/libmediawiki.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmediawiki.so.1
%attr(755,root,root) %{_libdir}/libkvkontakte.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkvkontakte.so.1
%attr(755,root,root) %{_libdir}/libdigikamcore.so.*.*.*
%attr(755,root,root) %{_libdir}/kde4/digikamimageplugin_*.so
%attr(755,root,root) %{_libdir}/kde4/kio_digikamalbums.so
%attr(755,root,root) %{_libdir}/kde4/kio_digikamdates.so
%attr(755,root,root) %{_libdir}/kde4/kio_digikammapimages.so
%attr(755,root,root) %{_libdir}/kde4/kio_digikamsearch.so
%attr(755,root,root) %{_libdir}/kde4/kio_digikamtags.so
%attr(755,root,root) %{_libdir}/kde4/kipiplugin_*.so
%attr(755,root,root) %{_libdir}/kde4/libexec/digikamdatabaseserver
%{_mandir}/man1/digitaglinktree.1*
%{_mandir}/man1/cleanup_digikamdb.1*
%dir %{_datadir}/apps/digikam
%{_datadir}/apps/digikam/about
%{_datadir}/apps/digikam/importui.rc
%{_datadir}/apps/digikam/data
%{_datadir}/apps/digikam/digikamimageplugin_*.rc
%{_datadir}/apps/digikam/digikamimagewindowui.rc
%{_datadir}/apps/digikam/digikamui.rc
%{_datadir}/apps/digikam/icons
%{_datadir}/apps/digikam/lighttablewindowui.rc
%{_datadir}/apps/digikam/queuemgrwindowui.rc
%{_datadir}/apps/digikam/tips
%{_datadir}/apps/gpssync
%{_datadir}/apps/kipi
%{_datadir}/apps/kipiplugin_*
%{_datadir}/apps/libkface
%{_datadir}/apps/libkgeomap
%{_datadir}/apps/photolayoutseditor
%{_datadir}/apps/showfoto
%{_datadir}/kde4/services/digikamalbums.protocol
%{_datadir}/kde4/services/digikamdates.protocol
%{_datadir}/kde4/services/digikamimageplugin_*.desktop
%{_datadir}/kde4/services/digikammapimages.protocol
%{_datadir}/kde4/services/digikamsearch.protocol
%{_datadir}/kde4/services/digikamtags.protocol
%{_datadir}/kde4/services/kipiplugin_*.desktop
%{_datadir}/apps/digikam/digikam.notifyrc
%{_datadir}/apps/solid/actions/digikam-opencamera.desktop
%{_datadir}/kde4/servicetypes/digikamimageplugin.desktop
%{_datadir}/kde4/servicetypes/photolayoutseditorborderplugin.desktop
%{_datadir}/kde4/servicetypes/photolayoutseditoreffectplugin.desktop
%{_datadir}/templates/kipiplugins_photolayoutseditor
%{_datadir}/config.kcfg/photolayoutseditor.kcfg
%{_iconsdir}/*/*/actions/*.png
%{_iconsdir}/*/*/apps/*.png
%{_iconsdir}/*/*/apps/*.svgz
%{_desktopdir}/kde4/*.desktop

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdigikamcore.so
%attr(755,root,root) %{_libdir}/libdigikamdatabase.so
%attr(755,root,root) %{_libdir}/libkface.so
%attr(755,root,root) %{_libdir}/libkgeomap.so
%attr(755,root,root) %{_libdir}/libkipiplugins.so
%attr(755,root,root) %{_libdir}/libmediawiki.so
%attr(755,root,root) %{_libdir}/libkvkontakte.so
%{_pkgconfigdir}/libkface.pc
%{_pkgconfigdir}/libkgeomap.pc
%{_pkgconfigdir}/libmediawiki.pc
%{_datadir}/apps/cmake/modules/FindKGeoMap.cmake
%{_datadir}/apps/cmake/modules/FindKface.cmake
%{_datadir}/apps/cmake/modules/FindMediawiki.cmake
%{_libdir}/cmake/LibKVkontakte
%{_includedir}/libkface
%{_includedir}/libkvkontakte
%{_includedir}/libkgeomap
%{_includedir}/libmediawiki
