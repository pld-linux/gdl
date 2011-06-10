Summary:	GNOME Devtool Libraries
Summary(pl.UTF-8):	Biblioteki GNOME Devtool
Name:		gdl
Version:	2.30.1
Release:	2
License:	GPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gdl/2.30/%{name}-%{version}.tar.bz2
# Source0-md5:	4af16be490b47ce4e828a2fb93633856
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.16.0
BuildRequires:	gtk-doc >= 1.4
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	pkgconfig
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains components and libraries that are intended to be
shared between GNOME development tools, including gnome-debug,
gnome-build, and anjuta2. The current pieces of GDL include: a symbol
browser bonobo component (symbol-browser-control), a docking widget
(gdl), a utility library that also contains the stubs and skels for
the symbol browser and text editor components (gdl, idl).

%description -l pl.UTF-8
Ten pakiet zawiera komponenty i biblioteki zaprojektowane jako wspólne
dla różnych narzędzi programistycznych GNOME, takich jak: gnome-debug,
gnome-build i anjuta2. Aktualnie GDL zawiera: przeglądarkę symboli
jako komponent bonobo (symbol-browser-control), dokowany element
interfejsu graficznego (gdl), bibliotekę narzędzi zawierającą także
szkielety dla przeglądarki symboli i komponentów edytora tekstu (gdl,
idl).

%package devel
Summary:	Header files for gdl development
Summary(pl.UTF-8):	Pliki nagłówkowe do biblioteki gdl
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.16.0
Requires:	libxml2-devel >= 1:2.6.26

%description devel
This package contains the header files needed to develop programs that
use these gdl.

%description devel -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających bibliotek gdl.

%package static
Summary:	Static libraries for gdl development
Summary(pl.UTF-8):	Statyczne biblioteki gdl
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains the static gdl libraries.

%description static -l pl.UTF-8
Pakiet zawiera statyczne biblioteki gdl.

%package apidocs
Summary:	gdl library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki gdl
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
gdl library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki gdl.

%prep
%setup -q

%build
%{__glib_gettextize}
%{__gtkdocize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--with-html-dir=%{_gtkdocdir} \
	--enable-gtk-doc \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}-1

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}-1.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libgdl-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgdl-1.so.3
%{_datadir}/gdl

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgdl-1.so
%{_includedir}/libgdl-1.0
%{_libdir}/libgdl-1.la
%{_pkgconfigdir}/gdl-1.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgdl-1.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gdl
