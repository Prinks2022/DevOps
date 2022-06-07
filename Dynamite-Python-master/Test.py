def books():
    books = [
        { 'id': 1, 'title': 'Clean Code', 'authors': 'Robert C. Martin' },
        { 'id': 2, 'title': 'The DevOps Handbook', 'authors': 'Gene Kim, Jez Humble, Patrick Debois, John Willis' },
        { 'id': 3, 'title': 'The Phoenix Project', 'authors': 'Gene Kim, Kevin Behr,George Spafford' }
    ]
    for book in books:
        print(book["title"])
    return books
print(books())