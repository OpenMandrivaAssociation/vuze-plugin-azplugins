
%define plugin	azplugins

Name:		vuze-plugin-%plugin
Version:	2.1.6
Release:	3
Summary:	Vuze plugin: Azureus Core Plugins
Group:		Networking/File transfer
License:	GPLv2+
URL:		http://azureus.sourceforge.net/
Source0:	http://azureus.sourceforge.net/plugins/%{plugin}_%{version}.jar
BuildRequires:	vuze
BuildRequires:	java-rpmbuild
BuildRequires:	ant
BuildRequires:	locales-en
Requires:	vuze
BuildArch:      noarch

%description
This contains the Tracker Web Templates and IRC Client plugins.

Tracker web pages can be customised by extracting them from the plugin
JAR file and placing them in a directory called "web" under the Azureus
user-data directory. When extracting them ensure that the prefix
directory hierarchy of "org/gudy/azureus2/ui/tracker/templates" is
*removed* leaving, for example, "index.tmpl" in the "web" directory.

This package is part of default vuze installation.

%prep
%setup -q -c
find -name '*.class' -delete
ln -s %{_datadir}/azureus/build.plugins.xml build.xml
[ -e plugin.properties ] && ! grep -q plugin.version plugin.properties

%build
export LC_ALL=ISO-8859-1
CLASSPATH="%{_datadir}/azureus/Azureus2.jar:$(build-classpath swt)" %ant makejar -Dsource.dir=. -Dplugin.version=%{version}

%install
install -d -m755 %{buildroot}%{_datadir}/azureus/plugins/%plugin
install -m644 %{plugin}_%{version}.jar %{buildroot}%{_datadir}/azureus/plugins/%plugin

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir %{_datadir}/azureus/plugins/%plugin
%{_datadir}/azureus/plugins/%plugin/%{plugin}_%{version}.jar


%changelog
* Sun Sep 20 2009 Anssi Hannula <anssi@mandriva.org> 2.1.6-1mdv2010.0
+ Revision: 445727
- initial Mandriva release

