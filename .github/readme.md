# Tivix Project Backend

## endpoints

- '/api' - api root
    - '/galleries'
        - returns list of galleries with:
            - id, type, title, description, and list of movies
    - '/productions'
        - returns list of productions with:
            - id, IMDBid, card, genres

- 'search/str:query/int:quantity' - search for a movie on OMDb
    - creates search gallery
    - redirects to gallery
