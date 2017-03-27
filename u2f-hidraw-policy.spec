Summary:	Udev rule to allow desktop access to HIDRAW U2F tokens
Name:		u2f-hidraw-policy
Version:	1.0.2
Release:	1
License:	LGPL v2+
Group:		Base
Source0:	https://github.com/amluto/u2f-hidraw-policy/archive/%{version}.tar.gz
# Source0-md5:	daf17918427fff12ccd5d0ce7dc53e27
URL:		https://github.com/amluto/u2f-hidraw-policy/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
u2f-hidraw-policy is a udev helper that detects U2F HID tokens as
described by the U2F spec.

%prep
%setup -q

%build
%{__make} \
	CFLAGS="%{rpmcflags} %{rpmcppflags} %{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
/lib/udev/rules.d/60-u2f-hidraw.rules
%attr(755,root,root) /lib/udev/u2f_hidraw_id
