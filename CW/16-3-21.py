class Book(object):
  def __init__(self, title, author, rating):
    self.title = title
    self.author = author
    self.rating = rating
  def getRatings(self):
    return self.rating
book1 = Book('Harry Potter', 'JK Rowling', 4.5)
print(book1.getRatings())