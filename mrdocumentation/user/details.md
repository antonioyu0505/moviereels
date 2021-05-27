# User details

Used to get the details of a user.

**URL** : `/user`

**Method** : `GET`

**Auth required** : YES

**Data constraints**

Headers

`Authorization: value`

**Data example**

Headers

`Authorization: 4`

## Success Response

**Condition** : If 'Authorization' value exists in the database.

**Code** : `200 OK`

**Content example**

Password will be removed at a later version.

```json
{
    "countryCode": "CO",
    "id": 4,
    "lastLogin": "2021-05-26T00:50:24",
    "password": "password",
    "username": "antonioyu"
}
```

## Error Response

**Condition** : If 'Authorization' value does not exists in the database.

**Code** : `401 UNAUTHORIZED`

**Content** :

```json
{}
```