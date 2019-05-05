=============
FSMEDHRO Core
=============

Dies ist die Grundlage für Webseite des Fachschaftsrates der medizinischen
Fakultät der Uni Rostock. Hier wird definiert, was ein `FachschaftsUser`, ein
`Studiengang` und ein `Studienabschnitt` ist und welche `Gender` es gibt.

Installation
------------

1. Fügt `fsmedhro_core` wie folgt zu deinen `INSTALLED_APPS` hinzu::

    INSTALLED_APPS = [
        ...
        'fsmedhro_core.apps.FachschaftConfig',
    ]

2. Erzeuge die Models mittels `python manage.py migrate`

3. Fügt das LDAP-Backend zu `AUTHENTICATION_BACKENDS` hinzu::

    AUTHENTICATION_BACKENDS = [
        'django.contrib.auth.backends.ModelBackend',
        'fsmedhro_core.backends.auth.LDAPUniRostock',
    ]


zu erledigen
------------

* Views und Templates für `FachschaftsUser` erstellen
* URLs klarmachen
