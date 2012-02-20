%define major 1
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	xcb-util's xcb-keysyms
Name:		xcb-util-keysyms
Version:	0.3.8
Release:	%mkrel 2
Url:		http://xcb.freedesktop.org
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
License:	MIT
Group:		System/X11
BuildRequires:	xcb-util-devel >= 0.3.8
BuildRequires:	x11-util-macros
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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
Conflicts:	%{mklibname xcb-keysyms 1} < 0.3.8

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
Conflicts:	%{mklibname xcb-util -d} < 0.3.8
Conflicts:	%{mklibname xcb-util -d -s} < 0.3.8

%description -n %{develname}
This pakcage includes the development files required to build software against
%{name}.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %buildroot%_libdir/*.la

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libxcb-keysyms.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc ChangeLog NEWS README
%{_includedir}/xcb/xcb_keysyms.h
%{_libdir}/libxcb-keysyms.a
%{_libdir}/libxcb-keysyms.so
%{_libdir}/pkgconfig/xcb-keysyms.pc
