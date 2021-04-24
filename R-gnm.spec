#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-gnm
Version  : 1.1.1
Release  : 24
URL      : https://cran.r-project.org/src/contrib/gnm_1.1-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/gnm_1.1-1.tar.gz
Summary  : Generalized Nonlinear Models
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-gnm-lib = %{version}-%{release}
Requires: R-qvcalc
Requires: R-relimp
BuildRequires : R-qvcalc
BuildRequires : R-relimp
BuildRequires : buildreq-R

%description
# gnm
[![CRAN\_Status\_Badge](http://www.r-pkg.org/badges/version/gnm)](https://cran.r-project.org/package=gnm)
[![Travis-CI Build
Status](https://travis-ci.org/hturner/gnm.svg?branch=master)](https://travis-ci.org/hturner/gnm)
[![AppVeyor Build
Status](https://ci.appveyor.com/api/projects/status/github/hturner/gnm?branch=master&svg=true)](https://ci.appveyor.com/project/hturner/gnm)

%package lib
Summary: lib components for the R-gnm package.
Group: Libraries

%description lib
lib components for the R-gnm package.


%prep
%setup -q -c -n gnm
cd %{_builddir}/gnm

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589752119

%install
export SOURCE_DATE_EPOCH=1589752119
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gnm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gnm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gnm
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc gnm || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/gnm/CITATION
/usr/lib64/R/library/gnm/DESCRIPTION
/usr/lib64/R/library/gnm/INDEX
/usr/lib64/R/library/gnm/Meta/Rd.rds
/usr/lib64/R/library/gnm/Meta/data.rds
/usr/lib64/R/library/gnm/Meta/demo.rds
/usr/lib64/R/library/gnm/Meta/features.rds
/usr/lib64/R/library/gnm/Meta/hsearch.rds
/usr/lib64/R/library/gnm/Meta/links.rds
/usr/lib64/R/library/gnm/Meta/nsInfo.rds
/usr/lib64/R/library/gnm/Meta/package.rds
/usr/lib64/R/library/gnm/Meta/vignette.rds
/usr/lib64/R/library/gnm/NAMESPACE
/usr/lib64/R/library/gnm/NEWS.md
/usr/lib64/R/library/gnm/R/gnm
/usr/lib64/R/library/gnm/R/gnm.rdb
/usr/lib64/R/library/gnm/R/gnm.rdx
/usr/lib64/R/library/gnm/WORDLIST
/usr/lib64/R/library/gnm/data/Rdata.rdb
/usr/lib64/R/library/gnm/data/Rdata.rds
/usr/lib64/R/library/gnm/data/Rdata.rdx
/usr/lib64/R/library/gnm/demo/gnm.R
/usr/lib64/R/library/gnm/doc/gnmOverview.R
/usr/lib64/R/library/gnm/doc/gnmOverview.Rnw
/usr/lib64/R/library/gnm/doc/gnmOverview.pdf
/usr/lib64/R/library/gnm/doc/index.html
/usr/lib64/R/library/gnm/help/AnIndex
/usr/lib64/R/library/gnm/help/aliases.rds
/usr/lib64/R/library/gnm/help/gnm.rdb
/usr/lib64/R/library/gnm/help/gnm.rdx
/usr/lib64/R/library/gnm/help/paths.rds
/usr/lib64/R/library/gnm/html/00Index.html
/usr/lib64/R/library/gnm/html/R.css
/usr/lib64/R/library/gnm/tests/testthat/outputs/RChomog2.rds
/usr/lib64/R/library/gnm/tests/testthat/outputs/biplotModel.rds
/usr/lib64/R/library/gnm/tests/testthat/outputs/doubleUnidiff-contrasts.rds
/usr/lib64/R/library/gnm/tests/testthat/outputs/doubleUnidiff.rds
/usr/lib64/R/library/gnm/tests/testthat/outputs/yaish-mult.rds
/usr/lib64/R/library/gnm/tests/testthat/test-RC.R
/usr/lib64/R/library/gnm/tests/testthat/test-RChomog.R
/usr/lib64/R/library/gnm/tests/testthat/test-biplot.R
/usr/lib64/R/library/gnm/tests/testthat/test-bwt.R
/usr/lib64/R/library/gnm/tests/testthat/test-diagonalRef.R
/usr/lib64/R/library/gnm/tests/testthat/test-doubleUnidiff.R
/usr/lib64/R/library/gnm/tests/testthat/test-gammi.R
/usr/lib64/R/library/gnm/tests/testthat/test-logistic.R
/usr/lib64/R/library/gnm/tests/testthat/test-stereotype.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/gnm/libs/gnm.so
/usr/lib64/R/library/gnm/libs/gnm.so.avx2
