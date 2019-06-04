%define url_ver %(echo %{version}|cut -d. -f1,2)

%define debug_package %{nil}

%define api	0.10
%define major	10
%define libname	%mklibname %{name} %{api} %{major}
%define devname	%mklibname -d %{name} %{api}
%define girname	%mklibname %{name}-gir %{api}

%define _disable_rebuild_configure 1

Summary:	Set of document centric objects and utilities for GLib/GTK
Name:		goffice
Version:	0.10.45
Release:	1
License:	GPLv2+
Group:		System/Libraries
Url:		http://www.gnome.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/goffice/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	perl-IO-Compress
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libgsf-1)
BuildRequires:	pkgconfig(libpcre)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(libxslt)

%description
There are common operations for document centric applications that are
conceptually simple, but complex to implement fully.
 - plugins
 - load/save documents
 - undo/redo

%files -f %{name}-%{version}.lang
%doc README NEWS AUTHORS BUGS MAINTAINERS
%{_libdir}/%{name}/%{version}/
%dir %{_libdir}/%{name}/
%{_datadir}/%{name}

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	%{summary}
Group:		%{group}

%description -n %{libname}
Shared library implementing document centric objects and utilities for
GLib/GTK.

%files -n %{libname}
%{_libdir}/libgoffice-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%files -n %{girname}
%{_libdir}/girepository-1.0/GOffice-%{api}.typelib

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	%{summary}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Requires:	%{girname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Development files of the Goffice library.

%files -n %{devname}
%{_includedir}/libgoffice-%{api}/
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gtk-doc/html/goffice-%{api}/
%{_datadir}/gir-1.0/*.gir

#----------------------------------------------------------------------------

%prep
%setup -q

%build

export CC=gcc
%configure2_5x \
	--disable-static \
	--enable-introspection=yes

%make

%install
%makeinstall_std
%find_lang %{name}-%{version}

