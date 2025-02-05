#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : qt6positioning
Version  : 6.8.2
Release  : 23
URL      : https://download.qt.io/official_releases/qt/6.8/6.8.2/submodules/qtpositioning-everywhere-src-6.8.2.zip
Source0  : https://download.qt.io/official_releases/qt/6.8/6.8.2/submodules/qtpositioning-everywhere-src-6.8.2.zip
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause GPL-2.0 GPL-3.0 LGPL-3.0 MIT
Requires: qt6positioning-lib = %{version}-%{release}
Requires: qt6positioning-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : pkg-config
BuildRequires : pkgconfig(gconf-2.0)
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package dev
Summary: dev components for the qt6positioning package.
Group: Development
Requires: qt6positioning-lib = %{version}-%{release}
Provides: qt6positioning-devel = %{version}-%{release}
Requires: qt6positioning = %{version}-%{release}

%description dev
dev components for the qt6positioning package.


%package lib
Summary: lib components for the qt6positioning package.
Group: Libraries
Requires: qt6positioning-license = %{version}-%{release}

%description lib
lib components for the qt6positioning package.


%package license
Summary: license components for the qt6positioning package.
Group: Default

%description license
license components for the qt6positioning package.


%prep
%setup -q -n qtpositioning-everywhere-src-6.8.2
cd %{_builddir}/qtpositioning-everywhere-src-6.8.2
pushd ..
cp -a qtpositioning-everywhere-src-6.8.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1738727247
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1738727247
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qt6positioning
cp %{_builddir}/qtpositioning-everywhere-src-%{version}/LICENSES/Apache-2.0.txt %{buildroot}/usr/share/package-licenses/qt6positioning/47b573e3824cd5e02a1a3ae99e2735b49e0256e4 || :
cp %{_builddir}/qtpositioning-everywhere-src-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/qt6positioning/79453f55fa8ee32d7b95581473edcbfd043e088f || :
cp %{_builddir}/qtpositioning-everywhere-src-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/qt6positioning/dc8f2e570bf431427dbc3bab9d4d551b53a60208 || :
cp %{_builddir}/qtpositioning-everywhere-src-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6positioning/7713a1753ce88f2c7e6b054ecc8e4c786df76300 || :
cp %{_builddir}/qtpositioning-everywhere-src-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6positioning/c70af14df11e3908dfc10397b1ba4b1f346661f3 || :
cp %{_builddir}/qtpositioning-everywhere-src-%{version}/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/qt6positioning/b31da5a75ef0821e013c5f5c3c3e3665ab20164b || :
cp %{_builddir}/qtpositioning-everywhere-src-%{version}/src/3rdparty/clip2tri/LICENSE %{buildroot}/usr/share/package-licenses/qt6positioning/4601642edc66a5a475be477c87b256d7a315151b || :
cp %{_builddir}/qtpositioning-everywhere-src-%{version}/src/3rdparty/poly2tri/LICENSE %{buildroot}/usr/share/package-licenses/qt6positioning/a5f7956759837791f77cd59a8b2818455494dc8a || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/QtPositioning/6.8.2/QtPositioning/private/qclipperutils_p.h
/usr/include/QtPositioning/6.8.2/QtPositioning/private/qdoublematrix4x4_p.h
/usr/include/QtPositioning/6.8.2/QtPositioning/private/qdoublevector2d_p.h
/usr/include/QtPositioning/6.8.2/QtPositioning/private/qdoublevector3d_p.h
/usr/include/QtPositioning/6.8.2/QtPositioning/private/qgeoaddress_p.h
/usr/include/QtPositioning/6.8.2/QtPositioning/private/qgeocircle_p.h
/usr/include/QtPositioning/6.8.2/QtPositioning/private/qgeocoordinate_p.h
/usr/include/QtPositioning/6.8.2/QtPositioning/private/qgeocoordinateobject_p.h
/usr/include/QtPositioning/6.8.2/QtPositioning/private/qgeolocation_p.h
/usr/include/QtPositioning/6.8.2/QtPositioning/private/qgeopath_p.h
/usr/include/QtPositioning/6.8.2/QtPositioning/private/qgeopolygon_p.h
/usr/include/QtPositioning/6.8.2/QtPositioning/private/qgeopositioninfo_p.h
/usr/include/QtPositioning/6.8.2/QtPositioning/private/qgeopositioninfosource_p.h
/usr/include/QtPositioning/6.8.2/QtPositioning/private/qgeorectangle_p.h
/usr/include/QtPositioning/6.8.2/QtPositioning/private/qgeosatelliteinfo_p.h
/usr/include/QtPositioning/6.8.2/QtPositioning/private/qgeosatelliteinfosource_p.h
/usr/include/QtPositioning/6.8.2/QtPositioning/private/qgeoshape_p.h
/usr/include/QtPositioning/6.8.2/QtPositioning/private/qlocationutils_p.h
/usr/include/QtPositioning/6.8.2/QtPositioning/private/qnmeapositioninfosource_p.h
/usr/include/QtPositioning/6.8.2/QtPositioning/private/qnmeasatelliteinfosource_p.h
/usr/include/QtPositioning/6.8.2/QtPositioning/private/qpositioningglobal_p.h
/usr/include/QtPositioning/6.8.2/QtPositioning/private/qtpositioning-config_p.h
/usr/include/QtPositioning/6.8.2/QtPositioning/private/qwebmercator_p.h
/usr/include/QtPositioning/QGeoAddress
/usr/include/QtPositioning/QGeoAreaMonitorInfo
/usr/include/QtPositioning/QGeoAreaMonitorSource
/usr/include/QtPositioning/QGeoCircle
/usr/include/QtPositioning/QGeoCoordinate
/usr/include/QtPositioning/QGeoLocation
/usr/include/QtPositioning/QGeoPath
/usr/include/QtPositioning/QGeoPolygon
/usr/include/QtPositioning/QGeoPositionInfo
/usr/include/QtPositioning/QGeoPositionInfoSource
/usr/include/QtPositioning/QGeoPositionInfoSourceFactory
/usr/include/QtPositioning/QGeoRectangle
/usr/include/QtPositioning/QGeoSatelliteInfo
/usr/include/QtPositioning/QGeoSatelliteInfoSource
/usr/include/QtPositioning/QGeoShape
/usr/include/QtPositioning/QNmeaPositionInfoSource
/usr/include/QtPositioning/QNmeaSatelliteInfoSource
/usr/include/QtPositioning/QtPositioning
/usr/include/QtPositioning/QtPositioningDepends
/usr/include/QtPositioning/QtPositioningVersion
/usr/include/QtPositioning/qgeoaddress.h
/usr/include/QtPositioning/qgeoareamonitorinfo.h
/usr/include/QtPositioning/qgeoareamonitorsource.h
/usr/include/QtPositioning/qgeocircle.h
/usr/include/QtPositioning/qgeocoordinate.h
/usr/include/QtPositioning/qgeolocation.h
/usr/include/QtPositioning/qgeopath.h
/usr/include/QtPositioning/qgeopolygon.h
/usr/include/QtPositioning/qgeopositioninfo.h
/usr/include/QtPositioning/qgeopositioninfosource.h
/usr/include/QtPositioning/qgeopositioninfosourcefactory.h
/usr/include/QtPositioning/qgeorectangle.h
/usr/include/QtPositioning/qgeosatelliteinfo.h
/usr/include/QtPositioning/qgeosatelliteinfosource.h
/usr/include/QtPositioning/qgeoshape.h
/usr/include/QtPositioning/qnmeapositioninfosource.h
/usr/include/QtPositioning/qnmeasatelliteinfosource.h
/usr/include/QtPositioning/qpositioningglobal.h
/usr/include/QtPositioning/qtpositioning-config.h
/usr/include/QtPositioning/qtpositioningexports.h
/usr/include/QtPositioning/qtpositioningversion.h
/usr/lib64/cmake/Qt6/FindGconf.cmake
/usr/lib64/cmake/Qt6/FindGypsy.cmake
/usr/lib64/cmake/Qt6BuildInternals/StandaloneTests/QtPositioningTestsConfig.cmake
/usr/lib64/cmake/Qt6Bundled_Clip2Tri/Qt6Bundled_Clip2TriDependencies.cmake
/usr/lib64/cmake/Qt6Positioning/Qt6PositioningAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Positioning/Qt6PositioningConfig.cmake
/usr/lib64/cmake/Qt6Positioning/Qt6PositioningConfigVersion.cmake
/usr/lib64/cmake/Qt6Positioning/Qt6PositioningConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Positioning/Qt6PositioningDependencies.cmake
/usr/lib64/cmake/Qt6Positioning/Qt6PositioningPlugins.cmake
/usr/lib64/cmake/Qt6Positioning/Qt6PositioningTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Positioning/Qt6PositioningTargets.cmake
/usr/lib64/cmake/Qt6Positioning/Qt6PositioningVersionlessAliasTargets.cmake
/usr/lib64/cmake/Qt6Positioning/Qt6PositioningVersionlessTargets.cmake
/usr/lib64/cmake/Qt6Positioning/Qt6QGeoPositionInfoSourceFactoryGeoclue2PluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Positioning/Qt6QGeoPositionInfoSourceFactoryGeoclue2PluginConfig.cmake
/usr/lib64/cmake/Qt6Positioning/Qt6QGeoPositionInfoSourceFactoryGeoclue2PluginConfigVersion.cmake
/usr/lib64/cmake/Qt6Positioning/Qt6QGeoPositionInfoSourceFactoryGeoclue2PluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Positioning/Qt6QGeoPositionInfoSourceFactoryGeoclue2PluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Positioning/Qt6QGeoPositionInfoSourceFactoryGeoclue2PluginTargets.cmake
/usr/lib64/cmake/Qt6Positioning/Qt6QGeoPositionInfoSourceFactoryNmeaPluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Positioning/Qt6QGeoPositionInfoSourceFactoryNmeaPluginConfig.cmake
/usr/lib64/cmake/Qt6Positioning/Qt6QGeoPositionInfoSourceFactoryNmeaPluginConfigVersion.cmake
/usr/lib64/cmake/Qt6Positioning/Qt6QGeoPositionInfoSourceFactoryNmeaPluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Positioning/Qt6QGeoPositionInfoSourceFactoryNmeaPluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Positioning/Qt6QGeoPositionInfoSourceFactoryNmeaPluginTargets.cmake
/usr/lib64/cmake/Qt6Positioning/Qt6QGeoPositionInfoSourceFactoryPollPluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Positioning/Qt6QGeoPositionInfoSourceFactoryPollPluginConfig.cmake
/usr/lib64/cmake/Qt6Positioning/Qt6QGeoPositionInfoSourceFactoryPollPluginConfigVersion.cmake
/usr/lib64/cmake/Qt6Positioning/Qt6QGeoPositionInfoSourceFactoryPollPluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Positioning/Qt6QGeoPositionInfoSourceFactoryPollPluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Positioning/Qt6QGeoPositionInfoSourceFactoryPollPluginTargets.cmake
/usr/lib64/libQt6Positioning.prl
/usr/lib64/libQt6Positioning.so
/usr/lib64/pkgconfig/Qt6Positioning.pc
/usr/lib64/qt6/mkspecs/modules/qt_lib_positioning.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_positioning_private.pri

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libQt6Positioning.so.6.8.2
/V3/usr/lib64/qt6/plugins/position/libqtposition_geoclue2.so
/V3/usr/lib64/qt6/plugins/position/libqtposition_nmea.so
/V3/usr/lib64/qt6/plugins/position/libqtposition_positionpoll.so
/usr/lib64/libQt6Positioning.so.6
/usr/lib64/libQt6Positioning.so.6.8.2
/usr/lib64/qt6/metatypes/qt6positioning_relwithdebinfo_metatypes.json
/usr/lib64/qt6/modules/Positioning.json
/usr/lib64/qt6/plugins/position/libqtposition_geoclue2.so
/usr/lib64/qt6/plugins/position/libqtposition_nmea.so
/usr/lib64/qt6/plugins/position/libqtposition_positionpoll.so
/usr/lib64/qt6/sbom/qtpositioning-6.8.2.spdx

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qt6positioning/4601642edc66a5a475be477c87b256d7a315151b
/usr/share/package-licenses/qt6positioning/47b573e3824cd5e02a1a3ae99e2735b49e0256e4
/usr/share/package-licenses/qt6positioning/7713a1753ce88f2c7e6b054ecc8e4c786df76300
/usr/share/package-licenses/qt6positioning/79453f55fa8ee32d7b95581473edcbfd043e088f
/usr/share/package-licenses/qt6positioning/a5f7956759837791f77cd59a8b2818455494dc8a
/usr/share/package-licenses/qt6positioning/b31da5a75ef0821e013c5f5c3c3e3665ab20164b
/usr/share/package-licenses/qt6positioning/c70af14df11e3908dfc10397b1ba4b1f346661f3
/usr/share/package-licenses/qt6positioning/dc8f2e570bf431427dbc3bab9d4d551b53a60208
