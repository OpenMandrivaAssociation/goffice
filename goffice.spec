%define api 0.10
%define major 9
%define libname %mklibname %{name} %{api}_%major
%define develname %mklibname -d %{name} %{api}

Summary: Set of document centric objects and utilities for glib/gtk
Name: goffice
Version: 0.9.2
Release: 1
License: GPLv2
Group: System/Libraries
Url: http://www.gnome.org
Source0: http://ftp.gnome.org/pub/GNOME/sources/goffice/%{name}-%{version}.tar.xz

BuildRequires: gtk-doc
BuildRequires: intltool
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(gconf-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libglade-2.0)
BuildRequires: pkgconfig(libgsf-1)
BuildRequires: pkgconfig(libpcre)
BuildRequires: pkgconfig(librsvg-2.0)

%description
There are common operations for document centric applications that are
conceptually simple, but complex to implement fully.
 - plugins
 - load/save documents
 - undo/redo

%package -n %{libname}
Summary:  %{summary}
Group: %{group}

%description -n %{libname}
Shared library implementing document centric objects and utilities for glib/gtk

%package -n %{develname}
Summary:  %{summary}
Group: Development/C
Requires: %{libname} = %{version}
Provides: %{name}-devel = %{version}-%{release}

%description -n %{develname}
Development files of the Goffice library.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static
%make

%install
rm -rf %{buildroot} %{name}-%{version}.lang
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
%find_lang %{name}-%{version}

%files -f %{name}-%{version}.lang
%doc README NEWS AUTHORS BUGS MAINTAINERS
%{_libdir}/%{name}/%{version}/
%dir %{_libdir}/%{name}/

%files -n %{libname}
%{_libdir}/libgoffice-%{api}.so.%{major}*

%files -n %{develname}
%{_includedir}/libgoffice-%{api}/
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gtk-doc/html/goffice-%{api}/

