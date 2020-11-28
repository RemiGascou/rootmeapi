## API v1.0


## /login

**Paramètres :**

 - login : Votre login
 - password : Votre mot de passe

## /challenges

**Paramètres :**

 - titre : Titre
 - soustitre : Sous titre
 - lang : Langue
 - score : Score

## /challenges/id_challenge

Exemple : python

```python
#!/usr/bin/python

import requests,json
cookies = {"spip_session": "***"}
resp = requests.get("https://api.www.root-me.org/challenges/5", cookies=cookies)
if resp.status_code != 200:
    raise Exception("GET /challenges/ {}".format(resp.status_code))
data = resp.json()
print(json.dumps(data, indent=4, sort_keys=True))
```

Output

```
titre:HTML
descriptif:<p>N&#8217;allez pas chercher trop loin&nbsp;!</p>
score:5
id_rubrique:68
```


## /auteurs

**Paramètres :**

 - nom : Nom
 - statut : Statut
 - lang : Langue

Exemple : BASH

```bash
#!/bin/bash

resp=$(curl -b "spip_session=***" https://api.www.root-me.org/auteurs)
echo "$resp" | sed -e "s/},/}}\n{/g" | grep id_auteur | head -3
```


Output

```
{"0":{"id_auteur":"1","nom":"g0uZ"}}
{"1":{"id_auteur":"9","nom":"invit\u00e9"}}
{"2":{"id_auteur":"61","nom":"1-vek"}}
...
```

## /auteurs/id_auteur

Exemple en PHP :

```
<?php

$opts = array(
  "http" => array(
    "method" => "GET",
    "header" => "Cookie: spip_session=***\r\n"
  )
);
$context = stream_context_create($opts);
$resp = file_get_contents("https://api.www.root-me.org/auteurs/1", false, $context);
$data = json_decode($resp);
echo(print_r($data));
?>
```

Output

```
Array
(
    [nom] => g0uZ
    [score] => 3165
    [position] => 849
    [challenges] => Array
        (
            [0] => Array
                (
                    [id_challenge] => 5
                    [url_challenge] => http://dev.root-me.org/fr/Challenges/Web-Serveur/HTML
    ...
?>
```


## /classement

Exemple en BASH :

```bash
#!/bin/bash

resp=$(curl -b "spip_session=***" https://api.www.root-me.org/classement?debut_classement=2450)
echo "$resp" | sed -e "s/},{/\n/g" | grep ":2500,"
```

Output

```
    "place":2500,"nom":"pouete","score":"1620"
    "place":2500,"nom":"N@tC@rm!n","score":"1620"
    "place":2500,"nom":"Zarked","score":"1620"
    "place":2500,"nom":"Mayden","score":"1620"
    ...
```

## /environnements_virtuels

**Paramètres :**

 - nom : Nom de l'environnement
 - os : Système d'exploitation

## /environnements_virtuels/id_environnement_virtuel
