Summary:	A KDE frontend for gphoto2
Summary(pl):	Interfejs KDE do gphoto2
Name:		digikam
Version:	0.6
Release:	1.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/digikam/%{name}-%{version}.tar.bz2
# Source0-md5:	c841d1bbd51d0105f545f106451d5ae5
URL:		http://digikam.sourceforge.net/
BuildRequires:	kdelibs-devel
BuildRequires:	libgphoto2-devel
BuildRequires:	libexif-devel >= 0.5.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _htmldir        /usr/share/doc/kde/HTML

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
Requires:	%{name} = %{version}

%description devel
A KDE frontend for gphoto2 - header files

%description -l pl
Interfejs KDE do gphoto2 - pliki nag³ówkowe

%prep
%setup -q 

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

#%{__make} -f admin/Makefile.common configure.in
#cp admin/acinclude.m4.in ./acinclude.m4
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
/usr/bin/perl -w admin/am_edit

%configure \
	--disable-rpath

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-kde

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_libdir}/*.*.*.*
%{_libdir}/kde3/*
%{_applnkdir}/Graphics/*
%{_datadir}/services/*
%{_datadir}/servicetypes/*
%{_datadir}/apps/digikam
%{_datadir}/apps/digikamcameraclient
%{_pixmapsdir}/[!l]*/*/*/*
%{_mandir}/man1/*

%files devel
%{_includedir}/digikam
%{_libdir}/*.la
%{_libdir}/*.so
