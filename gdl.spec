Summary:	Gnome Devtool Libraries
Name:		gdl
Version:	0.4.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/%{name}/0.4/%{name}-%{version}.tar.bz2
# Source0-md5:	eb4dfd9def266e4e5cd1e9883b5bdf2a
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libbonoboui-devel >= 2.2.0
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libgnomeui-devel >= 2.2.0
BuildRequires:	libtool
Requires(post):	GConf2
Requires(post):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains components and libraries that are intended to be
shared between GNOME development tools, including gnome-debug,
gnome-build, and anjuta2. The current pieces of GDL include: a symbol
browser bonobo component (symbol-browser-control), a docking widget (gdl),
a utility library that also contains the stubs and skels for the symbol
browser and text editor components (gdl, idl).

%package devel
Summary:	Header files for gdl development
Summary(pl):	Pliki nag³ówkowe do biblioteki gdl
Group:		Development/Libraries
Requires:	%{name} = %{version}

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
Requires:	%{name}-devel = %{version}

%description static
This package contains the static gdl libraries.

%description static -l pl
Pakiet zawiera statyczne biblioteki gdl.

%prep
%setup -q

%build
glib-gettextize --copy --force
%{__libtoolize}
%{__aclocal} -I %{_aclocaldir}/gnome2-macros
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang gdl-1 --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%gconf_schema_install

%postun -p /sbin/ldconfig

%files -f gdl-1.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_libdir}/bonobo/servers/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_datadir}/gdl
%{_datadir}/gnome-2.0/ui/*
%{_datadir}/idl/libgdl-1.0/*.idl

%files devel
%defattr(644,root,root,755)
%{_includedir}/libgdl-1.0
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
