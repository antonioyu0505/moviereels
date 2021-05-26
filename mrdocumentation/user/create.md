# User

Used to search for a specific movie or TV series.

**URL** : `/user/create`

**Method** : `POST`

**Auth required** : NO

**Data constraints**

```json
{
    "username":"[valid username]",
    "password":"[password hashed]",
    "countryCode":"[2 letter country code in ISO 3166-1 format]"
}
```

**Data example**

```json
{
    "username": "randomusername",
    "password": "randomhashedpassword",
    "countryCode":"US"
}
```

## Success Response

**Code** : `200 OK`

**Content example**

Content may be longer than what is posted below.

```json
{}
```

## Error Response

**Condition** : If 'username' is duplicated.

**Code** : `409 CONFLICT`

**Content** :

```json
{}
```