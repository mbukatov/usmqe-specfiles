==================
 USM QE Specfiles
==================

Spec files of of USM QE tools packaged as a software collection extending
standard `rh-python35`_ collection.

Creating new Software collection extending an existing one
==========================================================

This is a quick overview of extending `rh-python35`_ software collection with
another one (so called `dependent software collection`), which would contain
packages with usm qe tools.

First of all, we need to come up with the proper name for new software
collection. We are going to use ``rh-usmqetools10``, where:

* scl name prefix: ``rh-`` is vendor (aka provider or organization) id
* scl name base: ``usmqetools``
* scl name version: ``10`` (this stands for 1.0)

Now let's generate initial specfile of soft. colleciton metapackage::

    $ cd ~/projects/usmqe-specfiles
    $ spec2scl --meta-specfile rh-usmqetools10 > rh-usmqetools10.spec

TODO: continue here

And now something completelly different: based on the sdist tarball, generate
the initial spec file for mrglog module::

    $ cd ~/projects/usmqe-specfiles
    $ pyp2rpm -t epel7 -b 3 ~/rpmbuild/SOURCES/mrglog-0.1.1.tar.gz > python-mrglog.spec

The specfile needs inspection and changes (eg. add ``Source0``)::

    $ vim python-mrglog.spec


TODO: Old Notes
===============

When you are ok with the specfile, copy the files into rpmbuild directories::

    $ cp ~/projects/pytest-ansible-playbook/dist/pytest-ansible-playbook-0.3.0.tar.gz ~/rpmbuild/SOURCES
    $ cp ~/projects/usmqe-specfiles/python-pytest-ansible-playbook.spec ~/rpmbuild/SPECS

And then generate the source rpm::

    $ cd ~/rpmbuild/SPECS
    $ rpmbuild -bs python-pytest-ansible-playbook.spec 
    $ ls ~/rpmbuild/SRPMS
    python-pytest-ansible-playbook-0.3.0-1.fc24.src.rpm



.. _`sdist tarball`: https://packaging.python.org/glossary/?highlight=sdist#term-source-distribution-or-sdist
.. _`pyp2rpm`: https://github.com/fedora-python/pyp2rpm
.. _`mock`: https://github.com/rpm-software-management/mock/wiki#using-mock-outside-your-git-sandbox
.. _`copr`: https://developer.fedoraproject.org/deployment/copr/about.html
.. _`copr-cli tool`: https://developer.fedoraproject.org/deployment/copr/copr-cli.html
.. _`software collection`: https://www.softwarecollections.org/en/about/
.. _`rh-python35`: https://www.softwarecollections.org/en/scls/rhscl/rh-python35/
