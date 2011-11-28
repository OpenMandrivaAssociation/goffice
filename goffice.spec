%define name goffice
%define version 0.8.17

%define api 0.8
%define major 8
%define libname %mklibname %name %{api}_%major
%define develname %mklibname -d %name %api

Summary: Set of document centric objects and utilities for glib/gtk
Name: goffice
Version: 0.8.17
Release: 2
Source0: http://ftp.gnome.org/pub/GNOME/sources/goffice/%{name}-%{version}.tar.xz
License: GPLv2
Group: System/Libraries
Url: http://www.gnome.org

BuildRequires:	automake1.8
BuildRequires:	intltool
BuildRequires: gtk+2-devel
BuildRequires: libGConf2-devel dbus-glib-devel
BuildRequires: libgsf-devel >= 1:1.14.9
BuildRequires: libglade2.0-devel
BuildRequires: pcre libpcre-devel
BuildRequires: gtk-doc
BuildRequires: intltool
Obsoletes: goffice0.6 < 0.6.5-2
Obsoletes: goffice21 < 0.2.2-2

%description
There are common operations for document centric applications that are
conceptually simple, but complex to implement fully.
    - plugins
    - load/save documents
    - undo/redo

%package -n %libname
Summary:  %{summary}
Group: %{group}

%description -n %libname
Shared library implementing document centric objects and utilities for glib/gtk

%package -n %develname
Summary:  %{summary}
Group: Development/C
Requires: %libname = %version
Provides: %name-devel = %version-%release
Provides: lib%name-devel = %version-%release
Conflicts: %mklibname -d goffice 0_3
Conflicts: %mklibname -d goffice 0_4
Obsoletes: %mklibname -d goffice 0.5_5

%description -n %develname
Development files of the Goffice library.

%prep
%setup -q

%build
%configure2_5x 
#gw http://bugzilla.gnome.org/show_bug.cgi?id=580377
#--enable-gtk-doc
%make

%install
rm -rf $RPM_BUILD_ROOT %name-%version.lang
%makeinstall_std
%find_lang %name-%version
find %buildroot -name \*.la|xargs chmod 644

%files -f %name-%version.lang
%doc README NEWS AUTHORS BUGS MAINTAINERS
%_libdir/%name/%version/
%_datadir/%name
%_datadir/pixmaps/%name
%dir %_libdir/%name/

%files -n %libname
%_libdir/libgoffice-%api.so.%{major}*

%files -n %develname
%_includedir/libgoffice-%{api}/
%_libdir/lib*.so
%attr(644,root,root) %_libdir/lib*a
%_libdir/pkgconfig/*.pc
%_datadir/gtk-doc/html/goffice-%api/

