# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.25
# 

Name:       sdk-webapp

# >> macros
# << macros

Summary:    Mer SDK manager
Version:    0.5.6
Release:    1
Group:      Development Platform/Platform SDK
License:    GPLv2+
Source0:    sdk-webapp.tar.bz2
Source1:    sdk-webapp.service
Source100:  sdk-webapp.yaml
Requires:   sdk-webapp-bundle >= 0.4.0
Requires:   sdk-webapp-customization >= 0.4.0-2

%description
Allows web-based management of the Mer SDK. Adds toolchains, targets etc

%package mer
Summary:    Mer customization for SDK management web-application
Group:      Development Platform/Platform SDK
Requires:   %{name} = %{version}-%{release}
Provides:   sdk-webapp-customization

%description mer
Gives SDK manager it's default mer-ish look


%prep
%setup -q -n src

# >> setup
# << setup

%build
# >> build pre
# << build pre


make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
mkdir -p %{buildroot}%{_libdir}/systemd/user/
cp %{_sourcedir}/%{name}.service %{buildroot}%{_libdir}/systemd/user/
# << install post


%post
# >> post
/bin/ln -sf %{_libdir}/systemd/user/%{name}.service %{_sysconfdir}/systemd/system/multi-user.target.wants/
systemctl --system daemon-reload
systemctl start %{name}.service
# << post

%postun
# >> postun
if [ "$1" = "0" ]; then
# Perform tasks to prepare for the uninstallation
rm %{_sysconfdir}/systemd/system/multi-user.target.wants/%{name}.service
fi
systemctl --system daemon-reload
# << postun

%files
%defattr(-,root,root,-)
%{_libdir}/%{name}-bundle/config.ru
%{_libdir}/%{name}-bundle/sdk_helper.rb
%{_libdir}/%{name}-bundle/shell_process.rb
%{_libdir}/%{name}-bundle/i18n/en.ts
%{_libdir}/systemd/user/%{name}.service
%{_libdir}/%{name}-bundle/views/default.sass
%{_libdir}/%{name}-bundle/views/index.haml
%{_libdir}/%{name}-bundle/views/layout.haml
%{_libdir}/%{name}-bundle/views/targets.haml
%{_libdir}/%{name}-bundle/views/packages.haml
%{_libdir}/%{name}-bundle/views/toolchains.haml
%{_libdir}/%{name}-bundle/public/ttf
%{_libdir}/%{name}-bundle/public/css
# >> files
# << files

%files mer
%defattr(-,root,root,-)
%{_libdir}/%{name}-bundle/target_servers.rb
%{_libdir}/%{name}-bundle/views/index.sass
%{_libdir}/%{name}-bundle/public/images
# >> files mer
# << files mer
