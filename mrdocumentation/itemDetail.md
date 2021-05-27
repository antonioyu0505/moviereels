# Movie/TV series detail

Used to get the details for a specified movie or tv series

**URL** : `/movie/{id}` or `/tv/{id}`

**Method** : `GET`

**Auth required** : NO

## Success Response

**Code** : `200 OK`

**Content example**

**Search movie** : `/movie/13`
```json
{
    "genres": [
        "Comedy",
        "Drama",
        "Romance"
    ],
    "id": 13,
    "name": "Forrest Gump",
    "overview": "A man with a low IQ has accomplished great things in his life and been present during significant historic events—in each case, far exceeding what anyone imagined he could do. But despite all he has achieved, his one true love eludes him.",
    "posterPath": "/h5J4W4veyxMXDMjeNxZI46TsHOb.jpg"
}
```
**Search TV** : `/tv/{1668}`
```json
{
    "genres": [
        "Comedy",
        "Drama"
    ],
    "id": 1668,
    "name": "Friends",
    "overview": "The misadventures of a group of friends as they navigate the pitfalls of work, life and love in Manhattan.",
    "posterPath": "/f496cm9enuEsZkSPzCwnTESEK5s.jpg"
}
```