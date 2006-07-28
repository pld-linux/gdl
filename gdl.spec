Summary:	GNOME Devtool Libraries
Summary(pl):	Biblioteki GNOME Devtool
Name:		gdl
Version:	0.6.1
Release:	2
License:	GPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/gdl/0.6/%{name}-%{version}.tar.bz2
# Source0-md5:	6d902981efe30950af8f5033d937c270
Patch0:		%{name}-broken_locale.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.12.0
BuildRequires:	intltool
BuildRequires:	libbonoboui-devel >= 2.14.0
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgnomeui-devel >= 2.15.90
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains components and libraries that are intended to be
shared between GNOME development tools, including gnome-debug,
gnome-build, and anjuta2. The current pieces of GDL include: a symbol
browser bonobo component (symbol-browser-control), a docking widget
(gdl), a utility library that also contains the stubs and skels for
the symbol browser and text editor components (gdl, idl).

%description -l pl
Ten pakiet zawiera komponenty i biblioteki zaprojektowane jako wspólne
dla ró¿nych narzêdzi programistycznych GNOME, takich jak: gnome-debug,
gnome-build i anjuta2. Aktualnie GDL zawiera: przegl±darkê symboli
jako komponent bonobo (symbol-browser-control), dokowany element
interfejsu graficznego (gdl), bibliotekê narzêdzi zawieraj±c± tak¿e
szkielety dla przegl±darki symboli i komponentów edytora tekstu (gdl,
idl).

%package devel
Summary:	Header files for gdl development
Summary(pl):	Pliki nag³ówkowe do biblioteki gdl
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files needed to develop programs that
use these gdl.

%description devel -l pl
Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych bibliotek gdl.

%package static
Summary:	Static libraries for gdl development
Summary(pl):	Statyczne biblioteki gdl
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains the static gdl libraries.

%description static -l pl
Pakiet zawiera statyczne biblioteki gdl.

%prep
%setup -q
%patch0 -p1

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}-1 --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}-1.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_datadir}/gdl

%files devel
%defattr(644,root,root,755)
%{_includedir}/libgdl-1.0
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
