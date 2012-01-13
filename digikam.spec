#
%define		qtver	4.7.4
%define		kdever	4.7.4

Summary:	A KDE frontend for gphoto2
Summary(pl.UTF-8):	Interfejs KDE do gphoto2
Name:		digikam
Version:	2.4.1
Release:	3
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://downloads.sourceforge.net/digikam/%{name}-%{version}.tar.bz2
# Source0-md5:	4e36b8cc33f5ac589e4b45b22c902fdd
URL:		http://www.digikam.org/
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtDesigner-devel >= %{qtver}
BuildRequires:	QtSql-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	automoc4
BuildRequires:	clapack-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	gettext-devel
BuildRequires:	jasper-devel
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	kde4-kdepimlibs-devel >= %{kdever}
BuildRequires:	lcms-devel
BuildRequires:	lensfun-devel
BuildRequires:	libf2c-devel
BuildRequires:	libgphoto2-devel
BuildRequires:	libkdcraw-devel >= %{kdever}
BuildRequires:	libkdeedu-devel >= %{kdever}
BuildRequires:	libkexiv2-devel >= %{kdever}
BuildRequires:	libkipi-devel >= %{kdever}
BuildRequires:	libksane-devel >= %{kdever}
BuildRequires:	liblqr-devel >= 0.4.0
BuildRequires:	libpgf-devel
BuildRequires:	libtiff-devel
BuildRequires:	marble-devel >= %{kdever}
# fixed mysql_install_db in this version
BuildRequires:	mysql-extras >= 5.5.9-2
BuildRequires:	opencv-devel
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	qjson-devel >= 0.5
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
BuildRequires:	shared-desktop-ontologies-devel >= 0.2
BuildRequires:	soprano-devel
Requires:	QtSql-sqlite3
Obsoletes:	digikamimageplugins
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

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
	-DLIB_INSTALL_DIR_SUFFIX=64 \
%endif
	-DSERVERCMD_MYSQL=%{_sbindir}/mysqld \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

%find_lang %{name} --with-kde --all-name

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
%attr(755,root,root) %{_bindir}/libkgeomap_demo
%attr(755,root,root) %{_bindir}/panoramagui
%attr(755,root,root) %{_bindir}/photolayoutseditor
%attr(755,root,root) %{_bindir}/scangui
%{_datadir}/apps/digikam/lensfun
%dir %{_datadir}/apps/digikam/utils
%attr(755,root,root) %{_datadir}/apps/digikam/utils/digikam-camera
%dir %{_datadir}/apps/digikam/database
%{_datadir}/apps/digikam/database/dbconfig.xml
%{_datadir}/apps/digikam/database/mysql-global.conf
%attr(755,root,root) %{_bindir}/digitaglinktree
%attr(755,root,root) %{_bindir}/showfoto
%attr(755,root,root) %ghost %{_libdir}/libdigikamdatabase.so.2
%attr(755,root,root) %{_libdir}/libdigikamdatabase.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdigikamcore.so.2
%attr(755,root,root) %{_libdir}/libkface.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkface.so.1
%attr(755,root,root) %{_libdir}/libkgeomap.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkgeomap.so.1
%attr(755,root,root) %{_libdir}/libkipiplugins.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkipiplugins.so.2
%attr(755,root,root) %{_libdir}/libmediawiki.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmediawiki.so.1
%attr(755,root,root) %{_libdir}/libkvkontakte.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkvkontakte.so.1
%attr(755,root,root) %{_libdir}/libdigikamcore.so.*.*.*
%attr(755,root,root) %{_libdir}/kde4/digikamimageplugin_*.so
%attr(755,root,root) %{_libdir}/kde4/digikamnepomukservice.so
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
%{_datadir}/apps/digikam/cameraui.rc
%{_datadir}/apps/digikam/data
%{_datadir}/apps/digikam/digikamimageplugin_*.rc
%{_datadir}/apps/digikam/digikamimagewindowui.rc
%{_datadir}/apps/digikam/digikamui.rc
%{_datadir}/apps/digikam/icons
%{_datadir}/apps/digikam/lighttablewindowui.rc
%{_datadir}/apps/digikam/queuemgrwindowui.rc
%{_datadir}/apps/digikam/tips
%{_datadir}/apps/gpssync
%{_datadir}/apps/kipiplugin_*
%{_datadir}/apps/libkface
%{_datadir}/apps/libkgeomap
%{_datadir}/apps/photolayoutseditor
%{_datadir}/apps/showfoto
%{_datadir}/kde4/services/digikamalbums.protocol
%{_datadir}/kde4/services/digikamdates.protocol
%{_datadir}/kde4/services/digikamimageplugin_*.desktop
%{_datadir}/kde4/services/digikammapimages.protocol
%{_datadir}/kde4/services/digikamnepomukservice.desktop
%{_datadir}/kde4/services/digikamsearch.protocol
%{_datadir}/kde4/services/digikamtags.protocol
%{_datadir}/kde4/services/kipiplugin_*.desktop
%{_datadir}/apps/digikam/digikam.notifyrc
%{_datadir}/apps/solid/actions/digikam-opencamera.desktop
%{_datadir}/kde4/servicetypes/digikamimageplugin.desktop
%{_datadir}/kde4/servicetypes/photolayoutseditorborderplugin.desktop
%{_datadir}/kde4/servicetypes/photolayoutseditoreffectplugin.desktop
%{_datadir}/config.kcfg/PLEConfigSkeleton.kcfgc
%{_iconsdir}/*/*/actions/*.png
%{_iconsdir}/*/*/actions/*.svgz
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
