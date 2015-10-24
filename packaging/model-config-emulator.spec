Name:		model-config-emulator
Summary:	A Model configuration
Version:	0.0.2
Release:	0
Group:		System/Configuration
License:	Apache-2.0
BuildArch:	noarch
Source0:	%{name}-%{version}.tar.gz

%if "%{?tizen_profile_name}" == "tv"
ExcludeArch: %{arm}
%endif
%if "%{?tizen_profile_name}" == "wearable"
ExcludeArch: %{arm}
%endif
%if "%{?tizen_profile_name}" == "mobile"
ExcludeArch: %{arm}
%endif

%description
Model configuration data package

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/etc/config
%if "%{?tizen_profile_name}" == "wearable"
cp -f model-config_wearable.xml %{buildroot}/etc/config/model-config.xml
%else
%if "%{?tizen_profile_name}" == "mobile"
cp -f model-config_mobile.xml %{buildroot}/etc/config/model-config.xml
%else
cp -f model-config.xml %{buildroot}/etc/config/model-config.xml
%endif
%endif

mkdir -p %{buildroot}/usr/share/license
cp %{_builddir}/%{name}-%{version}/LICENSE.Apache-2.0 %{buildroot}/usr/share/license/%{name}

%files
/usr/share/license/%{name}
/etc/config/model-config.xml
%manifest model-config.manifest
