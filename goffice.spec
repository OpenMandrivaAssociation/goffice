%define name goffice
%define version 0.3.8

%define api 0
%define major 3
%define libname %mklibname %name %{api}_%major

Summary: Set of document centric objects and utilities for glib/gtk
Name: %{name}
Version: %{version}
Release: %mkrel 1
Source0: http://ftp.gnome.org/pub/GNOME/sources/goffice/%{name}-%{version}.tar.bz2
# (fc) 0.3.7-3mdv prevent crash for file with graphs with graph plugin disabled (GNOME bug #419955)
Patch0: goffice-0.3.7-fixcrash.patch
License: GPL
Group: System/Libraries
Url: http://www.gnome.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	automake1.8
BuildRequires:	intltool
BuildRequires: gtk+2-devel
BuildRequires: libgnomeprint-devel >= 2.8.2
BuildRequires: libgsf-devel >= 1:1.13.3
BuildRequires: libglade2.0-devel
BuildRequires: pcre libpcre-devel
BuildRequires: gtk-doc
BuildRequires: perl-XML-Parser

%description
There are common operations for document centric applications that are
conceptually simple, but complex to implement fully.
    - plugins
    - load/save documents
    - undo/redo

%package -n %libname
Summary:  %{summary}
Group: %{group}
Requires: %name >= %version

%description -n %libname
Shared library implementing document centric objects and utilities for glib/gtk

%package -n %libname-devel
Summary:  %{summary}
Group: Development/C
Requires: %libname = %version
Provides: %name-devel = %version-%release
Provides: lib%name-devel = %version-%release

%description -n %libname-devel
Development files of the Goffice library.

%prep
%setup -q
%patch0 -p1 -b .fixcrash

#fix build
aclocal-1.8
automake-1.8
autoconf

# remove generated files incorrectly in tarball (to be removed with 0.3.8)
rm -f goffice/goffice-paths.h

%build
%configure2_5x --enable-gtk-doc
%make

%install
rm -rf $RPM_BUILD_ROOT %name-%version.lang
%makeinstall_std
%find_lang %name-%version
find %buildroot -name \*.la|xargs chmod 644

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files -f %name-%version.lang
%defattr(-,root,root)
%doc README NEWS AUTHORS BUGS MAINTAINERS
%_datadir/%name
%_datadir/pixmaps/%name
%dir %_libdir/%name/

%files -n %libname
%defattr(-,root,root)
%_libdir/libgoffice-%api.so.%{major}*
%_libdir/%name/%version/

%files -n %libname-devel
%defattr(-,root,root)
%_includedir/libgoffice-0.3/
%_libdir/lib*.so
%attr(644,root,root) %_libdir/lib*a
%_libdir/pkgconfig/*.pc
%_datadir/gtk-doc/html/goffice/


