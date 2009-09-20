
%define plugin	azplugins

Name:		vuze-plugin-%plugin
Version:	2.1.6
Release:	%mkrel 1
Summary:	Vuze plugin: Azureus Core Plugins
Group:		Networking/File transfer
License:	GPLv2+
URL:		http://azureus.sourceforge.net/
Source0:	http://azureus.sourceforge.net/plugins/%{plugin}_%{version}.jar
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	vuze
BuildRequires:	java-rpmbuild
BuildRequires:	ant
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
CLASSPATH="%{_datadir}/azureus/Azureus2.jar:$(build-classpath swt)" %ant makejar -Dsource.dir=. -Dplugin.version=%{version}

%install
rm -rf %{buildroot}

install -d -m755 %{buildroot}%{_datadir}/azureus/plugins/%plugin
install -m644 %{plugin}_%{version}.jar %{buildroot}%{_datadir}/azureus/plugins/%plugin

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir %{_datadir}/azureus/plugins/%plugin
%{_datadir}/azureus/plugins/%plugin/%{plugin}_%{version}.jar
