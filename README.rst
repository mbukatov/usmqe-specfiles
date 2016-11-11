==================
 USM QE Specfiles
==================

Spec files of of USM QE server tools packaged as a `dependent software
collection`_ extending standard `rh-python35`_ `software collection`_.

Creating new Software collection extending an existing one
==========================================================

This is a quick overview of extending `rh-python35`_ `software collection`_
with another one, which would contain packages with usm qe server tools.

First of all, we need to come up with the proper name for new software
collection. We are going to use ``rh-usmqeserver10``, where:

* scl name prefix: ``rh-`` is vendor (aka provider or organization) id
* scl name base: ``usmqeserver``
* scl name version: ``10`` (this stands for 1.0)

Now let's generate initial specfile of `software collection metapackage`_ (via
`spec2scl`_)::

    $ cd ~/projects/usmqe-specfiles
    $ spec2scl --meta-specfile rh-usmqeserver10 > rh-usmqeserver10.spec

Such metapackage spec file needs a heavy editing though (TODO: describe the
changes needed).

And now something completelly different: based on the `sdist tarball`_,
generate the initial spec file for mrglog module (via `pyp2rpm`_)::

    $ cd ~/projects/usmqe-specfiles
    $ pyp2rpm -t epel7 -b 3 ~/rpmbuild/SOURCES/mrglog-0.1.1.tar.gz > python-mrglog.spec

The specfile needs inspection and changes (eg. add ``Source0``)::

    $ vim python-mrglog.spec

And again, this spec file needs a heavy editing (TODO: pyp2rpm template).


.. _`sdist tarball`: https://packaging.python.org/glossary/?highlight=sdist#term-source-distribution-or-sdist
.. _`pyp2rpm`: https://github.com/fedora-python/pyp2rpm
.. _`spec2scl`: https://bitbucket.org/bkabrda/spec2scl
.. _`mock`: https://github.com/rpm-software-management/mock/wiki#using-mock-outside-your-git-sandbox
.. _`copr`: https://developer.fedoraproject.org/deployment/copr/about.html
.. _`copr-cli tool`: https://developer.fedoraproject.org/deployment/copr/copr-cli.html

.. _`software collection`: https://www.softwarecollections.org/en/about/
.. _`software collection metapackage`: https://www.softwarecollections.org/en/docs/guide/#sect-Meta_Package
.. _`dependent software collection`: https://access.redhat.com/documentation/en-US/Red_Hat_Software_Collections/2/html-single/Packaging_Guide/index.html#sect-Extending_the_python27_and_rh-python34_Software_Collections
.. _`rh-python35`: https://www.softwarecollections.org/en/scls/rhscl/rh-python35/
