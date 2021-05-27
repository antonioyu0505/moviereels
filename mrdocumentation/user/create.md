# User creation

Used to create a user

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

```json
{}
```

## Error Response

**Condition** : If 'username' is duplicated.

**Code** : `401 UNAUTHORIZED`

**Content** :

```json
{}
```