#
# TODO: fix plugins location, can't find where it i defined in the code
#

%define		akonadi_ver	5.19.0
%define		qt5_ver		5.14.0
%define		qt6_ver		6.4.0
%define		kf_ver		5.95.0

%ifarch x32
# Qt5WebEngine not available
%define		with_qtwebkit	1
%endif
Summary:	A KDE frontend for gphoto2
Summary(pl.UTF-8):	Interfejs KDE do gphoto2
Name:		digikam
Version:	9.1.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Graphics
Source0:	https://download.kde.org/stable/digikam/%{version}/digiKam-%{version}.tar.xz
# Source0-md5:	3ce54c777ea70fe7246a0aa9b49c36cc
URL:		https://www.digikam.org/
BuildRequires:	ImageMagick-c++-devel >= 6.7.0
BuildRequires:	ImageMagick-devel >= 6.7.0
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	OpenGL-devel
BuildRequires:	bison >= 2.5.0
BuildRequires:	boost-devel >= 1.43.0
BuildRequires:	cmake >= 3.16
BuildRequires:	doxygen >= 1.8.0
BuildRequires:	eigen3 >= 3.0.0
BuildRequires:	exiv2-devel >= 0.27.1
BuildRequires:	expat-devel >= 1:2.0.0
BuildRequires:	ffmpeg-devel
BuildRequires:	flex >= 2.5.0
BuildRequires:	gettext-tools
BuildRequires:	jasper-devel >= 1.7.0
BuildRequires:	lcms2-devel >= 2.0
BuildRequires:	lensfun-devel >= 0.2.6
BuildRequires:	libgomp-devel
BuildRequires:	libgphoto2-devel >= 2.5.0
BuildRequires:	libheif-devel >= 1.6.0
BuildRequires:	libjpeg-devel >= 8
BuildRequires:	libjxl-devel >= 0.7
BuildRequires:	liblqr-devel >= 0.4.1
# internal libpgf is used (core/libs/pgfutils/libpgf)
BuildRequires:	Qt6Concurrent-devel >= %{qt6_ver}
BuildRequires:	Qt6Core-devel >= %{qt6_ver}
BuildRequires:	Qt6DBus-devel >= %{qt6_ver}
BuildRequires:	Qt6Gui-devel >= %{qt6_ver}
BuildRequires:	Qt6Multimedia-devel >= 6.5.0
BuildRequires:	Qt6MultimediaWidgets-devel >= 6.5.0
BuildRequires:	Qt6Network-devel >= %{qt6_ver}
BuildRequires:	Qt6NetworkAuth-devel >= %{qt6_ver}
BuildRequires:	Qt6OpenGL-devel >= %{qt6_ver}
BuildRequires:	Qt6PrintSupport-devel >= %{qt6_ver}
BuildRequires:	Qt6Qml-devel >= %{qt6_ver}
BuildRequires:	Qt6Sql-devel >= %{qt6_ver}
BuildRequires:	Qt6Svg-devel >= %{qt6_ver}
BuildRequires:	Qt6WebEngine-devel >= %{qt6_ver}
BuildRequires:	Qt6Widgets-devel >= %{qt6_ver}
BuildRequires:	Qt6Xml-devel >= %{qt6_ver}
BuildRequires:	ka6-akonadi-contacts-devel >= %{akonadi_ver}
BuildRequires:	ka6-akonadi-devel >= %{akonadi_ver}
BuildRequires:	ka6-libksane-devel >= 21.12.0
BuildRequires:	ka6-marble-devel >= 0.22.0
BuildRequires:	kf6-extra-cmake-modules >= 5.240.0
BuildRequires:	kf6-kcalendarcore-devel >= %{kf_ver}
BuildRequires:	kf6-kconfig-devel >= %{kf_ver}
BuildRequires:	kf6-kcontacts-devel >= %{akonadi_ver}
BuildRequires:	kf6-kcoreaddons-devel >= %{kf_ver}
BuildRequires:	kf6-kdoctools >= 5.38.0
BuildRequires:	kf6-kdoctools-devel >= %{kf_ver}
BuildRequires:	kf6-ki18n-devel >= %{kf_ver}
BuildRequires:	kf6-kiconthemes-devel >= %{kf_ver}
BuildRequires:	kf6-kio-devel >= %{kf_ver}
BuildRequires:	kf6-knotifications-devel >= %{kf_ver}
BuildRequires:	kf6-knotifyconfig-devel >= %{kf_ver}
BuildRequires:	kf6-kservice-devel >= %{kf_ver}
BuildRequires:	kf6-kwindowsystem-devel >= %{kf_ver}
BuildRequires:	kf6-kxmlgui-devel >= %{kf_ver}
BuildRequires:	kf6-solid-devel >= %{kf_ver}
BuildRequires:	kf6-sonnet-devel >= %{kf_ver}
BuildRequires:	kf6-threadweaver-devel >= %{kf_ver}
#BuildRequires:	libpgf-devel
BuildRequires:	libpng-devel >= 2:1.2.7
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	libtiff-devel >= 3.8.2
BuildRequires:	libx265-devel >= 2.2
BuildRequires:	libxml2-devel >= 1:2.7.0
BuildRequires:	libxslt-devel >= 1.1.0
BuildRequires:	opencv-devel >= 3.3.0
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	rpmbuild(macros) >= 1.606
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	zlib-devel
Requires:	Qt6Concurrent >= %{qt6_ver}
Requires:	Qt6Core >= %{qt6_ver}
Requires:	Qt6DBus >= %{qt6_ver}
Requires:	Qt6Gui >= %{qt6_ver}
Requires:	Qt6Multimedia >= 6.5.0
Requires:	Qt6MultimediaWidgets >= 6.5.0
Requires:	Qt6Network >= %{qt6_ver}
Requires:	Qt6OpenGL >= %{qt6_ver}
Requires:	Qt6PrintSupport >= %{qt6_ver}
Requires:	Qt6Qml >= %{qt6_ver}
Requires:	Qt6Sql >= %{qt6_ver}
Requires:	Qt6Sql-sqldriver-mysql >= %{qt6_ver}
Requires:	Qt6Sql-sqldriver-sqlite3 >= %{qt6_ver}
Requires:	Qt6Svg >= %{qt6_ver}
Requires:	Qt6WebEngine >= %{qt6_ver}
Requires:	Qt6Widgets >= %{qt6_ver}
Requires:	Qt6X11Extras >= %{qt6_ver}
Requires:	Qt6Xml >= %{qt6_ver}
Requires:	exiv2 >= 0.27.0
Requires:	jasper-libs >= 1.7.0
Requires:	ka6-akonadi-contacts >= %{akonadi_ver}
Requires:	ka6-libksane >= 21.12.0
Requires:	ka6-marble >= 0.22.0
Requires:	kf6-kcalendarcore >= %{kf_ver}
Requires:	kf6-kconfig >= %{kf_ver}
Requires:	kf6-kcontacts >= %{akonadi_ver}
Requires:	kf6-kcoreaddons >= %{kf_ver}
Requires:	kf6-kfilemetadata >= %{kf_ver}
Requires:	kf6-ki18n >= %{kf_ver}
Requires:	kf6-kiconthemes >= %{kf_ver}
Requires:	kf6-kio >= %{kf_ver}
Requires:	kf6-knotifications >= %{kf_ver}
Requires:	kf6-knotifyconfig >= %{kf_ver}
Requires:	kf6-kservice >= %{kf_ver}
Requires:	kf6-kwindowsystem >= %{kf_ver}
Requires:	kf6-kxmlgui >= %{kf_ver}
Requires:	kf6-solid >= %{kf_ver}
Requires:	kf6-threadweaver >= %{kf_ver}
Requires:	lcms2 >= 2.0
Requires:	lensfun >= 0.2.6
Requires:	libgphoto2 >= 2.5.0
Requires:	libheif >= 1.6.0
Requires:	liblqr >= 0.4.1
Requires:	libpng >= 2:1.2.7
Requires:	libtiff >= 3.8.2
Requires:	libx265 >= 2.2
Requires:	libxml2 >= 1:2.7.0
Requires:	libxslt >= 1.1.0
Requires:	opencv >= 3.3.0
Obsoletes:	digikamimageplugins < 0.9.2
Obsoletes:	kipi-plugins < 1.10
ExcludeArch:	%{ix86} x32
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
Requires:	Qt6Core-devel >= %{qt6_ver}
Requires:	Qt6Gui-devel >= %{qt6_ver}
Requires:	Qt6Sql-devel >= %{qt6_ver}
Requires:	Qt6Widgets-devel >= %{qt6_ver}
Requires:	libstdc++-devel >= 6:7

%description devel
A KDE frontend for gphoto2 - header files.

%description devel -l pl.UTF-8
Interfejs KDE do gphoto2 - pliki nagłówkowe.

%prep
%setup -q

%build
%cmake -B build \
	-DDIGIKAMSC_COMPILE_KIPIPLUGINS=ON \
	-DENABLE_AKONADICONTACTSUPPORT:BOOL=ON \
	-DENABLE_APPSTYLES:BOOL=ON \
	-DENABLE_KFILEMETADATASUPPORT:BOOL=ON \
	-DENABLE_MEDIAPLAYER:BOOL=ON \
	-DENABLE_MYSQLSUPPORT:BOOL=ON \
	-DENABLE_INTERNALMYSQL:BOOL=ON \
	-DENABLE_OPENCV3:BOOL=ON \
	-DBUILD_TESTING:BOOL=OFF \
	-DBUILD_WITH_QT6:BOOL=ON

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS CODE_OF_CONDUCT.md ChangeLog NEWS README.md
%attr(755,root,root) %{_bindir}/cleanup_digikamdb
%attr(755,root,root) %{_bindir}/digikam
%attr(755,root,root) %{_bindir}/digitaglinktree
%attr(755,root,root) %{_bindir}/showfoto
%{_libdir}/libdigikamdatabase.so.*.*.*
%{_libdir}/libdigikamgui.so.*.*
%{_libdir}/libdigikamcore.so.*.*.*
%dir %{_libdir}/qt6/plugins
%{_datadir}/knotifications6/digikam.notifyrc
%dir %{_libdir}/qt6/plugins/digikam
%dir %{_libdir}/qt6/plugins/digikam/bqm
%{_libdir}/qt6/plugins/digikam/bqm/Bqm_*_Plugin.so
%dir %{_libdir}/qt6/plugins/digikam/dimg
%{_libdir}/qt6/plugins/digikam/dimg/DImg_*_Plugin.so
%dir %{_libdir}/qt6/plugins/digikam/editor
%{_libdir}/qt6/plugins/digikam/editor/Editor_*_Plugin.so
%dir %{_libdir}/qt6/plugins/digikam/generic
%{_libdir}/qt6/plugins/digikam/generic/Generic_*_Plugin.so
%dir %{_libdir}/qt6/plugins/digikam/marble
%{_libdir}/qt6/plugins/digikam/marble/*FloatItem.so
%{_libdir}/qt6/plugins/digikam/marble/*Plugin.so
%{_libdir}/qt6/plugins/digikam/marble/MeasureTool.so
%{_libdir}/qt6/plugins/digikam/marble/OverviewMap.so
%dir %{_libdir}/qt6/plugins/digikam/rawimport
%{_libdir}/qt6/plugins/digikam/rawimport/RawImport_*_Plugin.so
%{_datadir}/%{name}
%{_datadir}/kxmlgui5/digikam
%{_datadir}/kxmlgui5/showfoto
%{_datadir}/metainfo/org.kde.digikam.appdata.xml
%{_datadir}/metainfo/org.kde.showfoto.appdata.xml
%{_datadir}/showfoto
%{_datadir}/solid/actions/digikam-opencamera.desktop
%{_desktopdir}/org.kde.digikam.desktop
%{_desktopdir}/org.kde.showfoto.desktop
%{_iconsdir}/hicolor/32x32/actions/albumfolder-*.png
%{_iconsdir}/hicolor/32x32/actions/tag.png
%{_iconsdir}/hicolor/32x32/actions/tag-*.png
%{_iconsdir}/hicolor/*x*/apps/digikam.png
%{_iconsdir}/hicolor/*x*/apps/dk-*.png
%{_iconsdir}/hicolor/*x*/apps/expoblending.png
%{_iconsdir}/hicolor/*x*/apps/panorama.png
%{_iconsdir}/hicolor/*x*/apps/showfoto.png
%{_iconsdir}/hicolor/scalable/apps/digikam.svgz
%{_iconsdir}/hicolor/scalable/apps/dk-*.svgz
%{_iconsdir}/hicolor/scalable/apps/panorama.svgz
%{_iconsdir}/hicolor/scalable/apps/showfoto.svgz
%{_mandir}/man1/digitaglinktree.1*
%{_mandir}/man1/cleanup_digikamdb.1*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libdigikamcore.so
%{_libdir}/libdigikamdatabase.so
%{_libdir}/libdigikamgui.so
%{_includedir}/digikam
%{_libdir}/cmake/DigikamCore
%{_libdir}/cmake/DigikamDatabase
%{_libdir}/cmake/DigikamGui
%{_libdir}/cmake/DigikamPlugin
