# Change Log
All enhancements and patches to cookiecutter-django will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

## [2015-10-09]
### Added
- 0.8.0: Optional reply_to to support Django 1.8 (@zakdoek)

## [2015-10-09]
### Added
- 0.7.3: Optional reply_to to support Django 1.8 (@zakdoek)


## [2015-09-24]
### Changed
- 0.7.2: Dictionary iterations to work with both Python 2 and 3. (@rollokb)
- 0.7.2: Added six to dependencies. (@pydanny)


## [2015-09-23]
### Removed
- 0.7.1: Old `build` directory that `setuptools` hadn't properly cleaned up when I flattened the architecture of this project. This fixes #28. (@pydanny)

## [2015-09-21]
### Added
- Ability to pass in extra tracking options to mailgun via API  (@wsmith)

## [2015-09-14]
### Added
- Support for `Recipient Variables` (@wsmith)
- Version specification in python module (@pydanny)

## [2015-09-08]
### Changed
- 0.5.0: Architecture flattening (@pydanny)
- 0.4.0: Moved more internals to requests library (@ghinch)
- 0.4.0: Flake8 setup and cleanup (@pydanny)

## [2015-09-07]
### Added
- Moved AUTHORS to CONTRIBUTORS.rst (@pydanny)
- Upgraded to Mailgun API V3 (@omidraha)

## [2015-09-06]
### Added
- Expanded tests and coverage is now 50% (@pydanny)

## [2015-09-04]
### Added
- Added configuration test (@pydanny)

## [2015-09-04]
### Added
- Changelog (@pydanny)
- .travis.yml file with codecov (@pydanny)
- Many new trove classifiers (@pydanny)
- .gitignore (@pydanny)
- .editorconfig (@pydanny)
- CONTRIBUTING.rst stub (@pydanny)
### Changed
- Fix unicode error in python2 (@ryneeverett)
- Better Python 3 support (@fwiles)
- PEP8 cleanup (@fwiles)
- Switched to using `six.StringIO` (@pydanny)
