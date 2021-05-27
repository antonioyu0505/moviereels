# Movie Reels

Where full URLs are provided in responses they will be rendered as if service
is running on 'http://127.0.0.1:5000'.

## Open Endpoints

Open endpoints require no Authentication.

* [Search movie](search.md) : `GET /search/movie?query={query}`
* [Search TV](search.md) : `GET /search/tv?query={query}`
* [Get movie detail](itemDetail.md) `GET /movie/{id}`
* [Get tv series detail](itemDetail.md) `GET /tv/{id}`
* [User creation](user/create.md) : `POST /user/create`

## Closed Endpoints

Closed endpoints require Authentication.

* [User details](user/details.md) : `GET /user`
* [Add item to list](list/add.md) : `POST /list/add`
* [Update item of a user's list](list/update.md) `PUT /list/update`
* [Get the user's list](list/list.md) `GET /list`