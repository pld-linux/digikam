
Summary:	A KDE frontend for gphoto2
Summary(pl.UTF-8):	Interfejs KDE do gphoto2
Name:		digikam
Version:	0.9.3
Release:	2
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/digikam/%{name}-%{version}.tar.bz2
# Source0-md5:	20497c1a02394505f899ef0757ebefad
Patch0:		kde-ac260-lt.patch
URL:		http://digikam.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	exiv2-devel >= 0.14
BuildRequires:	jasper-devel >= 1.7.0
BuildRequires:	kdelibs-devel
BuildRequires:	libgphoto2-devel
BuildRequires:	libkdcraw-devel >= 0.1.2
BuildRequires:	libkexiv2-devel >= 0.1.5
BuildRequires:	libkipi-devel >= 0.1
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
BuildRequires:	sqlite3-devel
Obsoletes:	digikamimageplugins
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
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
Requires:	kdelibs-devel
Requires:	libgphoto2-devel

%description devel
A KDE frontend for gphoto2 - header files.

%description devel -l pl.UTF-8
Interfejs KDE do gphoto2 - pliki nagłówkowe.

%prep
%setup -q
%patch0 -p1

%{__sed} -i -e "s,Categories.*,Categories=Qt;KDE;Graphics;Photograph;," \
	./digikam/digikam/digikam.desktop \
	./digikam/showfoto/showfoto.desktop
echo "# vi: encoding=utf-8" >> ./digikam/digikam/digikam.desktop
echo "# vi: encoding=utf-8" >> ./digikam/showfoto/showfoto.desktop
echo "# vi: encoding=utf-8" >> ./digikam/imageplugins/digikamimageplugin_core.desktop
echo "# vi: encoding=utf-8" >> ./digikam/utilities/imageeditor/digikamimageplugin.desktop

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--disable-rpath \
	--with-qt-libraries=%{_libdir} \
	--with-imlib2-config=%{_bindir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

rm $RPM_BUILD_ROOT%{_libdir}/kde3/*.la

[ -d $RPM_BUILD_ROOT%{_datadir}/locale/sr@latin ] || \
	mv -f $RPM_BUILD_ROOT%{_datadir}/locale/sr@{Latn,latin}
%find_lang %{name} --with-kde --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*.*.*
%attr(755,root,root) %{_libdir}/kde3/*.so
%attr(755,root,root) %{_datadir}/apps/digikam/utils/digikam-camera
%dir %{_datadir}/apps/digikam
%dir %{_datadir}/apps/digikam/utils
%{_datadir}/apps/digikam/icons
%{_datadir}/apps/digikam/themes
%{_datadir}/apps/digikam/about
%{_datadir}/apps/digikam/data
%{_datadir}/apps/digikam/profiles
%{_datadir}/apps/digikam/tips
%{_datadir}/apps/digikam/digikam-splash.png
%{_datadir}/apps/digikam/*.rc
%{_datadir}/services/*
%{_datadir}/servicetypes/*
%{_datadir}/apps/showfoto
%{_datadir}/apps/konqueror/servicemenus/digikam-*.desktop
%{_desktopdir}/kde/*.desktop
%{_iconsdir}/[!l]*/*/*/*
%{_mandir}/man1/digitaglinktree.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/*.h
%{_includedir}/digikam
