%define		_snap	040918
Summary:	A KDE frontend for gphoto2
Summary(pl):	Interfejs KDE do gphoto2
Name:		digikam
Version:	0.7.0
Release:	0.%{_snap}.1
License:	GPL
Group:		X11/Applications
#Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source0:	%{name}-%{_snap}.tar.bz2
# Source0-md5:	54e1b0b5697b90a439fd9734550c50bf
URL:		http://digikam.sourceforge.net/
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRequires:	kdesdk-po2xml
BuildRequires:	libexif-devel >= 1:0.5.7
BuildRequires:	libgphoto2-devel
BuildRequires:	lockdev-devel
BuildRequires:	imlib2-devel
BuildRequires:	libkipi-devel
BuildRequires:	libkexif-devel
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
%setup -q -n %{name}

%{__sed} -i -e "s,Terminal=0,Terminal=false,g" \
	./digikam/digikam/digikam.desktop \
	./digikam/imageplugins/digikamimageplugin_core.desktop \
	./digikam/digikamcameraclient/digikamcameraclient.desktop \
	./digikam/utilities/imageeditor/digikamimageplugin.desktop
echo "Categories=Qt;KDE;Graphics;Photograph;" >> ./digikam/digikam/digikam.desktop
echo "# vi: encoding=utf-8" >> ./digikam/digikam/digikam.desktop
echo "# vi: encoding=utf-8" >> ./digikam/imageplugins/digikamimageplugin_core.desktop
echo "# vi: encoding=utf-8" >> ./digikam/digikamcameraclient/digikamcameraclient.desktop
echo "# vi: encoding=utf-8" >> ./digikam/utilities/imageeditor/digikamimageplugin.desktop

%build
cp -f /usr/share/automake/config.sub admin
export UNSERMAKE=/usr/share/unsermake/unsermake
%{__make} -f admin/Makefile.common cvs

%configure \
	--disable-rpath \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT%{_desktopdir}/kde
mv $RPM_BUILD_ROOT/usr/share/applnk/Graphics/*.desktop $RPM_BUILD_ROOT%{_desktopdir}/kde


#find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

#%files -f %{name}.lang
%files 
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*.*.*
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_libdir}/kde3/*.la
%{_datadir}/services/*
%{_datadir}/servicetypes/*
%{_datadir}/apps/digikam
%{_desktopdir}/kde/*.desktop
%{_iconsdir}/[!l]*/*/*/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/digikam
