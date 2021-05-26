# Search

Used to search for a specific movie or TV series.

**URL** : `/search/movie?query={query}` or `/search/tv?query={query}`

**Method** : `GET`

**Auth required** : NO

## Success Response

**Code** : `200 OK`

**Content example**

Content may be longer than what is posted below.

**Search movie** : `/search/movie?query=forrest`
```json
{
    "id": 13,
    "name": "Forrest Gump",
    "overview": "A man with a low IQ has accomplished great things in his life and been present during significant historic events—in each case, far exceeding what anyone imagined he could do. But despite all he has achieved, his one true love eludes him.",
    "posterPath": "/h5J4W4veyxMXDMjeNxZI46TsHOb.jpg"
}{
    "id": 237353,
    "name": "Through the Eyes of Forrest Gump",
    "overview": "A look behind the scenes of Robert Zemeckis' 1994 Oscar-winning film, 'Forrest Gump'.",
    "posterPath": "/dfjLE1HjdR9XhEpN04elCGUOJfA.jpg"
}
```
**Search TV** : `/search/tv?query=friends`
```json
{
    "id": 1668,
    "name": "Friends",
    "overview": "The misadventures of a group of friends as they navigate the pitfalls of work, life and love in Manhattan.",
    "posterPath": "/f496cm9enuEsZkSPzCwnTESEK5s.jpg"
}{
    "id": 4887,
    "name": "Barney & Friends",
    "overview": "Barney & Friends is an American children's television series aimed at children from ages 2 to 5. The series, which first aired on April 6, 1992, features the title character Barney, a purple anthropomorphic Tyrannosaurus rex who conveys educational messages through songs and small dance routines with a friendly, optimistic attitude.\n\nNew episodes have not been produced since 2009; however reruns continue to air on various PBS stations.",
    "posterPath": "/ijt54PA1pZ2ae68ODBk3vfWSK0e.jpg"
}
```