
Summary:	A KDE frontend for gphoto2
Summary(pl):	Interfejs KDE do gphoto2
Name:		digikam
Version:	0.6.2
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://digikam.free.fr/Tarballs/%{name}-%{version}.tar.bz2
# Source0-md5:	842fd284823b48392a659936246da685
Patch0:		%{name}-desktop.patch
URL:		http://digikam.sourceforge.net/
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRequires:	kdesdk-po2xml
BuildRequires:	libexif-devel >= 1:0.5.7
BuildRequires:	libgphoto2-devel
BuildRequires:	lockdev-devel
BuildRequires:	imlib-devel
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

%description -l pl
Interfejs KDE do gphoto2 - pliki nag³ówkowe.

%prep
%setup -q -n %{name}3
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin

#%%{__make} -f admin/Makefile.common configure.in
#cp admin/acinclude.m4.in ./acinclude.m4
#%%{__libtoolize}
#%%{__aclocal}
#%%{__autoconf}
#%%{__autoheader}
#%%{__automake}
#%%{__perl} -w admin/am_edit

%configure \
	--disable-rpath

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	'kde_htmldir=%{_kdedocdir}'
install -d $RPM_BUILD_ROOT%{_desktopdir}/kde
mv $RPM_BUILD_ROOT/usr/share/applnk/Graphics/*.desktop $RPM_BUILD_ROOT%{_desktopdir}/kde
install -d $RPM_BUILD_ROOT%{_desktopdir}/kde

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*.*.*
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_libdir}/kde3/*.la
%{_datadir}/services/*
%{_datadir}/servicetypes/*
%{_datadir}/apps/digikam
%{_datadir}/apps/digikamcameraclient
%{_desktopdir}/kde/*.desktop
%{_iconsdir}/[!l]*/*/*/*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/digikam
