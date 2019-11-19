Name:           jimtcl
Version:        0.78
Release:        2
Summary:        A small embeddable Tcl interpreter
License:        BSD
URL:            http://jim.tcl.tk
Source0:        https://github.com/msteveb/jimtcl/archive/%{version}/jimtcl-%{version}.tar.gz

BuildRequires:  asciidoc

%description
Jim is an opensource small-footprint implementation of the Tcl programming language.
It implements a large subset of Tcl and adds new features like references with garbage
collection, closures, built-in Object Oriented Programming system, Functional Programming
commands, first-class arrays and UTF-8 support. All this with a binary size of about
100-200kB (depending upon selected options).

%package        devel
Summary:        Development files for jimtcl
Requires:       jimtcl = %{version}-%{release}

%description    devel
This package contains libraries and header files for developing applications that use jimtcl.

%prep
%autosetup -p1

%build
export CC=gcc LD=ld AR=ar RANLIB=ranlib STRIP=strip
%configure --full --shared --disable-option-checking
%make_build

%check
make test

%install
%make_install docdir=%{_docdir}/jimtcl
cd $RPM_BUILD_ROOT%{_libdir}; ln -s libjim.so.* libjim.so

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc LICENSE AUTHORS README
%{_docdir}/jimtcl/Tcl.html
%{_bindir}/jimsh
%{_libdir}/libjim.so.*

%files devel
%doc DEVELOPING README.metakit README.extensions README.namespaces README.oo README.utf-8 STYLE
%{_includedir}/
%{_bindir}/build-jim-ext
%{_libdir}/pkgconfig/jimtcl.pc
%{_libdir}/libjim.so
%exclude %{_datadir}/doc/jimtcl/
%exclude %{_libdir}/jim/{tcltest.tcl,README.extensions}

%changelog
* Tue Nov 05 2019 Lijin Yang <yanglijin@huawei.com> - 0.78-2
- inital package

