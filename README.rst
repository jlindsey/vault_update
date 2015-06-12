Vault Updater
=============

Simple tool to make updating keys in Vault_ more convenient.

Installation
------------

Clone this repo and run ``python setup.py install``.

Usage
-----

This tool requires two environment vars to be set: ``VAULT_URL`` and ``EDITOR``.

``VAULT_URL`` is used to connect to your vault server.

``EDITOR`` is used to call your preferred text editor with a file containing the current
values in the Vault key (in JSON format).

You are then able to edit the JSON as you please, and ``vault_updater`` will rewrite the
Vault key with the new data.

Copyright
---------

See LICENSE for details.

.. _Vault: https://vaultproject.io/

