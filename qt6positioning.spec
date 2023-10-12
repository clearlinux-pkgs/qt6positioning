#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
Name     : qt6positioning
Version  : 6.6.0
Release  : 2
URL      : https://download.qt.io/official_releases/qt/6.6/6.6.0/submodules/qtpositioning-everywhere-src-6.6.0.tar.xz
Source0  : https://download.qt.io/official_releases/qt/6.6/6.6.0/submodules/qtpositioning-everywhere-src-6.6.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause BSL-1.0 CC0-1.0 GFDL-1.3 GPL-2.0 GPL-3.0 LGPL-3.0 MIT
Requires: qt6positioning-lib = %{version}-%{release}
Requires: qt6positioning-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : mesa-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(gconf-2.0)
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
The scalable icons are from:
http://tango.freedesktop.org/Tango_Icon_Library
http://darkobra.deviantart.com/art/Tango-Weather-Icon-Pack-98024429

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
%setup -q -n qtpositioning-everywhere-src-6.6.0
cd %{_builddir}/qtpositioning-everywhere-src-6.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1697148274
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
%cmake ..
make  %{?_smp_mflags}
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
export SOURCE_DATE_EPOCH=1697148274
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qt6positioning
cp %{_builddir}/qtpositioning-everywhere-src-%{version}/LICENSES/Apache-2.0.txt %{buildroot}/usr/share/package-licenses/qt6positioning/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/qtpositioning-everywhere-src-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/qt6positioning/b073f11f0c81a95ab5e32aa6b5d23a5955a95274 || :
cp %{_builddir}/qtpositioning-everywhere-src-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/qt6positioning/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/qtpositioning-everywhere-src-%{version}/LICENSES/GFDL-1.3-no-invariants-only.txt %{buildroot}/usr/share/package-licenses/qt6positioning/715f995f11805ee85601834220c43b082f457ea3 || :
cp %{_builddir}/qtpositioning-everywhere-src-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/qt6positioning/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/qtpositioning-everywhere-src-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6positioning/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/qtpositioning-everywhere-src-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6positioning/f45ee1c765646813b442ca58de72e20a64a7ddba || :
cp %{_builddir}/qtpositioning-everywhere-src-%{version}/src/3rdparty/clip2tri/LICENSE %{buildroot}/usr/share/package-licenses/qt6positioning/69d5aab915ac11e2d4afbdbf664824e654b7ae93 || :
cp %{_builddir}/qtpositioning-everywhere-src-%{version}/src/3rdparty/clipper/LICENSE %{buildroot}/usr/share/package-licenses/qt6positioning/23b6196e1135fe02b4deb0607b016ff725275c79 || :
cp %{_builddir}/qtpositioning-everywhere-src-%{version}/src/3rdparty/poly2tri/LICENSE %{buildroot}/usr/share/package-licenses/qt6positioning/3c4a0cf53278b001dd25ca8dea8d543fc0374181 || :
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/lib64/qt6/metatypes/qt6positioning_relwithdebinfo_metatypes.json
/usr/lib64/qt6/mkspecs/modules/qt_lib_positioning.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_positioning_private.pri
/usr/lib64/qt6/modules/Positioning.json

%files dev
%defattr(-,root,root,-)
/usr/include/QtPositioning/6.6.0/QtPositioning/private/qclipperutils_p.h
/usr/include/QtPositioning/6.6.0/QtPositioning/private/qdoublematrix4x4_p.h
/usr/include/QtPositioning/6.6.0/QtPositioning/private/qdoublevector2d_p.h
/usr/include/QtPositioning/6.6.0/QtPositioning/private/qdoublevector3d_p.h
/usr/include/QtPositioning/6.6.0/QtPositioning/private/qgeoaddress_p.h
/usr/include/QtPositioning/6.6.0/QtPositioning/private/qgeocircle_p.h
/usr/include/QtPositioning/6.6.0/QtPositioning/private/qgeocoordinate_p.h
/usr/include/QtPositioning/6.6.0/QtPositioning/private/qgeocoordinateobject_p.h
/usr/include/QtPositioning/6.6.0/QtPositioning/private/qgeolocation_p.h
/usr/include/QtPositioning/6.6.0/QtPositioning/private/qgeopath_p.h
/usr/include/QtPositioning/6.6.0/QtPositioning/private/qgeopolygon_p.h
/usr/include/QtPositioning/6.6.0/QtPositioning/private/qgeopositioninfo_p.h
/usr/include/QtPositioning/6.6.0/QtPositioning/private/qgeopositioninfosource_p.h
/usr/include/QtPositioning/6.6.0/QtPositioning/private/qgeorectangle_p.h
/usr/include/QtPositioning/6.6.0/QtPositioning/private/qgeosatelliteinfo_p.h
/usr/include/QtPositioning/6.6.0/QtPositioning/private/qgeosatelliteinfosource_p.h
/usr/include/QtPositioning/6.6.0/QtPositioning/private/qgeoshape_p.h
/usr/include/QtPositioning/6.6.0/QtPositioning/private/qlocationutils_p.h
/usr/include/QtPositioning/6.6.0/QtPositioning/private/qnmeapositioninfosource_p.h
/usr/include/QtPositioning/6.6.0/QtPositioning/private/qnmeasatelliteinfosource_p.h
/usr/include/QtPositioning/6.6.0/QtPositioning/private/qpositioningglobal_p.h
/usr/include/QtPositioning/6.6.0/QtPositioning/private/qtpositioning-config_p.h
/usr/include/QtPositioning/6.6.0/QtPositioning/private/qtpositioningexports_p.h
/usr/include/QtPositioning/6.6.0/QtPositioning/private/qwebmercator_p.h
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

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt6Positioning.so.6
/usr/lib64/libQt6Positioning.so.6.6.0
/usr/lib64/qt6/plugins/position/libqtposition_geoclue2.so
/usr/lib64/qt6/plugins/position/libqtposition_nmea.so
/usr/lib64/qt6/plugins/position/libqtposition_positionpoll.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qt6positioning/23b6196e1135fe02b4deb0607b016ff725275c79
/usr/share/package-licenses/qt6positioning/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/qt6positioning/3c4a0cf53278b001dd25ca8dea8d543fc0374181
/usr/share/package-licenses/qt6positioning/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/qt6positioning/69d5aab915ac11e2d4afbdbf664824e654b7ae93
/usr/share/package-licenses/qt6positioning/715f995f11805ee85601834220c43b082f457ea3
/usr/share/package-licenses/qt6positioning/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/qt6positioning/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/qt6positioning/b073f11f0c81a95ab5e32aa6b5d23a5955a95274
/usr/share/package-licenses/qt6positioning/f45ee1c765646813b442ca58de72e20a64a7ddba
