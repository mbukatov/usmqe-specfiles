==================
 USM QE Specfiles
==================

Spec files for fedora builds of some USM QE tools.


Full example of the process
===========================

This is an example of packaging process for a small project
``pytest-ansible-playbook``, which is not (yet) available on PyPI.

In a git repo of the project, make sure we are in expected state (HEAD is in a
tagged commit, working directory is clean, ...)::

    $ cd ~/projects/pytest-ansible-playbook
    $ git describe --tags
    0.3.0
    $ git status
    On branch master
    Your branch is up-to-date with 'upstream/master'.
    nothing to commit, working directory clean


Creating initial spec file with pyp2rpm
---------------------------------------

Then generate `sdist tarball`_ for the project::

    $ python3 setup.py sdist
    $ ls dist/
    pytest-ansible-playbook-0.3.0.tar.gz

Now generate initial spec file via `pyp2rpm`_ using the sdist tarball::

    $ cd ~/projects/usmqe-specfiles
    $ pyp2rpm ~/projects/pytest-ansible-playbook/dist/pytest-ansible-playbook-0.3.0.tar.gz > python-pytest-ansible-playbook.spec

The specfile needs inspection and changes (eg. add ``Source0``)::

    $ vim python-pytest-ansible-playbook.spec

When you are ok with the specfile, copy the files into rpmbuild directories::

    $ cp ~/projects/pytest-ansible-playbook/dist/pytest-ansible-playbook-0.3.0.tar.gz ~/rpmbuild/SOURCES
    $ cp ~/projects/usmqe-specfiles/python-pytest-ansible-playbook.spec ~/rpmbuild/SPECS

And then generate the source rpm::

    $ cd ~/rpmbuild/SPECS
    $ rpmbuild -bs python-pytest-ansible-playbook.spec 
    $ ls ~/rpmbuild/SRPMS
    python-pytest-ansible-playbook-0.3.0-1.fc24.src.rpm


Local build with mock
---------------------

Such source rpm file can be uploaded into copr, but you may like to try to
build it locally with `mock`_ first::

    $ cd ~/rpmbuild/SPECS
    $ mock -r fedora-24-x86_64 --rebuild python-pytest-ansible-playbook-0.3.0-1.fc24.src.rpm

Note: mock does the build in clean chroot enviroment and it's used both by koji
and copr.

When the build finishes with success, the rpm packages can be found in the
result directory::

    $ ls /var/lib/mock/fedora-24-x86_64/result
    build.log
    python2-pytest-ansible-playbook-0.3.0-1.fc24.noarch.rpm
    python3-pytest-ansible-playbook-0.3.0-1.fc24.noarch.rpm
    python-pytest-ansible-playbook-0.3.0-1.fc24.src.rpm
    root.log
    state.log


Building with copr
------------------

Assuming we aready have a `copr`_ project for the package, and the `copr-cli
tool`_ has been configured, we can just upload the source rpm file into the
project::

    $ copr-cli build usmqe-fedora ~/rpmbuild/SRPMS/python-pytest-ansible-playbook-0.3.0-1.fc24.src.rpm


.. _`sdist tarball`: https://packaging.python.org/glossary/?highlight=sdist#term-source-distribution-or-sdist
.. _`pyp2rpm`: https://github.com/fedora-python/pyp2rpm
.. _`mock`: https://github.com/rpm-software-management/mock/wiki#using-mock-outside-your-git-sandbox
.. _`copr`: https://developer.fedoraproject.org/deployment/copr/about.html
.. _`copr-cli tool`: https://developer.fedoraproject.org/deployment/copr/copr-cli.html
