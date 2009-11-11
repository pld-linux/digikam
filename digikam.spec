#
%define		qtver	4.5.3
%define		kdever	4.2.4
%define		state	beta6

Summary:	A KDE frontend for gphoto2
Summary(pl.UTF-8):	Interfejs KDE do gphoto2
Name:		digikam
Version:	1.0.0
Release:	0.%{state}.1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/digikam/%{name}-%{version}-%{state}.tar.bz2
# Source0-md5:	a71462082f84891f20fc98d180c0f46e
URL:		http://www.digikam.org/
Patch0:		%{name}-link.patch
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtDesigner-devel >= %{qtver}
BuildRequires:	QtSql-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	automoc4
BuildRequires:	cmake >= 2.6.2
BuildRequires:	jasper-devel
#BuildRequires:	kde4-kdeedu-devel >= %{kdever}
BuildRequires:	kde4-kdegraphics-devel >= %{kdever}
BuildRequires:	kde4-kdepimlibs-devel >= %{kdever}
BuildRequires:	lcms-devel
BuildRequires:	lensfun-devel
BuildRequires:	libgphoto2-devel
BuildRequires:	liblqr-devel >= 0.4.0
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
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
%setup -q -n %{name}-%{version}-%{state}
%patch0 -p0

%build
# explicitely remove hne language support (re-add when glibc supports it)
%{__sed} -i -e 's/add_subdirectory(hne)//g' po/CMakeLists.txt
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
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
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/cleanup_digikamdb
%attr(755,root,root) %{_bindir}/digikam
%dir %{_datadir}/apps/digikam/utils
%attr(755,root,root) %{_datadir}/apps/digikam/utils/digikam-camera
%attr(755,root,root) %{_bindir}/digitaglinktree
%attr(755,root,root) %{_bindir}/showfoto
%attr(755,root,root) %ghost %{_libdir}/libdigikamdatabase.so.1
%attr(755,root,root) %{_libdir}/libdigikamdatabase.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdigikamcore.so.1
%attr(755,root,root) %{_libdir}/libdigikamcore.so.*.*.*
%attr(755,root,root) %{_libdir}/kde4/digikamimageplugin_*.so
%attr(755,root,root) %{_libdir}/kde4/digikamnepomukservice.so
%attr(755,root,root) %{_libdir}/kde4/kio_digikamalbums.so
%attr(755,root,root) %{_libdir}/kde4/kio_digikamdates.so
%attr(755,root,root) %{_libdir}/kde4/kio_digikamsearch.so
%attr(755,root,root) %{_libdir}/kde4/kio_digikamtags.so
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
%{_datadir}/apps/digikam/themes
%{_datadir}/apps/digikam/tips
%{_datadir}/apps/showfoto
%{_datadir}/kde4/services/digikamalbums.protocol
%{_datadir}/kde4/services/digikamdates.protocol
%{_datadir}/kde4/services/digikamimageplugin_*.desktop
%{_datadir}/kde4/services/digikamnepomukservice.desktop
%{_datadir}/kde4/services/digikamsearch.protocol
%{_datadir}/kde4/services/digikamtags.protocol
%{_datadir}/apps/solid/actions/digikam-opencamera.desktop
%{_datadir}/kde4/servicetypes/digikamimageplugin.desktop
%{_iconsdir}/*/*/apps/*.png
%{_desktopdir}/kde4/*.desktop

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdigikamcore.so
%attr(755,root,root) %{_libdir}/libdigikamdatabase.so
%{_includedir}/*.h
%{_includedir}/digikam
