Name:           ros-minimalist-message-generation
Version:        0.4.0
Release:        0%{?dist}
Summary:        ROS message_generation package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/message_generation
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-minimalist-gencpp
Requires:       ros-minimalist-geneus
Requires:       ros-minimalist-genlisp
Requires:       ros-minimalist-genmsg
Requires:       ros-minimalist-gennodejs
Requires:       ros-minimalist-genpy
BuildRequires:  ros-minimalist-catkin

%description
Package modeling the build-time dependencies for generating language bindings of
messages.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/minimalist/setup.sh" ]; then . "/opt/ros/minimalist/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/minimalist" \
        -DCMAKE_PREFIX_PATH="/opt/ros/minimalist" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/minimalist/setup.sh" ]; then . "/opt/ros/minimalist/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/minimalist

%changelog
* Tue Oct 18 2016 Dirk Thomas <dthomas@osrfoundation.org> - 0.4.0-0
- Autogenerated by Bloom

