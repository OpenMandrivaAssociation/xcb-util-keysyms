%define major 1
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	xcb-util's xcb-keysyms
Name:		xcb-util-keysyms
Version:	0.3.9
Release:	6
Url:		http://xcb.freedesktop.org
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
License:	MIT
Group:		System/X11
BuildRequires:	xcb-util-devel >= 0.3.9
BuildRequires:	x11-util-macros

%description
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%package -n %{libname}
Summary:	xcb-util-keysyms library package
Group:		System/X11
Conflicts:	%{mklibname xcb-keysyms 1} < 0.3.9

%description -n %{libname}
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

This is the xcb-util-keysyms library package.

%package -n %{develname}
Summary:	xcb-util-keysyms development files
Group:		Development/C
Provides:	libxcb-util-keysyms-devel = %{version}-%{release}
Provides:	xcb-util-keysyms-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Conflicts:	%{mklibname xcb-util -d} < 0.3.9
Conflicts:	%{mklibname xcb-util -d -s} < 0.3.9

%description -n %{develname}
This pakcage includes the development files required to build software against
%{name}.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libxcb-keysyms.so.%{major}*

%files -n %{develname}
%doc ChangeLog NEWS README
%{_includedir}/xcb/xcb_keysyms.h
%{_libdir}/libxcb-keysyms.so
%{_libdir}/pkgconfig/xcb-keysyms.pc


%changelog
* Mon Jun 04 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.3.9-1
+ Revision: 802331
- versioning fix
- version update 0.3.9

* Mon Feb 20 2012 Götz Waschk <waschk@mandriva.org> 0.3.8-2
+ Revision: 778050
- remove libtool archive

* Wed Oct 26 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.8-1
+ Revision: 707426
- import xcb-util-keysyms

