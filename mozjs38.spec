#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mozjs38
Version  : 38.2.1.0
Release  : 1
URL      : https://people.mozilla.org/~sstangl/mozjs-38.2.1.rc0.tar.bz2
Source0  : https://people.mozilla.org/~sstangl/mozjs-38.2.1.rc0.tar.bz2
Summary  : psutil is a cross-platform library for retrieving information onrunning processes and system utilization (CPU, memory, disks, network)in Python.
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause BSD-3-Clause-Clear GPL-2.0 LGPL-2.0 LGPL-2.1 MIT MPL-2.0-no-copyleft-exception
Requires: mozjs38-bin
Requires: psutil
Requires: py
Requires: pyOpenSSL
Requires: pyasn1
Requires: pytest
Requires: pytest-cov
Requires: wheel
BuildRequires : icu4c-dev
BuildRequires : nspr-dev
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pkgconfig(libffi)
BuildRequires : pkgconfig(x11)
BuildRequires : psutil
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : zlib-dev
Patch1: pytest.patch

%description
This directory contains SpiderMonkey 38.
This release is based on a revision of Mozilla 38:
http://hg.mozilla.org/releases/
The changes in the patches/ directory were applied.

%package bin
Summary: bin components for the mozjs38 package.
Group: Binaries

%description bin
bin components for the mozjs38 package.


%package dev
Summary: dev components for the mozjs38 package.
Group: Development
Requires: mozjs38-bin
Provides: mozjs38-devel

%description dev
dev components for the mozjs38 package.


%prep
%setup -q -n mozjs-38.0.0
%patch1 -p1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1491678894
pushd js/src
%configure --disable-static --with-x \
--with-system-zlib \
--enable-system-ffi \
--without-system-nspr \
--without-system-icu \
--without-intl-api
make V=1  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1491678894
rm -rf %{buildroot}
pushd js/src
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/lib64/libjs_static.ajs

%files bin
%defattr(-,root,root,-)
/usr/bin/js
/usr/bin/js-config

%files dev
%defattr(-,root,root,-)
/usr/include/mozjs-/js-config.h
/usr/include/mozjs-/js.msg
/usr/include/mozjs-/js/CallArgs.h
/usr/include/mozjs-/js/CallNonGenericMethod.h
/usr/include/mozjs-/js/CharacterEncoding.h
/usr/include/mozjs-/js/Class.h
/usr/include/mozjs-/js/Conversions.h
/usr/include/mozjs-/js/Date.h
/usr/include/mozjs-/js/Debug.h
/usr/include/mozjs-/js/GCAPI.h
/usr/include/mozjs-/js/HashTable.h
/usr/include/mozjs-/js/HeapAPI.h
/usr/include/mozjs-/js/Id.h
/usr/include/mozjs-/js/LegacyIntTypes.h
/usr/include/mozjs-/js/MemoryMetrics.h
/usr/include/mozjs-/js/Principals.h
/usr/include/mozjs-/js/ProfilingFrameIterator.h
/usr/include/mozjs-/js/ProfilingStack.h
/usr/include/mozjs-/js/Proxy.h
/usr/include/mozjs-/js/RequiredDefines.h
/usr/include/mozjs-/js/RootingAPI.h
/usr/include/mozjs-/js/SliceBudget.h
/usr/include/mozjs-/js/StructuredClone.h
/usr/include/mozjs-/js/TracingAPI.h
/usr/include/mozjs-/js/TrackedOptimizationInfo.h
/usr/include/mozjs-/js/TypeDecls.h
/usr/include/mozjs-/js/UbiNode.h
/usr/include/mozjs-/js/UbiNodeTraverse.h
/usr/include/mozjs-/js/Utility.h
/usr/include/mozjs-/js/Value.h
/usr/include/mozjs-/js/Vector.h
/usr/include/mozjs-/js/WeakMapPtr.h
/usr/include/mozjs-/jsalloc.h
/usr/include/mozjs-/jsapi.h
/usr/include/mozjs-/jsbytecode.h
/usr/include/mozjs-/jsclist.h
/usr/include/mozjs-/jscpucfg.h
/usr/include/mozjs-/jsfriendapi.h
/usr/include/mozjs-/jsperf.h
/usr/include/mozjs-/jsprf.h
/usr/include/mozjs-/jsprototypes.h
/usr/include/mozjs-/jspubtd.h
/usr/include/mozjs-/jstypes.h
/usr/include/mozjs-/jsversion.h
/usr/include/mozjs-/jswrapper.h
/usr/include/mozjs-/mozilla/Alignment.h
/usr/include/mozjs-/mozilla/AllocPolicy.h
/usr/include/mozjs-/mozilla/AlreadyAddRefed.h
/usr/include/mozjs-/mozilla/Array.h
/usr/include/mozjs-/mozilla/ArrayUtils.h
/usr/include/mozjs-/mozilla/Assertions.h
/usr/include/mozjs-/mozilla/Atomics.h
/usr/include/mozjs-/mozilla/Attributes.h
/usr/include/mozjs-/mozilla/BinarySearch.h
/usr/include/mozjs-/mozilla/BloomFilter.h
/usr/include/mozjs-/mozilla/Casting.h
/usr/include/mozjs-/mozilla/ChaosMode.h
/usr/include/mozjs-/mozilla/Char16.h
/usr/include/mozjs-/mozilla/CheckedInt.h
/usr/include/mozjs-/mozilla/Compiler.h
/usr/include/mozjs-/mozilla/Compression.h
/usr/include/mozjs-/mozilla/Constants.h
/usr/include/mozjs-/mozilla/DebugOnly.h
/usr/include/mozjs-/mozilla/Decimal.h
/usr/include/mozjs-/mozilla/Endian.h
/usr/include/mozjs-/mozilla/EnumSet.h
/usr/include/mozjs-/mozilla/EnumeratedArray.h
/usr/include/mozjs-/mozilla/FloatingPoint.h
/usr/include/mozjs-/mozilla/GuardObjects.h
/usr/include/mozjs-/mozilla/HashFunctions.h
/usr/include/mozjs-/mozilla/IntegerPrintfMacros.h
/usr/include/mozjs-/mozilla/IntegerRange.h
/usr/include/mozjs-/mozilla/IntegerTypeTraits.h
/usr/include/mozjs-/mozilla/IteratorTraits.h
/usr/include/mozjs-/mozilla/JSONWriter.h
/usr/include/mozjs-/mozilla/Likely.h
/usr/include/mozjs-/mozilla/LinkedList.h
/usr/include/mozjs-/mozilla/LinuxSignal.h
/usr/include/mozjs-/mozilla/MacroArgs.h
/usr/include/mozjs-/mozilla/MacroForEach.h
/usr/include/mozjs-/mozilla/MathAlgorithms.h
/usr/include/mozjs-/mozilla/Maybe.h
/usr/include/mozjs-/mozilla/MaybeOneOf.h
/usr/include/mozjs-/mozilla/MemoryChecking.h
/usr/include/mozjs-/mozilla/MemoryReporting.h
/usr/include/mozjs-/mozilla/Move.h
/usr/include/mozjs-/mozilla/NullPtr.h
/usr/include/mozjs-/mozilla/NumericLimits.h
/usr/include/mozjs-/mozilla/Pair.h
/usr/include/mozjs-/mozilla/PodOperations.h
/usr/include/mozjs-/mozilla/Poison.h
/usr/include/mozjs-/mozilla/Range.h
/usr/include/mozjs-/mozilla/RangedPtr.h
/usr/include/mozjs-/mozilla/ReentrancyGuard.h
/usr/include/mozjs-/mozilla/RefCountType.h
/usr/include/mozjs-/mozilla/RefPtr.h
/usr/include/mozjs-/mozilla/ReverseIterator.h
/usr/include/mozjs-/mozilla/RollingMean.h
/usr/include/mozjs-/mozilla/SHA1.h
/usr/include/mozjs-/mozilla/Scoped.h
/usr/include/mozjs-/mozilla/SegmentedVector.h
/usr/include/mozjs-/mozilla/SizePrintfMacros.h
/usr/include/mozjs-/mozilla/SplayTree.h
/usr/include/mozjs-/mozilla/TaggedAnonymousMemory.h
/usr/include/mozjs-/mozilla/TemplateLib.h
/usr/include/mozjs-/mozilla/ThreadLocal.h
/usr/include/mozjs-/mozilla/ToString.h
/usr/include/mozjs-/mozilla/TypeTraits.h
/usr/include/mozjs-/mozilla/TypedEnumBits.h
/usr/include/mozjs-/mozilla/Types.h
/usr/include/mozjs-/mozilla/UniquePtr.h
/usr/include/mozjs-/mozilla/Vector.h
/usr/include/mozjs-/mozilla/WeakPtr.h
/usr/include/mozjs-/mozilla/double-conversion.h
/usr/include/mozjs-/mozilla/unused.h
/usr/include/mozjs-/mozilla/utils.h
/usr/lib64/libmozjs-.so
/usr/lib64/pkgconfig/js.pc
