# Update item on the list

Used to get the list of a user

**URL** : `/list`

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

```json
{
  "items": [
    {
      "tag": "watched",
      "type": "movie",
      "typeId": 550
    },
    {
      "tag": "watched",
      "type": "tv",
      "typeId": 1668
    },
    {
      "tag": "watched",
      "type": "movie",
      "typeId": 13
    }
  ],
  "userId": "4"
}
```

## Error Response

**Condition** : If 'Authorization' value does not exists in the database.

**Code** : `401 UNAUTHORIZED`

**Content** :

```json
{}
```