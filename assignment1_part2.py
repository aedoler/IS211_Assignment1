#!user/bin/env python
# -*- coding: utf-8 -*-
"""Part 2"""


class Book(object):
    """A class that outputs title and author"""
    author = ''
    title = ''

    def __init__(self, title, author):
        """Takes in title and author
        Atts:
            title: (str) title of book
            author: (str) author of book
        Examples:
            OBJ = Book("Of Mice and Men", "Author")
        """
        self.author = author
        self.title = title

    def display(self):
        """Display str of author and title
        Examples:
            >>> print OBJ.display()
            Of Mice and Men, written by Author.
        """
        message = "{}, written by {}.".format(self.title, self.author)
        return message


# Instanciate class object
OBJ = Book("Of Mice and Men", "Author")
print OBJ.display()
