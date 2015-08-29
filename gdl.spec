#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	GNOME Devtools Library
Summary(pl.UTF-8):	Biblioteka GNOME Devtools Library
Name:		gdl
Version:	3.16.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gdl/3.16/%{name}-%{version}.tar.xz
# Source0-md5:	e4f976256b4e059033b82cf1fc866054
BuildRequires:	autoconf >= 2.65
BuildRequires:	automake >= 1:1.10
BuildRequires:	docbook-dtd43-xml
BuildRequires:	gettext-tools
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	gtk-doc >= 1.4
BuildRequires:	intltool >= 0.40.4
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	pkgconfig
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GNOME Devtools Library package provides a docking system and
several utilities useful to GNOME development tools and GNOME
applications in general.

%description -l pl.UTF-8
Pakiet GNOME Devtools Library zapewnia system dokujący oraz kilka
narzędzi przydatnych w narzędziach programistycznych GNOME oraz
ogólnie aplikacjach GNOME.

%package devel
Summary:	Header files for gdl development
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gdl
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+3-devel >= 3.0.0
Requires:	libxml2-devel >= 1:2.6.26

%description devel
This package contains the header files needed to develop programs that
use these gdl.

%description devel -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających bibliotek gdl.

%package static
Summary:	Static gdl library
Summary(pl.UTF-8):	Statyczna biblioteka gdl
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains the static gdl library.

%description static -l pl.UTF-8
Pakiet zawiera statyczną bibliotekę gdl.

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
#{__glib_gettextize}
%{__gtkdocize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gtk-doc \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static} \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name}-3

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}-3.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%attr(755,root,root) %{_libdir}/libgdl-3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgdl-3.so.5
%{_libdir}/girepository-1.0/Gdl-3.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgdl-3.so
%{_datadir}/gir-1.0/Gdl-3.gir
%{_includedir}/libgdl-3.0
%{_pkgconfigdir}/gdl-3.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgdl-3.a
%endif

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gdl-3.0
