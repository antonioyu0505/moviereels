# Update item on the list

Used to update the tag of an item, either a movie or tv series, of a user's list

**URL** : `/list/update`

**Method** : `PUT`

**Auth required** : YES

**Data constraints**

Headers

`Authorization: value`

```json
{
  "type" : "[type of item to add]",
  "typeId" : "[valid item id]",
  "tag" : "[valid tag]"
}
```

**Data example**

Headers

`Authorization: 4`

```json
{
  "type" : "tv",
  "typeId" : 1668,
  "tag" : "dropped"
}
```

## Success Response

**Condition** : If 'Authorization' value exists in the database and the user has added the item previously.

**Code** : `200 OK`

**Content example**

```json
{}
```

## Error Response

**Condition** : If 'Authorization' value does not exists in the database.

**Code** : `401 UNAUTHORIZED`

**Content** :

```json
{}
```

**Condition** : If the user inputs a type aside from 'movie' or 'tv'.

**Code** : `400 BAD REQUEST`

**Content** :

```json
{}
```