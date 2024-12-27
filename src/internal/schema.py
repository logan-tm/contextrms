# Import necessary modules from SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Create an SQLite database engine; replace with your database URL
# engine = create_engine("sqlite:///example.db", echo=True)
engine = create_engine(r"sqlite:///data/database.db")

# Create a base class for declarative class definitions
Base = declarative_base()


# Define a model class that inherits from Base
class Context(Base):
    __tablename__ = "contexts"  # Define the name of the table

    id = Column(
        Integer, primary_key=True, autoincrement=True, unique=True
    )  # Define the primary key column
    name = Column(String, nullable=False)  # Define a regular column
    color = Column(Integer, nullable=False)  # Define another column

    def __repr__(self):
        return f"<Context(name={self.name}, color={self.color})>"


# Create a session factory
Session = sessionmaker(bind=engine)

# Create the tables in the database
Base.metadata.create_all(engine)
