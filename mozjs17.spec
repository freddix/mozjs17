Summary:	JavaScript interpreter and libraries
Name:		mozjs17
Version:	17.0.0
Release:	1
License:	MPL 1.1 or GPL v2+ or LGPL v2.1+
Group:		Libraries
Source0:	http://ftp.mozilla.org/pub/mozilla.org/js/mozjs%{version}.tar.gz
# Source0-md5:	20b6f8f1140ef6e47daa3b16965c9202
URL:		http://www.mozilla.org/js/
BuildRequires:	libstdc++-devel
BuildRequires:	nspr-devel >= 4.7.0
BuildRequires:	perl-base
BuildRequires:	python
BuildRequires:	readline-devel
BuildRequires:	rpm-perlprov
BuildRequires:	sed >= 4.0
Provides:	js = %{version}-%{release}
Obsoletes:	js < %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JavaScript Reference Implementation (codename SpiderMonkey). The
package contains JavaScript runtime (compiler, interpreter,
decompiler, garbage collector, atom manager, standard classes) and
small "shell" program that can be used interactively and with .js
files to run scripts.

%package devel
Summary:	Header files for JavaScript reference library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
Provides:	js-devel = %{version}-%{release}
Obsoletes:	js-devel < %{version}-%{release}

%description devel
Header files for JavaScript reference library.

%prep
%setup -qn mozjs%{version}

%build
cd js/src
%configure2_13 \
	--enable-readline	\
	--enable-threadsafe	\
	--with-system-ffi	\
	--with-system-nspr
%{__make}

%check
%{__make} -j1 -C js/src check

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C js/src install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc js/src/README.html
%attr(755,root,root) %{_bindir}/js17
%attr(755,root,root) %{_libdir}/libmozjs-17.0.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/js17-config
%{_includedir}/js-17.0
%{_pkgconfigdir}/mozjs-17.0.pc

