# TODO
# - build Qt GUI for Linux Crash (spec/lkcdutils-qlcrash.spec)
# - make it build
# - cflags
# - has patched bfd, see if it still needed
Summary:	Linux Kernel Crash Dump (LKCD) Utilities
Name:		lkcdutils
Version:	6.2.0
Release:	0.1
License:	- (enter GPL/GPL v2/GPL v3/LGPL/BSD/BSD-like/other license name here)
Group:		Applications
Source0:	http://dl.sourceforge.net/lkcd/%{name}-%{version}.tar.gz
# Source0-md5:	8cd68ff9115d210d4f1c6458929559a3
URL:		http://lkcd.sourceforge.net/
BuildRequires:	byacc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This software package contains system crash dump analyzer tools. It
includes Linux Crash (lcrash) and all appropriate user level scripts
required for saving and configuring system crash dumps. This package
should be installed after the lkcd kernel patches are installed on the
system.

%prep
%setup -q -n %{name}

%build
# not autotools generated configure
./configure \
	--prefix=%{_prefix} \
	--mandir=%{_mandir} \

#	--cflags=%{rpmcflags} \
#	--lflags=%{rpmldflags}

%{__make}
%ifnarch s390 s390x
%{__make} -C netdump
%endif

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%ifnarch s390 s390x
%{__make} -C netdump install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%ifarch s390 s390x
# We do not need these files for s390 and s390x
rm -f $RPM_BUILD_ROOT/etc/sysconfig/dump \
	$RPM_BUILD_ROOT/sbin/lkcd \
	$RPM_BUILD_ROOT/sbin/lkcd_config \
$RPM_BUILD_ROOT%{_prefix}/man/man1/lkcd_config.1*
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
