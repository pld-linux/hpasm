Summary:	HP Server Management Drivers and Agents
Name:		hpasm
Version:	7.7.0
Release:	0.1
License:	2006 Hewlett-Packard Development Company, L.P.
Group:		Applications
#Source0:	ftp://ftp.compaq.com/pub/products/servers/supportsoftware/linux/hpasm-6.30.0-12.Redhat8_0.i386.rpm
Source0:	ftp://ftp.compaq.com/pub/products/servers/supportsoftware/linux/%{name}-%{version}-115.rhel4.x86_64.rpm
# NoSource0-md5:	97aac9286c4f12a6881600d3b5addd7d
NoSource:	0
URL:		http://h18000.www1.hp.com/products/servers/linux/documentation.html
BuildRequires:	rpm-utils
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The hp System Health Application and Insight Management Agents package
provides extended capabilities to ProLiant Servers. These capabilities
include monitoring of temperature thresholds, fan, processor and
memory failures. Should a parameter be out of normal operating
conditions, the Linux operating system will be automatically shutdown.
The hp Advanced Server Management Application(hpasmd) is the interface
to the Advanced Server Management (ASM) ASIC. This application will
work with both the P roLiant ASM (0x0E11A0F1) and the ProLiant iLO
Advance Server Management (0x0E11B203) ASICs. The hpasmd also provides
an inter face so other software can log events to the hp ProLiant
Integrated Management Log (IML).

hp Server, Storage and Foundation Agents for Linux provide a full
spectrum of management data. This package includes the Server Standard
Equipment and Health Agent for hp Servers. It also contains the hp Web
Agent. This information is available using the hp Insight Manager
Console, any Internet browser, or other management applications using
SNMP.

%prep
%setup -qcT
rpm2cpio %{SOURCE0} | cpio -i -d
gzip -d usr/share/man/man*/*.gz

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/sbin
cd opt/compaq/utils
install bootcfg $RPM_BUILD_ROOT/sbin
install cpqimlview $RPM_BUILD_ROOT/sbin
install cpqimlview.tcl $RPM_BUILD_ROOT/sbin
install hpasmcli $RPM_BUILD_ROOT/sbin
install hpimlview $RPM_BUILD_ROOT/sbin
install hplog $RPM_BUILD_ROOT/sbin
install hpuid $RPM_BUILD_ROOT/sbin
install imlbe $RPM_BUILD_ROOT/sbin
cd -

install -d $RPM_BUILD_ROOT/etc/rc.d/init.d
install etc/init.d/hpasm $RPM_BUILD_ROOT/etc/rc.d/init.d

install -d $RPM_BUILD_ROOT%{_mandir}/man{4,8}
cp -a usr/share/man/man4/* $RPM_BUILD_ROOT%{_mandir}/man4
cp -a usr/share/man/man8/* $RPM_BUILD_ROOT%{_mandir}/man8

install -d $RPM_BUILD_ROOT%{_pixmapsdir}
cd opt/compaq/utils
cp -a hplogo.xbm $RPM_BUILD_ROOT%{_pixmapsdir}
cp -a m_blue.gif $RPM_BUILD_ROOT%{_pixmapsdir}
cp -a m_fail.gif $RPM_BUILD_ROOT%{_pixmapsdir}
cp -a m_green.gif $RPM_BUILD_ROOT%{_pixmapsdir}
cp -a m_red.gif $RPM_BUILD_ROOT%{_pixmapsdir}
cp -a m_yellow.gif $RPM_BUILD_ROOT%{_pixmapsdir}
cd -

# opt/hp/hpsmh/
# opt/compaq/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/hpasm
%attr(755,root,root) /sbin/bootcfg
%attr(755,root,root) /sbin/cpqimlview
%attr(755,root,root) /sbin/cpqimlview.tcl
%attr(755,root,root) /sbin/hpasmcli
%attr(755,root,root) /sbin/hpimlview
%attr(755,root,root) /sbin/hplog
%attr(755,root,root) /sbin/hpuid
%attr(755,root,root) /sbin/imlbe
%{_mandir}/man4/hpasm.4*
%{_mandir}/man4/hpasmcli.4*
%{_mandir}/man8/cpqimlview.8*
%{_mandir}/man8/hplog.8*
%{_mandir}/man8/hpuid.8*
%{_pixmapsdir}/hplogo.xbm
%{_pixmapsdir}/m_blue.gif
%{_pixmapsdir}/m_fail.gif
%{_pixmapsdir}/m_green.gif
%{_pixmapsdir}/m_red.gif
%{_pixmapsdir}/m_yellow.gif
