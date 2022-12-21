import abc
import typing

from src.entities.movie import Movie

# CRUD


class RepositoryException(Exception):
    pass


class MovieRepository(abc.ABC):
    def create(self, movie: Movie):
        """
        Creates a movie and returns true on success

        Raises RepositoryException on failure
        """
        raise NotImplementedError

    def get(self, movie_id: str) -> typing.Optional[Movie]:
        """
        Retrieves a movie by it's ID and if the movie is not found it will return None.
        """
        raise NotImplementedError

    def get_by_title(self, title: str) -> typing.List[Movie]:
        """
        Retrieves a list of movies which share the same title.
        """
        raise NotImplementedError

    def delete(self, movie_id: str):
        """
        Deletes a movie by it's ID.

        Raises RepositoryException on failure
        """
        raise NotImplementedError

    def update(self, movie_id: str, update_parameters: dict):
        """
        Updates a movie by it's ID.

        Raises RepositoryException on failure
        """
        raise NotImplementedError
