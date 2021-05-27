# Add item to list

Used to add an item, either a movie or tv series, to the user's list with a tag of watched, watching or dropped.

**URL** : `/list/add`

**Method** : `POST`

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
  "tag" : "watched"
}
```

## Success Response

**Condition** : If 'Authorization' value exists in the database and the user has not added the item to his list yet.

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

**Condition** : If the user has already added the item to his list.

**Code** : `409 CONFLICT`

**Content** :

```json
{}
```