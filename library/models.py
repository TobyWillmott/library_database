from sqlalchemy import Column, Integer, String, Table, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

book_author = Table("book_author",
                    Base.metadata,
                    Column("id", Integer, primary_key=True),
                    Column("book_id", ForeignKey("book.book_id")),
                    Column("author_id", ForeignKey("author.author_id")),
                    UniqueConstraint("book_id", "author_id")
                    )


class Book(Base):
    __tablename__ = "book"
    book_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    ISBN_number = Column(Integer, nullable=False)
    num_pages = Column(Integer, nullable=False)
    publication_date = Column(Integer, nullable=False)
    publisher_id = Column(Integer, ForeignKey("publisher.publisher_id"))

    authors = relationship("Author",
                           secondary=book_author,
                           order_by="(Author.author_name)",
                           back_populates="books"
                           )
    publisher = relationship("Publisher", back_populates="books")


class Author(Base):
    __tablename__ = "author"
    author_id = Column(Integer, primary_key=True, autoincrement=True)
    author_name = Column(String, nullable=False)
    books = relationship("Book",
                         secondary=book_author,
                         order_by="(Book.title)",
                         back_populates="authors"
                         )


class Publisher(Base):
    __tablename__ = "publisher"
    publisher_id = Column(Integer, primary_key=True, autoincrement=True)
    publisher_name = Column(String, nullable=False)

    books = relationship("Book", back_populates="publisher")
