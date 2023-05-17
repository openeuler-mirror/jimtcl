Name:           jimtcl
Version:        0.82
Release:        1
Summary:        A small embeddable Tcl interpreter
License:        BSD-2-Clause-Views
URL:            http://jim.tcl.tk
Source0:        https://github.com/msteveb/jimtcl/archive/%{version}/jimtcl-%{version}.tar.gz

BuildRequires:  asciidoc gcc-c++ make	
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(hiredis)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  hostname

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
rm -rf sqlite3

%build
export CC=gcc LD=ld AR=ar RANLIB=ranlib STRIP=strip
%ifarch loongarch64
rm -rf autosetup/autosetup-config.sub
rm -rf autosetup/autosetup-config.guess
/usr/bin/cp -fv /usr/lib/rpm/openEuler/config.guess autosetup/autosetup-config.guess
/usr/bin/cp -fv /usr/lib/rpm/openEuler/config.sub autosetup/autosetup-config.sub
%endif

%configure --shared --disable-option-checking --allextmod --docdir=%{_datadir}/doc/%{name}
%make_build

%check
rm tests/ssl.test
make test

%install
%make_install INSTALL_DOCS=nodocs
rm %{buildroot}/%{_libdir}/jim/README.extensions

%files
%license LICENSE
%doc AUTHORS README README.ensemble README.extensions README.namespaces
%doc README.oo README.redis README.sqlite README.utf-8
%doc %{_datadir}/doc/%{name}/Tcl.html
%{_bindir}/jimdb
%{_bindir}/jimsh
%dir %{_libdir}/jim
%{_libdir}/jim/*.tcl
%{_libdir}/jim/*.so
%{_libdir}/libjim.so.*

%files devel
%doc DEVELOPING STYLE
%{_includedir}/*
%{_bindir}/build-jim-ext
%{_libdir}/libjim.so
%{_libdir}/pkgconfig/jimtcl.pc

%changelog
* Wed May 17 2023 liyanan <thistleslyn@163.com> - 0.82-1
- update to 0.82

* Tue Dec 13 2022 Wenlong Zhang<zhangwenlong@loongson.cn> - 0.78-5
- update autosetup-config.guess and autosetup-config.sub to support loongarch

* Wed May 11 2022 wulei <wulei80@h-partners.com> - 0.78-4
- License compliance rectification

* Thu Jun 03 2021 wulei <wulei80@huawei.com> - 0.78-3
- fixes failed: Could not find a C compiler

* Tue Nov 05 2019 Lijin Yang <yanglijin@huawei.com> - 0.78-2
- inital package

