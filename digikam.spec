#
%define		_beta	rc2
%define		qtver	4.4.3
%define		kdever	4.1.96

Summary:	A KDE frontend for gphoto2
Summary(pl.UTF-8):	Interfejs KDE do gphoto2
Name:		digikam
Version:	0.10.0
Release:	0.%{_beta}.1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/digikam/%{name}-%{version}-%{_beta}.tar.bz2
# Source0-md5:	7e149f44b3ba743ee6f8880ba748c282
URL:		http://digikam.sourceforge.net/
Patch0:		%{name}-link.patch
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtSql-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	automoc4
BuildRequires:	cmake >= 2.6.2
BuildRequires:	jasper-devel
BuildRequires:	kde4-kdegraphics-devel >= %{kdever}
BuildRequires:	kde4-kdepimlibs-devel >= %{kdever}
BuildRequires:	lcms-devel
BuildRequires:	lensfun-devel
BuildRequires:	libgphoto2-devel
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
# FIXME - add new BR
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
%setup -q -n %{name}-%{version}-%{_beta}
%patch0 -p0

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
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
%attr(755,root,root) %{_bindir}/digikam
%attr(755,root,root) %{_datadir}/apps/digikam/utils/digikam-camera
%attr(755,root,root) %{_bindir}/digikamthemedesigner
%attr(755,root,root) %{_bindir}/digitaglinktree
%attr(755,root,root) %{_bindir}/showfoto
%attr(755,root,root) %ghost %{_libdir}/libdigikamdatabase.so.1
%attr(755,root,root) %{_libdir}/libdigikamdatabase.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdigikamcore.so.1
%attr(755,root,root) %{_libdir}/libdigikamcore.so.*.*.*
%attr(755,root,root) %{_libdir}/kde4/digikamimageplugin_*.so
%attr(755,root,root) %{_libdir}/kde4/kio_digikamalbums.so
%attr(755,root,root) %{_libdir}/kde4/kio_digikamdates.so
%attr(755,root,root) %{_libdir}/kde4/kio_digikamsearch.so
%attr(755,root,root) %{_libdir}/kde4/kio_digikamtags.so
%{_mandir}/man1/digitaglinktree.1*
%dir %{_datadir}/apps/digikam
%{_datadir}/apps/digikam/about
%{_datadir}/apps/digikam/cameraui.rc
%{_datadir}/apps/digikam/data
%{_datadir}/apps/digikam/digikamimageplugin_*.rc
%{_datadir}/apps/digikam/digikamimagewindowui.rc
%{_datadir}/apps/digikam/digikamui.rc
%{_datadir}/apps/digikam/icons
%{_datadir}/apps/digikam/lighttablewindowui.rc
%{_datadir}/apps/digikam/themes
%{_datadir}/apps/digikam/tips
%{_datadir}/apps/showfoto
%{_datadir}/kde4/services/digikamalbums.protocol
%{_datadir}/kde4/services/digikamdates.protocol
%{_datadir}/kde4/services/digikamimageplugin_*.desktop
%{_datadir}/kde4/services/digikamsearch.protocol
%{_datadir}/kde4/services/digikamtags.protocol
%{_datadir}/apps/solid/actions/digikam-opencamera.desktop
%{_datadir}/kde4/servicetypes/digikamimageplugin.desktop
%{_desktopdir}/kde4/*.desktop
%exclude %{_iconsdir}/*/scalable
%{_iconsdir}/*/*/actions/adjustcurves.*
%{_iconsdir}/*/*/actions/adjusthsl.*
%{_iconsdir}/*/*/actions/adjustlevels.*
%{_iconsdir}/*/*/actions/adjustrgb.*
%{_iconsdir}/*/*/actions/antivignetting.*
%{_iconsdir}/*/*/actions/autocorrection.*
%{_iconsdir}/*/*/actions/blurfx.*
%{_iconsdir}/*/*/actions/blurimage.*
%{_iconsdir}/*/*/actions/bordertool.*
%{_iconsdir}/*/*/actions/bwtonal.*
%{_iconsdir}/*/*/actions/channelmixer.*
%{_iconsdir}/*/*/actions/charcoaltool.*
%{_iconsdir}/*/*/actions/colorfx.*
%{_iconsdir}/*/*/actions/colormanagement.*
%{_iconsdir}/*/*/actions/contrast.*
%{_iconsdir}/*/*/actions/depth16to8.*
%{_iconsdir}/*/*/actions/depth8to16.*
%{_iconsdir}/*/*/actions/distortionfx.*
%{_iconsdir}/*/*/actions/editimage.*
%{_iconsdir}/*/*/actions/embosstool.*
%{_iconsdir}/*/*/actions/exifinfo.*
%{_iconsdir}/*/*/actions/filmgrain.*
%{_iconsdir}/*/*/actions/freerotation.*
%{_iconsdir}/*/*/actions/hotpixels.*
%{_iconsdir}/*/*/actions/imagecomment.*
%{_iconsdir}/*/*/actions/infrared.*
%{_iconsdir}/*/*/actions/inpainting.*
%{_iconsdir}/*/*/actions/invertimage.*
%{_iconsdir}/*/*/actions/lensdistortion.*
%{_iconsdir}/*/*/actions/lighttable.*
%{_iconsdir}/*/*/actions/lighttableadd.*
%{_iconsdir}/*/*/actions/noisereduction.*
%{_iconsdir}/*/*/actions/oilpaint.*
%{_iconsdir}/*/*/actions/perspective.*
%{_iconsdir}/*/*/actions/raindrop.*
%{_iconsdir}/*/*/actions/ratiocrop.*
%{_iconsdir}/*/*/actions/redeyes.*
%{_iconsdir}/*/*/actions/restoration.*
%{_iconsdir}/*/*/actions/sharpenimage.*
%{_iconsdir}/*/*/actions/shear.*
%{_iconsdir}/*/*/actions/superimpose.*
%{_iconsdir}/*/*/actions/texture.*
%{_iconsdir}/*/*/actions/transform-crop-and-resize.*
%{_iconsdir}/*/*/actions/viewimage.*
%{_iconsdir}/*/*/actions/view-object-histogram-linear.*
%{_iconsdir}/*/*/actions/view-object-histogram-logarithmic.*
%{_iconsdir}/*/*/actions/whitebalance.*
%{_iconsdir}/*/*/actions/zoom-select-fit.*
%{_iconsdir}/*/*/apps/digikam.*
%{_iconsdir}/*/*/apps/showfoto.*
%{_iconsdir}/*/*/mimetypes/raw.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdigikamcore.so
%attr(755,root,root) %{_libdir}/libdigikamdatabase.so
%{_includedir}/*.h
%{_includedir}/digikam
