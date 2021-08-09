Name:           tinyxml2
Version:        9.0.0
Release:        1
Summary:        Simple, small and efficient C++ XML parser

Group:          Development/Libraries
License:        zlib
URL:            https://github.com/leethomason/tinyxml2
Source :        %{name}-%{version}.tar.gz
BuildRequires:  cmake

%description
TinyXML-2 is a simple, small, efficient, C++ XML parser that can be
easily integrated into other programs. It uses a Document Object Model
(DOM), meaning the XML data is parsed into a C++ objects that can be
browsed and manipulated, and then written to disk or another output stream.

TinyXML-2 doesn't parse or use DTDs (Document Type Definitions) nor XSLs
(eXtensible Stylesheet Language).

TinyXML-2 uses a similar API to TinyXML-1, But the implementation of the
parser was completely re-written to make it more appropriate for use in a
game. It uses less memory, is faster, and uses far fewer memory allocations.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the libraries and header files that are needed
for writing applications with the %{name} library.

%prep
%autosetup -n %{name}-%{version}/upstream
chmod -c -x *.cpp *.h

%build
mkdir -p objdir
cd objdir
%cmake .. -DBUILD_STATIC_LIBS=OFF
make

%install
rm -rf %{buildroot}
cd objdir
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc readme.md
%{_libdir}/lib%{name}.so.%{version}
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}/%{name}-config-version.cmake
%{_libdir}/cmake/%{name}/%{name}-config.cmake
%{_libdir}/cmake/%{name}/%{name}-shared-targets-noconfig.cmake
%{_libdir}/cmake/%{name}/%{name}-shared-targets.cmake
