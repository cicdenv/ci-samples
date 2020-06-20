## Overview
Python 3 with virtualenv.

## Auto Activating virtualenv
```
environment {
    BASH_ENV = "${WORKSPACE}/.bashrc"
}

sh "echo '. ${WORKSPACE}/venv/bin/activate' > .bashrc"
```

Subsequent `sh '...'` steps will automatically activate the virtualenv.

## Caching
Use a virtual environment and cache that folder.

```
withCaching(keys: ['requirements.txt'], folders: ['venv']) {
    sh 'virtualenv venv'
    ...
    sh 'pip install -r requirements.txt'
}
```

## Build Environment
* https://hub.docker.com/_/python
  * https://hub.docker.com/_/python?tab=description (review Image Variants section)
  * https://github.com/docker-library/python
  * https://hub.docker.com/_/buildpack-deps/ (base)

## Test Reports
* https://coderbook.com/@marcus/generate-python-unit-test-flake8-reports-for-junit/
  ```groovy
  post {
      always {
          junit testResults: 'test-reports/report-*.xml'
      }
  }
  ```
