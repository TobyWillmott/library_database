from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Book, Author, Publisher

authors = [Author(author_name="Roald Dahl"),
           Author(author_name="J.K. Rowling"),
           Author(author_name="George Orwell"),
           Author(author_name="David Walliams"),
           ]
publishers = [Publisher(publisher_name="Puffin"),
              Publisher(publisher_name="Macmillan"),
              Publisher(publisher_name="Bloomsbury")
              ]
books = [Book(title="The boy in the dress", ISBN_number="9780007329267", num_pages=365, publication_date=2000, publisher_id=1),
         Book(title="1984", ISBN_number="9780033329467", num_pages=265, publication_date=1948, publisher_id=2),
         Book(title="Harry Potter and the philosphers stone", ISBN_number="9782207329211", num_pages=165, publication_date=1995, publisher_id=3),
         Book(title="James and the giant peach", ISBN_number="243908732467", num_pages=144, publication_date=1934, publisher_id=1),
         ]
books[0].authors.append(authors[3])
books[1].authors.append(authors[2])
books[2].authors.append(authors[1])
books[3].authors.append(authors[0])


engine = create_engine("sqlite:///library.sqlite", echo=True)

with Session(engine) as sess:
    sess.add_all(publishers)
    sess.add_all(books)
    sess.commit()

