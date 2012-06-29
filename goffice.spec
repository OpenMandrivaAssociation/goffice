%define api	0.10
%define major	9
%define libname	%mklibname %{name} %{api} %major
%define devname	%mklibname -d %{name} %{api}
%define girname	%mklibname %{name}-gir %{api}

Summary:	Set of document centric objects and utilities for glib/gtk
Name:		goffice
Version:	0.9.4
Release:	1
License:	GPLv2
Group:		System/Libraries
Url:		http://www.gnome.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/goffice/%{name}-%{version}.tar.xz

BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(libgsf-1)
BuildRequires:	pkgconfig(libpcre)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)

%description
There are common operations for document centric applications that are
conceptually simple, but complex to implement fully.
 - plugins
 - load/save documents
 - undo/redo

%package -n %{libname}
Summary:	%{summary}
Group:		%{group}

%description -n %{libname}
Shared library implementing document centric objects and utilities for glib/gtk

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{devname}
Summary:	%{summary}
Group:		Development/C
Requires:	%{libname} = %{version}
Requires:	%{girname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Development files of the Goffice library.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static \
	--enable-introspection=yes

%make

%install
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%find_lang %{name}-%{version}

%files -f %{name}-%{version}.lang
%doc README NEWS AUTHORS BUGS MAINTAINERS
%{_libdir}/%{name}/%{version}/
%dir %{_libdir}/%{name}/

%files -n %{libname}
%{_libdir}/libgoffice-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/GOffice-%{api}.typelib

%files -n %{devname}
%{_includedir}/libgoffice-%{api}/
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gtk-doc/html/goffice-%{api}/
%{_datadir}/gir-1.0/*.gir

