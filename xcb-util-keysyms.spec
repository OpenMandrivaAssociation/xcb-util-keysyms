%ifarch %{x86_64}
%bcond_without compat32
%endif

%define major 1
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d
%define lib32name %mklib32name %{name} %{major}
%define devel32name %mklib32name %{name} -d

%global optflags %{optflags} -O3

Summary:	xcb-util's xcb-keysyms
Name:		xcb-util-keysyms
Version:	0.4.1
Release:	2
Url:		https://xcb.freedesktop.org
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.xz
License:	MIT
Group:		System/X11
BuildRequires:	pkgconfig(xcb-util)
BuildRequires:	pkgconfig(xorg-macros)
%if %{with compat32}
BuildRequires:	devel(libxcb-util)
BuildRequires:	devel(libxcb)
BuildRequires:	devel(libXau)
BuildRequires:	devel(libX11)
BuildRequires:	devel(libXdmcp)
%endif

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
Provides:	xcb-util-keysyms-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Conflicts:	%{mklibname xcb-util -d} < 0.3.9
Conflicts:	%{mklibname xcb-util -d -s} < 0.3.9

%description -n %{develname}
This pakcage includes the development files required to build software against
%{name}.

%if %{with compat32}
%package -n %{lib32name}
Summary:	xcb-util-keysyms library package (32-bit)
Group:		System/X11

%description -n %{lib32name}
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

This is the xcb-util-keysyms library package.

%package -n %{devel32name}
Summary:	xcb-util-keysyms development files (32-bit)
Group:		Development/C
Requires:	%{develname} = %{version}-%{release}
Requires:	%{lib32name} = %{version}-%{release}

%description -n %{devel32name}
This pakcage includes the development files required to build software against
%{name}.
%endif

%prep
%autosetup -p1
export CONFIGURE_TOP="$(pwd)"

%if %{with compat32}
mkdir build32
cd build32
%configure32 --with-pic
cd ..
%endif

mkdir build
cd build
%configure --with-pic

%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build

%files -n %{libname}
%{_libdir}/libxcb-keysyms.so.%{major}*

%files -n %{develname}
%doc ChangeLog NEWS README.md
%{_includedir}/xcb/xcb_keysyms.h
%{_libdir}/libxcb-keysyms.so
%{_libdir}/pkgconfig/xcb-keysyms.pc

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libxcb-keysyms.so.%{major}*

%files -n %{devel32name}
%{_prefix}/lib/libxcb-keysyms.so
%{_prefix}/lib/pkgconfig/xcb-keysyms.pc
%endif
