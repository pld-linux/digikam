#
# TODO: fix plugins location, can't find where it i defined in the code
#
%define		qtver	4.8.3
%define		kdever	4.10.0

Summary:	A KDE frontend for gphoto2
Summary(pl.UTF-8):	Interfejs KDE do gphoto2
Name:		digikam
Version:	7.1.0
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	https://download.kde.org/stable/digikam/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	165347a16396f3ef1d96315f683dccf8
Patch0:		qt-5.15.patch
URL:		https://www.digikam.org/
BuildRequires:	ImageMagick-devel
BuildRequires:	Qt5WebEngine-devel
BuildRequires:	clapack-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	eigen3
BuildRequires:	exiv2-devel >= 0.26
BuildRequires:	gettext-tools
BuildRequires:	jasper-devel
BuildRequires:	java-opencv
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-kdoctools >= 5.38.0
BuildRequires:	kf5-extra-cmake-modules
BuildRequires:	ka5-libkipi-devel
BuildRequires:	kf5-kdoctools-devel
BuildRequires:	kf5-kfilemetadata-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kiconthemes-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-knotifications-devel
BuildRequires:	kf5-knotifyconfig-devel
BuildRequires:	kf5-kservice-devel
BuildRequires:	kf5-solid-devel
BuildRequires:	kf5-threadweaver-devel
BuildRequires:	kf5-kwindowsystem-devel
BuildRequires:	kf5-kxmlgui-devel
BuildRequires:	lcms-devel
BuildRequires:	lensfun-devel >= 0.2.6
BuildRequires:	libf2c-devel >= 20110801
BuildRequires:	libgphoto2-devel
BuildRequires:	liblqr-devel >= 0.4.0
BuildRequires:	libpgf-devel
BuildRequires:	libtiff-devel
BuildRequires:	opencv-devel
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	qjson-devel >= 0.5
BuildRequires:	qtav-devel
BuildRequires:	rpmbuild(macros) >= 1.606
BuildRequires:	sed >= 4.0
BuildRequires:	shared-desktop-ontologies-devel >= 0.2
BuildRequires:	soprano-devel
Requires:	Qt5Sql-sqldriver-mysql
Requires:	Qt5Sql-sqldriver-sqlite3
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

%build
install -d build
cd build
%cmake \
	-DENABLE_AKONADICONTACTSUPPORT:BOOL=ON \
	-DENABLE_APPSTYLES:BOOL=ON \
	-DENABLE_KFILEMETADATASUPPORT:BOOL=ON \
	-DENABLE_MEDIAPLAYER:BOOL=ON \
	-DENABLE_MYSQLSUPPORT:BOOL=ON \
	-DENABLE_INTERNALMYSQL:BOOL=ON \
	-DENABLE_OPENCV3:BOOL=ON \
	-DDIGIKAMSC_COMPILE_KIPIPLUGINS=ON \
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
%doc AUTHORS ChangeLog CODE_OF_CONDUCT.md COPYING* NEWS PACKAGING README.md README.DEVEL
%attr(755,root,root) %{_bindir}/cleanup_digikamdb
%attr(755,root,root) %{_bindir}/digikam
%attr(755,root,root) %{_bindir}/digitaglinktree
%attr(755,root,root) %{_bindir}/showfoto
%attr(755,root,root) %{_libdir}/libdigikamdatabase.so.*.*.*
%attr(755,root,root) %{_libdir}/libdigikamgui.so.*.*
%attr(755,root,root) %{_libdir}/libdigikamcore.so.*.*.*
%dir %{_libdir}/plugins
%dir %{_libdir}/plugins/digikam
%dir %{_libdir}/plugins/digikam/bqm
%attr(755,root,root) %{_libdir}/plugins/digikam/bqm/*.so
%dir %{_libdir}/plugins/digikam/dimg
%attr(755,root,root) %{_libdir}/plugins/digikam/dimg/*.so
%dir %{_libdir}/plugins/digikam/editor
%attr(755,root,root) %{_libdir}/plugins/digikam/editor/*.so
%dir %{_libdir}/plugins/digikam/generic
%attr(755,root,root) %{_libdir}/plugins/digikam/generic/*.so
%dir %{_libdir}/plugins/digikam/rawimport
%attr(755,root,root) %{_libdir}/plugins/digikam/rawimport/*.so
%{_datadir}/%{name}
%{_datadir}/knotifications5/digikam.notifyrc
%{_datadir}/kxmlgui5/digikam
%{_datadir}/kxmlgui5/showfoto
%{_desktopdir}/org.kde.digikam.desktop
%{_desktopdir}/org.kde.showfoto.desktop
%{_datadir}/metainfo/org.kde.digikam.appdata.xml
%{_datadir}/metainfo/org.kde.showfoto.appdata.xml
%{_datadir}/showfoto
%{_datadir}/solid/actions/digikam-opencamera.desktop
%{_mandir}/man1/digitaglinktree.1*
%{_mandir}/man1/cleanup_digikamdb.1*
%{_iconsdir}/*/*/actions/*.png
%{_iconsdir}/*/*/apps/*.png
%{_iconsdir}/*/*/apps/*.svgz

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdigikamcore.so
%attr(755,root,root) %{_libdir}/libdigikamdatabase.so
%attr(755,root,root) %{_libdir}/libdigikamgui.so
