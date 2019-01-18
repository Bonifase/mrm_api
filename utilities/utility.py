import datetime
import validators
from helpers.database import db_session


def validate_url(**kwargs):
    """
    Function to validate url when
    saving an object
    :params kwargs
    """
    if not validators.url(kwargs.get('image_url')):
        raise AttributeError("Please enter a valid image url")


def validate_empty_fields(**kwargs):
    """
    Function to validate empty fields when
    saving an object
    :params kwargs
    """
    for field in kwargs:
        value = kwargs.get(field)
        if not type(value) is bool and not value:
            raise AttributeError(field + " is required field")


def update_entity_fields(entity, **kwargs):
    """
    Function to update an entities fields
    :param kwargs
    :param entity
    """
    keys = kwargs.keys()
    for key in keys:
        exec("entity.{0} = kwargs['{0}']".format(key))
    return entity


def validate_rating_field(**kwargs):
    """
    Function to validate rating fields when
    saving an object
    :params kwargs
    """
    rating = [1, 2, 3, 4, 5]
    if kwargs['rate'] not in rating:
        raise AttributeError("Please rate between 1 and 5")


def validate_date_time_range(**kwargs):
    """
    Function to validate the dates entered
    for questions for feedback
    :params kwargs
    """
    if ('start_date' and 'end_date' in kwargs) and\
            kwargs['start_date'] < datetime.datetime.now():
        raise ValueError('startDate should be today or after')
    elif ('start_date' and 'end_date' in kwargs) and\
            kwargs['end_date'] - kwargs['start_date'] < datetime.timedelta(
                days=1
            ):
        raise ValueError(
            'endDate should be at least a day after startDate'
        )


def validate_missing_items_field(**kwargs):
    """
    Function to validate the missing item field
    when saving a check question response
    :params kwargs
    """
    if 'missing_items' not in kwargs:
        raise AttributeError("Provide the missing items")


class Utility(object):

    def save(self):
        """Function for saving new objects"""
        db_session.add(self)
        db_session.commit()

    def delete(self):
        """Function for deleting objects"""
        db_session.delete(self)
        db_session.commit()
