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

%package static
Summary:	Static ... library
Group:		Development/Libraries
#Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ... library.

%prep
%setup -qcT
rpm2cpio %{SOURCE0} | cpio -i -d
gzip -d usr/share/man/man*/*.gz

# move to real locations instead of symlinks
install -d .{/%{_lib},/lib,%{_libdir},%{_prefix}/lib}
D=$(pwd)
cd opt/compaq/utils
mv bootcfg $D/sbin
mv cpqimlview $D/sbin
mv cpqimlview.tcl $D/sbin
mv hpasmcli $D/sbin
mv hpimlview $D/sbin
mv hplog $D/sbin
mv hpuid $D/sbin
mv imlbe $D/sbin
cd -

cd opt/compaq/utils
mv hplogo.xbm $D%{_pixmapsdir}
mv m_blue.gif $D%{_pixmapsdir}
mv m_fail.gif $D%{_pixmapsdir}
mv m_green.gif $D%{_pixmapsdir}
mv m_red.gif $D%{_pixmapsdir}
mv m_yellow.gif $D%{_pixmapsdir}
cd -

%if "%{_lib}" == "lib64"
mv opt/compaq/hpasm/addon/lib*64.so* $D/%{_lib}
mv opt/compaq/hpasm/addon/lib*64.a $D%{_libdir}
%endif
mv opt/compaq/hpasm/addon/lib*so* $D/lib
mv opt/compaq/hpasm/addon/lib*a $D%{_prefix}/lib

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/sbin
install sbin/* $RPM_BUILD_ROOT/sbin

install -d $RPM_BUILD_ROOT{/%{_lib},/lib,%{_libdir},%{_prefix}/lib}
cp -a ./%{_lib}/* $RPM_BUILD_ROOT/%{_lib}
%if "%{_lib}" != "lib"
cp -a ./lib/* $RPM_BUILD_ROOT/lib
%endif
cp -a ./%{_libdir}/* $RPM_BUILD_ROOT%{_libdir}
%if "%{_lib}" != "lib"
cp -a ./%{_prefix}/lib/* $RPM_BUILD_ROOT%{_prefix}/%{_lib}
%endif

install -d $RPM_BUILD_ROOT%{_pixmapsdir}
cp -a ./%{_pixmapsdir}/* $RPM_BUILD_ROOT%{_pixmapsdir}

install -d $RPM_BUILD_ROOT/etc/rc.d/init.d
install etc/init.d/hpasm $RPM_BUILD_ROOT/etc/rc.d/init.d

install -d $RPM_BUILD_ROOT%{_mandir}/man{4,8}
cp -a usr/share/man/man4/* $RPM_BUILD_ROOT%{_mandir}/man4
cp -a usr/share/man/man8/* $RPM_BUILD_ROOT%{_mandir}/man8

# opt/hp/hpsmh/
# opt/compaq/

%clean
rm -rf $RPM_BUILD_ROOT


%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

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
%attr(755,root,root) /lib/libcmacommon.so.1.0
%attr(755,root,root) /lib/libcmapeer.so.1.0
%attr(755,root,root) /lib/libcpqci.so.1.0
%attr(755,root,root) /lib/libhpasmintrfc.so.1.0
%attr(755,root,root) /lib/libhpev.so.1.0
%if "%{_lib}" == "lib64"
%attr(755,root,root) /%{_lib}/libcmaX64.so.1.0
%attr(755,root,root) /%{_lib}/libcpqci64.so.1.0
%attr(755,root,root) /%{_lib}/libhpasmintrfc64.so.1.0
%endif
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

%files static
%defattr(644,root,root,755)
%{_libdir}/libcpqci*.a
