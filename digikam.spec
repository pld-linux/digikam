%define		_snap	rc2
Summary:	A KDE frontend for gphoto2
Summary(pl):	Interfejs KDE do gphoto2
Name:		digikam
Version:	0.9.0
Release:	0.%{_snap}.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/digikam/%{name}-%{version}-%{_snap}.tar.bz2
# Source0-md5:	2285dc1f5c52769e99cbfe1a6d24ac45
URL:		http://digikam.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	exiv2-devel >= 0.12
BuildRequires:	gdbm-devel
BuildRequires:	imlib2-devel
BuildRequires:	kdelibs-devel
BuildRequires:	kdesdk-po2xml
BuildRequires:	libstdc++-devel
BuildRequires:	libgphoto2-devel
BuildRequires:	libkexif-devel >= 0.2
BuildRequires:	libkipi-devel >= 0.1
BuildRequires:	libtiff-devel
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
BuildRequires:	sqlite3-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Designed to be a standalone application to preview and download images
from a digital camera on a Linux machine.

%description -l pl
Samodzielna aplikacja do ogl±dania i ¶ci±gania obrazków z aparatów
cyfrowych pod Linuksem.

%package devel
Summary:	A KDE frontend for gphoto2 - header files
Summary(pl):	Interfejs KDE do gphoto2 - pliki nag³ówkowe
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	kdelibs-devel
Requires:	libgphoto2-devel

%description devel
A KDE frontend for gphoto2 - header files.

%description devel -l pl
Interfejs KDE do gphoto2 - pliki nag³ówkowe.

%prep
%setup -q -n %{name}-%{version}-%{_snap}

%build

%{__sed} -i -e "s,Categories.*,Categories=Qt;KDE;Graphics;Photograph;," \
	./digikam/digikam/digikam.desktop \
	./digikam/showfoto/showfoto.desktop
echo "# vi: encoding=utf-8" >> ./digikam/digikam/digikam.desktop
echo "# vi: encoding=utf-8" >> ./digikam/showfoto/showfoto.desktop
echo "# vi: encoding=utf-8" >> ./digikam/imageplugins/digikamimageplugin_core.desktop
echo "# vi: encoding=utf-8" >> ./digikam/utilities/imageeditor/digikamimageplugin.desktop

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
%{_libdir}/kde3/*.la
%{_datadir}/services/*
%{_datadir}/servicetypes/*
%{_datadir}/apps/digikam
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
