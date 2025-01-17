#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: f4a13a5
#
Name     : R-gnm
Version  : 1.1.5
Release  : 50
URL      : https://cran.r-project.org/src/contrib/gnm_1.1-5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/gnm_1.1-5.tar.gz
Summary  : Generalized Nonlinear Models
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-gnm-lib = %{version}-%{release}
Requires: R-qvcalc
Requires: R-relimp
BuildRequires : R-qvcalc
BuildRequires : R-relimp
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
including models with multiplicative interaction terms such as the
    UNIDIFF model from sociology and the AMMI model from crop science, and
    many others.  Over-parameterized representations of models are used
    throughout; functions are provided for inference on estimable
    parameter combinations, as well as standard methods for diagnostics
    etc.

%package lib
Summary: lib components for the R-gnm package.
Group: Libraries

%description lib
lib components for the R-gnm package.


%prep
%setup -q -n gnm
pushd ..
cp -a gnm buildavx2
popd
pushd ..
cp -a gnm buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1737146275

%install
export SOURCE_DATE_EPOCH=1737146275
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
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
/usr/lib64/R/library/gnm/tests/testthat.R
/usr/lib64/R/library/gnm/tests/testthat/_snaps/biplot.md
/usr/lib64/R/library/gnm/tests/testthat/_snaps/confint.gnm.md
/usr/lib64/R/library/gnm/tests/testthat/_snaps/doubleUnidiff.md
/usr/lib64/R/library/gnm/tests/testthat/test-RC.R
/usr/lib64/R/library/gnm/tests/testthat/test-RChomog.R
/usr/lib64/R/library/gnm/tests/testthat/test-Symm.R
/usr/lib64/R/library/gnm/tests/testthat/test-biplot.R
/usr/lib64/R/library/gnm/tests/testthat/test-bwt.R
/usr/lib64/R/library/gnm/tests/testthat/test-confint.gnm.R
/usr/lib64/R/library/gnm/tests/testthat/test-diagonalRef.R
/usr/lib64/R/library/gnm/tests/testthat/test-doubleUnidiff.R
/usr/lib64/R/library/gnm/tests/testthat/test-gammi.R
/usr/lib64/R/library/gnm/tests/testthat/test-glm.R
/usr/lib64/R/library/gnm/tests/testthat/test-hskewL.R
/usr/lib64/R/library/gnm/tests/testthat/test-logistic.R
/usr/lib64/R/library/gnm/tests/testthat/test-stereotype.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/gnm/libs/gnm.so
/V4/usr/lib64/R/library/gnm/libs/gnm.so
/usr/lib64/R/library/gnm/libs/gnm.so
